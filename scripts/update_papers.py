#!/usr/bin/env python3
"""Generate a daily computer-vision paper reading feed.

The script intentionally uses only Python's standard library so it can run
reliably on GitHub Actions without dependency installation.
"""

from __future__ import annotations

import html
import json
import re
import os
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
DEEP_SOURCE_SCAN = os.environ.get("DEEP_SOURCE_SCAN", "").lower() in {"1", "true", "yes"}

UTC8 = timezone(timedelta(hours=8))


ARXIV_QUERIES = [
    # COD / camouflage direct line
    'all:"camouflaged object detection"',
    'all:"camouflaged object segmentation"',
    'all:"concealed object detection"',
    'all:"concealed object segmentation"',
    'all:"open-vocabulary camouflaged"',
    'all:"training-free camouflaged"',
    'all:"unsupervised camouflaged object detection"',
    'all:"SAM" AND all:"camouflaged object detection"',
    'all:"frequency" AND all:"camouflaged object detection"',
    'all:"boundary" AND all:"camouflaged object detection"',
    'all:"depth" AND all:"camouflaged object detection"',
    'all:"salient object detection" AND all:"foundation model"',
    'all:"transparent object detection"',
    'all:"low contrast object detection"',
    # Broad CV methods likely useful for COD
    'all:"open-vocabulary segmentation"',
    'all:"training-free segmentation"',
    'all:"vision-language" AND all:"segmentation"',
    'all:"vision foundation model" AND all:"segmentation"',
    'all:"multimodal large language model" AND all:"grounding"',
    'all:"visual reasoning" AND all:"segmentation"',
    'all:"anomaly detection" AND all:"vision foundation model"',
    'all:"diffusion" AND all:"segmentation"',
    'all:"test-time adaptation" AND all:"segmentation"',
    'all:"weakly supervised segmentation" AND all:"foundation model"',
    'all:"domain generalization" AND all:"segmentation"',
    'all:"medical image segmentation" AND all:"foundation model"',
    'all:"remote sensing" AND all:"open-vocabulary segmentation"',
]


CVF_CONFERENCES = [
    ("CVPR2026", "CVPR 2026", "https://openaccess.thecvf.com/CVPR2026?day=all"),
    ("CVPR2025", "CVPR 2025", "https://openaccess.thecvf.com/CVPR2025?day=all"),
    ("WACV2026", "WACV 2026", "https://openaccess.thecvf.com/WACV2026?day=all"),
    ("WACV2025", "WACV 2025", "https://openaccess.thecvf.com/WACV2025?day=all"),
    ("ICCV2025", "ICCV 2025", "https://openaccess.thecvf.com/ICCV2025?day=all"),
    ("CVPR2024", "CVPR 2024", "https://openaccess.thecvf.com/CVPR2024?day=all"),
    ("ACCV2024", "ACCV 2024", "https://openaccess.thecvf.com/ACCV2024?day=all"),
]


SEMANTIC_SCHOLAR_QUERIES = [
    "camouflaged object detection",
    "concealed object detection segmentation",
    "open vocabulary segmentation vision language",
    "training free segmentation foundation model",
    "weakly supervised semantic segmentation foundation model",
    "vision language grounding segmentation",
    "multimodal large language model visual grounding",
    "segment anything model medical image segmentation",
    "test time adaptation semantic segmentation",
    "domain generalization semantic segmentation",
    "anomaly detection vision foundation model",
    "diffusion model segmentation",
    "salient object detection foundation model",
    "transparent object detection",
    "remote sensing open vocabulary segmentation",
    "small object detection dense prediction",
    "boundary aware segmentation frequency",
    "depth estimation segmentation geometry",
]


