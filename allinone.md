# Supplemental Paper Search Report - 2026-07-29

This report records the complete supplemental search run requested for the three linked monitoring clusters. It preserves source-level successes and failures, then separates raw discovery from primary-source verification and screening. No paper was promoted from title matching alone.

- Search window: 2024-2026
- Maximum returned records: 10 per source
- Aggregators: arXiv, DBLP, OpenAlex, OpenReview, Semantic Scholar, Crossref
- Duplicate gates: `data/feed_history.json` historical `sections.highlights` and `F:\文献整理\每日精读论文\_downloaded_papers.json`
- Result of duplicate gate: all 12 screened candidates below are absent from both historical deep-reading selections and the local download index.

## 1. Cluster A - Safety-critical perception, multimodal reliability, OOD and risk

Query:

`safety-critical multimodal perception missing degraded modality out-of-distribution selective prediction risk control hazard anticipation`

### Source errors and degraded-source evidence

The source runner emitted the following errors exactly:

```text
[openreview] Error: openreview not installed. pip install openreview-py
[open_alex] Error: 504 Server Error: Gateway Timeout for url: https://api.openalex.org/works?search.semantic=safety-critical+multimodal+perception+missing+degraded+modality+out-of-distribution+selective+prediction+risk+control+hazard+anticipation&filter=publication_year%3A2024-2026&sort=relevance_score%3Adesc&page=1&per-page=10
```

The runner also emitted repeated `Rate limited. Waiting 3 seconds...` messages. DBLP and Semantic Scholar completed with zero returned records; this is recorded as a degraded retrieval outcome, not as proof that the cluster has no relevant papers.

### Crossref - 10 returned records

| # | Title | Authors | Year / venue | URL |
|---|---|---|---|---|
| 1 | Guarantees That Survive a Missing Scan: Modality-Conditional Conformal Prediction for Multimodal Medical Diagnosis | Aaron Ajit | year unavailable / venue unavailable | https://doi.org/10.21203/rs.3.rs-10336064/v1 |
| 2 | Safety-Calibrated Out-of-Distribution Prediction via Contrastive Embeddings for Safety-Critical Systems | Ahmad O. Aseeri | 2026 / Electronics | https://doi.org/10.3390/electronics15112408 |
| 3 | Engineering Safety Requirements for Maritime Autonomous Surface Systems: Hazard Scenarios, Control Loss, and Recovery in Degraded Operations | Karim Hardy | year unavailable / venue unavailable | https://doi.org/10.21203/rs.3.rs-9752188/v1 |
| 4 | Multimodal Sentiment Analysis Based Textual-information Enhancement With Modality Missing | TengFei Song; Shuo Wang | year unavailable / venue unavailable | https://doi.org/10.2139/ssrn.5679165 |
| 5 | Sparse multimodal observability under degraded traffic sensing: critical-density theory and tail-risk evidence | Claire Y.T. Chen; Edward Sun; Yihan Huang et al. | year unavailable / venue unavailable | https://doi.org/10.2139/ssrn.6879078 |
| 6 | Differentiable Optimization Layered Safety-Critical Control for Risk-Aware Navigation via Conformal Prediction | Jinyang Dong; Shizhen Wu; Yongchun Fang | year unavailable / venue unavailable | https://doi.org/10.2139/ssrn.6742618 |
| 7 | A multimodal deep learning framework for enzyme turnover prediction with missing modality | Xin Sun; Yu Guang Wang; Yiqing Shen | 2025 / Computers in Biology and Medicine | https://doi.org/10.1016/j.compbiomed.2025.110348 |
| 8 | Factors Influencing Motorcycle Crash Risk and Accident Prediction Ability: The Role of Hazard Perception Training in Thailand | Thanchanok Inmor; Kunnawee Kanitpong | year unavailable / venue unavailable | https://doi.org/10.2139/ssrn.6477779 |
| 9 | Text-based Multimodal Sentiment Analysis: Missing Modality Prompt Learning and Hyper-modality Representation | Yanzu Wei; Hongrui Zhao | 2025 / ICSP | https://doi.org/10.1109/icsp65755.2025.11086658 |
| 10 | Temporal Multimodal Knowledge Distillation for Modality-Missing RGBT Tracking | Rui Ruan; Yunlong Kang; Lei Liu et al. | year unavailable / venue unavailable | https://doi.org/10.2139/ssrn.5953538 |

### arXiv - 10 returned records

