# Supplemental Paper Search Report - 2026-08-01

This report logs the complete supplemental six-source search run used alongside the project's expanded CV scan. Raw discovery is kept separate from full-text promotion: none of the entries below entered the five-paper queue from title matching alone.

- Query: `safety-critical multimodal visual grounding missing modality out-of-distribution tiny object UAV fire smoke detection`
- Search window: 2024-2026
- Maximum records: 8 per API source
- Run date: 2026-08-01

## Source Errors

The search runner emitted these source messages verbatim:

```text
[openreview] Error: openreview not installed. pip install openreview-py
Rate limited. Waiting 3 seconds...
[dblp] Error: 503 Server Error: Service Unavailable for url: https://dblp.org/search/publ/api?q=safety-critical+multimodal+visual+grounding+missing+modality+out-of-distribution+tiny+object+UAV+fire+smoke+detection&format=json&h=8&f=0
[open_alex] Error: 504 Server Error: Gateway Timeout for url: https://api.openalex.org/works?search.semantic=safety-critical+multimodal+visual+grounding+missing+modality+out-of-distribution+tiny+object+UAV+fire+smoke+detection&filter=publication_year%3A2024-2026&sort=relevance_score%3Adesc&page=1&per-page=8
```

Semantic Scholar returned no records after rate limiting. These failures were not retried blindly; the affected topic clusters remain in the local candidate cache and next-run plan.

## All Results

### Semantic Scholar (0 papers)

No matches were returned in this run after rate limiting.

### OpenAlex (0 papers)

The source failed with HTTP 504; no records were returned.

### arXiv (8 papers)