TOP_JOURNALS = [
    {
        "name": "IEEE Transactions on Pattern Analysis and Machine Intelligence",
        "short": "TPAMI",
        "rank": "CCF-A / 顶刊",
        "issn": "0162-8828",
    },
    {
        "name": "International Journal of Computer Vision",
        "short": "IJCV",
        "rank": "CCF-A / 顶刊",
        "issn": "0920-5691",
    },
    {
        "name": "IEEE Transactions on Image Processing",
        "short": "TIP",
        "rank": "CCF-A / 顶刊",
        "issn": "1057-7149",
    },
    {
        "name": "IEEE Transactions on Multimedia",
        "short": "TMM",
        "rank": "CCF-B / 顶刊",
        "issn": "1520-9210",
    },
    {
        "name": "IEEE Transactions on Circuits and Systems for Video Technology",
        "short": "TCSVT",
        "rank": "CCF-B / 顶刊",
        "issn": "1051-8215",
    },
    {
        "name": "Pattern Recognition",
        "short": "PR",
        "rank": "CCF-B / 顶刊",
        "issn": "0031-3203",
    },
    {
        "name": "Computer Vision and Image Understanding",
        "short": "CVIU",
        "rank": "CCF-B / 视觉期刊",
        "issn": "1077-3142",
    },
    {
        "name": "IEEE Transactions on Geoscience and Remote Sensing",
        "short": "TGRS",
        "rank": "遥感顶刊",
        "issn": "0196-2892",
    },
    {
        "name": "ISPRS Journal of Photogrammetry and Remote Sensing",
        "short": "ISPRS JPRS",
        "rank": "遥感顶刊",
        "issn": "0924-2716",
    },
    {
        "name": "Medical Image Analysis",
        "short": "MedIA",
        "rank": "医学影像顶刊",
        "issn": "1361-8415",
    },
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
    "detection",
    "detect",
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
    "salient",
    "saliency",
    "transparent",
    "low contrast",
    "small object",
    "dense prediction",
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
    "domain generalization",
    "domain adaptation",
    "medical image",
    "low-light",
    "restoration",
]


QUALITY_SOURCE_HINTS = {
    "cvpr": 14,
    "iccv": 14,
    "eccv": 14,
    "neurips": 12,
    "iclr": 12,
    "aaai": 10,
    "ijcai": 10,
    "acm multimedia": 10,
    "tpami": 16,
    "ijcv": 16,
    "tip": 14,
    "tmm": 12,
    "tcsvt": 12,
    "pattern recognition": 12,
    "cviu": 9,
    "tgrs": 10,
    "isprs": 10,
    "medical image analysis": 10,
    "journal": 6,
    "transactions": 6,
}


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


def strip_markup(text: str) -> str:
    text = re.sub(r"<[^>]+>", " ", text or "")
    return clean_text(text)


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
        ("saliency/transparent", ["salient", "saliency", "transparent", "low contrast"]),
        ("domain adaptation", ["domain generalization", "domain adaptation", "test-time adaptation"]),
        ("medical imaging", ["medical image", "mri", "ct", "ultrasound", "histopathology"]),
    ]
    for tag, words in checks:
        if any(w in text for w in words):
            tags.append(tag)
    if "SAM" in tags and not re.search(r"\b(segment anything|sam)\b", text):
        tags.remove("SAM")
    if "medical imaging" in tags and not re.search(
        r"\b(medical image|mri|ct|ultrasound|histopathology)\b", text
    ):
        tags.remove("medical imaging")
    return tags or ["computer vision"]


def score_paper(paper: Paper) -> int:
    text = f"{paper.title} {paper.summary}".lower()
    source = paper.source.lower()
    score = 0
    for kw in COD_KEYWORDS:
        if kw in text:
            score += 30
    for kw in BROAD_KEYWORDS:
        if kw in text:
            score += 6
    for hint, bonus in QUALITY_SOURCE_HINTS.items():
        if hint in source:
            score += bonus
    if "cvpr 2026" in source:
        score += 8
    if "iccv 2025" in source or "wacv 2026" in source:
        score += 5
    if "arxiv" in source:
        score += 3
    if "semantic scholar" in source:
        score += 4
    if "crossref" in source:
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


def fetch_semantic_scholar(max_results_per_query: int = 8) -> list[Paper]:
    papers: list[Paper] = []
    fields = ",".join(
        [
            "title",
            "abstract",
            "year",
            "venue",
            "authors",
            "url",
            "openAccessPdf",
            "publicationDate",
            "citationCount",
        ]
    )
    queries = SEMANTIC_SCHOLAR_QUERIES if DEEP_SOURCE_SCAN else SEMANTIC_SCHOLAR_QUERIES[:6]
    for query in queries:
        params = {
            "query": query,
            "limit": str(max_results_per_query),
            "year": "2024-",
            "fields": fields,
        }
        url = "https://api.semanticscholar.org/graph/v1/paper/search?" + urllib.parse.urlencode(params)
        try:
            data = json.loads(fetch_url(url, timeout=60))
        except Exception as exc:  # pragma: no cover - network resilience
            print(f"[warn] Semantic Scholar query failed: {query}: {exc}", file=sys.stderr)
            time.sleep(1.0)
            continue
        for item in data.get("data", []):
            title = clean_text(item.get("title", ""))
            if not title:
                continue
            summary = clean_text(item.get("abstract") or "")
            venue = clean_text(item.get("venue") or "")
            citation_count = item.get("citationCount") or 0
            published = item.get("publicationDate") or str(item.get("year") or "")
            authors = [
                clean_text(author.get("name", ""))
                for author in item.get("authors", [])
                if author.get("name")
            ]
            oa_pdf = item.get("openAccessPdf") or {}
            pdf = oa_pdf.get("url") or ""
            source = "Semantic Scholar"
            if venue:
                source += f" / {venue}"
            if citation_count:
                source += f" / citations {citation_count}"
            paper = Paper(
                title=title,
                url=item.get("url") or "",
                pdf=pdf,
                authors=authors,
                source=source,
                published=published[:10],
                summary=summary or f"Semantic Scholar result for query: {query}.",
            )
            paper.tags = derive_tags(title, paper.summary)
            paper.score = score_paper(paper)
            if citation_count >= 25:
                paper.score += 4
            papers.append(paper)
        time.sleep(1.0)
    return papers