| # | Title | Authors | Year | URL |
|---|---|---|---|---|
| 1 | Safety-Critical Stabilization of Force-Controlled Nonholonomic Mobile Robots | Tianyu Han; Bo Wang | 2024 | http://arxiv.org/abs/2408.10941v2 |
| 2 | Model Predictive Control of Hybrid Dynamical Systems | Ricardo G. Sanfelice; Berk Altin | 2026 | http://arxiv.org/abs/2604.21989v1 |
| 3 | Constructive Safety-Critical Control: Synthesizing Control Barrier Functions for Partially Feedback Linearizable Systems | Max H. Cohen; Ryan K. Cosner; Aaron D. Ames | 2024 | http://arxiv.org/abs/2406.02709v1 |
| 4 | Input-to-State Safe Backstepping: Robust Safety-Critical Control with Unmatched Uncertainties | Max H. Cohen; Pio Ong; Aaron D. Ames | 2026 | http://arxiv.org/abs/2602.03691v1 |
| 5 | Evidential Fusion Network for Multimodal Survival Prediction under Missing Modalities | Yucheng Xing; Hailan Mo; Zi Wang et al. | 2026 | http://arxiv.org/abs/2606.20757v1 |
| 6 | Next Token Prediction Towards Multimodal Intelligence: A Comprehensive Survey | Liang Chen; Zekun Wang; Shuhuai Ren et al. | 2024 | http://arxiv.org/abs/2412.18619v2 |
| 7 | Dynamic Modality and View Selection for Multimodal Emotion Recognition with Missing Modalities | Luciana Trinkaus Menon; Luiz Carlos Ribeiro Neduziak; Jean Paul Barddal et al. | 2024 | http://arxiv.org/abs/2404.12251v1 |
| 8 | AMBER: An Adaptive Multimodal Mask Transformer for Beam Prediction with Missing Modalities | Chenyiming Wen; Binpu Shi; Min Li et al. | 2025 | http://arxiv.org/abs/2512.11331v2 |
| 9 | Differentiable Optimization Layered Safety-Critical Control for Risk-Aware Navigation via Conformal Prediction | Jinyang Dong; Shizhen Wu; Yongchun Fang | 2026 | http://arxiv.org/abs/2605.16327v1 |
| 10 | Risk-Aware Vehicle Trajectory Prediction Under Safety-Critical Scenarios | Qingfan Wang; Dongyang Xu; Gaoyuan Kuang et al. | 2024 | http://arxiv.org/abs/2407.13480v1 |

### Cluster-A screening judgment

The long conjunctive query over-weighted control and generic missing-modality records, so none of its raw hits was promoted directly. Official CVF follow-up instead verified five stronger ICCV 2025 papers: UniFuse, SimMLM, MD2N, MissRAG, and SyP. This is an important retrieval lesson for the next automation run: the linked cluster should be decomposed into narrow subqueries rather than treated as one literal phrase.

## 2. Cluster B - Grounded/open-vocabulary reasoning and compositional generalization

Query:

`open-vocabulary visual grounding grounded visual reasoning compositional generalization open-world segmentation`

### Source errors and adjusted execution

The initial six-source run exceeded the 180-second command limit and returned:

```text
command timed out after 184037 milliseconds
```

A source-isolated retry was justified because it changed the execution strategy rather than blindly repeating the same request. The first isolated Crossref process exposed a Windows-console encoding fault:

```text
UnicodeEncodeError: 'gbk' codec can't encode character '\u1d43' in position 28: illegal multibyte sequence
```

After setting `PYTHONIOENCODING=utf-8`, arXiv, DBLP, and Crossref completed. DBLP returned zero records. OpenAlex, Semantic Scholar, and OpenReview were not re-run after the global timeout; that missing coverage remains explicitly recorded for the next run.

### arXiv - 10 returned records

