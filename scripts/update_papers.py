#!/usr/bin/env python3
"""Generate a daily computer-vision paper reading feed.

The script intentionally uses only Python's standard library so it can run
reliably on GitHub Actions without dependency installation.
"""

from __future__ import annotations

import html
import hashlib
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
from datetime import date, datetime, timedelta, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
DATA = ROOT / "data"
DAILY_MD = DOCS / "md"
DAILY_HTML = DOCS / "html"
HISTORY_FILE = DATA / "feed_history.json"
ABSTRACT_DETAILS_FILE = DATA / "abstract_details.json"
DEEP_SOURCE_SCAN = os.environ.get("DEEP_SOURCE_SCAN", "").lower() in {"1", "true", "yes"}

HIGHLIGHT_LIMIT = 5
QUALITY_LIMIT = 10
COD_LIMIT = 12
UAV_LIMIT = 10
FIRE_MULTISPECTRAL_LIMIT = 10
FIRE_FOUNDATION_LIMIT = 10
BROAD_LIMIT = 12
DOWNLOAD_LIMIT = 5
DOWNLOAD_ROOT = Path(
    os.environ.get("PAPER_DOWNLOAD_ROOT", r"F:\文献整理\每日精读论文")
)
DOWNLOAD_INDEX_NAME = "_downloaded_papers.json"
ZOTERO_IMPORT_DISABLED = os.environ.get("ZOTERO_IMPORT_DISABLED", "").lower() in {
    "1",
    "true",
    "yes",
}
ZOTERO_ROOT_COLLECTION = os.environ.get("ZOTERO_ROOT_COLLECTION", "每日精读论文")

UTC8 = timezone(timedelta(hours=8))
FIRE_TOPIC_START_DATE = date(2026, 7, 14)


def fire_topic_enabled(at: date | datetime | str | None = None) -> bool:
    if at is None:
        current_date = datetime.now(UTC8).date()
    elif isinstance(at, datetime):
        current_date = at.astimezone(UTC8).date() if at.tzinfo else at.date()
    elif isinstance(at, str):
        current_date = date.fromisoformat(at[:10])
    else:
        current_date = at
    return current_date >= FIRE_TOPIC_START_DATE


ARXIV_QUERIES = [
    # COD / camouflage direct line. These are kept as anchors, but the daily
    # deep-read queue is intentionally biased toward transferable methods below.
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
    # Cross-domain method papers that may open new COD research directions
    'all:"object discovery" AND all:"foundation model"',
    'all:"open-world segmentation"',
    'all:"referring image segmentation" AND all:"reasoning"',
    'all:"visual prompt" AND all:"segmentation"',
    'all:"negative prompt" AND all:"segmentation"',
    'all:"uncertainty" AND all:"segmentation"',
    'all:"calibration" AND all:"segmentation"',
    'all:"out-of-distribution" AND all:"segmentation"',
    'all:"counterfactual" AND all:"vision"',
    'all:"causal" AND all:"segmentation"',
    'all:"self-supervised" AND all:"dense prediction"',
    'all:"representation learning" AND all:"dense prediction"',
    'all:"object-centric" AND all:"vision"',
    'all:"compositional" AND all:"segmentation"',
    'all:"interactive segmentation" AND all:"foundation model"',
    'all:"active learning" AND all:"segmentation"',
    'all:"continual learning" AND all:"segmentation"',
    'all:"world model" AND all:"vision"',
    'all:"concept bottleneck" AND all:"vision"',
    # UAV / aerial tiny-object perception
    'all:"UAV small object detection"',
    'all:"drone small object detection"',
    'all:"aerial tiny object detection"',
    'all:"small target detection" AND all:"UAV"',
    'all:"UAV object tracking" AND all:"small object"',
    'all:"aerial image" AND all:"small object segmentation"',
    'all:"UAV" AND all:"foundation model" AND all:"detection"',
    'all:"drone" AND all:"vision-language" AND all:"detection"',
]


FIRE_ARXIV_QUERIES = [
    # Multispectral fire detection
    'all:"multispectral fire detection"',
    'all:"multispectral wildfire detection"',
    'all:"visible infrared" AND all:"fire detection"',
    'all:"thermal infrared" AND all:"wildfire detection"',
    'all:"hyperspectral" AND all:"fire detection"',
    'all:"VIIRS" AND all:"active fire"',
    'all:"Sentinel-2" AND all:"wildfire detection"',
    # Foundation models and large multimodal models for fire monitoring
    'all:"wildfire monitoring" AND all:"foundation model"',
    'all:"wildfire detection" AND all:"vision-language"',
    'all:"fire monitoring" AND all:"multimodal large language model"',
    'all:"wildfire" AND all:"segment anything"',
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
    "object discovery foundation model vision",
    "open world segmentation",
    "referring image segmentation visual reasoning",
    "uncertainty calibration semantic segmentation",
    "out of distribution segmentation dense prediction",
    "counterfactual causal vision segmentation",
    "self supervised dense prediction representation learning",
    "object centric learning computer vision",
    "compositional visual reasoning segmentation",
    "interactive segmentation foundation model",
    "active learning semantic segmentation",
    "continual learning dense prediction",
    "visual concept bottleneck model",
    "UAV small object detection",
    "drone tiny object detection",
    "aerial image small target detection",
    "UAV small object tracking",
    "aerial dense object detection occlusion",
    "UAV foundation model object detection",
    "drone vision language object grounding",
]


FIRE_SEMANTIC_SCHOLAR_QUERIES = [
    "multispectral wildfire fire detection",
    "visible thermal infrared fire smoke detection",
    "hyperspectral wildfire active fire detection",
    "Sentinel-2 VIIRS multispectral active fire detection",
    "wildfire monitoring foundation model remote sensing",
    "fire smoke detection vision language model",
    "wildfire multimodal large language model",
    "wildfire segment anything foundation model",
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
        "name": "Remote Sensing of Environment",
        "short": "RSE",
        "rank": "遥感顶刊",
        "issn": "0034-4257",
    },
    {
        "name": "International Journal of Applied Earth Observation and Geoinformation",
        "short": "JAG",
        "rank": "遥感高水平期刊",
        "issn": "1569-8432",
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


FIRE_CONTEXT_KEYWORDS = [
    "wildfire",
    "wildland fire",
    "forest fire",
    "fire detection",
    "fire monitoring",
    "fire segmentation",
    "flame detection",
    "smoke detection",
    "fire smoke",
    "active fire",
    "burned area",
    "burnt area",
]


MULTISPECTRAL_FIRE_MODALITY_KEYWORDS = [
    "multispectral",
    "multi-spectral",
    "hyperspectral",
    "thermal infrared",
    "thermal-infrared",
    "visible infrared",
    "visible-infrared",
    "visible thermal",
    "visible-thermal",
    "infrared-visible",
    "rgb-t",
    "rgbt",
    "rgb-ir",
    "infrared",
    "thermal",
    "multi-band",
    "multiband",
    "spectral band",
    "sentinel-2",
    "landsat",
    "modis",
    "viirs",
    "multi-sensor",
    "multisensor",
]


FIRE_FOUNDATION_MODEL_KEYWORDS = [
    "foundation model",
    "vision foundation model",
    "remote sensing foundation model",
    "vision-language model",
    "vision language model",
    "large vision-language model",
    "large vision language model",
    "multimodal large language model",
    "large multimodal model",
    "large language model",
    "segment anything",
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
    "object discovery",
    "object-centric",
    "open-world",
    "open set",
    "uncertainty",
    "calibration",
    "counterfactual",
    "causal",
    "invariant",
    "self-supervised",
    "masked image modeling",
    "dense feature",
    "representation learning",
    "interactive",
    "active learning",
    "continual learning",
    "compositional",
    "concept bottleneck",
    "world model",
    "uav",
    "drone",
    "aerial",
    "tiny object",
    "small target",
    "low altitude",
    "foundation model",
]


DIRECT_COD_SCORE = 18
MULTISPECTRAL_FIRE_SCORE = 18
FIRE_FOUNDATION_MODEL_SCORE = 20
DIRECT_COD_HIGHLIGHT_LIMIT = 1
MIN_IDEA_TRANSFER_SCORE = 18
NON_COD_IDEA_BONUS = 8

IDEA_TRANSFER_KEYWORD_WEIGHTS = {
    "counterfactual": 12,
    "causal": 10,
    "invariant": 8,
    "uncertainty": 10,
    "calibration": 8,
    "open-world": 10,
    "open world": 10,
    "open set": 8,
    "out-of-distribution": 10,
    "object discovery": 12,
    "object-centric": 10,
    "compositional": 9,
    "concept bottleneck": 9,
    "self-supervised": 9,
    "masked image modeling": 8,
    "representation learning": 8,
    "dense feature": 8,
    "interactive segmentation": 8,
    "active learning": 7,
    "continual learning": 7,
    "world model": 8,
    "reasoning": 8,
    "negative prompt": 7,
    "referring image segmentation": 7,
    "uav": 9,
    "drone": 9,
    "aerial": 8,
    "tiny object": 10,
    "small target": 10,
}

TRANSFER_TAG_WEIGHTS = {
    "causal/counterfactual": 14,
    "uncertainty/calibration": 12,
    "open-world": 12,
    "object discovery": 12,
    "object-centric": 10,
    "self-supervised": 10,
    "representation learning": 10,
    "compositionality": 9,
    "active/interactive": 8,
    "continual learning": 8,
    "reasoning": 8,
    "VLM/MLLM": 8,
    "SAM": 7,
    "open-vocabulary": 7,
    "training-free": 7,
    "anomaly/OOD": 7,
    "domain adaptation": 7,
    "diffusion": 6,
    "boundary/frequency": 6,
    "depth/geometry": 6,
    "remote sensing": 5,
    "medical imaging": 5,
    "video": 5,
    "UAV/small-object": 10,
    "multispectral fire": 12,
    "fire foundation model": 12,
}

TRANSFER_TAGS = set(TRANSFER_TAG_WEIGHTS)


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
    "remote sensing of environment": 14,
    "applied earth observation": 11,
    "igarss": 10,
    "medical image analysis": 10,
    "journal": 6,
    "transactions": 6,
}