def crossref_date(item: dict) -> str:
    for key in ["published-online", "published-print", "issued"]:
        date_parts = item.get(key, {}).get("date-parts")
        if not date_parts or not date_parts[0]:
            continue
        parts = [str(part) for part in date_parts[0]]
        if len(parts) == 1:
            return parts[0]
        if len(parts) == 2:
            return f"{int(parts[0]):04d}-{int(parts[1]):02d}"
        return f"{int(parts[0]):04d}-{int(parts[1]):02d}-{int(parts[2]):02d}"
    return ""


def crossref_authors(item: dict) -> list[str]:
    authors = []
    for author in item.get("author", [])[:12]:
        given = author.get("given", "")
        family = author.get("family", "")
        name = clean_text(f"{given} {family}")
        if name:
            authors.append(name)
    return authors


def fetch_crossref_journals(rows_per_query: int = 4) -> list[Paper]:
    papers: list[Paper] = []
    broad_query = (
        "camouflaged OR concealed OR segmentation OR detection OR "
        "vision-language OR foundation model OR anomaly"
    )
    deep_queries = [
        "camouflaged object detection",
        "concealed object detection",
        "open vocabulary segmentation",
        "vision language segmentation",
        "foundation model segmentation",
        "anomaly detection vision",
        "salient object detection",
        "remote sensing segmentation",
    ]
    queries = deep_queries if DEEP_SOURCE_SCAN else [broad_query]
    from_date = f"{datetime.now(UTC8).year - 1}-01-01"
    for journal in TOP_JOURNALS:
        for query in queries:
            params = {
                "filter": f"issn:{journal['issn']},from-pub-date:{from_date}",
                "query": query,
                "rows": str(rows_per_query),
                "sort": "published",
                "order": "desc",
                "select": "title,author,DOI,URL,published-print,published-online,issued,container-title,abstract",
            }
            url = "https://api.crossref.org/works?" + urllib.parse.urlencode(params)
            try:
                data = json.loads(fetch_url(url, timeout=60))
            except Exception as exc:  # pragma: no cover - network resilience
                print(
                    f"[warn] Crossref query failed: {journal['short']} / {query}: {exc}",
                    file=sys.stderr,
                )
                time.sleep(0.5)
                continue
            for item in data.get("message", {}).get("items", []):
                titles = item.get("title") or []
                title = clean_text(titles[0] if titles else "")
                if not title:
                    continue
                summary = strip_markup(item.get("abstract", ""))
                tag_text = f"{title} {summary}"
                if not summary and not any(
                    kw in title.lower() for kw in COD_KEYWORDS + BROAD_KEYWORDS
                ):
                    continue
                container = item.get("container-title") or [journal["name"]]
                venue = clean_text(container[0] if container else journal["name"])
                doi = clean_text(item.get("DOI", ""))
                paper = Paper(
                    title=title,
                    url=item.get("URL") or (f"https://doi.org/{doi}" if doi else ""),
                    pdf="",
                    authors=crossref_authors(item),
                    source=f"Crossref / {journal['short']} / {journal['rank']} / {venue}",
                    published=crossref_date(item),
                    summary=summary or f"{journal['short']} article matched by title in a top journal; abstract unavailable from Crossref.",
                )
                paper.tags = derive_tags(title, tag_text)
                paper.score = score_paper(paper)
                papers.append(paper)
            time.sleep(0.5)
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


def short_summary(paper: Paper) -> str:
    return sentence_intro(paper.summary, max_chars=210)