| # | Title | Authors | Year | URL |
|---|---|---|---|---|
| 1 | Explain Before You Answer: A Survey on Compositional Visual Reasoning | Fucai Ke; Joy Hsu; Zhixi Cai et al. | 2025 | http://arxiv.org/abs/2508.17298v3 |
| 2 | Visual Reasoning Tracer: Object-Level Grounded Reasoning Benchmark | Haobo Yuan; Yueyi Sun; Yanwei Li et al. | 2025 | http://arxiv.org/abs/2512.05091v1 |
| 3 | Towards Visual Grounding: A Survey | Linhui Xiao; Xiaoshan Yang; Xiangyuan Lan et al. | 2024 | http://arxiv.org/abs/2412.20206v3 |
| 4 | DEGround: An Effective Baseline for Ego-centric 3D Visual Grounding with a Homogeneous Framework | Yani Zhang; Dongming Wu; Hao Shi et al. | 2025 | http://arxiv.org/abs/2506.05199v3 |
| 5 | Visual Boosting Techniques for Spatiotemporal Dense Pixel Visualizations | Julius Rauscher; Frederik L. Dennig; Udo Schlegel et al. | 2026 | http://arxiv.org/abs/2604.25298v1 |
| 6 | Multi-Task Learning for Visually Grounded Reasoning in Gastrointestinal VQA | Itbaan Safwan; Muhammad Annas Shaikh; Muhammad Haaris et al. | 2025 | http://arxiv.org/abs/2511.04384v1 |
| 7 | Grounded Reinforcement Learning for Visual Reasoning | Gabriel Sarch; Snigdha Saha; Naitik Khandelwal et al. | 2025 | http://arxiv.org/abs/2505.23678v3 |
| 8 | Visual Generation Unlocks Human-Like Reasoning through Multimodal World Models | Jialong Wu; Xiaoying Zhang; Hongyi Yuan et al. | 2026 | http://arxiv.org/abs/2601.19834v1 |
| 9 | ScanReason: Empowering 3D Visual Grounding with Reasoning Capabilities | Chenming Zhu; Tai Wang; Wenwei Zhang et al. | 2024 | http://arxiv.org/abs/2407.01525v3 |
| 10 | OpenSeg-R: Improving Open-Vocabulary Segmentation via Step-by-Step Visual Reasoning | Zongyan Han; Jiale Cao; Shuo Chen et al. | 2025 | http://arxiv.org/abs/2505.16974v2 |

### Crossref - 10 returned records

| # | Title | Authors | Year / venue | URL |
|---|---|---|---|---|
| 1 | CARVE: Open-Vocabulary Product Discovery and Segmentation for Measuring Commercial Content in Visual Social Media | Andrew Dunton; Mohammad Masum | year unavailable / venue unavailable | https://doi.org/10.2139/ssrn.6485441 |
| 2 | Visual Programming for Zero-Shot Open-Vocabulary 3D Visual Grounding | Zhihao Yuan; Jinke Ren; Chun-Mei Feng et al. | 2024 / CVPR | https://doi.org/10.1109/cvpr52733.2024.01949 |
| 3 | IndoGroundingDINO: Monolingual Open-Vocabulary Visual Grounding with Swin-T and IndoBERT | Diva Aninditha; Suryo Adhi Wibowo; Koredianto Usman | 2025 / ICITCOM | https://doi.org/10.1109/icitcom66635.2025.11265614 |
| 4 | OV3DSeg-VGGT: Open-Vocabulary 3D Segmentation with Visual Geometry-Grounded Transformers | Jingke Zhou; Xianliang Huang; Yixin Ren et al. | 2026 / Visual Informatics | https://doi.org/10.1016/j.visinf.2026.100311 |
| 5 | Generalization-Preserving Adaptation of Vision-Language Models for Open-Vocabulary Segmentation | Zhen Chen; Hao Tang; Shiliang Zhang | year unavailable / venue unavailable | https://doi.org/10.2139/ssrn.5134414 |
| 6 | In Defense of Lazy Visual Grounding for Open-Vocabulary Semantic Segmentation | Dahyun Kang; Minsu Cho | 2025 metadata / ECCV 2024 proceedings | https://doi.org/10.1007/978-3-031-72940-9_9 |
| 7 | ReasonGrounder: LVLM-Guided Hierarchical Feature Splatting for Open-Vocabulary 3D Visual Grounding and Reasoning | Zhenyang Liu; Yikai Wang; Sixiao Zheng et al. | 2025 / CVPR | https://doi.org/10.1109/cvpr52734.2025.00352 |
| 8 | DAR-Net: Resolving Visual and Semantic Ambiguity for Open-Vocabulary Camouflaged Object Segmentation | Xiaoao Zhou; Yuchen Li; Yi Liu et al. | year unavailable / venue unavailable | https://doi.org/10.2139/ssrn.6444450 |
| 9 | A Neural Representation Framework with LLM-Driven Spatial Reasoning for Open-Vocabulary 3D Visual Grounding | Zhenyang Liu; Sixiao Zheng; Siyu Chen et al. | 2025 / ACM Multimedia | https://doi.org/10.1145/3746027.3754918 |
| 10 | GAN-DRIVEN OPEN-VOCABULARY VISUAL SPEECH RECONSTRUCTION WITH CROSS-SPEAKER GENERALIZATION | S. Geetha; M. Sangeetha; P. Latha et al. | 2026 / International Journal of Drug Delivery Technology | https://doi.org/10.25258/ijddt.16.60s.156 |

## 3. Cluster C - UAV/tiny perception and RGB-T fire/smoke

Query:

`UAV aerial remote sensing tiny small object detection tracking fire smoke RGB-T visible thermal`

### Source errors

The source runner emitted repeated rate-limit waits and the following OpenAlex failure exactly:

```text
[open_alex] Error: 504 Server Error: Gateway Timeout for url: https://api.openalex.org/works?search.semantic=UAV+aerial+remote+sensing+tiny+small+object+detection+tracking+fire+smoke+RGB-T+visible+thermal&filter=publication_year%3A2024-2026&sort=relevance_score%3Adesc&page=1&per-page=10
```

DBLP returned zero records. Semantic Scholar returned one record. arXiv and Crossref each returned ten.

### Crossref - 10 returned records

| # | Title | Authors | Year / venue | URL |
|---|---|---|---|---|
| 1 | Contextual-Semantic Interactive Perception Network for Small Object Detection in UAV Aerial Images | Yiming Xu; Hongbing Ji | 2025 / Remote Sensing | https://doi.org/10.3390/rs17213581 |
| 2 | Uncertainty-Guided VMamba for RGB-Infrared Oriented Object Detection in UAV Remote Sensing | Zhiguo Liu; Jialin Li; Lin Wang | year unavailable / venue unavailable | https://doi.org/10.2139/ssrn.6773850 |
| 3 | Cross-modal Semantic Hypergraph Network for RGB-T Object Detection in UAV Remote Sensing | Qi Tian; Tingyao Jiang; Hao Zhang | year unavailable / venue unavailable | https://doi.org/10.2139/ssrn.7149244 |
| 4 | Pseudo-Segmentation Guided Detection Refinement for Remote Sensing Small Object Tracking | Chenyang Yan | year unavailable / venue unavailable | https://doi.org/10.21203/rs.3.rs-8181069/v1 |
| 5 | HAFM-Net: Hierarchical Alignment Fusion and Mapping for UAV-Based Misaligned RGB-T Salient Object Detection | Zhijie Zhang; Kaihong Chen; Chen Yang et al. | 2026 / Remote Sensing | https://doi.org/10.3390/rs18122039 |
| 6 | DCS-YOLOv8: A Lightweight Context-Aware Network for Small Object Detection in UAV Remote Sensing Imagery | Xiaozheng Zhao; Zhongjun Yang; Huaici Zhao | 2025 / Remote Sensing | https://doi.org/10.3390/rs17172989 |
| 7 | SODet-YOLO: A Small Object Detection Algorithm for UAV Aerial Photography Perspective | Ke Zeng; Wangsheng Yu; Siyu Long et al. | 2026 / Remote Sensing | https://doi.org/10.3390/rs18111714 |
| 8 | Dual-Level Attention Relearning for Cross-Modality Rotated Object Detection in UAV RGB-Thermal Imagery | Zhuqiang Li; Zhijun Zhen; Shengbo Chen et al. | 2025 / Remote Sensing | https://doi.org/10.3390/rs18010107 |
| 9 | LFS-YOLO: A Lightweight Frequency-Semantic Network for Dense Tiny Object Detection in UAV Aerial Images | Xue Feng; Hongmin Zhang; Qing Chen | year unavailable / venue unavailable | https://doi.org/10.2139/ssrn.6512539 |
| 10 | Sparse-Gated RGB-Event Fusion for Small Object Detection in the Wild | Yangsi Shi; Miao Li; Nuo Chen et al. | 2025 / Remote Sensing | https://doi.org/10.3390/rs17173112 |

### arXiv - 10 returned records