RECENT_PUBLISHED_YEAR_WINDOW = 2
ARXIV_HIGHLIGHT_MAX_AGE_DAYS = 180
ARXIV_HIGHLIGHT_MIN_SCORE = 45
PUBLISHED_SOURCE_BONUS = 10
ARXIV_SOURCE_PENALTY = 5
STRONG_ARXIV_TAGS = {
    "COD",
    "open-vocabulary",
    "training-free",
    "SAM",
    "VLM/MLLM",
    "reasoning",
    "diffusion",
    "domain adaptation",
    "remote sensing",
    "saliency/transparent",
    "multispectral fire",
    "fire foundation model",
} | TRANSFER_TAGS


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


def fetch_bytes(url: str, timeout: int = 90) -> tuple[bytes, str]:
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": "cv-paper-feed/1.0 (daily literature monitor; contact: none)"
        },
    )
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        content_type = resp.headers.get("content-type", "")
        return resp.read(), content_type


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


def fire_context_signal(text: str) -> bool:
    text = text.lower()
    return any(keyword in text for keyword in FIRE_CONTEXT_KEYWORDS)


def multispectral_fire_signal(text: str) -> bool:
    text = text.lower()
    return fire_context_signal(text) and any(
        keyword in text for keyword in MULTISPECTRAL_FIRE_MODALITY_KEYWORDS
    )


def fire_foundation_model_signal(text: str) -> bool:
    text = text.lower()
    return fire_context_signal(text) and any(
        keyword in text for keyword in FIRE_FOUNDATION_MODEL_KEYWORDS
    )


def derive_tags(
    title: str,
    summary: str,
    *,
    include_fire: bool | None = None,
) -> list[str]:
    text = f"{title} {summary}".lower()
    tags = []
    if include_fire is None:
        include_fire = fire_topic_enabled()
    if include_fire:
        if multispectral_fire_signal(text):
            tags.append("multispectral fire")
        if fire_foundation_model_signal(text):
            tags.append("fire foundation model")
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
        (
            "UAV/small-object",
            [
                "uav",
                "drone",
                "aerial image",
                "aerial imagery",
                "tiny object",
                "small target",
                "small object detection",
                "low-altitude",
            ],
        ),
        ("anomaly/OOD", ["anomaly", "ood", "out-of-distribution"]),
        ("causal/counterfactual", ["causal", "causality", "counterfactual"]),
        ("uncertainty/calibration", ["uncertainty", "calibration", "confidence"]),
        ("open-world", ["open-world", "open world", "open-set", "open set"]),
        ("object discovery", ["object discovery", "class-agnostic discovery"]),
        ("object-centric", ["object-centric", "object centric"]),
        ("self-supervised", ["self-supervised", "self supervised", "masked image modeling"]),
        ("representation learning", ["representation learning", "dense feature", "dense representation"]),
        ("compositionality", ["compositional", "composition"]),
        ("active/interactive", ["interactive segmentation", "active learning"]),
        ("continual learning", ["continual learning", "lifelong learning"]),
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


def direct_cod_signal(text: str) -> bool:
    return any(kw in text for kw in COD_KEYWORDS)


def idea_keyword_score(text: str) -> int:
    return sum(
        bonus for keyword, bonus in IDEA_TRANSFER_KEYWORD_WEIGHTS.items() if keyword in text
    )


def score_paper(paper: Paper) -> int:
    text = f"{paper.title} {paper.summary}".lower()
    source = paper.source.lower()
    score = 0
    is_direct_cod = direct_cod_signal(text)
    if is_direct_cod:
        score += DIRECT_COD_SCORE
    if fire_topic_enabled():
        if multispectral_fire_signal(text):
            score += MULTISPECTRAL_FIRE_SCORE
        if fire_foundation_model_signal(text):
            score += FIRE_FOUNDATION_MODEL_SCORE
    for kw in BROAD_KEYWORDS:
        if kw in text:
            score += 6
    idea_score = idea_keyword_score(text)
    score += idea_score
    if not is_direct_cod and idea_score >= 8:
        score += NON_COD_IDEA_BONUS
    for hint, bonus in QUALITY_SOURCE_HINTS.items():
        if hint in source:
            score += bonus
    if "arxiv" not in source and (
        any(hint in source for hint in QUALITY_SOURCE_HINTS) or "crossref" in source
    ):
        score += PUBLISHED_SOURCE_BONUS
    if "cvpr 2026" in source:
        score += 8
    if "iccv 2025" in source or "wacv 2026" in source:
        score += 5
    if "arxiv" in source:
        score -= ARXIV_SOURCE_PENALTY
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


def has_real_abstract(paper: Paper) -> bool:
    summary = clean_text(paper.summary)
    if len(summary) < 120:
        return False
    placeholders = [
        "CVF OpenAccess paper.",
        "Semantic Scholar result for query:",
        "abstract unavailable from Crossref",
    ]
    return not any(marker.lower() in summary.lower() for marker in placeholders)


def fetch_cvf_abstract(paper: Paper) -> str:
    if "openaccess.thecvf.com" not in paper.url:
        return ""
    page = fetch_url(paper.url, timeout=35)
    match = re.search(r'<div id="abstract"[^>]*>(.*?)</div>', page, re.S | re.I)
    if not match:
        return ""
    abstract = strip_markup(match.group(1))
    return abstract if len(abstract) >= 120 else ""


def enrich_paper_abstracts(papers: list[Paper]) -> None:
    for paper in papers:
        if has_real_abstract(paper):
            continue
        try:
            abstract = fetch_cvf_abstract(paper)
        except Exception as exc:  # pragma: no cover - network resilience
            print(f"[warn] abstract fetch failed: {paper.title}: {exc}", file=sys.stderr)
            continue
        if not abstract:
            continue
        paper.summary = abstract
        paper.tags = derive_tags(paper.title, abstract)
        paper.score = score_paper(paper)
        time.sleep(0.2)


def paper_age_days(paper: Paper) -> int | None:
    if not paper.published or not re.match(r"^\d{4}-\d{2}-\d{2}", paper.published):
        return None
    try:
        pub = datetime.fromisoformat(paper.published[:10]).replace(tzinfo=timezone.utc)
    except ValueError:
        return None
    return (datetime.now(timezone.utc) - pub).days