def task_setting(paper: Paper) -> str:
    tags = set(paper.tags)
    if "COD" in tags:
        return "伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。"
    if "open-vocabulary" in tags:
        return "开放词汇视觉识别/分割，目标类别或文本提示在训练时未必出现。"
    if "training-free" in tags:
        return "免训练或少训练迁移设定，重点看 prompt、特征选择和后处理。"
    if "SAM" in tags or "VLM/MLLM" in tags:
        return "基础模型驱动的视觉定位/分割/推理，可用于自动提示生成或 mask 筛选。"
    if "anomaly/OOD" in tags:
        return "异常检测或分布外识别，可类比伪装目标的弱异常发现。"
    if "remote sensing" in tags:
        return "遥感/大场景密集视觉任务，关注小目标、尺度变化和复杂背景。"
    if "medical imaging" in tags:
        return "医学影像分割/检测，常见弱边界、低对比和标注稀缺问题。"
    if "video" in tags:
        return "视频/时序视觉任务，关注跨帧一致性、运动线索和长期上下文。"
    return "通用计算机视觉任务，先判断是否能迁移到 COD 的感知、定位或分割环节。"


def method_core(paper: Paper) -> str:
    text = f"{paper.title} {paper.summary}".lower()
    cues = [
        (["counterfactual"], "反事实建模/拒识机制，用来降低误检或判断目标是否存在。"),
        (["diffusion", "generative"], "扩散/生成式建模，可能用于数据合成、先验建模或掩码优化。"),
        (["prompt"], "提示学习或提示生成，重点看文本/视觉 prompt 如何约束定位。"),
        (["sam", "segment anything"], "借助 SAM/基础分割模型产生候选 mask，再做筛选或适配。"),
        (["clip", "vision-language", "multimodal"], "视觉-语言对齐，把语义文本信息引入检测或分割。"),
        (["llm", "large language", "reasoning"], "多模态大模型推理，可能用于目标描述、区域判断或链式推理。"),
        (["frequency", "wavelet"], "频域/纹理特征增强，适合处理伪装背景与目标细粒度差异。"),
        (["boundary", "edge"], "边界感知建模，适合改善伪装目标轮廓不清的问题。"),
        (["depth", "geometry", "3d"], "几何/深度线索建模，可能补充 RGB 外的结构先验。"),
        (["test-time", "domain adaptation", "domain generalization"], "测试时适配或域泛化，重点看跨数据集鲁棒性。"),
        (["anomaly", "ood"], "异常/OOD 建模，把目标从复杂背景中作为低概率区域凸显出来。"),
    ]
    for words, description in cues:
        if any(word in text for word in words):
            return description
    return "摘要层面未显示明确模块，建议先看方法图确认 backbone、监督信号和损失设计。"


def experiment_takeaway(paper: Paper) -> str:
    text = paper.summary.lower()
    if not paper.summary or paper.summary.startswith("CVF OpenAccess paper"):
        return "当前来源只提供标题级信息；需要打开论文页确认数据集、指标和消融。"
    if any(word in text for word in ["state-of-the-art", "sota", "outperform", "superior"]):
        return "摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。"
    if any(word in text for word in ["benchmark", "dataset"]):
        return "可能包含新数据集/基准；适合看评测协议、失败案例和是否能服务 COD。"
    if any(word in text for word in ["ablation", "robust", "generalization"]):
        return "摘要强调消融、鲁棒性或泛化；适合优先看实验设计和跨域表现。"
    return "摘要未给出强实验信号；先看实验表格和图 1，再决定是否精读。"


def relation_to_topic(paper: Paper) -> str:
    tags = set(paper.tags)
    if "COD" in tags:
        return "和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。"
    if "saliency/transparent" in tags:
        return "和 COD 同属低显著/弱边界目标发现，可迁移目标-背景分离思想。"
    if "open-vocabulary" in tags or "training-free" in tags:
        return "适合拓展到开放词汇、零样本或少标注 COD。"
    if "boundary/frequency" in tags or "depth/geometry" in tags:
        return "可补充 COD 中纹理、边界、几何先验不足的问题。"
    if "VLM/MLLM" in tags or "reasoning" in tags:
        return "可用于伪装目标的语义描述、环境理解和候选区域判断。"
    if "anomaly/OOD" in tags:
        return "可把伪装目标看作复杂背景中的弱异常区域来借鉴。"
    return "不是 COD 直系论文，但可能提供可迁移的视觉表征、训练策略或评测思路。"