| # | Title | Authors | Year | URL |
|---|---|---|---|---|
| 1 | Real-Time Oriented Object Detection Transformer in Remote Sensing Images | Zeyu Ding; Yong Zhou; Jiaqi Zhao et al. | 2026 | http://arxiv.org/abs/2603.15497v1 |
| 2 | Change-Agent: Towards Interactive Comprehensive Remote Sensing Change Interpretation and Analysis | Chenyang Liu; Keyan Chen; Haotian Zhang et al. | 2024 | http://arxiv.org/abs/2403.19646v3 |
| 3 | Vision-Language Modeling Meets Remote Sensing: Models, Datasets and Perspectives | Xingxing Weng; Chao Pang; Gui-Song Xia | 2025 | http://arxiv.org/abs/2505.14361v1 |
| 4 | Remote Sensing SpatioTemporal Vision-Language Models: A Comprehensive Survey | Chenyang Liu; Jiafan Zhang; Keyan Chen et al. | 2024 | http://arxiv.org/abs/2412.02573v3 |
| 5 | TimeSenCLIP: A Time Series Vision-Language Model for Remote Sensing | Pallavi Jain; Diego Marcos; Dino Ienco et al. | 2025 | http://arxiv.org/abs/2508.11919v3 |
| 6 | A Progressive Image Restoration Network for High-order Degradation Imaging in Remote Sensing | Yujie Feng; Yin Yang; Xiaohong Fan et al. | 2024 | http://arxiv.org/abs/2412.07195v2 |
| 7 | Prompt-Calibrated SAM 3 for Open-Vocabulary Remote Sensing Semantic Segmentation | Yanghui Song; Nanqing Liu; Haonan Yin et al. | 2026 | http://arxiv.org/abs/2606.21863v2 |
| 8 | NBBOX: Noisy Bounding Box Improves Remote Sensing Object Detection | Yechan Kim; SooYeon Kim; Moongu Jeon | 2024 | http://arxiv.org/abs/2409.09424v3 |
| 9 | Fusion of Cellular ISAC and Passive RF Sensing for UAV Detection and Tracking | Cole Dickerson; Sean Kearney; Sultan Manjur et al. | 2025 | http://arxiv.org/abs/2512.14608v1 |
| 10 | Improving the Detection of Small Oriented Objects in Aerial Images | Chandler Timm C. Doloriel; Rhandley D. Cajote | 2024 | http://arxiv.org/abs/2401.06503v1 |

### Semantic Scholar - 1 returned record

| # | Title | Authors | Year / venue | URL |
|---|---|---|---|---|
| 1 | Edge-Deployable RGB-Thermal UAV Monitoring for Wildfires in Power Transmission Corridors | Biao Wang; Daochun Huang; Yifeng Lin et al. | 2026 / Remote Sensing | https://www.semanticscholar.org/paper/9ee8bfd911a83f4e4a3e98348a5f9c47023dd365 |

## 4. Primary-source-verified non-duplicate shortlist

All papers in this section were checked against the official proceedings or publisher full text, not only aggregator snippets. Every title is absent from the historical deep-reading `highlights` and from the local PDF index. “Equation availability” describes what is actually present in the paper; it is not a promise that a title implies mathematics.

### A. Multimodal reliability under missing, degraded, or misaligned evidence

1. **UniFuse: A Unified All-in-One Framework for Multi-Modal Medical Image Fusion Under Diverse Degradations and Misalignments** - ICCV 2025.
   - Official page: https://openaccess.thecvf.com/content/ICCV2025/html/Su_UniFuse_A_Unified_All-in-One_Framework_for_Multi-Modal_Medical_Image_Fusion_ICCV_2025_paper.html
   - Full PDF: https://openaccess.thecvf.com/content/ICCV2025/papers/Su_UniFuse_A_Unified_All-in-One_Framework_for_Multi-Modal_Medical_Image_Fusion_ICCV_2025_paper.pdf
   - Actual mechanism: degradation-aware prompt learning drives a one-stage alignment/restoration/fusion pipeline; Omni Unified Feature Representation uses Spatial Mamba; feature alignment predicts deformation; Universal Feature Restoration & Fusion uses an Adaptive LoRA Synergistic Network.
   - Equation availability: rich. The PDF formalizes prompt conditioning, Spatial-Mamba scanning, deformation/warping, adaptive LoRA routing, and restoration/fusion objectives.
   - Transfer value: directly tests the usually hidden assumption that paired modalities are both clean and registered. This is highly transferable to RGB-T fire, UAV motion/misalignment, and COD systems that add depth/thermal cues.

2. **SimMLM: A Simple Framework for Multi-modal Learning with Missing Modality** - ICCV 2025.
   - Official page: https://openaccess.thecvf.com/content/ICCV2025/html/Li_SimMLM_A_Simple_Framework_for_Multi-modal_Learning_with_Missing_Modality_ICCV_2025_paper.html
   - Full PDF: https://openaccess.thecvf.com/content/ICCV2025/papers/Li_SimMLM_A_Simple_Framework_for_Multi-modal_Learning_with_Missing_Modality_ICCV_2025_paper.pdf
   - Actual mechanism: a Dynamic Mixture of Modality Experts gates only the available experts, while More-vs-Fewer ranking loss enforces the monotonic reliability prior that adding a modality should not make a prediction worse.
   - Equation availability: moderate and central. Gating/fusion, task objectives, and the pairwise MoFe ranking constraint are explicitly defined.
   - Transfer value: offers a falsifiable reliability property for RGB-T fire and UAV fusion, and a clean way to test whether an auxiliary depth/thermal stream truly helps COD rather than introducing shortcut noise.