def publication_year(paper: Paper) -> int | None:
    text = f"{paper.published} {paper.source}"
    match = re.search(r"\b(20\d{2})\b", text)
    if not match:
        return None
    return int(match.group(1))


def is_arxiv(paper: Paper) -> bool:
    return "arxiv" in paper.source.lower()


def has_quality_published_source(paper: Paper) -> bool:
    source = paper.source.lower()
    if is_arxiv(paper):
        return False
    return "crossref" in source or any(hint in source for hint in QUALITY_SOURCE_HINTS)


def transfer_potential(paper: Paper) -> int:
    tags = set(paper.tags)
    text = f"{paper.title} {paper.summary}".lower()
    score = sum(TRANSFER_TAG_WEIGHTS[tag] for tag in tags if tag in TRANSFER_TAG_WEIGHTS)
    score += min(24, idea_keyword_score(text))
    if "COD" not in tags and score > 0:
        score += NON_COD_IDEA_BONUS
    if has_quality_published_source(paper):
        score += 6
    if is_arxiv(paper):
        age = paper_age_days(paper)
        if age is not None and age <= ARXIV_HIGHLIGHT_MAX_AGE_DAYS:
            score += 3
    if "COD" in tags and not (tags & TRANSFER_TAGS):
        score -= 6
    return score


def is_recent_published_source(paper: Paper) -> bool:
    year = publication_year(paper)
    if year is None:
        return False
    current_year = datetime.now(UTC8).year
    return (
        has_quality_published_source(paper)
        and year >= current_year - RECENT_PUBLISHED_YEAR_WINDOW
    )


def is_high_quality_arxiv(paper: Paper) -> bool:
    if not is_arxiv(paper):
        return False
    age = paper_age_days(paper)
    if age is None or age > ARXIV_HIGHLIGHT_MAX_AGE_DAYS:
        return False
    strong_tags = set(paper.tags) & STRONG_ARXIV_TAGS
    if transfer_potential(paper) >= MIN_IDEA_TRANSFER_SCORE and paper.score >= 35:
        return True
    if "COD" in strong_tags and paper.score >= ARXIV_HIGHLIGHT_MIN_SCORE - 3:
        return True
    return paper.score >= ARXIV_HIGHLIGHT_MIN_SCORE and len(strong_tags) >= 2


def highlight_tier(paper: Paper) -> int:
    potential = transfer_potential(paper)
    if is_recent_published_source(paper) and potential >= MIN_IDEA_TRANSFER_SCORE:
        return 5
    if is_recent_published_source(paper):
        return 4
    if has_quality_published_source(paper) and potential >= MIN_IDEA_TRANSFER_SCORE:
        return 4
    if has_quality_published_source(paper):
        return 3
    if is_high_quality_arxiv(paper):
        return 2
    if "COD" in paper.tags and paper.score >= ARXIV_HIGHLIGHT_MIN_SCORE:
        return 1
    return 0


def highlight_rank(paper: Paper) -> tuple[int, int, int, int, int, str]:
    return (
        highlight_tier(paper),
        transfer_potential(paper),
        int("COD" not in paper.tags),
        paper.score,
        publication_year(paper) or 0,
        paper.published,
    )


def topic_rank(paper: Paper) -> tuple[int, int, int, int, str]:
    source = paper.source.lower()
    source_quality = max(
        (bonus for hint, bonus in QUALITY_SOURCE_HINTS.items() if hint in source),
        default=0,
    )
    return (
        int(has_quality_published_source(paper)),
        source_quality,
        paper.score,
        publication_year(paper) or 0,
        paper.published,
    )


def is_pure_cod_anchor(paper: Paper) -> bool:
    return "COD" in paper.tags and transfer_potential(paper) < MIN_IDEA_TRANSFER_SCORE


def paper_identity_keys(paper: Paper) -> set[str]:
    keys: set[str] = set()
    normalized_title = re.sub(r"\W+", "", paper.title.casefold())
    if normalized_title:
        digest = hashlib.sha1(normalized_title.encode("utf-8")).hexdigest()
        keys.add("title:" + digest)

    for raw_url in (paper.url, paper.pdf):
        if not raw_url:
            continue
        url = urllib.parse.unquote(raw_url.strip())
        arxiv = re.search(r"arxiv\.org/(?:abs|pdf)/([^?#]+)", url, re.I)
        if arxiv:
            arxiv_id = arxiv.group(1).removesuffix(".pdf")
            arxiv_id = re.sub(r"v\d+$", "", arxiv_id, flags=re.I)
            keys.add("arxiv:" + arxiv_id.casefold())

        doi = re.search(r"(?:doi\.org/)?(10\.\d{4,9}/[^?#\s]+)", url, re.I)
        if doi:
            keys.add("doi:" + doi.group(1).rstrip("/.").casefold())

        parsed = urllib.parse.urlsplit(url)
        host = parsed.netloc.casefold().removeprefix("www.")
        path = parsed.path.rstrip("/").casefold()
        if host and path:
            digest = hashlib.sha1(f"{host}{path}".encode("utf-8")).hexdigest()
            keys.add("url:" + digest)
    return keys


def select_highlights(
    papers: list[Paper],
    excluded_keys: set[str] | None = None,
    initial_pure_cod_count: int = 0,
) -> list[Paper]:
    highlight_pool = [
        paper
        for paper in papers
        if highlight_tier(paper) > 0 or transfer_potential(paper) >= MIN_IDEA_TRANSFER_SCORE
    ]
    ranked = sorted(highlight_pool, key=highlight_rank, reverse=True)
    highlights: list[Paper] = []
    selected_keys = set(excluded_keys or ())
    pure_cod_count = initial_pure_cod_count
    for paper in ranked:
        identity_keys = paper_identity_keys(paper)
        if not identity_keys or not selected_keys.isdisjoint(identity_keys):
            continue
        if is_pure_cod_anchor(paper):
            if pure_cod_count >= DIRECT_COD_HIGHLIGHT_LIMIT:
                continue
            pure_cod_count += 1
        highlights.append(paper)
        selected_keys.update(identity_keys)
        if len(highlights) >= HIGHLIGHT_LIMIT:
            break

    if len(highlights) < HIGHLIGHT_LIMIT:
        for paper in sorted(papers, key=highlight_rank, reverse=True):
            identity_keys = paper_identity_keys(paper)
            if not identity_keys or not selected_keys.isdisjoint(identity_keys):
                continue
            if is_pure_cod_anchor(paper):
                if pure_cod_count >= DIRECT_COD_HIGHLIGHT_LIMIT:
                    continue
                pure_cod_count += 1
            highlights.append(paper)
            selected_keys.update(identity_keys)
            if len(highlights) >= HIGHLIGHT_LIMIT:
                break
    return highlights