| # | Title | Date | Venue | Citations |
|---|---|---:|---|---:|
| [1](http://arxiv.org/abs/2506.05199v3) | DEGround: An Effective Baseline for Ego-centric 3D Visual Grounding with a Homogeneous Framework | 2025 | arXiv | 0 |
| [2](http://arxiv.org/abs/2412.20206v3) | Towards Visual Grounding: A Survey | 2024 | arXiv | 0 |
| [3](http://arxiv.org/abs/2604.17585v1) | DGSSM: Diffusion guided state-space models for multimodal salient object detection | 2026 | arXiv | 0 |
| [4](http://arxiv.org/abs/2410.16642v1) | Fire and Smoke Detection with Burning Intensity Representation | 2024 | arXiv | 0 |
| [5](http://arxiv.org/abs/2507.11252v2) | MFGDiffusion: Mask-Guided Smoke Synthesis for Enhanced Forest Fire Detection | 2025 | arXiv | 0 |
| [6](http://arxiv.org/abs/2411.02844v1) | Correlation of Object Detection Performance with Visual Saliency and Depth Estimation | 2024 | arXiv | 0 |
| [7](http://arxiv.org/abs/2510.10108v1) | Uncertainty-Aware Post-Detection Framework for Enhanced Fire and Smoke Detection in Compact Deep Learning Models | 2025 | arXiv | 0 |
| [8](http://arxiv.org/abs/2607.13678v1) | M3F-UAV: A Missing-Modality Multimodal Foundation Model for Low-Altitude Wireless Sensing | 2026 | arXiv | 0 |

### OpenReview (0 papers)

The local `openreview-py` package is unavailable, so this source returned no records.

### Crossref (8 papers)

| # | Title | Date | Venue | Citations |
|---|---|---:|---|---:|
| [1](https://doi.org/10.2139/ssrn.5052256) | Improving Tiny Object Detection in Challenging Situation Using Uav Imaging and Applied Innovative Guided-Object Inference Framework | Unknown | SSRN | 0 |
| [2](https://doi.org/10.3390/fire9050182) | GLAFC-YOLO: Multimodal Object Detection of Personnel for Indoor Fire Rescue in Smoke-Obscured Environments | 2026 | Fire | 0 |
| [3](https://doi.org/10.20944/preprints202606.0287.v1) | CC-MBS: A Missing-Modality-Robust Multimodal Sample Selection Strategy for UAV Swarms | Unknown | Preprints.org | 0 |
| [4](https://doi.org/10.1145/3778534.3778562) | Layer-Adaptive Modality Interaction Network for UAV-based Multimodal Object Detection | 2025 | ICAIIP | 0 |
| [5](https://doi.org/10.1109/icicat68430.2025.11414658) | Real-Time Fire and Smoke Detection Using Multimodal Object Detection | 2025 | ICICAT | 0 |
| [6](https://doi.org/10.3934/math.2024526) | YOLOv7-FIRE: A tiny-fire identification and detection method applied on UAV | 2024 | AIMS Mathematics | 10 |
| [7](https://doi.org/10.2139/ssrn.6512539) | LFS-YOLO: A Lightweight Frequency-Semantic Network for Dense Tiny Object Detection in UAV Aerial Images | Unknown | SSRN | 0 |
| [8](https://doi.org/10.1109/cac63892.2024.10864802) | A Novel YOLOv5s-Based Tiny Object Detection Model for UAV | 2024 | China Automation Congress | 1 |

### DBLP (0 papers)

The source failed with HTTP 503; no records were returned.

### Model Knowledge (0 papers)

No unverified memory-only entries were added. The 2026 portion of the query is fast-moving, and the automation uses independently verified CVF/OpenReview primary sources instead of padding this table with uncertain recollections.

## Summary

### 1. Overview

The API run returned 16 records from arXiv and Crossref across 2024-2026. It spans visual grounding, missing-modality multimodal learning, UAV tiny-object detection, and fire/smoke perception, but source degradation makes it a supplemental discovery sample rather than a complete venue survey.

### 2. Trends

The returned titles cluster around three shifts: from single-modality detectors to multimodal or missing-modality systems; from generic aerial detection to tiny-object and low-altitude sensing; and from binary fire classification to smoke synthesis, uncertainty, and obscured-environment rescue. The citation signal is too sparse and recent to support a reliable temporal-growth claim. Venue quality is mixed, with arXiv preprints, Crossref-indexed journals, proceedings, and unreviewed records represented together.

### 3. Key Themes

1. **UAV tiny-object preservation:** Crossref [1], [6], [7], and [8] focus on tiny targets under aerial scale and background constraints.
2. **Fire/smoke perception:** arXiv [4], [5], and [7] cover intensity representation, synthetic smoke, and uncertainty-aware post-detection.
3. **Missing or multimodal evidence:** arXiv [3] and [8], plus Crossref [2]-[5], study fusion or missing-modality robustness.
4. **Grounded spatial reasoning:** arXiv [1] and [2] represent 3D grounding and the broader visual-grounding landscape.
5. **Weak-evidence reliability:** arXiv [6] and [7] connect saliency, depth, and uncertainty to failure-aware detection.

### 4. Keywords Frequency

Counts below are title-level document frequencies, not token occurrences in abstracts.

| Keyword | Count |
|---|---:|
| Detection | 12 |
| UAV / aerial | 7 |
| Multimodal | 6 |
| Fire / smoke | 6 |
| Tiny object | 4 |

### 5. Most Cited by Accepted Paper

Citation counts are the values returned by the source at run time. Ties at zero are ordered by relevance to the query.

| Rank | Title | Year | Citations |
|---:|---|---:|---:|
| 1 | YOLOv7-FIRE: A tiny-fire identification and detection method applied on UAV | 2024 | 10 |
| 2 | A Novel YOLOv5s-Based Tiny Object Detection Model for UAV | 2024 | 1 |
| 3 | GLAFC-YOLO: Multimodal Object Detection of Personnel for Indoor Fire Rescue in Smoke-Obscured Environments | 2026 | 0 |
| 4 | Layer-Adaptive Modality Interaction Network for UAV-based Multimodal Object Detection | 2025 | 0 |
| 5 | Real-Time Fire and Smoke Detection Using Multimodal Object Detection | 2025 | 0 |

### 6. Most Cited by First Author

| Rank | Author | Papers in set | Total citations |
|---:|---|---:|---:|
| 1 | Baoshan Sun | 1 | 10 |
| 2 | Jie Yuan | 1 | 1 |
| 3 | Chengyao Hou | 1 | 0 |
| 4 | Chen Chen | 1 | 0 |
| 5 | Xiaoyi Han | 1 | 0 |

### 7. Recommendations for Reading

1. **Towards Visual Grounding: A Survey** provides terminology and task boundaries before reading narrow grounding systems; it is a survey and should not substitute for primary-method evidence.
2. **DEGround** offers a recent homogeneous baseline for 3D grounding and helps separate spatial grounding from ordinary detection.
3. **Fire and Smoke Detection with Burning Intensity Representation** is a direct fire anchor whose representation claim can be tested against cloud, haze, sunset, and reflection negatives.
4. **MFGDiffusion** is useful for examining whether generated smoke improves rare-condition recall without amplifying synthetic artifacts.
5. **M3F-UAV** is the closest returned record to missing-modality low-altitude sensing, but it remains a recent arXiv candidate and requires full-text and venue verification before promotion.

The automation's actual five-paper selections are documented separately in `D:\Codex输出\daily-cv-literature-feed-update\final\2026-08-01\2026-08-01-检索与筛选报告.md`; they were chosen only after official full-text verification and historical deduplication.

---

# Verified Daily Search Update - 2026-08-04

The expanded scan ran with `DEEP_SOURCE_SCAN=1` and covered causal/OOD vision, object-centric self-supervision, UAV tiny-object perception, missing/degraded multimodal learning, grounded reasoning, selective risk, and RGB-T fire perception. Discovery produced 845 arXiv records, 3,921 cumulative CVF records, 4,709 cumulative Crossref records, and 10,534 merged cached candidates. Semantic Scholar returned 429 records for the safety/multimodal cluster before rate limiting; OpenAlex, DBLP, and OpenReview were degraded or unavailable, so final promotion relied on official CVF/IEEE pages and the actual PDFs.

The exact non-duplicate deep-reading queue is:

1. **From Easy to Hard: Progressive Active Learning Framework for Infrared Small Target Detection with Single Point Supervision** (ICCV 2025)
2. **U2Flow: Uncertainty-Aware Unsupervised Optical Flow Estimation** (CVPR 2026)
3. **Visual Prototype Conditioned Focal Region Generation for UAV-Based Object Detection** (CVPR 2026)
4. **What You Have is What You Track: Adaptive and Robust Multimodal Tracking** (ICCV 2025)
5. **FlameFinder: Illuminating Obscured Fire Through Smoke With Attentive Deep Metric Learning** (IEEE TGRS 2024)

All five PDFs passed page-count/signature/text preflight and were checked beyond the abstract. The queue deliberately joins progressive weak supervision, temporal uncertainty estimation, UAV-specific synthetic data, missing-modality temporal routing, and a direct visible-thermal fire anchor. A release-stage audit caught two initially proposed historical highlights and replaced them with PAL and U2Flow; the final five have zero prior deep-reading matches in both the historical highlight set and the F-drive download index.

Strong retained candidates include *SkySense V2*, *SegEarth-OV*, MD2N, Synergistic Prompting, missing-modality semi-supervised segmentation, RGBT-3M, MISSRAG, and GroundingME. They remain in the dedicated UAV, fire, reliability, or grounding sections rather than being forced into the five. The complete evidence and exclusion rationale is in `D:\Codex输出\daily-cv-literature-feed-update\final\2026-08-04\2026-08-04-检索与筛选报告.md`.

---

# Verified Daily Search Update - 2026-08-09

The expanded project scan ran with `DEEP_SOURCE_SCAN=1`: arXiv returned 865 records, CVF accumulated 10,268 raw records, Crossref accumulated 11,066 raw records, and 10,720 cached candidates were merged. Semantic Scholar entered degraded mode after three 429 responses, and one Remote Sensing of Environment Crossref query returned 429. These source clusters remain cached for the next run.

An independent six-source Paper Search queried `open-world segmentation selective prediction missing modality infrared small target visual grounding` for 2023–2026. OpenReview was unavailable because `openreview-py` is not installed; DBLP returned HTTP 500; OpenAlex returned HTTP 504; Semantic Scholar returned no record. The complete returned discovery set was:

## Crossref results

1. [Modality Discrepancy Reduction for Visible-Infrared Person Re-Identification under Complete Modality Missing](https://doi.org/10.21203/rs.3.rs-4142107/v1)
2. [LW-IRSTNet: Lightweight Infrared Small Target Segmentation Network, version 1](https://doi.org/10.36227/techrxiv.22280995.v1)
3. [LW-IRSTNet: Lightweight Infrared Small Target Segmentation Network, version 2](https://doi.org/10.36227/techrxiv.22280995.v2)
4. [LW-IRSTNet: Lightweight Infrared Small Target Segmentation Network, version 3](https://doi.org/10.36227/techrxiv.22280995.v3)
5. [Temporal Segmentation Modeling with Sample Augmentation for Moving Infrared Small Target Detection](https://doi.org/10.2139/ssrn.5181885)

## arXiv results

1. [MiM-ISTD: Mamba-in-Mamba for Efficient Infrared Small Target Detection](http://arxiv.org/abs/2403.02148v4)
2. [Rethinking Generalizable Infrared Small Target Detection: A Real-scene Benchmark and Cross-view Representation Learning](http://arxiv.org/abs/2504.16487v1)
3. [AdaMSS: Adaptive Multi-Modality Segmentation-to-Survival Learning for Survival Outcome Prediction from PET/CT Images](http://arxiv.org/abs/2305.09946v3)
4. [DEGround: An Effective Baseline for Ego-centric 3D Visual Grounding with a Homogeneous Framework](http://arxiv.org/abs/2506.05199v3)
5. [Lidar Panoptic Segmentation in an Open World](http://arxiv.org/abs/2409.14273v1)

None of these discovery-only records was promoted solely from a title or search abstract. The final verified, historically non-duplicate queue is UniGeoSeg (CVPR 2026), Prior2Former (ICCV 2025), SCOD (ECCV 2024), SimMLM (ICCV 2025), and Text-IRSTD (ICCV 2025); all five were selected only after official full-PDF reading and page-integrity checks. Full evidence and exclusions are in `D:\Codex输出\daily-cv-literature-feed-update\final\2026-08-09\2026-08-09-检索与筛选报告.md`.

---

# Verified Daily Search Update - 2026-08-10

The expanded project scan ran with `DEEP_SOURCE_SCAN=1`. It returned 18 arXiv records, accumulated 9,421 CVF raw records and 10,221 Crossref raw records, merged 10,727 cached candidates, and formed a final pool of 10,730 records. arXiv COD/concealed-object queries entered degraded mode after HTTP 429, timeout, and 503 failures; Semantic Scholar entered degraded mode after three HTTP 429 responses on the safety, multimodal, and open-world clusters. Those clusters remain in the cache and next-run plan.

The independent six-source Paper Search produced 160 source records and 154 unique titles; 150 were not exact historical deep-reading duplicates. It recorded 16 source errors: six missing-OpenReview-dependency failures, five arXiv timeouts, three OpenAlex 504 responses, and two DBLP 500 responses. Complete stdout, stderr, candidates, and error records are retained under `D:\Codex输出\daily-cv-literature-feed-update\research\2026-08-10\paper-search`.

The final queue was deduplicated against 164 normalized historical titles from feed history, daily highlights, and the F-drive download index:

1. **FE-CLIP: Frequency Enhanced CLIP Model for Zero-Shot Anomaly Detection and Segmentation** (ICCV 2025)
2. **Synthesizing Near-Boundary OOD Samples for Out-of-Distribution Detection** (ICCV 2025)
3. **Talking to DINO: Bridging Self-Supervised Vision Backbones with Language for Open-Vocabulary Segmentation** (ICCV 2025)
4. **Rotation Invariant and Symmetry Aware Pixel Difference Network for Remote Sensing Object Detection** (CVPR 2026)
5. **Delving Aleatoric Uncertainty in Medical Image Segmentation via Vision Foundation Models** (CVPR 2026)

All five official main PDFs passed signature, page-count, page-enumeration, and reader-count preflight. Official supplements were also obtained and passed for FE-CLIP, Talk2DINO, RIS-PiDiNet, and the AUV medical-segmentation paper; the official SynOOD page does not expose a supplement. The queue deliberately combines frequency evidence, near-boundary hard-negative synthesis, dense vision-language alignment, aerial rotation/symmetry, and data-level uncertainty instead of filling the list with direct COD papers.

RIS-PiDiNet is the direct UAV/remote-sensing anchor. RareSpot+, MANTA, prompt-free remote-sensing open-world detection, TAIS-Net, UAV-OVVIS, and RIS-LAD remain in the dedicated aerial section. Strong fire candidates include spatiotemporal wildfire forecasting, AusSmoke/MultiNatSmoke, RGB-T distillation, on-orbit MWIR detection, uncertainty-aware smoke-density classification, and UAV teacher-student segmentation; none was forced into the five because full-text strength, venue status, or method novelty was insufficient relative to the selected set. The complete evidence and exclusion rationale is in `D:\Codex输出\daily-cv-literature-feed-update\final\2026-08-10\2026-08-10-检索与筛选报告.md`.

---

# Verified Daily Search Update - 2026-08-11

The expanded project scan ran with `DEEP_SOURCE_SCAN=1`. It accumulated 9,403 raw CVF records and 10,202 cumulative Crossref records, merged 10,730 cached candidates, and retained 10,561 historically new titles after exact normalized-title exclusion. arXiv COD discovery degraded after HTTP 429, timeout, and another 429; Semantic Scholar degraded after three HTTP 429 responses on the safety-critical, multimodal-hazard, and open-world-multimodal clusters. These failures are recorded in the retained search artifacts and the affected clusters remain in the next-run plan.

The independent Paper Search produced 100 source records and 93 normalized unique titles, of which 91 were not exact historical deep-reading duplicates. It recorded 19 source failures and 120 rate-limit notices: OpenReview was unavailable because its client dependency is not installed, DBLP returned HTTP 503, OpenAlex returned HTTP 504, and arXiv timed out or returned HTTP 429. Final promotion therefore relied on official CVF pages and the actual main and supplemental PDFs rather than title matches or discovery snippets.

The final queue was deduplicated against 169 normalized historical titles from feed history, daily highlights, and the download index:

1. **ANTS: Adaptive Negative Textual Space Shaping for OOD Detection via Test-Time MLLM Understanding and Reasoning** (CVPR 2026)
2. **ReAttnCLIP: Training-Free Open-Vocabulary Remote Sensing Image Segmentation via Re-defined Attention in CLIP** (CVPR 2026)
3. **Hyperbolic Prototype Learning with Uncertainty-Aware Consistency for Continual Test-Time Segmentation** (CVPR 2026)
4. **SegCompass: Exploring Interpretable Alignment with Sparse Autoencoders for Enhanced Reasoning Segmentation** (CVPR 2026)
5. **Adaptive 3D Perception for Small Aerial Targets Under Sparse Sampling via Reinforcement Learning** (CVPR 2026)

All five official main PDFs passed signature, page-count, page-enumeration, and reader-count preflight. Official supplements were also checked for ANTS, ReAttnCLIP, HyperProtoSeg, and SegCompass; the A3PRL official record exposes no supplement. The queue combines test-time negative-space OOD reasoning, remote-sensing open-vocabulary segmentation, uncertainty-aware continual adaptation, interpretable reasoning segmentation, and a direct small-aerial-target anchor. The complete evidence, source failures, UAV/fire candidates, and historical exclusions are in `D:\Codex输出\daily-cv-literature-feed-update\final\2026-08-11\2026-08-11-检索与筛选报告.md`.

---

# Verified Daily Search Update - 2026-08-12

The expanded project scan ran with `DEEP_SOURCE_SCAN=1`. It collected 9,403 raw CVF records, reached 10,202 cumulative Crossref records, merged 10,732 cached candidates after live-source degradation, and produced a final pool of 10,742 records. arXiv returned HTTP 503/429 responses and Semantic Scholar entered degraded mode after repeated 429 responses; the affected research clusters remain in the cache and next-run plan.

The independent 2024-2026 six-source search covered five linked clusters: safety-critical hazard perception and risk control, grounded/compositional reasoning, multimodal reliability under missing/degraded/OOD evidence, UAV aerial tiny-object perception, and fire/smoke RGB-T sensing. It returned 110 records and 104 normalized unique titles, with 101 not present in the historical index. Sixteen source errors and 34 rate-limit notices were retained verbatim under `D:\Codex输出\daily-cv-literature-feed-update\research\2026-08-12\paper-search`; no title-only candidate was promoted.

The final queue was deduplicated against 359 normalized historical project titles and 145 Zotero-imported download-index records:

1. **Spectral Conformal Risk Control: Distribution-Free Tail Guarantees via Bayesian Quadrature** (CVPR 2026)
2. **FoSS: Modeling Long-Range Dependencies and Multimodal Uncertainty in Trajectory Prediction via Fourier-State Space Integration** (CVPR 2026)
3. **Test-Time Multi-Prompt Adaptation for Open-Vocabulary Remote Sensing Image Segmentation** (CVPR 2026)
4. **3M-TI: High-Quality Mobile Thermal Imaging via Calibration-free Multi-Camera Cross-Modal Diffusion** (CVPR 2026)
5. **MCAM: Multimodal Causal Analysis Model for Ego-Vehicle-Level Driving Video Understanding** (ICCV 2025)

All five official main PDFs passed signature, page-count, enumeration, and reader-count preflight. Official supplements were also checked for Spectral CRC, TMPA, and 3M-TI; the FoSS and MCAM official pages expose no supplement. The queue combines spectral tail-risk certification, time-frequency state-space prediction, open-vocabulary aerial adaptation, unregistered RGB-T thermal restoration, and causal-graph-inspired hazard reasoning. The complete evidence, formula audits, source failures, UAV/fire transfer boundaries, and exclusions are in `D:\Codex输出\daily-cv-literature-feed-update\final\2026-08-12\2026-08-12-检索与筛选报告.md`.

---

# Verified Daily Search Update - 2026-08-13

The expanded project scan ran with `DEEP_SOURCE_SCAN=1`. It accumulated 9,403 raw CVF records and 10,200 cumulative Crossref records, merged 10,742 cached candidates, and formed a final pool of 10,743 records. arXiv returned HTTP 429 for the first three COD-related queries, while Semantic Scholar returned HTTP 429 for the safety-critical, multimodal-hazard, and open-world-multimodal clusters; those clusters remain explicitly retained in the cache and next-run plan. The automatic downloader wrote one provisional PDF only to the isolated D-drive scan directory and did not touch Zotero.

The final queue was selected after official main-PDF and available supplemental-material reading, mathematical inspection, and exact normalized-title exclusion against all prior feed sections and the Zotero download index:

1. **Prompt-Free Unknown Label Generation for Open World Detection in Remote Sensing** (CVPR 2026)
2. **VIRST: Video-Instructed Reasoning Assistant for SpatioTemporal Segmentation** (CVPR 2026)
3. **DiMPLe - Disentangled Multi-Modal Prompt Learning: Enhancing Out-Of-Distribution Alignment with Invariant and Spurious Feature Separation** (ICCV 2025)
4. **Reasoning-Driven Anomaly Detection and Localization with Image-Level Supervision** (CVPR 2026)
5. **Learning to Identify Out-of-Distribution Objects for 3D LiDAR Anomaly Segmentation** (CVPR 2026)

All five are formally peer-reviewed CVF papers and none is a direct COD paper. The queue combines prompt-free remote-sensing unknown discovery, video-grounded temporal segmentation, multimodal spurious-factor separation, image-level-supervised anomaly localization, and efficient LiDAR OOD segmentation. HSGDet anchors the dedicated UAV/remote-sensing section; strong UAV and fire candidates remain surfaced separately without forcing a weaker or unverified fire paper into the five. The complete source failures, selection evidence, exclusions, and COD/UAV/fire transfer boundaries are retained in `D:\Codex输出\daily-cv-literature-feed-update\final\2026-08-13\2026-08-13-检索与筛选报告.md`.

---

# Verified Daily Search Update - 2026-08-14

The expanded project scan ran with `DEEP_SOURCE_SCAN=1`. It collected 9,403 CVF records, reached 10,194 raw records after Crossref journal queries, merged 10,743 cached candidates after live-source degradation, and formed a final pool of 10,747 records. arXiv and Semantic Scholar each entered degraded mode after three HTTP 429 responses; one JAG Crossref query also returned HTTP 429. The independent paper-search pass additionally recorded OpenAlex 504 responses, a DBLP SSL failure, and a missing local OpenReview client. These affected clusters remain in the retained cache and next-run plan.

The final queue was frozen only after excluding the provisional 2026-08-14 snapshot and comparing against all sections from the prior 39 days, the daily-highlight ledger, and the 155-entry Zotero-imported download index. The union contained 369 normalized historical titles; all five selected titles and official CVF URLs were new, and their closest title-token Jaccard scores ranged from 0.154 to 0.286:

1. **U4D: Uncertainty-Aware 4D World Modeling from LiDAR Sequences** (CVPR 2026)
2. **CoSMo3D: Open-World Promptable 3D Semantic Segmentation through LLM-Guided Canonical Spatial Modeling** (CVPR 2026)
3. **OmniVTG: A Large-Scale Dataset and Training Paradigm for Open-World Video Temporal Grounding** (CVPR 2026)
4. **Alert-CLIP: Abnormality-aware Latent-Enhanced Representation Tuning of CLIP for Video Anomaly Detection** (CVPR 2026)
5. **RHCNet: Residual-Guided Hierarchical Calibration Network for Robust Underwater Object Detection** (CVPR 2026)

All five are formally peer-reviewed CVF papers with verified full PDFs. The queue combines uncertainty-prioritized world generation, canonical open-world grounding, rare-event temporal localization, abnormality-aware vision-language alignment, and degraded weak-evidence calibration. RHCNet remains included with an explicit evidence warning: its camera-ready UTDAC table reports AP 53.35, while an older review-copy supplement reports AP 50.87 for the nominally complete configuration without explaining the version difference.

The dedicated UAV pool retains **Rethinking Occlusion Modeling for UAV Tracking**, F2Net, SPAR-Det, and **Tracking Tiny Drones against Clutter**. The fire transfer pool retains **SmokeSVD**, RealX3D, and FireMan-UAV-RGBT; SmokeSVD contributes dynamic, translucent, physics-consistent smoke modeling but is not presented as an early-wildfire detector. The complete evidence, source failures, historical exclusions, and COD/UAV/fire transfer boundaries are retained in `D:\Codex输出\daily-cv-literature-feed-update\final\2026-08-14\2026-08-14-检索与筛选报告.md`.

---

# Verified Daily Search Update - 2026-08-15

The expanded scan ran with `DEEP_SOURCE_SCAN=1` and isolated all automatic downloads on the D drive while Zotero import was disabled. It collected 9,403 raw CVF records, reached 10,194 cumulative Crossref records, merged 10,747 cached candidates, and formed a final pool of 10,751 papers. arXiv entered degraded mode after three HTTP 429 responses; Semantic Scholar did the same for the safety-critical, multimodal-hazard, and open-world-multimodal clusters; selected TPAMI Crossref queries also returned 429. These clusters remain in the cache and next-run plan rather than being treated as empty results.

The final queue was frozen after excluding the provisional 2026-08-15 snapshot and checking normalized titles plus official CVF HTML/PDF identities against all feed sections through 2026-08-14, the curated-highlight ledger, and the 160-entry Zotero-imported download index:

1. **Memory-Augmented Scene Understanding and Exploration for Open-World Aerial Object-Goal Navigation** (CVPR 2026)
2. **The Road Less Seen: Segment Exploration for Weakly Supervised Video Anomaly Detection** (CVPR 2026)
3. **Uni-Encoder Meets Multi-Encoders: Representation Before Fusion for Brain Tumor Segmentation with Missing Modalities** (CVPR 2026)
4. **Diagnosing and Repairing Unsafe Channels in Vision-Language Models via Causal Discovery and Dual-Modal Safety Subspace Projection** (CVPR 2026)
5. **ADSeeker: A Knowledge-Grounded Reasoning Framework for Industry Anomaly Detection and Reasoning** (CVPR 2026)

All five official main PDFs and available supplements passed signature and three-way page-count preflight and were read beyond their abstracts. The queue combines open-world aerial active perception, low-FPR video-anomaly evaluation, missing-modality representation learning, causal VLM safety repair, and knowledge-grounded anomaly reasoning. AerialMemory is the dedicated UAV anchor. SmokeSVD remains a fire-transfer candidate because it models dynamic translucent smoke in 3D, but it was not promoted as an early-fire detector because it does not evaluate alarm recall, practical false positives, cloud/fog/haze/sunset/reflection negatives, RGB-T reliability, or edge deployment. Full source failures, evidence boundaries, specialist UAV/fire candidates, and selection rationale are retained in `D:\Codex输出\daily-cv-literature-feed-update\final\2026-08-15\2026-08-15-检索与筛选报告.md`.