3. **Unbiased Missing-modality Multimodal Learning** - ICCV 2025.
   - Official page: https://openaccess.thecvf.com/content/ICCV2025/html/Dai_Unbiased_Missing-modality_Multimodal_Learning_ICCV_2025_paper.html
   - Full PDF: https://openaccess.thecvf.com/content/ICCV2025/papers/Dai_Unbiased_Missing-modality_Multimodal_Learning_ICCV_2025_paper.pdf
   - Actual mechanism: MD2N is a duplex diffusion model in which available and missing streams generate each other through global-structure generation, modality transfer, and local cross-modal refinement, reducing generation-direction bias.
   - Equation availability: rich. Forward/reverse diffusion, duplex conditioning, modality-transfer/refinement, and training losses are mathematically specified.
   - Transfer value: the useful question is not merely “can a missing modality be synthesized?” but “is reconstruction quality asymmetric by direction?” That matters for reconstructing thermal from RGB in fire scenes and weak structural cues from appearance in COD.

4. **MissRAG: Addressing the Missing Modality Challenge in Multimodal Large Language Models** - ICCV 2025.
   - Official page: https://openaccess.thecvf.com/content/ICCV2025/html/Pipoli_MissRAG_Addressing_the_Missing_Modality_Challenge_in_Multimodal_Large_Language_ICCV_2025_paper.html
   - Full PDF: https://openaccess.thecvf.com/content/ICCV2025/papers/Pipoli_MissRAG_Addressing_the_Missing_Modality_Challenge_in_Multimodal_Large_Language_ICCV_2025_paper.pdf
   - Actual mechanism: frozen contrastive encoders map audio/video/text into a shared space; available modalities query a training-set prototype bank; top-k missing-modality tokens are averaged or concatenated; status-aware prompts tell the MLLM which streams are present, retrieved, or absent.
   - Equation availability: limited-to-moderate. The paper formalizes missing-subset scenarios and similarity/top-k retrieval, but most novelty is architectural and prompting rather than derivation-heavy.
   - Transfer value: prototype retrieval avoids hallucinating a precise absent sensor stream. It is a useful contrastive baseline for COD/UAV/fire systems that should retrieve analogous evidence and carry provenance rather than fabricate pixels.

5. **Synergistic Prompting for Robust Visual Recognition with Missing Modalities** - ICCV 2025.
   - Official page: https://openaccess.thecvf.com/content/ICCV2025/html/Zhang_Synergistic_Prompting_for_Robust_Visual_Recognition_with_Missing_Modalities_ICCV_2025_paper.html
   - Full PDF: https://openaccess.thecvf.com/content/ICCV2025/papers/Zhang_Synergistic_Prompting_for_Robust_Visual_Recognition_with_Missing_Modalities_ICCV_2025_paper.pdf
   - Actual mechanism: a Dynamic Adapter generates input-specific scaling factors for a base prompt; static prompts retain shared prior knowledge; the synergistic strategy injects their combination across image/text branches and missingness conditions.
   - Equation availability: moderate. Dynamic scaling, prompt construction/injection, branch fusion, and supervised objectives are explicit.
   - Transfer value: supports low-parameter adaptation to changing sensor availability, but its image-text setting is not automatically equivalent to RGB-T alignment; that boundary should be tested explicitly.

### B. Grounding, open vocabulary, and compositional reasoning

6. **ReasonGrounder: LVLM-Guided Hierarchical Feature Splatting for Open-Vocabulary 3D Visual Grounding and Reasoning** - CVPR 2025.
   - Official page: https://openaccess.thecvf.com/content/CVPR2025/html/Liu_ReasonGrounder_LVLM-Guided_Hierarchical_Feature_Splatting_for_Open-Vocabulary_3D_Visual_Grounding_CVPR_2025_paper.html
   - Full PDF: https://openaccess.thecvf.com/content/CVPR2025/papers/Liu_ReasonGrounder_LVLM-Guided_Hierarchical_Feature_Splatting_for_Open-Vocabulary_3D_Visual_Grounding_CVPR_2025_paper.pdf
   - Actual mechanism: SAM masks and 3DGS depth yield physical-scale supervision; latent Gaussian features are mapped into hierarchical language and instance fields; CLIP/contrastive supervision enforces multiview consistency; an LVLM selects a reference view for implicit-query and amodal grounding.
   - Equation availability: rich. 3D Gaussian rendering, physical-scale estimation, hierarchical feature mapping, and contrastive objectives are present.
   - Transfer value: physical-scale-conditioned grouping could keep tiny UAV targets separate and let COD/fire reasoning refer to occluded or only partially visible evidence, though 3D scene assumptions break for translucent smoke.