def fetch_arxiv(max_results_per_query: int = 18) -> list[Paper]:
    ns = {"a": "http://www.w3.org/2005/Atom"}
    papers: list[Paper] = []
    queries = list(ARXIV_QUERIES)
    if fire_topic_enabled():
        queries.extend(FIRE_ARXIV_QUERIES)
    for query in queries:
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
        text = fetch_url(url, timeout=25)
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
    queries = (
        list(SEMANTIC_SCHOLAR_QUERIES)
        if DEEP_SOURCE_SCAN
        else list(SEMANTIC_SCHOLAR_QUERIES[:6])
    )
    if fire_topic_enabled():
        queries.extend(FIRE_SEMANTIC_SCHOLAR_QUERIES)
    for query in queries:
        params = {
            "query": query,
            "limit": str(max_results_per_query),
            "year": "2024-",
            "fields": fields,
        }
        url = "https://api.semanticscholar.org/graph/v1/paper/search?" + urllib.parse.urlencode(params)
        try:
            data = json.loads(fetch_url(url, timeout=25))
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
    fire_queries = [
        "multispectral wildfire detection",
        "thermal infrared fire smoke detection",
        "wildfire monitoring foundation model vision language",
    ]
    queries = list(deep_queries) if DEEP_SOURCE_SCAN else [broad_query]
    if fire_topic_enabled():
        if not DEEP_SOURCE_SCAN:
            queries[0] += " OR wildfire OR fire monitoring"
        queries.extend(fire_queries)
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
                data = json.loads(fetch_url(url, timeout=25))
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
    if {"multispectral fire", "fire foundation model"} <= tags:
        return "同时覆盖多光谱感知和大模型推理，可重点看跨模态对齐、时空监测与告警可靠性。"
    if "multispectral fire" in tags:
        return "直接覆盖多光谱火灾探测，可重点看可见光、红外/热红外与遥感波段如何互补。"
    if "fire foundation model" in tags:
        return "直接覆盖火灾监测大模型，可重点看基础模型适配、开放场景泛化和可解释告警。"
    if tags & {
        "causal/counterfactual",
        "uncertainty/calibration",
        "open-world",
        "object discovery",
        "object-centric",
        "self-supervised",
        "representation learning",
        "compositionality",
    }:
        return "不是只看任务相似度，而是看它能否给 COD 带来新的建模角度、假设或实验问题。"
    if "COD" in tags:
        return "直接关联伪装目标检测/分割，主要作为背景、对照和失败案例参考。"
    if "open-vocabulary" in tags or "training-free" in tags:
        return "适合迁移到开放词汇、零样本或无训练 COD。"
    if "SAM" in tags or "VLM/MLLM" in tags:
        return "适合借鉴为 prompt 生成、mask 选择或视觉推理模块。"
    if "boundary/frequency" in tags or "depth/geometry" in tags:
        return "适合补充伪装场景中的边界、纹理、几何先验。"
    if "anomaly/OOD" in tags:
        return "可把伪装目标看作弱异常/低显著目标，借鉴不确定性与负样本思想。"
    if "UAV/small-object" in tags:
        return "无人机小目标与 COD 都需要在复杂背景中保留微弱目标证据，可重点借鉴多尺度特征、密集检测和高效推理。"
    if "remote sensing" in tags or "video" in tags:
        return "适合迁移多模态、时序或大场景密集推理方法。"
    return "方法上可能可迁移，建议先读摘要和图 1。"


def short_summary(paper: Paper) -> str:
    return sentence_intro(paper.summary, max_chars=210)


def task_setting(paper: Paper) -> str:
    tags = set(paper.tags)
    if {"multispectral fire", "fire foundation model"} <= tags:
        return "多光谱火灾感知与基础模型联合监测，关注跨模态融合、早期发现、时空推理、误报控制和跨区域泛化。"
    if "multispectral fire" in tags:
        return "可见光、红外/热红外、高光谱或多传感器火灾探测，关注早期火焰/烟雾发现、复杂环境误报和全天候监测。"
    if "fire foundation model" in tags:
        return "基础模型或视觉语言大模型驱动的火灾监测，关注开放场景识别、时空理解、告警解释和少样本迁移。"
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
    if "UAV/small-object" in tags:
        return "无人机/航拍小目标检测、分割或跟踪，重点处理目标像素少、尺度变化大、密集遮挡、运动模糊和边缘部署限制。"
    if "remote sensing" in tags:
        return "遥感/大场景密集视觉任务，关注小目标、尺度变化和复杂背景。"
    if "medical imaging" in tags:
        return "医学影像分割/检测，常见弱边界、低对比和标注稀缺问题。"
    if "video" in tags:
        return "视频/时序视觉任务，关注跨帧一致性、运动线索和长期上下文。"
    return "通用计算机视觉任务，先判断是否能迁移到 COD 的感知、定位或分割环节。"


