#!/usr/bin/env python3
"""Generate a daily computer-vision paper reading feed.

The script intentionally uses only Python's standard library so it can run
reliably on GitHub Actions without dependency installation.
"""

from __future__ import annotations

import html
import json
import re
import sys
import textwrap
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
DATA = ROOT / "data"
HISTORY_FILE = DATA / "feed_history.json"

UTC8 = timezone(timedelta(hours=8))


ARXIV_QUERIES = [
    # COD / camouflage direct line
    'all:"camouflaged object detection"',
    'all:"camouflaged object segmentation"',
    'all:"open-vocabulary camouflaged"',
    'all:"training-free camouflaged"',
    'all:"unsupervised camouflaged object detection"',
    'all:"SAM" AND all:"camouflaged object detection"',
    'all:"frequency" AND all:"camouflaged object detection"',
    'all:"boundary" AND all:"camouflaged object detection"',
    'all:"depth" AND all:"camouflaged object detection"',
    # Broad CV methods likely useful for COD
    'all:"open-vocabulary segmentation"',
    'all:"training-free segmentation"',
    'all:"vision-language" AND all:"segmentation"',
    'all:"multimodal large language model" AND all:"grounding"',
    'all:"visual reasoning" AND all:"segmentation"',
    'all:"anomaly detection" AND all:"vision foundation model"',
    'all:"diffusion" AND all:"segmentation"',
    'all:"test-time adaptation" AND all:"segmentation"',
    'all:"remote sensing" AND all:"open-vocabulary segmentation"',
]


CVF_CONFERENCES = [
    ("CVPR2026", "CVPR 2026", "https://openaccess.thecvf.com/CVPR2026?day=all"),
    ("WACV2026", "WACV 2026", "https://openaccess.thecvf.com/WACV2026?day=all"),
    ("ICCV2025", "ICCV 2025", "https://openaccess.thecvf.com/ICCV2025?day=all"),
]


COD_KEYWORDS = [
    "camouflage",
    "camouflaged",
    "concealed",
    "cod",
    "ovcos",
    "ucod",
]


BROAD_KEYWORDS = [
    "segmentation",
    "segment",
    "open-vocabulary",
    "training-free",
    "zero-shot",
    "weakly",
    "unsupervised",
    "sam",
    "clip",
    "dino",
    "vision-language",
    "multimodal",
    "large multimodal",
    "grounding",
    "visual reasoning",
    "diffusion",
    "retrieval",
    "prototype",
    "anomaly",
    "ood",
    "remote sensing",
    "earth observation",
    "sar",
    "hyperspectral",
    "frequency",
    "boundary",
    "depth",
    "video",
    "tracking",
    "gaussian splatting",
    "3d",
    "4d",
    "test-time",
    "low-light",
    "restoration",
]


STOP_TITLES = {
    # Titles that match broad keywords but are usually far from the user's goal.
    "multimodal protein language models",
    "chemical structures",
}


@dataclass
class Paper:
    title: str
    url: str
    pdf: str = ""
    authors: list[str] = field(default_factory=list)
    source: str = ""
    published: str = ""
    summary: str = ""
    tags: list[str] = field(default_factory=list)
    score: int = 0


def fetch_url(url: str, timeout: int = 45) -> str:
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": "cv-paper-feed/1.0 (daily literature monitor; contact: none)"
        },
    )
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return resp.read().decode("utf-8", errors="ignore")