7. **In Defense of Lazy Visual Grounding for Open-Vocabulary Semantic Segmentation** - ECCV 2024.
   - Official DOI: https://doi.org/10.1007/978-3-031-72940-9_9
   - Full PDF: https://arxiv.org/pdf/2408.04961
   - Actual mechanism: discover object masks before reading class text, using iterative Normalized Cuts over visual features; only after object discovery does late CLIP-based interaction attach open-vocabulary labels.
   - Equation availability: moderate. Affinity/graph partitioning, iterative mask discovery, and late grounding scores are formalized.
   - Transfer value: decoupling “where is a coherent region?” from “what word names it?” is a strong COD hypothesis because text priors can bias the model away from visually ambiguous foregrounds; it also supplies a clean open-vocabulary fire/COD baseline.

8. **Visual Programming for Zero-shot Open-Vocabulary 3D Visual Grounding** - CVPR 2024.
   - Official page: https://openaccess.thecvf.com/content/CVPR2024/html/Yuan_Visual_Programming_for_Zero-shot_Open-Vocabulary_3D_Visual_Grounding_CVPR_2024_paper.html
   - Full PDF: https://openaccess.thecvf.com/content/CVPR2024/papers/Yuan_Visual_Programming_for_Zero-shot_Open-Vocabulary_3D_Visual_Grounding_CVPR_2024_paper.pdf
   - Actual mechanism: an LLM compiles a referring expression into executable view-independent, view-dependent, and functional modules; a language-object correlation component opens a conventional 3D detector’s vocabulary; the program composes target, anchor, and relation operations.
   - Equation availability: sparse. The contribution is executable module semantics and program traces, with few central mathematical equations.
   - Transfer value: provides auditable compositional grounding for hazard queries such as “smoke behind the tower” or “tiny vehicle nearest the fire front,” while also exposing parsing and detector-proposal failure separately.

### C. UAV/tiny targets and fire/smoke

9. **Uncertainty-Aware Gradient Stabilization for Small Object Detection** - ICCV 2025.
   - Official page: https://openaccess.thecvf.com/content/ICCV2025/html/Sun_Uncertainty-Aware_Gradient_Stabilization_for_Small_Object_Detection_ICCV_2025_paper.html
   - Full PDF: https://openaccess.thecvf.com/content/ICCV2025/papers/Sun_Uncertainty-Aware_Gradient_Stabilization_for_Small_Object_Detection_ICCV_2025_paper.pdf
   - Actual mechanism: the paper diagnoses sharper localization-loss curvature for small objects, quantizes continuous box labels into non-uniform intervals, replaces regression with bounded classification gradients, minimizes entropy, and adversarially perturbs/refines uncertain regions.
   - Equation availability: rich. Hessian/gradient analysis, discretization, classification localization, uncertainty-minimization entropy, and adversarial refinement are all formalized.
   - Transfer value: reframes UAV tiny-object weakness as an optimization instability rather than only a feature-resolution problem. The same diagnostic can test whether weak COD boundaries and early flame/smoke boxes also remain in high-curvature nonconverged regions.

10. **From Easy to Hard: Progressive Active Learning Framework for Infrared Small Target Detection with Single Point Supervision** - ICCV 2025.
    - Official page: https://openaccess.thecvf.com/content/ICCV2025/html/Yu_From_Easy_to_Hard_Progressive_Active_Learning_Framework_for_Infrared_ICCV_2025_paper.html
    - Full PDF: https://openaccess.thecvf.com/content/ICCV2025/papers/Yu_From_Easy_to_Hard_Progressive_Active_Learning_Framework_for_Infrared_ICCV_2025_paper.pdf
    - Actual mechanism: easy-sample pseudo-label generation pre-starts the detector; progressive active selection adds harder samples only after the learner becomes task-capable; a refined dual update evolves both training pool and pseudo-masks; a decay factor prevents uncontrolled mask expansion.
    - Equation availability: rich. Easy-sample scoring, selection/update rules, pseudo-label evolution, decay, and optimization losses are specified.
    - Transfer value: directly informs cheap point supervision for UAV tiny targets and early flame spots. For COD, the hard/easy order must be redefined by foreground-background similarity rather than target size alone.