def method_core(paper: Paper) -> str:
    text = f"{paper.title} {paper.summary}".lower()
    tags = set(paper.tags)
    if {"multispectral fire", "fire foundation model"} <= tags:
        return "融合多光谱/多传感器观测与基础模型语义推理，用于火情定位、演化理解和可靠告警。"
    if "multispectral fire" in tags:
        return "融合可见光、红外/热红外、高光谱或卫星多波段信息，增强微弱火焰、烟雾和热点的可分辨性。"
    if "fire foundation model" in tags:
        return "利用视觉基础模型、视觉语言模型或多模态大模型进行火情识别、区域定位、时序理解或告警解释。"
    if "neural architecture search" in text or re.search(r"\bnas\b", text):
        return "神经架构搜索/结构自动设计，重点看搜索空间、效率约束和是否适合 COD 解码器。"
    if re.search(r"\b(segment anything|sam)\b", text):
        return "借助 SAM/基础分割模型产生候选 mask，再做筛选或适配。"
    cues = [
        (["uncertainty", "calibration", "confidence"], "不确定性/置信度校准建模，可用于判断伪装区域是否可靠、是否需要拒识或二次推理。"),
        (["open-world", "open world", "open-set", "open set"], "开放世界/开放集设定，适合思考 COD 中未知目标、目标缺失和非目标干扰的判别边界。"),
        (["object discovery"], "类别无关目标发现，适合把 COD 从固定类别分割改写成复杂背景中的潜在目标发现问题。"),
        (["object-centric", "object centric"], "对象中心表征学习，适合把目标从背景纹理中解耦出来，形成更强的候选对象假设。"),
        (["self-supervised", "masked image modeling", "representation learning", "dense feature"], "自监督/稠密表征学习，重点看无需 COD 标注时如何获得可迁移的局部结构与语义特征。"),
        (["compositional", "concept bottleneck"], "组合式或概念瓶颈建模，可把 COD 拆成颜色、纹理、边界、环境关系等可解释概念。"),
        (["interactive segmentation", "active learning"], "交互式/主动学习设定，适合思考少量提示或少量标注下如何快速适配 COD。"),
        (["continual learning", "lifelong"], "持续学习设定，适合思考 COD 在新场景、新物种、新背景下的增量适配。"),
        (["counterfactual"], "反事实建模/拒识机制，用来降低误检或判断目标是否存在。"),
        (["diffusion", "generative"], "扩散/生成式建模，可能用于数据合成、先验建模或掩码优化。"),
        (["prompt"], "提示学习或提示生成，重点看文本/视觉 prompt 如何约束定位。"),
        (["clip", "vision-language", "language-grounded"], "视觉-语言对齐，把语义文本信息引入检测或分割。"),
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


def load_abstract_details() -> dict[str, str]:
    if not ABSTRACT_DETAILS_FILE.exists():
        return {}
    try:
        data = json.loads(ABSTRACT_DETAILS_FILE.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return {}
    if not isinstance(data, dict):
        return {}
    return {
        str(title): clean_text(str(detail))
        for title, detail in data.items()
        if detail
    }


def abstract_sentences(summary: str) -> list[str]:
    summary = clean_text(summary)
    return [
        sentence.strip()
        for sentence in re.split(r"(?<=[.!?])\s+", summary)
        if sentence.strip()
    ]


def join_limited(sentences: list[str], max_chars: int = 650) -> str:
    result: list[str] = []
    length = 0
    for sentence in sentences:
        if result and length + len(sentence) > max_chars:
            break
        result.append(sentence)
        length += len(sentence)
    return " ".join(result)


def generated_abstract_explanation(paper: Paper) -> str:
    if not has_real_abstract(paper):
        return "当前来源尚未取得可靠摘要，不能仅凭标题推断方法；需要先打开论文页或 PDF 补齐摘要后再详解。"

    sentences = abstract_sentences(paper.summary)
    if not sentences:
        return "摘要文本为空，暂时无法生成可靠详解。"
    problem = join_limited(sentences[:2], max_chars=420)
    method_markers = [
        "we propose",
        "we present",
        "we introduce",
        "our method",
        "our framework",
        "specifically",
        "first",
        "then",
        "further",
    ]
    result_markers = [
        "experiment",
        "results",
        "outperform",
        "achieve",
        "demonstrate",
        "show that",
        "state-of-the-art",
    ]
    method_sentences = [
        sentence
        for sentence in sentences[1:]
        if any(marker in sentence.lower() for marker in method_markers)
    ][:4]
    if not method_sentences:
        method_sentences = sentences[2:5] or sentences[1:3]
    result_sentences = [
        sentence
        for sentence in sentences
        if any(marker in sentence.lower() for marker in result_markers)
    ][:2]
    method_text = join_limited(method_sentences, max_chars=760)
    result_text = join_limited(result_sentences, max_chars=420)
    if not result_text:
        result_text = "摘要未给出具体数值，需要到实验部分核对数据集、指标和对比结果。"
    return (
        f"研究问题：{problem} "
        f"方法与流程：{method_core(paper)} 摘要中的具体做法包括：{method_text} "
        f"摘要结论：{result_text}"
    )


def abstract_explanation(paper: Paper) -> str:
    curated = load_abstract_details().get(paper.title)
    return curated or generated_abstract_explanation(paper)


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
    if {"multispectral fire", "fire foundation model"} <= tags:
        return "同时命中两个新增方向，可作为多源感知与大模型监测协同设计的核心候选。"
    if "multispectral fire" in tags:
        return "直接对应多光谱火灾探测，重点关注不同谱段在烟雾、火焰、热点和夜间场景中的互补性。"
    if "fire foundation model" in tags:
        return "直接对应火灾监测大模型，重点关注基础模型在新区域、新传感器和少标注火情上的泛化。"
    if "COD" in tags and (tags & TRANSFER_TAGS):
        return "它既触及 COD，又包含可迁移的新方法线索；适合作为把外部范式落到 COD 的桥梁论文。"
    if "COD" in tags:
        return "和伪装目标检测高度相关，可作为背景、baseline 或问题定义参考；精读时重点看它还缺少哪些外部方法视角。"
    if "UAV/small-object" in tags:
        return "与 COD 的交叉点是弱目标证据：无人机目标通常尺寸极小，COD 目标通常与背景相似；二者都需要避免下采样丢失细节，并抑制复杂背景误检。"
    if "causal/counterfactual" in tags:
        return "可把 COD 从像素匹配问题改写成因果/反事实问题：如果移除背景纹理或环境线索，目标判断是否仍成立。"
    if "uncertainty/calibration" in tags:
        return "可迁移到 COD 的误检拒识、mask 置信度校准和目标缺失判断，适合做更可信的检测系统。"
    if "open-world" in tags or "object discovery" in tags:
        return "可帮助 COD 跳出固定类别监督，转向未知目标发现、开放世界分割和类别无关候选生成。"
    if "object-centric" in tags or "compositionality" in tags:
        return "可把 COD 重新建模为对象-背景解耦或概念组合问题，而不只是做边界更清晰的分割。"
    if "self-supervised" in tags or "representation learning" in tags:
        return "可用于少标注/无标注 COD，重点借鉴稠密表征如何保留弱边界和局部结构。"
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
    if "multispectral fire" in tags:
        points.append("可见光-红外/热红外对齐、谱段融合、早期烟火特征与全天候监测")
    if "fire foundation model" in tags:
        points.append("基础模型适配、视觉语言告警、时空推理、少样本迁移与可解释输出")
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
    if "causal/counterfactual" in tags:
        points.append("反事实验证、目标存在性判断、误检拒识")
    if "uncertainty/calibration" in tags:
        points.append("mask 置信度校准、不确定性图、低置信样本处理")
    if "open-world" in tags or "object discovery" in tags:
        points.append("类别无关候选发现、未知目标设定、目标缺失场景")
    if "object-centric" in tags or "compositionality" in tags:
        points.append("对象-背景解耦、概念分解、可解释中间变量")
    if "self-supervised" in tags or "representation learning" in tags:
        points.append("无标注稠密表征、预训练特征选择、局部结构保持")
    if "active/interactive" in tags or "continual learning" in tags:
        points.append("少量提示适配、增量场景学习、人工反馈闭环")
    if "UAV/small-object" in tags:
        points.append("小目标特征保真、多尺度融合、密集遮挡处理、轻量化实时推理")
    if not points:
        points.append("任务建模、损失函数、消融组织方式")
    return "；".join(points) + "。"


def improvement_ideas(paper: Paper) -> str:
    tags = set(paper.tags)
    if {"multispectral fire", "fire foundation model"} <= tags:
        return "可进一步研究缺失模态与传感器噪声下的稳健融合，并让大模型输出可校准的火情位置、置信度、证据和告警等级。"
    if "multispectral fire" in tags:
        return "可重点验证跨传感器配准误差、昼夜变化、云雾遮挡、热点干扰和缺失谱段，并报告跨区域泛化与误报率。"
    if "fire foundation model" in tags:
        return "可重点验证开放世界火情、跨区域/跨传感器迁移、幻觉抑制、时序一致性和边缘端推理成本。"
    if "UAV/small-object" in tags:
        return "可把无人机小目标的高分辨率分支、多尺度候选和轻量检测头迁移到 COD，并验证其是否改善小型伪装目标、远景目标和复杂背景误检。"
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
    if "causal/counterfactual" in tags:
        return "可把反事实干预落到 COD：替换背景、扰动纹理、隐藏候选区域，验证模型是否真正依赖目标而非环境偏差。"
    if "uncertainty/calibration" in tags:
        return "可进一步做 COD mask 置信度校准，让模型在看不准时拒识或触发二阶段推理。"
    if "open-world" in tags or "object discovery" in tags:
        return "可设计开放世界 COD：图像中可能没有伪装目标，或目标类别未知，模型需要先发现再判别。"
    if "self-supervised" in tags or "representation learning" in tags:
        return "可尝试用无标注自然图像预训练稠密表征，再用少量 COD 标注验证跨数据集泛化。"
    return "可思考是否缺少 COD 场景验证、复杂背景失败分析或轻量化部署。"


def should_deep_read(paper: Paper) -> str:
    fire_tags = {"multispectral fire", "fire foundation model"} & set(paper.tags)
    if fire_tags and has_quality_published_source(paper):
        return "建议精读：直接命中新增火灾方向，且来自正式发表的高质量来源。"
    if fire_tags and paper.score >= 35:
        return "建议泛读：主题高度相关；若为预印本，需再核验正式发表状态与实验可靠性。"
    if transfer_potential(paper) >= MIN_IDEA_TRANSFER_SCORE:
        return "建议精读：它的价值不只在任务相似，而在可能给 COD 带来新问题设定或新方法范式。"
    if "COD" in paper.tags and paper.score >= 45:
        return "可精读但不必只看结论：重点找它没有解决的盲点，以及能否被外部方法重写。"
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
            f"   - 摘要详解：{abstract_explanation(paper)}",
            f"   - 实验结论：{experiment_takeaway(paper)}",
            f"   - 和关注方向的关系：{relation_to_topic(paper)}",
            f"   - 可借鉴点：{borrow_points(paper)}",
            f"   - 可改进点：{improvement_ideas(paper)}",
            f"   - 是否值得精读：{should_deep_read(paper)}",
        ]
    )
    return "\n".join(parts)