def clean_text(text: str) -> str:
    text = html.unescape(text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def sentence_intro(summary: str, max_chars: int = 260) -> str:
    summary = clean_text(summary)
    if not summary:
        return "暂无摘要；建议打开论文页查看 abstract 和 method。"
    sentences = re.split(r"(?<=[.!?])\s+", summary)
    intro = " ".join(sentences[:2]).strip()
    if len(intro) > max_chars:
        intro = intro[: max_chars - 1].rstrip() + "..."
    return intro


def derive_tags(title: str, summary: str) -> list[str]:
    text = f"{title} {summary}".lower()
    tags = []
    checks = [
        ("COD", ["camouflage", "camouflaged", "concealed"]),
        ("open-vocabulary", ["open-vocabulary", "open vocabulary"]),
        ("training-free", ["training-free", "training free"]),
        ("unsupervised", ["unsupervised", "weakly", "semi-supervised"]),
        ("SAM", ["segment anything", "sam"]),
        ("VLM/MLLM", ["vision-language", "multimodal large", "llm", "mlLM".lower()]),
        ("reasoning", ["reasoning", "chain-of-thought", "cot", "grounding"]),
        ("diffusion", ["diffusion", "generative", "dit"]),
        ("retrieval/prototype", ["retrieval", "prototype", "memory bank"]),
        ("boundary/frequency", ["boundary", "frequency", "wavelet", "edge"]),
        ("depth/geometry", ["depth", "geometric", "geometry", "3d", "4d"]),
        ("video", ["video", "temporal", "tracking", "motion"]),
        ("remote sensing", ["remote sensing", "earth observation", "sar", "hyperspectral"]),
        ("anomaly/OOD", ["anomaly", "ood", "out-of-distribution"]),
        ("low-level", ["low-light", "restoration", "enhancement", "denoising"]),
    ]
    for tag, words in checks:
        if any(w in text for w in words):
            tags.append(tag)
    return tags or ["computer vision"]


def score_paper(paper: Paper) -> int:
    text = f"{paper.title} {paper.summary}".lower()
    score = 0
    for kw in COD_KEYWORDS:
        if kw in text:
            score += 30
    for kw in BROAD_KEYWORDS:
        if kw in text:
            score += 6
    if "cvpr 2026" in paper.source.lower():
        score += 8
    if "iccv 2025" in paper.source.lower() or "wacv 2026" in paper.source.lower():
        score += 5
    if "arxiv" in paper.source.lower():
        score += 3
    if paper.published:
        try:
            pub = datetime.fromisoformat(paper.published[:10]).replace(tzinfo=timezone.utc)
            age = datetime.now(timezone.utc) - pub
            if age.days <= 7:
                score += 14
            elif age.days <= 30:
                score += 8
            elif age.days <= 120:
                score += 4
        except ValueError:
            pass
    if any(stop in text for stop in STOP_TITLES):
        score -= 40
    return score


def paper_age_days(paper: Paper) -> int | None:
    if not paper.published or not re.match(r"^\d{4}-\d{2}-\d{2}", paper.published):
        return None
    try:
        pub = datetime.fromisoformat(paper.published[:10]).replace(tzinfo=timezone.utc)
    except ValueError:
        return None
    return (datetime.now(timezone.utc) - pub).days


def fetch_arxiv(max_results_per_query: int = 18) -> list[Paper]:
    ns = {"a": "http://www.w3.org/2005/Atom"}
    papers: list[Paper] = []
    for query in ARXIV_QUERIES:
        params = {
            "search_query": query,
            "start": "0",
            "max_results": str(max_results_per_query),
            "sortBy": "submittedDate",
            "sortOrder": "descending",
        }
        url = "https://export.arxiv.org/api/query?" + urllib.parse.urlencode(params)
        try:
            xml_text = fetch_url(url, timeout=60)
            root = ET.fromstring(xml_text)
        except Exception as exc:  # pragma: no cover - network resilience
            print(f"[warn] arXiv query failed: {query}: {exc}", file=sys.stderr)
            continue

        for entry in root.findall("a:entry", ns):
            title = clean_text(entry.findtext("a:title", "", ns))
            summary = clean_text(entry.findtext("a:summary", "", ns))
            abs_url = entry.findtext("a:id", "", ns).strip()
            published = entry.findtext("a:published", "", ns)[:10]
            authors = [
                clean_text(a.findtext("a:name", "", ns))
                for a in entry.findall("a:author", ns)
            ]
            pdf = abs_url.replace("/abs/", "/pdf/")
            paper = Paper(
                title=title,
                url=abs_url,
                pdf=pdf,
                authors=authors,
                source="arXiv",
                published=published,
                summary=summary,
            )
            paper.tags = derive_tags(title, summary)
            paper.score = score_paper(paper)
            papers.append(paper)
        time.sleep(3.1)  # arXiv asks clients to be polite.
    return papers


def parse_cvf_listing(conf_id: str, conf_name: str, url: str) -> list[Paper]:
    try:
        text = fetch_url(url, timeout=90)
    except Exception as exc:  # pragma: no cover - network resilience
        print(f"[warn] CVF fetch failed: {conf_name}: {exc}", file=sys.stderr)
        return []
    pattern = re.compile(
        r'<dt class="ptitle"><br><a href="(?P<link>[^"]+)">(?P<title>.*?)</a></dt>\s*<dd>(?P<dd>.*?)</dd>',
        re.S,
    )
    papers: list[Paper] = []
    for match in pattern.finditer(text):
        title = clean_text(re.sub("<.*?>", " ", match.group("title")))
        title_l = title.lower()
        if not any(kw in title_l for kw in COD_KEYWORDS + BROAD_KEYWORDS):
            continue
        link = "https://openaccess.thecvf.com" + match.group("link")
        pdf = link.replace("/html/", "/papers/").replace(".html", ".pdf")
        authors = [
            clean_text(a)
            for a in re.findall(
                r'<input type="hidden" name="query_author" value="([^"]+)">',
                match.group("dd"),
            )
        ]
        paper = Paper(
            title=title,
            url=link,
            pdf=pdf,
            authors=authors,
            source=conf_name,
            published=conf_id[-4:],
            summary="CVF OpenAccess paper. Open the paper page for full abstract and method details.",
        )
        paper.tags = derive_tags(title, paper.summary)
        paper.score = score_paper(paper)
        papers.append(paper)
    return papers


def fetch_cvf() -> list[Paper]:
    papers: list[Paper] = []
    for conf_id, conf_name, url in CVF_CONFERENCES:
        papers.extend(parse_cvf_listing(conf_id, conf_name, url))
        time.sleep(1.0)
    return papers


def dedupe(papers: list[Paper]) -> list[Paper]:
    seen: dict[str, Paper] = {}
    for paper in papers:
        key = re.sub(r"\W+", "", paper.title.lower())
        if not key:
            continue
        existing = seen.get(key)
        if existing is None or paper.score > existing.score:
            seen[key] = paper
    return list(seen.values())


def format_authors(authors: list[str], limit: int = 5) -> str:
    if not authors:
        return ""
    if len(authors) <= limit:
        return ", ".join(authors)
    return ", ".join(authors[:limit]) + " et al."


def why_read(paper: Paper) -> str:
    tags = set(paper.tags)
    if "COD" in tags:
        return "直接关联伪装目标检测/分割，优先看方法和消融。"
    if "open-vocabulary" in tags or "training-free" in tags:
        return "适合迁移到开放词汇、零样本或无训练 COD。"
    if "SAM" in tags or "VLM/MLLM" in tags:
        return "适合借鉴为 prompt 生成、mask 选择或视觉推理模块。"
    if "boundary/frequency" in tags or "depth/geometry" in tags:
        return "适合补充伪装场景中的边界、纹理、几何先验。"
    if "anomaly/OOD" in tags:
        return "可把伪装目标看作弱异常/低显著目标，借鉴不确定性与负样本思想。"
    if "remote sensing" in tags or "video" in tags:
        return "适合迁移多模态、时序或大场景密集推理方法。"
    return "方法上可能可迁移，建议先读摘要和图 1。"


def md_paper_item(idx: int, paper: Paper) -> str:
    authors = format_authors(paper.authors)
    tag_text = ", ".join(paper.tags)
    links = f"[paper]({paper.url})"
    if paper.pdf:
        links += f" / [pdf]({paper.pdf})"
    parts = [
        f"{idx}. **{paper.title}**",
        f"   - Source: {paper.source}" + (f", {paper.published}" if paper.published else ""),
    ]
    if authors:
        parts.append(f"   - Authors: {authors}")
    parts.extend(
        [
            f"   - Tags: {tag_text}",
            f"   - Links: {links}",
            f"   - 简介：{sentence_intro(paper.summary)}",
            f"   - 为什么值得读：{why_read(paper)}",
        ]
    )
    return "\n".join(parts)


def select_feed_sections(papers: list[Paper]) -> dict[str, list[Paper]]:
    cod = [p for p in papers if "COD" in p.tags]
    broad = [p for p in papers if "COD" not in p.tags]

    cod = sorted(cod, key=lambda p: p.score, reverse=True)[:35]
    broad = sorted(broad, key=lambda p: p.score, reverse=True)[:60]
    recent = [
        p
        for p in papers
        if (paper_age_days(p) is not None and paper_age_days(p) <= 30)
    ]
    highlights = sorted(recent, key=lambda p: (p.score, p.published), reverse=True)[:12]
    if len(highlights) < 8:
        fallback = [p for p in papers if p not in highlights]
        highlights.extend(sorted(fallback, key=lambda p: p.score, reverse=True)[: 12 - len(highlights)])
    return {
        "highlights": highlights,
        "cod": cod,
        "broad": broad,
    }


def paper_to_dict(paper: Paper) -> dict:
    return paper.__dict__


def paper_from_dict(data: dict) -> Paper:
    authors = data.get("authors", [])
    if not isinstance(authors, list):
        authors = []
    tags = data.get("tags", [])
    if not isinstance(tags, list):
        tags = []
    paper = Paper(
        title=data.get("title", ""),
        url=data.get("url", ""),
        pdf=data.get("pdf", ""),
        authors=authors,
        source=data.get("source", ""),
        published=data.get("published", ""),
        summary=data.get("summary", ""),
        tags=tags,
        score=int(data.get("score", 0)),
    )
    return paper


def previous_update_time() -> str:
    md_path = DOCS / "literature.md"
    if md_path.exists():
        try:
            text = md_path.read_text(encoding="utf-8")
        except OSError:
            text = ""
        match = re.search(r"^Last updated:\s*(.+?)\s+Asia/Shanghai", text, re.MULTILINE)
        if match:
            return match.group(1).strip()
    latest_path = DATA / "latest_papers.json"
    if latest_path.exists():
        ts = datetime.fromtimestamp(latest_path.stat().st_mtime, UTC8)
        return ts.strftime("%Y-%m-%d %H:%M")
    return datetime.now(UTC8).strftime("%Y-%m-%d %H:%M")


def legacy_snapshot_from_latest() -> dict | None:
    latest_path = DATA / "latest_papers.json"
    if not latest_path.exists():
        return None
    try:
        data = json.loads(latest_path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return None
    if not isinstance(data, list):
        return None
    papers = [paper_from_dict(item) for item in data if isinstance(item, dict)]
    if not papers:
        return None
    generated_at = previous_update_time()
    try:
        date_text = datetime.strptime(generated_at[:10], "%Y-%m-%d").strftime("%Y-%m-%d")
    except ValueError:
        date_text = datetime.now(UTC8).strftime("%Y-%m-%d")
    snapshot = make_snapshot(papers, datetime.now(UTC8))
    snapshot["date"] = date_text
    snapshot["generated_at"] = generated_at
    snapshot["legacy"] = True
    return snapshot


def load_history() -> list[dict]:
    if not HISTORY_FILE.exists():
        legacy = legacy_snapshot_from_latest()
        return [legacy] if legacy else []
    try:
        data = json.loads(HISTORY_FILE.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return []
    if not isinstance(data, list):
        return []
    return [item for item in data if isinstance(item, dict)]


def make_snapshot(papers: list[Paper], now: datetime) -> dict:
    sections = select_feed_sections(papers)
    return {
        "date": now.strftime("%Y-%m-%d"),
        "generated_at": now.strftime("%Y-%m-%d %H:%M"),
        "timezone": "Asia/Shanghai",
        "total_selected": len(papers),
        "sections": {
            name: [paper_to_dict(paper) for paper in section_papers]
            for name, section_papers in sections.items()
        },
    }


def update_history(papers: list[Paper], now: datetime) -> list[dict]:
    snapshot = make_snapshot(papers, now)
    history = [
        item
        for item in load_history()
        if item.get("generated_at") != snapshot["generated_at"]
    ]
    history.insert(0, snapshot)
    HISTORY_FILE.write_text(
        json.dumps(history, ensure_ascii=False, indent=2),
        encoding="utf-8",
        newline="\n",
    )
    return history


def snapshot_sections(snapshot: dict) -> dict[str, list[Paper]]:
    sections = snapshot.get("sections", {})
    if not isinstance(sections, dict):
        sections = {}
    return {
        "highlights": [paper_from_dict(item) for item in sections.get("highlights", [])],
        "cod": [paper_from_dict(item) for item in sections.get("cod", [])],
        "broad": [paper_from_dict(item) for item in sections.get("broad", [])],
    }


def render_markdown(history: list[dict]) -> str:
    now = datetime.now(UTC8)
    current = history[0] if history else {
        "generated_at": now.strftime("%Y-%m-%d %H:%M"),
        "total_selected": 0,
        "sections": {},
    }
    sections = snapshot_sections(current)
    highlights = sections["highlights"]
    cod = sections["cod"]
    broad = sections["broad"]
    history_items = history[1:]

    lines = [
        "# Daily CV Paper Feed",
        "",
        f"Last updated: {current.get('generated_at', now.strftime('%Y-%m-%d %H:%M'))} Asia/Shanghai",
        f"Archive days kept: {len(history)}",
        "",
        "This page tracks new and useful computer-vision papers, with COD/camouflaged object detection kept as the primary reading thread and broader CV methods included for inspiration.",
        "",
        "历史更新不会被删除；如果当天没看完，可以继续往下翻到对应日期。",
        "",
        "## 今日优先读：近 30 天新文献优先",
        "",
    ]
    for i, paper in enumerate(highlights, 1):
        lines.append(md_paper_item(i, paper))
        lines.append("")

    lines.extend(["## COD / 伪装目标检测相关", ""])
    for i, paper in enumerate(cod, 1):
        lines.append(md_paper_item(i, paper))
        lines.append("")

    lines.extend(["## 泛计算机视觉方法池", ""])
    for i, paper in enumerate(broad, 1):
        lines.append(md_paper_item(i, paper))
        lines.append("")

    if history_items:
        lines.extend(["## 历史更新归档", ""])
        for item in history_items:
            generated_at = item.get("generated_at", item.get("date", ""))
            sections = snapshot_sections(item)
            lines.append(f"## {generated_at} 更新")
            lines.append("")
            lines.append(f"Selected papers: {item.get('total_selected', 0)}")
            lines.append("")
            lines.append("### 当日优先读")
            lines.append("")
            for i, paper in enumerate(sections["highlights"], 1):
                lines.append(md_paper_item(i, paper))
                lines.append("")
            lines.append("### 当日 COD / 伪装目标检测相关")
            lines.append("")
            for i, paper in enumerate(sections["cod"], 1):
                lines.append(md_paper_item(i, paper))
                lines.append("")
            lines.append("### 当日泛计算机视觉方法池")
            lines.append("")
            for i, paper in enumerate(sections["broad"], 1):
                lines.append(md_paper_item(i, paper))
                lines.append("")

    lines.extend(
        [
            "## 阅读记录模板",
            "",
            "```text",
            "论文：",
            "任务设定：",
            "核心假设：",
            "方法模块：",
            "对 COD / 我的课题的可迁移点：",
            "我能改进的地方：",
            "```",
            "",
            "## 数据源",
            "",
            "- arXiv API: recent preprints from COD and broad CV queries.",
            "- CVF OpenAccess: CVPR 2026, WACV 2026, ICCV 2025 title-level scan.",
            "",
        ]
    )
    return "\n".join(lines)


def render_html(markdown_text: str) -> str:
    """Small Markdown subset renderer for this generated report."""
    body: list[str] = []
    in_code = False
    in_archive = False
    in_details = False
    for raw in markdown_text.splitlines():
        line = raw.rstrip()
        if line.startswith("```"):
            if not in_code:
                body.append("<pre><code>")
                in_code = True
            else:
                body.append("</code></pre>")
                in_code = False
            continue
        if in_code:
            body.append(html.escape(line))
            continue
        if line.startswith("# "):
            body.append(f"<h1>{html.escape(line[2:])}</h1>")
        elif line.startswith("## "):
            title = line[3:]
            if in_details:
                body.append("</details>")
                in_details = False
            if title == "历史更新归档":
                in_archive = True
                body.append(f"<h2>{html.escape(title)}</h2>")
            elif in_archive and title.endswith(" 更新"):
                body.append("<details class='archive-day'>")
                body.append(f"<summary>{html.escape(title)}</summary>")
                in_details = True
            else:
                body.append(f"<h2>{html.escape(title)}</h2>")
        elif line.startswith("### "):
            body.append(f"<h4>{html.escape(line[4:])}</h4>")
        elif re.match(r"^\d+\. \*\*", line):
            content = re.sub(r"^\d+\. ", "", line)
            body.append("<article class='paper'>")
            body.append("<h3>" + markdown_inline(content) + "</h3>")
        elif line.startswith("   - "):
            body.append("<p class='meta'>" + markdown_inline(line[5:]) + "</p>")
        elif line.strip() == "":
            if body and not body[-1].endswith("</article>"):
                # Close article when a paper block ends.
                if any(body[-1].startswith(prefix) for prefix in ["<p class='meta'", "<h3>"]):
                    body.append("</article>")
        else:
            body.append(f"<p>{markdown_inline(line)}</p>")
    if in_code:
        body.append("</code></pre>")
    if in_details:
        body.append("</details>")

    return f"""<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Daily CV Paper Feed</title>
  <style>
    :root {{
      color-scheme: light;
      --ink: #1f2933;
      --muted: #52606d;
      --line: #d9e2ec;
      --accent: #1d4ed8;
      --bg: #f8fafc;
      --card: #ffffff;
    }}
    body {{
      margin: 0;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "Noto Sans SC", sans-serif;
      background: var(--bg);
      color: var(--ink);
      line-height: 1.65;
    }}
    main {{
      max-width: 1100px;
      margin: 0 auto;
      padding: 32px 20px 56px;
    }}
    h1 {{ font-size: 32px; margin: 0 0 8px; }}
    h2 {{ margin-top: 40px; padding-bottom: 8px; border-bottom: 1px solid var(--line); }}
    h3 {{ margin: 0 0 10px; font-size: 18px; line-height: 1.4; }}
    h4 {{ margin: 22px 0 10px; font-size: 16px; }}
    a {{ color: var(--accent); text-decoration: none; }}
    a:hover {{ text-decoration: underline; }}
    .paper {{
      background: var(--card);
      border: 1px solid var(--line);
      border-radius: 8px;
      padding: 16px 18px;
      margin: 14px 0;
      box-shadow: 0 1px 2px rgba(15, 23, 42, 0.04);
    }}
    .meta {{ margin: 6px 0; color: var(--muted); }}
    .archive-day {{
      background: var(--card);
      border: 1px solid var(--line);
      border-radius: 8px;
      margin: 14px 0;
      padding: 8px 12px;
    }}
    .archive-day > summary {{
      cursor: pointer;
      font-weight: 700;
      color: var(--ink);
      padding: 6px 0;
    }}
    .archive-day .paper {{
      box-shadow: none;
      background: #fbfdff;
    }}
    pre {{
      background: #111827;
      color: #f9fafb;
      padding: 14px;
      border-radius: 8px;
      overflow: auto;
    }}
  </style>
</head>
<body>
<main>
{chr(10).join(body)}
</main>
</body>
</html>
"""


def markdown_inline(text: str) -> str:
    text = html.escape(text)
    text = re.sub(r"\*\*(.*?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', text)
    return text


def main() -> None:
    DATA.mkdir(exist_ok=True)
    DOCS.mkdir(exist_ok=True)

    print("[info] fetching arXiv")
    papers = fetch_arxiv()
    print(f"[info] arXiv papers: {len(papers)}")

    print("[info] fetching CVF")
    papers.extend(fetch_cvf())
    print(f"[info] total raw papers: {len(papers)}")

    papers = dedupe(papers)
    for paper in papers:
        paper.score = score_paper(paper)
    papers = [p for p in papers if p.score >= 12]
    papers.sort(key=lambda p: p.score, reverse=True)

    now = datetime.now(UTC8)
    history = update_history(papers, now)
    md = render_markdown(history)
    (DOCS / "literature.md").write_text(md, encoding="utf-8", newline="\n")
    (DOCS / "index.html").write_text(render_html(md), encoding="utf-8", newline="\n")

    serializable = [paper_to_dict(paper) for paper in papers]
    (DATA / "latest_papers.json").write_text(
        json.dumps(serializable, ensure_ascii=False, indent=2),
        encoding="utf-8",
        newline="\n",
    )
    print(f"[info] selected papers: {len(papers)}")
    print(f"[info] wrote {(DOCS / 'index.html')}")


if __name__ == "__main__":
    main()