def borrow_points(paper: Paper) -> str:
    tags = set(paper.tags)
    points = []
    if "COD" in tags:
        points.append("数据集设置、评价指标、失败案例分析")
    if "open-vocabulary" in tags or "training-free" in tags:
        points.append("prompt 设计、类别文本构造、免训练迁移流程")
    if "SAM" in tags or "VLM/MLLM" in tags:
        points.append("候选 mask 生成、视觉-语言筛选、推理式定位")
    if "boundary/frequency" in tags:
        points.append("边界/频域增强模块")
    if "depth/geometry" in tags:
        points.append("深度或几何先验融合")
    if "domain adaptation" in tags or "anomaly/OOD" in tags:
        points.append("跨域鲁棒性、不确定性或异常分数")
    if not points:
        points.append("任务建模、损失函数、消融组织方式")
    return "；".join(points) + "。"


def improvement_ideas(paper: Paper) -> str:
    tags = set(paper.tags)
    if "COD" in tags and ("VLM/MLLM" not in tags and "SAM" not in tags):
        return "可尝试引入基础模型、文本先验或更强的环境上下文建模。"
    if "open-vocabulary" in tags or "training-free" in tags:
        return "可改进 prompt 自动生成、负样本约束和 mask 置信度校准。"
    if "SAM" in tags or "VLM/MLLM" in tags:
        return "可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。"
    if "boundary/frequency" in tags:
        return "可结合多尺度语义上下文，避免只强化纹理导致误检。"
    if "domain adaptation" in tags:
        return "可验证在 COD 跨数据集上的泛化，加入目标缺失场景。"
    return "可思考是否缺少 COD 场景验证、复杂背景失败分析或轻量化部署。"


def should_deep_read(paper: Paper) -> str:
    if "COD" in paper.tags and paper.score >= 45:
        return "值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。"
    if paper.score >= 55:
        return "建议精读：高质量来源或方法迁移价值较高。"
    if paper.score >= 35:
        return "建议泛读：先看摘要、图 1 和实验表，确认是否能迁移。"
    return "暂不精读：先收藏标题，需要相关模块时再回看。"


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
            f"   - 论文：{paper.title}",
            f"   - 一句话总结：{short_summary(paper)}",
            f"   - 任务设定：{task_setting(paper)}",
            f"   - 方法核心：{method_core(paper)}",
            f"   - 实验结论：{experiment_takeaway(paper)}",
            f"   - 和我课题的关系：{relation_to_topic(paper)}",
            f"   - 可借鉴点：{borrow_points(paper)}",
            f"   - 可改进点：{improvement_ideas(paper)}",
            f"   - 是否值得精读：{should_deep_read(paper)}",
        ]
    )
    return "\n".join(parts)


def select_feed_sections(papers: list[Paper]) -> dict[str, list[Paper]]:
    cod = [p for p in papers if "COD" in p.tags]
    broad = [p for p in papers if "COD" not in p.tags]
    quality = [
        p
        for p in papers
        if any(hint in p.source.lower() for hint in QUALITY_SOURCE_HINTS)
        or "crossref" in p.source.lower()
    ]

    cod = sorted(cod, key=lambda p: p.score, reverse=True)[:35]
    broad = sorted(broad, key=lambda p: p.score, reverse=True)[:60]
    quality = sorted(quality, key=lambda p: p.score, reverse=True)[:30]
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
        "quality": quality,
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
        "quality": [paper_from_dict(item) for item in sections.get("quality", [])],
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
    quality = sections["quality"]
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

    lines.extend(["## 高质量来源优先读：CCF-A/B 与顶刊顶会", ""])
    for i, paper in enumerate(quality, 1):
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
            lines.append("### 当日高质量来源优先读")
            lines.append("")
            for i, paper in enumerate(sections["quality"], 1):
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
            "- arXiv API: recent preprints from COD, weak/salient/transparent objects, VLM, segmentation, diffusion, adaptation, medical and remote-sensing queries.",
            "- CVF OpenAccess: CVPR/ECCV/ICCV/WACV title-level scan.",
            "- Semantic Scholar Graph API: broad high-quality venue and topic search when rate limits allow.",
            "- Crossref API: TPAMI, IJCV, TIP, TMM, TCSVT, Pattern Recognition, CVIU, TGRS, ISPRS JPRS, Medical Image Analysis.",
            "",
            "说明：自动简介是基于题名、摘要和来源的初筛笔记，不等同于阅读全文后的结论；精读时建议再核对 method、experiment 和 limitation。",
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

    print("[info] fetching Semantic Scholar")
    papers.extend(fetch_semantic_scholar())
    print(f"[info] total raw papers: {len(papers)}")

    print("[info] fetching Crossref journals")
    papers.extend(fetch_crossref_journals())
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