def select_feed_sections(
    papers: list[Paper],
    excluded_highlight_keys: set[str] | None = None,
    preserved_highlights: list[Paper] | None = None,
) -> dict[str, list[Paper]]:
    cod = [p for p in papers if "COD" in p.tags]
    uav = [p for p in papers if "UAV/small-object" in p.tags]
    fire_multispectral = [p for p in papers if "multispectral fire" in p.tags]
    fire_foundation = [p for p in papers if "fire foundation model" in p.tags]
    fire_tags = {"multispectral fire", "fire foundation model"}
    broad = [
        p
        for p in papers
        if "COD" not in p.tags and not (set(p.tags) & fire_tags)
    ]
    quality = [
        p
        for p in papers
        if any(hint in p.source.lower() for hint in QUALITY_SOURCE_HINTS)
        or "crossref" in p.source.lower()
    ]

    cod = sorted(cod, key=lambda p: p.score, reverse=True)[:COD_LIMIT]
    uav = sorted(uav, key=highlight_rank, reverse=True)[:UAV_LIMIT]
    fire_multispectral = sorted(
        fire_multispectral, key=topic_rank, reverse=True
    )[:FIRE_MULTISPECTRAL_LIMIT]
    fire_foundation = sorted(
        fire_foundation, key=topic_rank, reverse=True
    )[:FIRE_FOUNDATION_LIMIT]
    broad = sorted(broad, key=lambda p: p.score, reverse=True)[:BROAD_LIMIT]
    quality = sorted(quality, key=lambda p: p.score, reverse=True)[:QUALITY_LIMIT]
    highlights: list[Paper] = []
    preserved_keys: set[str] = set()
    for paper in preserved_highlights or []:
        identity_keys = paper_identity_keys(paper)
        if not identity_keys or not preserved_keys.isdisjoint(identity_keys):
            continue
        highlights.append(paper)
        preserved_keys.update(identity_keys)
        if len(highlights) >= HIGHLIGHT_LIMIT:
            break

    remaining = HIGHLIGHT_LIMIT - len(highlights)
    if remaining > 0:
        excluded_keys = set(excluded_highlight_keys or ()) | preserved_keys
        preserved_pure_cod_count = sum(
            int(is_pure_cod_anchor(paper)) for paper in highlights
        )
        highlights.extend(
            select_highlights(
                papers,
                excluded_keys,
                initial_pure_cod_count=preserved_pure_cod_count,
            )[:remaining]
        )
    return {
        "highlights": highlights,
        "quality": quality,
        "cod": cod,
        "uav": uav,
        "fire_multispectral": fire_multispectral,
        "fire_foundation": fire_foundation,
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


def download_root_available() -> bool:
    if os.name != "nt" and "PAPER_DOWNLOAD_ROOT" not in os.environ:
        return False
    drive = DOWNLOAD_ROOT.drive
    if drive and not Path(drive + "\\").exists():
        return False
    return True


def download_index_path() -> Path:
    return DOWNLOAD_ROOT / DOWNLOAD_INDEX_NAME


def load_download_index() -> dict:
    path = download_index_path()
    if not path.exists():
        return {}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return {}
    return data if isinstance(data, dict) else {}


def save_download_index(index: dict) -> None:
    DOWNLOAD_ROOT.mkdir(parents=True, exist_ok=True)
    download_index_path().write_text(
        json.dumps(index, ensure_ascii=False, indent=2),
        encoding="utf-8",
        newline="\n",
    )


def paper_key(paper: Paper) -> str:
    title_key = re.sub(r"\W+", "", paper.title.lower())
    if title_key:
        return "title:" + hashlib.sha1(title_key.encode("utf-8")).hexdigest()
    url = paper.url or paper.pdf
    arxiv = re.search(r"arxiv\.org/(?:abs|pdf)/([^/?#]+)", url)
    if arxiv:
        arxiv_id = re.sub(r"v\d+$", "", arxiv.group(1))
        return "arxiv:" + arxiv_id.lower()
    return "url:" + hashlib.sha1(url.encode("utf-8")).hexdigest()


def safe_filename(text: str, max_chars: int = 120) -> str:
    text = clean_text(text)
    text = re.sub(r'[<>:"/\\|?*\x00-\x1f]', " ", text)
    text = re.sub(r"\s+", " ", text).strip(" .")
    if not text:
        text = "paper"
    if len(text) > max_chars:
        text = text[:max_chars].rstrip(" .")
    return text


def daily_download_dir(date_text: str) -> Path:
    year, month, day = date_text.split("-")
    return DOWNLOAD_ROOT / year / month / day


def download_candidates(snapshot: dict) -> list[Paper]:
    sections = snapshot_sections(snapshot)
    candidates: list[Paper] = []

    def add_unique(paper: Paper) -> None:
        if not paper.pdf:
            return
        key = paper_key(paper)
        if any(paper_key(existing) == key for existing in candidates):
            return
        candidates.append(paper)

    # The download cache and Zotero collection must mirror the rendered
    # deep-reading queue exactly; re-ranking other sections can displace it.
    for paper in sections["highlights"]:
        add_unique(paper)
    return candidates[:DOWNLOAD_LIMIT]


def write_download_readme(folder: Path, snapshot: dict, downloaded: list[dict], skipped: list[dict]) -> None:
    lines = [
        f"# {snapshot.get('date', '')} 每日精读论文 PDF",
        "",
        f"Generated at: {snapshot.get('generated_at', '')} Asia/Shanghai",
        f"Target: {DOWNLOAD_LIMIT} new PDFs",
        "",
        "## 已下载",
        "",
    ]
    if downloaded:
        for item in downloaded:
            lines.extend(
                [
                    f"- **{item['title']}**",
                    f"  - File: {item['file']}",
                    f"  - Source: {item.get('source', '')}",
                    f"  - URL: {item.get('url', '')}",
                    f"  - Zotero: {item.get('zotero_collection_path', 'not imported yet')}",
                    "",
                ]
            )
    else:
        lines.append("- 本次没有下载新的 PDF。")
        lines.append("")
    if skipped:
        lines.extend(["## 跳过", ""])
        for item in skipped:
            lines.append(f"- {item['title']}：{item['reason']}")
        lines.append("")
    folder.mkdir(parents=True, exist_ok=True)
    (folder / "README.md").write_text("\n".join(lines), encoding="utf-8", newline="\n")


def import_daily_pdfs_to_zotero(date_text: str, records: list[dict]) -> bool:
    if ZOTERO_IMPORT_DISABLED:
        return False
    try:
        script_dir = str(Path(__file__).resolve().parent)
        if script_dir not in sys.path:
            sys.path.insert(0, script_dir)
        from zotero_db_importer import import_records_to_zotero
    except ImportError as exc:  # pragma: no cover - local installation guard
        print(
            f"[warn] Zotero import skipped; local importer unavailable: {exc}",
            file=sys.stderr,
        )
        return False
    return import_records_to_zotero(
        date_text,
        records,
        root_collection=ZOTERO_ROOT_COLLECTION,
        close_running=True,
    )


def download_daily_pdfs(snapshot: dict) -> None:
    if not download_root_available():
        print(f"[warn] download root is unavailable, skipping PDF download: {DOWNLOAD_ROOT}", file=sys.stderr)
        return
    date_text = snapshot.get("date") or str(snapshot.get("generated_at", ""))[:10]
    if not re.match(r"^\d{4}-\d{2}-\d{2}$", date_text):
        print(f"[warn] invalid snapshot date, skipping PDF download: {date_text}", file=sys.stderr)
        return

    index = load_download_index()
    folder = daily_download_dir(date_text)
    folder.mkdir(parents=True, exist_ok=True)
    existing_today = [
        record
        for record in index.values()
        if isinstance(record, dict) and record.get("date") == date_text
    ]
    downloaded: list[dict] = []
    skipped: list[dict] = []

    if len(existing_today) >= DOWNLOAD_LIMIT:
        if import_daily_pdfs_to_zotero(date_text, existing_today[:DOWNLOAD_LIMIT]):
            save_download_index(index)
        write_download_readme(folder, snapshot, existing_today[:DOWNLOAD_LIMIT], skipped)
        print(f"[info] daily PDF quota already satisfied: {folder}")
        return

    for paper in download_candidates(snapshot):
        if len(existing_today) + len(downloaded) >= DOWNLOAD_LIMIT:
            break
        key = paper_key(paper)
        previous = index.get(key)
        if previous:
            skipped.append(
                {
                    "title": paper.title,
                    "reason": f"已在 {previous.get('date', 'previous day')} 下载过",
                }
            )
            continue
        try:
            content, content_type = fetch_bytes(paper.pdf, timeout=90)
        except Exception as exc:  # pragma: no cover - network resilience
            skipped.append({"title": paper.title, "reason": f"下载失败：{exc}"})
            continue
        if not content.startswith(b"%PDF") and "pdf" not in content_type.lower():
            skipped.append({"title": paper.title, "reason": "链接返回的不是 PDF"})
            continue
        sequence = len(existing_today) + len(downloaded) + 1
        filename = f"{sequence:02d} - {safe_filename(paper.title)}.pdf"
        path = folder / filename
        path.write_bytes(content)
        record = {
            "date": date_text,
            "title": paper.title,
            "source": paper.source,
            "published": paper.published,
            "authors": paper.authors,
            "summary": paper.summary,
            "tags": paper.tags,
            "score": paper.score,
            "url": paper.url,
            "pdf": paper.pdf,
            "file": str(path),
        }
        index[key] = record
        downloaded.append(record)
        print(f"[info] downloaded PDF: {path}")

    if import_daily_pdfs_to_zotero(date_text, existing_today + downloaded):
        save_download_index(index)
    else:
        save_download_index(index)
    write_download_readme(folder, snapshot, downloaded, skipped)
    print(f"[info] downloaded {len(downloaded)} new PDFs to {folder}")


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
    snapshot = make_snapshot(papers, datetime.now(UTC8), enrich_abstracts=False)
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


def enrich_selected_sections(sections: dict[str, list[Paper]]) -> None:
    highlights = sections.get("highlights", [])
    enrich_paper_abstracts(highlights)
    enriched = {
        re.sub(r"\W+", "", paper.title.lower()): paper
        for paper in highlights
        if paper.title
    }
    for section_papers in sections.values():
        for paper in section_papers:
            source = enriched.get(re.sub(r"\W+", "", paper.title.lower()))
            if source is None:
                continue
            paper.summary = source.summary
            paper.tags = list(source.tags)
            paper.score = source.score


def make_snapshot(
    papers: list[Paper],
    now: datetime,
    enrich_abstracts: bool = True,
    excluded_highlight_keys: set[str] | None = None,
    preserved_highlights: list[Paper] | None = None,
) -> dict:
    sections = select_feed_sections(
        papers,
        excluded_highlight_keys,
        preserved_highlights,
    )
    if enrich_abstracts:
        enrich_selected_sections(sections)
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


def snapshot_sort_key(snapshot: dict) -> str:
    return snapshot.get("generated_at") or snapshot.get("date") or ""


def collapse_history_by_date(history: list[dict]) -> list[dict]:
    collapsed: list[dict] = []
    seen_dates: set[str] = set()
    for item in sorted(history, key=snapshot_sort_key, reverse=True):
        date_text = item.get("date") or str(item.get("generated_at", ""))[:10]
        if not date_text or date_text in seen_dates:
            continue
        item["date"] = date_text
        seen_dates.add(date_text)
        collapsed.append(item)
    return collapsed


def snapshot_date_text(snapshot: dict) -> str:
    return snapshot.get("date") or str(snapshot.get("generated_at", ""))[:10]


def snapshot_highlights(snapshot: dict) -> list[Paper]:
    sections = snapshot.get("sections", {})
    if not isinstance(sections, dict):
        return []
    highlights = sections.get("highlights", [])
    if not isinstance(highlights, list):
        return []
    return [paper_from_dict(item) for item in highlights if isinstance(item, dict)]


def history_highlight_keys(history: list[dict]) -> set[str]:
    keys: set[str] = set()
    for snapshot in history:
        for paper in snapshot_highlights(snapshot):
            keys.update(paper_identity_keys(paper))
    return keys


def update_history(
    papers: list[Paper],
    now: datetime,
    preserve_same_day_highlights: bool = True,
) -> list[dict]:
    date_text = now.strftime("%Y-%m-%d")
    loaded_history = load_history()
    same_day = [
        item for item in loaded_history if snapshot_date_text(item) == date_text
    ]
    current_snapshot = max(same_day, key=snapshot_sort_key, default=None)
    history = [
        item for item in loaded_history if snapshot_date_text(item) != date_text
    ]
    snapshot = make_snapshot(
        papers,
        now,
        excluded_highlight_keys=history_highlight_keys(history),
        preserved_highlights=(
            snapshot_highlights(current_snapshot)
            if current_snapshot and preserve_same_day_highlights
            else None
        ),
    )
    history.insert(0, snapshot)
    history = collapse_history_by_date(history)
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
        "uav": [paper_from_dict(item) for item in sections.get("uav", [])],
        "fire_multispectral": [
            paper_from_dict(item) for item in sections.get("fire_multispectral", [])
        ],
        "fire_foundation": [
            paper_from_dict(item) for item in sections.get("fire_foundation", [])
        ],
        "broad": [paper_from_dict(item) for item in sections.get("broad", [])],
    }