11. **Breaking Smooth-Motion Assumptions: A UAV Benchmark for Multi-Object Tracking in Complex and Adverse Conditions** - CVPR 2026.
    - Official page: https://openaccess.thecvf.com/content/CVPR2026/html/Ye_Breaking_Smooth-Motion_Assumptions_A_UAV_Benchmark_for_Multi-Object_Tracking_in_CVPR_2026_paper.html
    - Full PDF: https://openaccess.thecvf.com/content/CVPR2026/papers/Ye_Breaking_Smooth-Motion_Assumptions_A_UAV_Benchmark_for_Multi-Object_Tracking_in_CVPR_2026_paper.pdf
    - Actual mechanism: DynUAV contributes 42 long UAV sequences and over 1.7 million boxes under deliberate agile ego-motion, drastic scale/view change, blur, diverse environments, and non-linear apparent trajectories; it diagnoses coupled detection-association failure rather than proposing a new tracker.
    - Equation availability: sparse. The paper mainly uses established tracking metrics and dataset statistics; there is no equation-heavy novel model.
    - Transfer value: valuable as an evaluation viewpoint. Fire/smoke monitoring and UAV COD should report robustness to ego-motion-induced temporal flicker instead of assuming smooth cameras and treating each frame independently.

12. **Edge-Deployable RGB-Thermal UAV Monitoring for Wildfires in Power Transmission Corridors** - Remote Sensing 2026.
    - Official full-text page: https://www.mdpi.com/2072-4292/18/12/1869
    - Full PDF: https://www.mdpi.com/2072-4292/18/12/1869/pdf
    - DOI: https://doi.org/10.3390/rs18121869
    - Actual mechanism: YOLO-MMSC combines mirrored RGB/TIR branches, MBConv lightweight blocks, Shallow Detail Fusion for alignment/denoising, Content-Guided Attention for adaptive fusion, and NWD box regression for distant small targets; YOLO-MMSC-T adds temporal-consistency fine-tuning.
    - Equation availability: moderate. MBConv/fusion operations, NWD localization, and temporal consistency are explicit; this is an integrated engineering paper rather than a new mathematical theory.
    - Transfer value: this is the most direct fire anchor. It reports 94.6% mAP@0.5, 95.0% precision, 93.9% recall, 60 FPS on Jetson Orin NX, CDR 95.6%, and jitter index 2.8e-3, while explicitly testing nighttime, smoke/vegetation occlusion, long-range targets, hard negatives, and 60-210 m UAV altitude.

## 5. Final deep-reading queue and selection rationale

After the supplemental search was merged with the independently verified CVPR 2026 pool, the final five are **Anchor-Guided Gradient Alignment for Incomplete Multimodal Learning (ANGA)**, **Spatio-Temporal Conditional Denoising Transformer for Modality-Missing RGBT Tracking (SCDT)**, **SRA-Det**, **Synthetic Object Compositions (SOC)**, and **Towards Persistence: Learning Topological Constraints for Event-based Small Object Detection (SpTopoNet)**. All five were checked from official CVF full text, are absent from prior daily highlight queues, and expose complete method equations suitable for the required long-form reading.

This final set deliberately separates five questions rather than selecting papers by keyword match: ANGA studies optimization imbalance caused by reconstructed modalities; SCDT studies temporal recovery and enhancement under missing RGB-T streams; SRA-Det tests attribute-level compositional grounding beyond category names; SOC turns controllable composition into high-integrity detection, segmentation, and grounding supervision; SpTopoNet imposes persistent topological structure on sparse event-camera small-target evidence. The result is not COD-saturated, includes a direct UAV/tiny-target paper, and gives fire perception two concrete transfer routes through RGB-T reliability and temporal weak-evidence modeling without forcing a lower-confidence fire paper into the five.

The earlier candidate recommendation of UniFuse, SimMLM, ReasonGrounder, Uncertainty-Aware Gradient Stabilization, and From Easy to Hard is retained above as a verified follow-up pool, not today's queue. UniFuse, MD2N, MissRAG, SyP, Lazy Grounding, Visual Programming, DynUAV, and the RGB-T wildfire paper remain next-run candidates. The wildfire paper is still the direct fire anchor for the dedicated section, but its integrated journal-engineering contribution was not promoted over the five stronger method questions solely to satisfy topic coverage.

## 6. Retrieval gaps retained for the next run

- Install or isolate `openreview-py` before treating OpenReview as covered.
- Split Cluster A into at least three narrow queries: missing/degraded modalities, multimodal OOD/calibration, and selective/risk-controlling perception.
- Re-run Cluster B on OpenAlex and Semantic Scholar only after their current timeout/rate-limit window clears; do not rerun the same six-source monolithic request.
- Keep the exact fire query (`RGB-T wildfire smoke temporal consistency hard negatives`) separate from generic UAV detection, which otherwise suppresses fire records in semantic search.
- Preserve UniFuse, MD2N, MissRAG, SyP, Lazy Grounding, Visual Programming, DynUAV, and the RGB-T wildfire paper in the cached-candidate pool if they are not selected today.