def render_snapshot_markdown(snapshot: dict) -> str:
    now = datetime.now(UTC8)
    current = snapshot or {
        "date": now.strftime("%Y-%m-%d"),
        "generated_at": now.strftime("%Y-%m-%d %H:%M"),
        "total_selected": 0,
        "sections": {},
    }
    sections = snapshot_sections(current)
    highlights = sections["highlights"]
    quality = sections["quality"]
    cod = sections["cod"]
    uav = sections["uav"]
    fire_multispectral = sections["fire_multispectral"]
    fire_foundation = sections["fire_foundation"]
    broad = sections["broad"]
    date_text = current.get("date", now.strftime("%Y-%m-%d"))
    show_fire_topics = fire_topic_enabled(str(date_text))
    limits = [
        f"{HIGHLIGHT_LIMIT} 篇当日精读",
        f"{QUALITY_LIMIT} 篇高质量来源",
        f"{COD_LIMIT} 篇 COD 相关",
        f"{UAV_LIMIT} 篇无人机小目标",
    ]
    if show_fire_topics:
        limits.extend(
            [
                f"{FIRE_MULTISPECTRAL_LIMIT} 篇多光谱火灾探测",
                f"{FIRE_FOUNDATION_LIMIT} 篇火灾监测大模型",
            ]
        )
    limits.append(f"{BROAD_LIMIT} 篇泛视觉候选")
    arxiv_source = (
        "- arXiv API: recent preprints from COD, UAV small objects, VLM, "
        "segmentation, diffusion, adaptation, medical and remote-sensing queries, "
        "plus transferable-method queries such as object discovery, open-world "
        "segmentation, uncertainty, counterfactual/causal vision, self-supervised "
        "dense prediction, object-centric learning, compositional reasoning, "
        "interactive segmentation, continual learning, world models, and concept "
        "bottlenecks."
    )
    selection_policy = (
        "- Selection policy: the daily deep-reading queue prioritizes idea transfer "
        "into COD, not direct COD similarity. Recent top-conference/top-journal "
        "papers are preferred."
    )
    if show_fire_topics:
        arxiv_source = (
            "- arXiv API: recent preprints from COD, UAV small objects, multispectral "
            "fire detection, fire-monitoring foundation models, VLM, segmentation, "
            "diffusion, adaptation, medical and remote-sensing queries, plus "
            "transferable-method queries such as object discovery, open-world "
            "segmentation, uncertainty, counterfactual/causal vision, self-supervised "
            "dense prediction, object-centric learning, compositional reasoning, "
            "interactive segmentation, continual learning, world models, and concept "
            "bottlenecks."
        )
        selection_policy = (
            "- Selection policy: the daily deep-reading queue prioritizes idea "
            "transfer into COD, not direct COD similarity. The two fire sections "
            "rank formally published top-conference/top-journal results before "
            "preprints, then use relevance and recency."
        )

    lines = [
        f"# {date_text} CV Paper Feed",
        "",
        "[返回首页](../index.html)",
        "",
        f"Last updated: {current.get('generated_at', now.strftime('%Y-%m-%d %H:%M'))} Asia/Shanghai",
        f"Candidate pool: {current.get('total_selected', 0)} papers",
        "",
        f"慢读模式：本页只展示 {'、'.join(limits)}。完整候选池保存在 data/latest_papers.json。",
        "精读队列优先选择能给 COD 带来新问题设定或新方法范式的论文，例如开放世界、目标发现、反事实/因果、不确定性、自监督稠密表征、对象中心建模和视觉推理；纯 COD 直系论文主要作为背景和对照。",
        "",
        "## 当日精读队列",
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

    lines.extend(["## 无人机 / 航拍小目标", ""])
    for i, paper in enumerate(uav, 1):
        lines.append(md_paper_item(i, paper))
        lines.append("")

    if show_fire_topics:
        lines.extend(["## 多光谱火灾探测", ""])
        for i, paper in enumerate(fire_multispectral, 1):
            lines.append(md_paper_item(i, paper))
            lines.append("")

        lines.extend(["## 火灾监测大模型", ""])
        for i, paper in enumerate(fire_foundation, 1):
            lines.append(md_paper_item(i, paper))
            lines.append("")

    lines.extend(["## 泛计算机视觉方法池", ""])
    for i, paper in enumerate(broad, 1):
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
            arxiv_source,
            "- CVF OpenAccess: CVPR/ECCV/ICCV/WACV title-level scan.",
            "- Semantic Scholar Graph API: broad high-quality venue and topic search when rate limits allow.",
            "- Crossref API: TPAMI, IJCV, TIP, TMM, TCSVT, Pattern Recognition, CVIU, TGRS, ISPRS JPRS, RSE, JAG, Medical Image Analysis.",
            selection_policy,
            "",
            "说明：自动简介是基于题名、摘要和来源的初筛笔记，不等同于阅读全文后的结论；精读时建议再核对 method、experiment 和 limitation。",
            "",
        ]
    )
    return "\n".join(lines)


def render_markdown(history: list[dict]) -> str:
    history = collapse_history_by_date(history)
    now = datetime.now(UTC8)
    current = history[0] if history else {
        "date": now.strftime("%Y-%m-%d"),
        "generated_at": now.strftime("%Y-%m-%d %H:%M"),
        "total_selected": 0,
    }
    current_date = current.get("date", now.strftime("%Y-%m-%d"))
    show_fire_topics = fire_topic_enabled(str(current_date))
    daily_limits = [
        f"{HIGHLIGHT_LIMIT} 篇精读",
        f"{QUALITY_LIMIT} 篇高质量来源",
        f"{COD_LIMIT} 篇 COD",
        f"{UAV_LIMIT} 篇无人机小目标",
    ]
    if show_fire_topics:
        daily_limits.extend(
            [
                f"{FIRE_MULTISPECTRAL_LIMIT} 篇多光谱火灾探测",
                f"{FIRE_FOUNDATION_LIMIT} 篇火灾监测大模型",
            ]
        )
    daily_limits.append(f"{BROAD_LIMIT} 篇泛视觉")
    lines = [
        "# Daily CV Paper Feed",
        "",
        f"Last updated: {current.get('generated_at', now.strftime('%Y-%m-%d %H:%M'))} Asia/Shanghai",
        f"Archive days kept: {len(history)}",
        "",
        "这是文献日报目录页。每天更新会生成一个独立 Markdown 文件，文件名就是日期；想看哪一天，直接点对应日期即可。HTML 文件单独放在 html/ 目录，仅作为网页预览备用。",
        "从 2026-07-09 开始，精读队列不再只追 COD 直系论文，而是优先寻找 COD 尚未充分使用、但可能迁移出新 idea 的计算机视觉方法。",
        "从 2026-07-14 开始，新增多光谱火灾探测与火灾监测大模型两个独立栏目，优先展示正式发表的顶会顶刊与领域高水平期刊论文。",
        "",
        "## 最新日报",
        "",
        f"- [{current.get('date', now.strftime('%Y-%m-%d'))} Markdown](md/{current.get('date', now.strftime('%Y-%m-%d'))}.md) / [HTML 预览](html/{current.get('date', now.strftime('%Y-%m-%d'))}.html)",
        "",
        "## 每日 Markdown 文件",
        "",
    ]
    for item in history:
        date_text = item.get("date", str(item.get("generated_at", ""))[:10])
        generated_at = item.get("generated_at", date_text)
        total = item.get("total_selected", 0)
        lines.append(
            f"- [{date_text}](md/{date_text}.md) / [html](html/{date_text}.html) - {generated_at}，候选池 {total} 篇"
        )
    lines.extend(
        [
            "",
            "## 阅读节奏",
            "",
            f"- 每日页面默认只展示少量精选：{'、'.join(daily_limits)}。",
            "- 精读优先级看“能不能启发新的 COD 论文问题”，不是只看标题里有没有 camouflaged object detection。",
            "- 旧 Markdown 日报不会被覆盖；同一天重复更新只刷新当天文件。",
            "- 后台仍保留完整候选池，方便以后需要时再扩展检索。",
            "",
            "## 数据源",
            "",
            "- arXiv API",
            "- CVF OpenAccess",
            "- Semantic Scholar Graph API",
            "- Crossref API: TPAMI, IJCV, TIP, TMM, TCSVT, Pattern Recognition, CVIU, TGRS, ISPRS JPRS, RSE, JAG, Medical Image Analysis",
            "- Deep-reading priority: transferable methods for COD first, including open-world, object discovery, uncertainty/calibration, causal/counterfactual vision, self-supervised dense representation, object-centric/compositional reasoning, and interactive/continual adaptation.",
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


def write_daily_files(history: list[dict]) -> None:
    DAILY_MD.mkdir(exist_ok=True)
    DAILY_HTML.mkdir(exist_ok=True)
    for snapshot in collapse_history_by_date(history):
        write_snapshot_files(snapshot)


def write_snapshot_files(snapshot: dict) -> None:
    date_text = snapshot.get("date", str(snapshot.get("generated_at", ""))[:10])
    if not re.match(r"^\d{4}-\d{2}-\d{2}$", date_text):
        return
    md = render_snapshot_markdown(snapshot)
    (DAILY_MD / f"{date_text}.md").write_text(md, encoding="utf-8", newline="\n")
    (DAILY_HTML / f"{date_text}.html").write_text(
        render_html(md),
        encoding="utf-8",
        newline="\n",
    )


def render_existing_history(history: list[dict] | None = None, latest_only: bool = False) -> None:
    DATA.mkdir(exist_ok=True)
    DOCS.mkdir(exist_ok=True)
    DAILY_MD.mkdir(exist_ok=True)
    DAILY_HTML.mkdir(exist_ok=True)
    history = collapse_history_by_date(history if history is not None else load_history())
    md = render_markdown(history)
    (DOCS / "literature.md").write_text(md, encoding="utf-8", newline="\n")
    (DOCS / "index.html").write_text(render_html(md), encoding="utf-8", newline="\n")
    if latest_only and history:
        write_snapshot_files(history[0])
    else:
        write_daily_files(history)


def refresh_current_abstracts() -> None:
    history = collapse_history_by_date(load_history())
    if not history:
        print("[warn] no feed history to refresh", file=sys.stderr)
        return
    current = history[0]
    sections = snapshot_sections(current)
    enrich_selected_sections(sections)
    current["sections"] = {
        name: [paper_to_dict(paper) for paper in section_papers]
        for name, section_papers in sections.items()
    }
    HISTORY_FILE.write_text(
        json.dumps(history, ensure_ascii=False, indent=2),
        encoding="utf-8",
        newline="\n",
    )

    latest_path = DATA / "latest_papers.json"
    if latest_path.exists():
        try:
            latest = json.loads(latest_path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            latest = []
        enriched = {
            re.sub(r"\W+", "", paper.title.lower()): paper
            for paper in sections["highlights"]
        }
        for item in (latest if isinstance(latest, list) else []):
            key = re.sub(r"\W+", "", str(item.get("title", "")).lower())
            source = enriched.get(key)
            if source is None:
                continue
            item["summary"] = source.summary
            item["tags"] = source.tags
            item["score"] = source.score
        latest_path.write_text(
            json.dumps(latest, ensure_ascii=False, indent=2),
            encoding="utf-8",
            newline="\n",
        )
    render_existing_history(history, latest_only=True)
    print(f"[info] refreshed abstracts for {current.get('date', 'current day')}")


def markdown_inline(text: str) -> str:
    text = html.escape(text)
    text = re.sub(r"\*\*(.*?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', text)
    return text


def main() -> None:
    DATA.mkdir(exist_ok=True)
    DOCS.mkdir(exist_ok=True)
    DAILY_MD.mkdir(exist_ok=True)
    DAILY_HTML.mkdir(exist_ok=True)

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
    if history:
        download_daily_pdfs(history[0])
    render_existing_history(history, latest_only=True)

    serializable = [paper_to_dict(paper) for paper in papers]
    (DATA / "latest_papers.json").write_text(
        json.dumps(serializable, ensure_ascii=False, indent=2),
        encoding="utf-8",
        newline="\n",
    )
    print(f"[info] selected papers: {len(papers)}")
    print(f"[info] wrote {(DOCS / 'index.html')}")
    print(f"[info] wrote Markdown files under {DAILY_MD}")
    print(f"[info] wrote HTML previews under {DAILY_HTML}")


if __name__ == "__main__":
    if "--refresh-current-abstracts" in sys.argv:
        refresh_current_abstracts()
    elif "--render-only" in sys.argv:
        render_existing_history(latest_only=True)
    else:
        main()
