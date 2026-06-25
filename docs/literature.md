# Daily CV Paper Feed

Last updated: 2026-06-26 01:27 Asia/Shanghai

This page tracks new and useful computer-vision papers, with COD/camouflaged object detection kept as the primary reading thread and broader CV methods included for inspiration.

## 今日优先读：近 30 天新文献优先

1. **CFCamo: A Counterfactual Detect-or-Abstain Framework for Camouflaged Object Detection**
   - Source: arXiv, 2026-05-28
   - Authors: Suhang Li, Osamu Yoshie, Yuya Ieiri
   - Tags: COD, SAM, VLM/MLLM
   - Links: [paper](http://arxiv.org/abs/2606.11231v1) / [pdf](http://arxiv.org/pdf/2606.11231v1)
   - 简介：Vision-language reinforcement learning has recently shown strong target-present localization for camouflaged object detection (COD). Yet localization is only one side of the decision: when the agent faces an ordinary image with no camouflaged target, will it...
   - 为什么值得读：直接关联伪装目标检测/分割，优先看方法和消融。

2. **A Retinomorphic Optical Spiking Neuron for Camouflaged Object Detection**
   - Source: arXiv, 2026-05-30
   - Authors: Srilagna Sahoo, Adwaaiit Pande, Kartikey Thakar, Shubham Sahay, Saurabh Lodha
   - Tags: COD, boundary/frequency
   - Links: [paper](http://arxiv.org/abs/2606.00818v1) / [pdf](http://arxiv.org/pdf/2606.00818v1)
   - 简介：Advanced vision systems require retinomorphic, energy-efficient spike-based preprocessing of dynamic visual scenes. Here, we demonstrate multiple retinal preprocessing functionalities by leveraging a Hodgkin-Huxley-based optical spiking neuron (OSHN) that inc...
   - 为什么值得读：直接关联伪装目标检测/分割，优先看方法和消融。

3. **ARTEMIS: Agent-guided Reliability-aware Temporal Mask Evolution for Imperfectly Supervised Video Polyp Segmentation**
   - Source: arXiv, 2026-06-18
   - Authors: Tong Wang, Siwen Wang, Yaolei Qi, Jinxing Zhou, Yuting He et al.
   - Tags: SAM, VLM/MLLM, retrieval/prototype, boundary/frequency, depth/geometry, video
   - Links: [paper](http://arxiv.org/abs/2606.20161v1) / [pdf](http://arxiv.org/pdf/2606.20161v1)
   - 简介：Imperfectly supervised video polyp segmentation (VPS) aims to learn dense, temporally consistent masks from inexpensive supervision, including weak annotations (points, scribbles) and semi-supervision with few densely labeled frames. This setting is clinicall...
   - 为什么值得读：适合借鉴为 prompt 生成、mask 选择或视觉推理模块。

4. **Vision-Language Model Reasoning for Contextual Semantic Mapping in Intralogistics**
   - Source: arXiv, 2026-06-23
   - Authors: Marvin Rüdt, Hao Pang, Constantin Enke, Zäzilia Seibold, Kai Furmans
   - Tags: open-vocabulary, SAM, VLM/MLLM, reasoning, depth/geometry
   - Links: [paper](http://arxiv.org/abs/2606.24814v1) / [pdf](http://arxiv.org/pdf/2606.24814v1)
   - 简介：Autonomous mobile robots operating in intralogistics environments rely on geometric maps for localization and navigation, but lack semantic understanding of objects and their contextual properties. We present a contextual semantic mapping pipeline that combin...
   - 为什么值得读：适合迁移到开放词汇、零样本或无训练 COD。

5. **ActiveSAM: Image-Conditional Class Pruning for Fast and Accurate Open-Vocabulary Segmentation**
   - Source: arXiv, 2026-06-15
   - Authors: Tran Dinh Tien, Zhiqiang Shen
   - Tags: open-vocabulary, training-free, SAM, diffusion, remote sensing
   - Links: [paper](http://arxiv.org/abs/2606.16996v1) / [pdf](http://arxiv.org/pdf/2606.16996v1)
   - 简介：Segment Anything Model 3 (SAM 3) provides a strong frozen backbone for concept-prompted segmentation, but applying it directly to open-vocabulary semantic segmentation (OVSS) is inefficient: full-resolution decoding is typically run over the entire dataset vo...
   - 为什么值得读：适合迁移到开放词汇、零样本或无训练 COD。

6. **Jolia: Concept-Level Vision-Language Alignment for 3D CT Contrastive Learning**
   - Source: arXiv, 2026-06-23
   - Authors: Julien Khlaut, Charles Corbière, Baptiste Callard, Amaury Prat, Leo Butsanets et al.
   - Tags: VLM/MLLM, depth/geometry
   - Links: [paper](http://arxiv.org/abs/2606.24570v2) / [pdf](http://arxiv.org/pdf/2606.24570v2)
   - 简介：Vision-language contrastive pretraining has become the dominant recipe for 3D medical foundation models, leveraging the large volumes of paired scans and reports produced in clinical practice. However, medical images usually span dozens of organs, and radiolo...
   - 为什么值得读：适合借鉴为 prompt 生成、mask 选择或视觉推理模块。

7. **UniDrive: A Unified Vision-Language and Grounding Framework for Interpretable Risk Understanding in Autonomous Driving**
   - Source: arXiv, 2026-06-23
   - Authors: Xiaowei Gao, Pengxiang Li, Yitai Cheng, Ruihan Xu, James Haworth et al.
   - Tags: VLM/MLLM, reasoning, video
   - Links: [paper](http://arxiv.org/abs/2606.24759v1) / [pdf](http://arxiv.org/pdf/2606.24759v1)
   - 简介：Recent multimodal large language models (MLLMs) have shown strong potential for autonomous driving scene understanding, yet existing methods still face a fundamental trade-off between temporal reasoning and spatial precision. Models that rely on single-frame...
   - 为什么值得读：适合借鉴为 prompt 生成、mask 选择或视觉推理模块。

8. **HPP: Hierarchical Programmatic Probing for Long Video Understanding by Decoupling Perception and Reasoning**
   - Source: arXiv, 2026-06-19
   - Authors: Awais Rauf, Ahmed Hasssan, Greg Slabaugh
   - Tags: VLM/MLLM, reasoning, retrieval/prototype, video
   - Links: [paper](http://arxiv.org/abs/2606.21734v1) / [pdf](http://arxiv.org/pdf/2606.21734v1)
   - 简介：Understanding long videos requires fine-grained perception and multi-step, higher-order reasoning over complex, long-range spatio-temporal dynamics. Vision-language models (VLMs) encode video frames into visual tokens and attempt to perform both perception an...
   - 为什么值得读：适合借鉴为 prompt 生成、mask 选择或视觉推理模块。

9. **EnTrust: Modeling Inter-Modal Conflict for Trustworthy Multimodal Medical Image Analysis**
   - Source: arXiv, 2026-06-19
   - Authors: Dwarikanath Mahapatra, Abhijit Das, Behzad Bozorgtabar, Zongyuan Ge, Sudipta Roy et al.
   - Tags: SAM, diffusion
   - Links: [paper](http://arxiv.org/abs/2606.21384v1) / [pdf](http://arxiv.org/pdf/2606.21384v1)
   - 简介：Multimodal medical imaging fuses complementary anatomical and functional information, yet modalities frequently disagree in pathologically heterogeneous regions. Current segmentation models handle this in one of two inadequate ways: deterministic fusion that...
   - 为什么值得读：适合借鉴为 prompt 生成、mask 选择或视觉推理模块。

10. **Object Tokens as a Bridge Between Segmentation and Visual Question Answering in Robotic Surgery**
   - Source: arXiv, 2026-06-14
   - Authors: Yiping Li, Ronald de Jong, Romy van Jaarsveld, Franco Badaloni, Gino Kuiper et al.
   - Tags: SAM, VLM/MLLM, reasoning
   - Links: [paper](http://arxiv.org/abs/2606.15861v1) / [pdf](http://arxiv.org/pdf/2606.15861v1)
   - 简介：Visual Question Answering (VQA) in robotic surgery, referred to as surgical VQA, requires high-level understanding of complex surgical scenes and the integration of visual perception with language reasoning, with the potential to support surgical training and...
   - 为什么值得读：适合借鉴为 prompt 生成、mask 选择或视觉推理模块。

11. **High-Fidelity Synthetic Transmission Electron Microscopy Image Generation Using Diffusion Probabilistic Models for Data-Limited Semiconductor Metrology**
   - Source: arXiv, 2026-06-23
   - Authors: Johannes Boehm, Bappaditya Dey
   - Tags: SAM, diffusion, low-level
   - Links: [paper](http://arxiv.org/abs/2606.24817v1) / [pdf](http://arxiv.org/pdf/2606.24817v1)
   - 简介：Advanced semiconductor nodes drastically increased demand for Transmission Electron Microscopy (TEM), yet destructive sample preparation, slow imaging and high costs severely limit the availability of diverse datasets needed for downstream machine learning (M...
   - 为什么值得读：适合借鉴为 prompt 生成、mask 选择或视觉推理模块。

12. **Prob-BBDM: a Probabilistic Brownian Bridge Diffusion Model for MRI sequence image-to-image translation**
   - Source: arXiv, 2026-06-23
   - Authors: Martin Valls, Pascal Bourdon, Christine Fernandez-Maloigne, Guillaume Herpe, David Helbert
   - Tags: diffusion, depth/geometry
   - Links: [paper](http://arxiv.org/abs/2606.24313v1) / [pdf](http://arxiv.org/pdf/2606.24313v1)
   - 简介：AI-driven image-to-image synthesis is rapidly advancing, with growing applications in medical imaging. Multi-modal image analysis plays a crucial role in optimizing examination quality, yet acquiring multiple imaging modalities in clinical settings remains re...
   - 为什么值得读：适合补充伪装场景中的边界、纹理、几何先验。

## COD / 伪装目标检测相关

1. **Open-Vocabulary Camouflaged Object Segmentation**
   - Source: arXiv, 2023-11-19
   - Authors: Youwei Pang, Xiaoqi Zhao, Jiaming Zuo, Lihe Zhang, Huchuan Lu
   - Tags: COD, open-vocabulary, VLM/MLLM, boundary/frequency, depth/geometry, low-level
   - Links: [paper](http://arxiv.org/abs/2311.11241v3) / [pdf](http://arxiv.org/pdf/2311.11241v3)
   - 简介：Recently, the emergence of the large-scale vision-language model (VLM), such as CLIP, has opened the way towards open-world object perception. Many works have explored the utilization of pre-trained VLM for the challenging open-vocabulary dense prediction tas...
   - 为什么值得读：直接关联伪装目标检测/分割，优先看方法和消融。

2. **Debate-Enhanced Pseudo Labeling and Frequency-Aware Progressive Debiasing for Weakly-Supervised Camouflaged Object Detection with Scribble Annotations**
   - Source: arXiv, 2025-12-23
   - Authors: Jiawei Ge, Jiuxin Cao, Xinyi Li, Xuelin Zhu, Chang Liu et al.
   - Tags: COD, unsupervised, SAM, boundary/frequency
   - Links: [paper](http://arxiv.org/abs/2512.20260v5) / [pdf](http://arxiv.org/pdf/2512.20260v5)
   - 简介：Weakly-Supervised Camouflaged Object Detection (WSCOD) aims to locate and segment objects that are visually concealed within their surrounding scenes, relying solely on sparse supervision such as scribble annotations. Despite recent progress, existing WSCOD m...
   - 为什么值得读：直接关联伪装目标检测/分割，优先看方法和消融。

3. **UCOD-DPL: Unsupervised Camouflaged Object Detection via Dynamic Pseudo-label Learning**
   - Source: arXiv, 2025-06-08
   - Authors: Weiqi Yan, Lvhai Chen, Huaijia Kou, Shengchuan Zhang, Yan Zhang et al.
   - Tags: COD, unsupervised, boundary/frequency, remote sensing
   - Links: [paper](http://arxiv.org/abs/2506.07087v1) / [pdf](http://arxiv.org/pdf/2506.07087v1)
   - 简介：Unsupervised Camoflaged Object Detection (UCOD) has gained attention since it doesn't need to rely on extensive pixel-level labels. Existing UCOD methods typically generate pseudo-labels using fixed strategies and train 1 x1 convolutional layers as a simple d...
   - 为什么值得读：直接关联伪装目标检测/分割，优先看方法和消融。

4. **EReCu: Pseudo-label Evolution Fusion and Refinement with Multi-Cue Learning for Unsupervised Camouflage Detection**
   - Source: arXiv, 2026-03-12
   - Authors: Shuo Jiang, Gaojia Zhang, Min Tan, Yufei Yin, Gang Pan
   - Tags: COD, unsupervised, diffusion, boundary/frequency, depth/geometry, low-level
   - Links: [paper](http://arxiv.org/abs/2603.11521v1) / [pdf](http://arxiv.org/pdf/2603.11521v1)
   - 简介：Unsupervised Camouflaged Object Detection (UCOD) remains a challenging task due to the high intrinsic similarity between target objects and their surroundings, as well as the reliance on noisy pseudo-labels that hinder fine-grained texture learning. While exi...
   - 为什么值得读：直接关联伪装目标检测/分割，优先看方法和消融。

5. **SAM3-Adapter: Efficient Adaptation of Segment Anything 3 for Camouflage Object Segmentation, Shadow Detection, and Medical Image Segmentation**
   - Source: arXiv, 2025-11-24
   - Authors: Tianrun Chen, Runlong Cao, Xinda Yu, Lanyun Zhu, Chaotao Ding et al.
   - Tags: COD, SAM
   - Links: [paper](http://arxiv.org/abs/2511.19425v1) / [pdf](http://arxiv.org/pdf/2511.19425v1)
   - 简介：The rapid rise of large-scale foundation models has reshaped the landscape of image segmentation, with models such as Segment Anything achieving unprecedented versatility across diverse vision tasks. However, previous generations-including SAM and its success...
   - 为什么值得读：直接关联伪装目标检测/分割，优先看方法和消融。

6. **High-Resolution Underwater Camouflaged Object Detection: GBU-UCOD Dataset and Topology-Aware and Frequency-Decoupled Networks**
   - Source: arXiv, 2026-02-03
   - Authors: Wenji Wu, Shuo Ye, Yiyu Liu, Jiguang He, Zhuo Wang et al.
   - Tags: COD, SAM, diffusion, boundary/frequency, depth/geometry
   - Links: [paper](http://arxiv.org/abs/2602.03591v1) / [pdf](http://arxiv.org/pdf/2602.03591v1)
   - 简介：Underwater Camouflaged Object Detection (UCOD) is a challenging task due to the extreme visual similarity between targets and backgrounds across varying marine depths. Existing methods often struggle with topological fragmentation of slender creatures in the...
   - 为什么值得读：直接关联伪装目标检测/分割，优先看方法和消融。

7. **ZS-VCOS: Zero-Shot Video Camouflaged Object Segmentation By Optical Flow and Open Vocabulary Object Detection**
   - Source: arXiv, 2025-04-10
   - Authors: Wenqi Guo, Mohamed Shehata, Shan Du
   - Tags: COD, open-vocabulary, unsupervised, SAM, VLM/MLLM, diffusion, video
   - Links: [paper](http://arxiv.org/abs/2505.01431v2) / [pdf](http://arxiv.org/pdf/2505.01431v2)
   - 简介：Camouflaged object segmentation presents unique challenges compared to traditional segmentation tasks, primarily due to the high similarity in patterns and colors between camouflaged objects and their backgrounds. Effective solutions to this problem have sign...
   - 为什么值得读：直接关联伪装目标检测/分割，优先看方法和消融。

8. **First RAG, Second SEG: A Training-Free Paradigm for Camouflaged Object Detection**
   - Source: arXiv, 2025-08-21
   - Authors: Wutao Liu, YiDan Wang, Pan Gao
   - Tags: COD, training-free, unsupervised, SAM, retrieval/prototype, anomaly/OOD
   - Links: [paper](http://arxiv.org/abs/2508.15313v2) / [pdf](http://arxiv.org/pdf/2508.15313v2)
   - 简介：Camouflaged object detection (COD) poses a significant challenge in computer vision due to the high similarity between objects and their backgrounds. Existing approaches often rely on heavy training and large computational resources.
   - 为什么值得读：直接关联伪装目标检测/分割，优先看方法和消融。

9. **When SAM2 Meets Video Camouflaged Object Segmentation: A Comprehensive Evaluation and Adaptation**
   - Source: arXiv, 2024-09-27
   - Authors: Yuli Zhou, Guolei Sun, Yawei Li, Guo-Sen Xie, Luca Benini et al.
   - Tags: COD, SAM, VLM/MLLM, diffusion, video
   - Links: [paper](http://arxiv.org/abs/2409.18653v2) / [pdf](http://arxiv.org/pdf/2409.18653v2)
   - 简介：This study investigates the application and performance of the Segment Anything Model 2 (SAM2) in the challenging task of video camouflaged object segmentation (VCOS). VCOS involves detecting objects that blend seamlessly in the surroundings for videos, due t...
   - 为什么值得读：直接关联伪装目标检测/分割，优先看方法和消融。

10. **COMPrompter: reconceptualized segment anything model with multiprompt network for camouflaged object detection**
   - Source: arXiv, 2024-11-28
   - Authors: Xiaoqin Zhang, Zhenni Yu, Li Zhao, Deng-Ping Fan, Guobao Xiao
   - Tags: COD, SAM, boundary/frequency
   - Links: [paper](http://arxiv.org/abs/2411.18858v1) / [pdf](http://arxiv.org/pdf/2411.18858v1)
   - 简介：We rethink the segment anything model (SAM) and propose a novel multiprompt network called COMPrompter for camouflaged object detection (COD). SAM has zero-shot generalization ability beyond other models and can provide an ideal framework for COD.
   - 为什么值得读：直接关联伪装目标检测/分割，优先看方法和消融。

11. **Exploring Deeper! Segment Anything Model with Depth Perception for Camouflaged Object Detection**
   - Source: arXiv, 2024-07-17
   - Authors: Zhenni Yu, Xiaoqin Zhang, Li Zhao, Yi Bin, Guobao Xiao
   - Tags: COD, SAM, boundary/frequency, depth/geometry
   - Links: [paper](http://arxiv.org/abs/2407.12339v1) / [pdf](http://arxiv.org/pdf/2407.12339v1)
   - 简介：This paper introduces a new Segment Anything Model with Depth Perception (DSAM) for Camouflaged Object Detection (COD). DSAM exploits the zero-shot capability of SAM to realize precise segmentation in the RGB-D domain.
   - 为什么值得读：直接关联伪装目标检测/分割，优先看方法和消融。

12. **BED-SAM2: Boundary-Enhanced-Depth SAM2 via Monocular Geometric Priors**
   - Source: arXiv, 2026-05-24
   - Authors: Tyler Rust, Dara McNally, Kyle O'Donnell, Colin Kelly, Chandra Kambhamettu
   - Tags: COD, SAM, boundary/frequency, depth/geometry
   - Links: [paper](http://arxiv.org/abs/2605.24893v1) / [pdf](http://arxiv.org/pdf/2605.24893v1)
   - 简介：Building upon the SAM2 vision foundation model for downstream segmentation, this study introduces Boundary Enhanced Depth (BED)-SAM2. The SAM2 Hiera encoder architecture is modified to directly encode monocular depth information from RGB images, thereby provi...
   - 为什么值得读：直接关联伪装目标检测/分割，优先看方法和消融。

13. **FCL-COD: Weakly Supervised Camouflaged Object Detection with Frequency-aware and Contrastive Learning**
   - Source: arXiv, 2026-03-24
   - Authors: Jingchen Ni, Quan Zhang, Dan Jiang, Keyu Lv, Ke Zhang et al.
   - Tags: COD, unsupervised, SAM, diffusion, boundary/frequency
   - Links: [paper](http://arxiv.org/abs/2603.22969v1) / [pdf](http://arxiv.org/pdf/2603.22969v1)
   - 简介：Existing camouflage object detection (COD) methods typically rely on fully-supervised learning guided by mask annotations. However, obtaining mask annotations is time-consuming and labor-intensive.
   - 为什么值得读：直接关联伪装目标检测/分割，优先看方法和消融。

14. **Stepwise Decomposition and Dual-stream Focus: A Novel Approach for Training-free Camouflaged Object Segmentation**
   - Source: arXiv, 2025-06-07
   - Authors: Chao Yin, Hao Li, Kequan Yang, Jide Li, Pinpin Zhu et al.
   - Tags: COD, training-free, SAM, reasoning
   - Links: [paper](http://arxiv.org/abs/2506.06818v3) / [pdf](http://arxiv.org/pdf/2506.06818v3)
   - 简介：While promptable segmentation (\textit{e.g.}, SAM) has shown promise for various segmentation tasks, it still requires manual visual prompts for each object to be segmented. In contrast, task-generic promptable segmentation aims to reduce the need for such de...
   - 为什么值得读：直接关联伪装目标检测/分割，优先看方法和消融。

15. **CamSAM2: Segment Anything Accurately in Camouflaged Videos**
   - Source: arXiv, 2025-03-25
   - Authors: Yuli Zhou, Yawei Li, Yuqian Fu, Luca Benini, Ender Konukoglu et al.
   - Tags: COD, SAM, retrieval/prototype, video
   - Links: [paper](http://arxiv.org/abs/2503.19730v3) / [pdf](http://arxiv.org/pdf/2503.19730v3)
   - 简介：Video camouflaged object segmentation (VCOS), aiming at segmenting camouflaged objects that seamlessly blend into their environment, is a fundamental vision task with various real-world applications. With the release of SAM2, video segmentation has witnessed...
   - 为什么值得读：直接关联伪装目标检测/分割，优先看方法和消融。

16. **SAM2-UNeXT: An Improved High-Resolution Baseline for Adapting Foundation Models to Downstream Segmentation Tasks**
   - Source: arXiv, 2025-08-05
   - Authors: Xinyu Xiong, Zihuang Wu, Lei Zhang, Lei Lu, Ming Li et al.
   - Tags: COD, SAM, remote sensing
   - Links: [paper](http://arxiv.org/abs/2508.03566v1) / [pdf](http://arxiv.org/pdf/2508.03566v1)
   - 简介：Recent studies have highlighted the potential of adapting the Segment Anything Model (SAM) for various downstream tasks. However, constructing a more powerful and generalizable encoder to further enhance performance remains an open challenge.
   - 为什么值得读：直接关联伪装目标检测/分割，优先看方法和消融。

17. **Depth-guided Texture Diffusion for Image Semantic Segmentation**
   - Source: arXiv, 2024-08-17
   - Authors: Wei Sun, Yuan Li, Qixiang Ye, Jianbin Jiao, Yanzhao Zhou
   - Tags: COD, diffusion, boundary/frequency, depth/geometry
   - Links: [paper](http://arxiv.org/abs/2408.09097v1) / [pdf](http://arxiv.org/pdf/2408.09097v1)
   - 简介：Depth information provides valuable insights into the 3D structure especially the outline of objects, which can be utilized to improve the semantic segmentation tasks. However, a naive fusion of depth information can disrupt feature and compromise accuracy du...
   - 为什么值得读：直接关联伪装目标检测/分割，优先看方法和消融。

18. **Weakly Supervised Camouflaged Object Detection Based on the SAM Model and Mask Guidance**
   - Source: arXiv, 2026-05-25
   - Authors: Xia Li, Xinran Liu, Lin Qi, Junyu Dong
   - Tags: COD, unsupervised, SAM, boundary/frequency, low-level
   - Links: [paper](http://arxiv.org/abs/2605.25385v1) / [pdf](http://arxiv.org/pdf/2605.25385v1)
   - 简介：Camouflaged object detection (COD) from a single image is a challenging task due to the high similarity between objects and their surroundings. Existing fully supervised methods require labor-intensive pixel-level annotations, making weakly supervised methods...
   - 为什么值得读：直接关联伪装目标检测/分割，优先看方法和消融。

19. **RIDE: Retinex-Informed Decoupling for Exposing Concealed Objects**
   - Source: arXiv, 2026-05-14
   - Authors: Chunming He, Rihan Zhang, Dingming Zhang, Chengyu Fang, Longxiang Tang et al.
   - Tags: COD, SAM, boundary/frequency
   - Links: [paper](http://arxiv.org/abs/2605.15450v1) / [pdf](http://arxiv.org/pdf/2605.15450v1)
   - 简介：Concealed Object Segmentation (COS) encompasses a family of dense-prediction tasks, including camouflaged object detection, polyp segmentation, transparent object detection, and industrial defect inspection, where targets are visually entangled with their sur...
   - 为什么值得读：直接关联伪装目标检测/分割，优先看方法和消融。

20. **Exploring Boundary-Aware Spatial-Frequency Fusion for Camouflaged Object Detection**
   - Source: arXiv, 2026-04-20
   - Authors: Song Yu, Yang Hu, Haokang Ding, Zhifang Liao, Yucheng Song
   - Tags: COD, diffusion, boundary/frequency
   - Links: [paper](http://arxiv.org/abs/2604.17879v1) / [pdf](http://arxiv.org/pdf/2604.17879v1)
   - 简介：Camouflaged Object Detection is challenging due to the high degree of similarity between camouflaged objects and their surrounding backgrounds. Current COD methods mainly rely on edge extraction in the spatial domain and local pixel-level information, neglect...
   - 为什么值得读：直接关联伪装目标检测/分割，优先看方法和消融。

21. **IP-SAM: Prompt-Space Conditioning for Prompt-Absent Camouflaged Object Detection**
   - Source: arXiv, 2026-03-28
   - Authors: Huiyao Zhang, Jin Bai, Rui Guo, JianWen Tan, HongFei Wang et al.
   - Tags: COD, SAM, diffusion
   - Links: [paper](http://arxiv.org/abs/2603.27250v1) / [pdf](http://arxiv.org/pdf/2603.27250v1)
   - 简介：Prompt-conditioned foundation segmenters have emerged as a dominant paradigm for image segmentation, where explicit spatial prompts (e.g., points, boxes, masks) guide mask decoding. However, many real-world deployments require fully automatic segmentation, cr...
   - 为什么值得读：直接关联伪装目标检测/分割，优先看方法和消融。

22. **Language-Guided Structure-Aware Network for Camouflaged Object Detection**
   - Source: arXiv, 2026-03-25
   - Authors: Min Zhang
   - Tags: COD, boundary/frequency, low-level
   - Links: [paper](http://arxiv.org/abs/2603.24355v1) / [pdf](http://arxiv.org/pdf/2603.24355v1)
   - 简介：Camouflaged Object Detection (COD) aims to segment objects that are highly integrated with the background in terms of color, texture, and structure, making it a highly challenging task in computer vision. Although existing methods introduce multi-scale fusion...
   - 为什么值得读：直接关联伪装目标检测/分割，优先看方法和消融。

23. **An Instance-Aware Prompting Framework for Training-free Camouflaged Object Segmentation**
   - Source: arXiv, 2025-08-09
   - Authors: Chao Yin, Jide Li, Hang Yao, Xiaoqiang Li
   - Tags: COD, training-free, SAM
   - Links: [paper](http://arxiv.org/abs/2508.06904v3) / [pdf](http://arxiv.org/pdf/2508.06904v3)
   - 简介：Training-free Camouflaged Object Segmentation (COS) seeks to segment camouflaged objects without task-specific training, by automatically generating visual prompts to guide the Segment Anything Model (SAM). However, existing pipelines mostly yield semantic-le...
   - 为什么值得读：直接关联伪装目标检测/分割，优先看方法和消融。

24. **Open-Vocabulary Camouflaged Object Segmentation with Cascaded Vision Language Models**
   - Source: arXiv, 2025-06-24
   - Authors: Kai Zhao, Wubang Yuan, Zheng Wang, Guanyi Li, Xiaoqiang Zhu et al.
   - Tags: COD, open-vocabulary, SAM
   - Links: [paper](http://arxiv.org/abs/2506.19300v2) / [pdf](http://arxiv.org/pdf/2506.19300v2)
   - 简介：Open-Vocabulary Camouflaged Object Segmentation (OVCOS) seeks to segment and classify camouflaged objects from arbitrary categories, presenting unique challenges due to visual ambiguity and unseen categories.Recent approaches typically adopt a two-stage parad...
   - 为什么值得读：直接关联伪装目标检测/分割，优先看方法和消融。

25. **Towards Real Zero-Shot Camouflaged Object Segmentation without Camouflaged Annotations**
   - Source: arXiv, 2024-10-22
   - Authors: Cheng Lei, Jie Fan, Xinran Li, Tianzhu Xiang, Ao Li et al.
   - Tags: COD, VLM/MLLM, diffusion
   - Links: [paper](http://arxiv.org/abs/2410.16953v2) / [pdf](http://arxiv.org/pdf/2410.16953v2)
   - 简介：Camouflaged Object Segmentation (COS) faces significant challenges due to the scarcity of annotated data, where meticulous pixel-level annotation is both labor-intensive and costly, primarily due to the intricate object-background boundaries. Addressing the c...
   - 为什么值得读：直接关联伪装目标检测/分割，优先看方法和消融。

26. **Beyond Single Images: Retrieval Self-Augmented Unsupervised Camouflaged Object Detection**
   - Source: arXiv, 2025-10-21
   - Authors: Ji Du, Xin Wang, Fangwei Hao, Mingyang Yu, Chunyuan Chen et al.
   - Tags: COD, unsupervised, retrieval/prototype
   - Links: [paper](http://arxiv.org/abs/2510.18437v1) / [pdf](http://arxiv.org/pdf/2510.18437v1)
   - 简介：At the core of Camouflaged Object Detection (COD) lies segmenting objects from their highly similar surroundings. Previous efforts navigate this challenge primarily through image-level modeling or annotation-based optimization.
   - 为什么值得读：直接关联伪装目标检测/分割，优先看方法和消融。

27. **DGA-Net: Enhancing SAM with Depth Prompting and Graph-Anchor Guidance for Camouflaged Object Detection**
   - Source: arXiv, 2026-01-06
   - Authors: Yuetong Li, Qing Zhang, Yilin Zhao, Gongyang Li, Zeming Liu
   - Tags: COD, SAM, depth/geometry, low-level
   - Links: [paper](http://arxiv.org/abs/2601.02831v1) / [pdf](http://arxiv.org/pdf/2601.02831v1)
   - 简介：To fully exploit depth cues in Camouflaged Object Detection (COD), we present DGA-Net, a specialized framework that adapts the Segment Anything Model (SAM) via a novel ``depth prompting" paradigm. Distinguished from existing approaches that primarily rely on...
   - 为什么值得读：直接关联伪装目标检测/分割，优先看方法和消融。

28. **Phantom-Insight: Adaptive Multi-cue Fusion for Video Camouflaged Object Detection with Multimodal LLM**
   - Source: arXiv, 2025-09-08
   - Authors: Hua Zhang, Changjiang Luo, Ruoyu Chen
   - Tags: COD, SAM, VLM/MLLM, diffusion, boundary/frequency, video
   - Links: [paper](http://arxiv.org/abs/2509.06422v1) / [pdf](http://arxiv.org/pdf/2509.06422v1)
   - 简介：Video camouflaged object detection (VCOD) is challenging due to dynamic environments. Existing methods face two main issues: (1) SAM-based methods struggle to separate camouflaged object edges due to model freezing, and (2) MLLM-based methods suffer from poor...
   - 为什么值得读：直接关联伪装目标检测/分割，优先看方法和消融。

29. **Improving SAM for Camouflaged Object Detection via Dual Stream Adapters**
   - Source: arXiv, 2025-03-08
   - Authors: Jiaming Liu, Linghe Kong, Guihai Chen
   - Tags: COD, SAM, diffusion, boundary/frequency, depth/geometry
   - Links: [paper](http://arxiv.org/abs/2503.06042v2) / [pdf](http://arxiv.org/pdf/2503.06042v2)
   - 简介：Segment anything model (SAM) has shown impressive general-purpose segmentation performance on natural images, but its performance on camouflaged object detection (COD) is unsatisfactory. In this paper, we propose SAM-COD that performs camouflaged object detec...
   - 为什么值得读：直接关联伪装目标检测/分割，优先看方法和消融。

30. **Refining Context-Entangled Content Segmentation via Curriculum Selection and Anti-Curriculum Promotion**
   - Source: arXiv, 2026-02-01
   - Authors: Chunming He, Rihan Zhang, Fengyang Xiao, Dingming Zhang, Zhiwen Cao et al.
   - Tags: COD, SAM, boundary/frequency, video, low-level
   - Links: [paper](http://arxiv.org/abs/2602.01183v2) / [pdf](http://arxiv.org/pdf/2602.01183v2)
   - 简介：Biological learning proceeds from easy to difficult tasks, gradually reinforcing perception and robustness. Inspired by this principle, we address Context-Entangled Content Segmentation (CECS), a challenging setting where objects share intrinsic visual patter...
   - 为什么值得读：直接关联伪装目标检测/分割，优先看方法和消融。

31. **Assisted Refinement Network Based on Channel Information Interaction for Camouflaged and Salient Object Detection**
   - Source: arXiv, 2025-12-12
   - Authors: Kuan Wang, Yanjun Qin, Mengge Lu, Liejun Wang, Xiaoming Tao
   - Tags: COD, SAM, diffusion, boundary/frequency, low-level
   - Links: [paper](http://arxiv.org/abs/2512.11369v1) / [pdf](http://arxiv.org/pdf/2512.11369v1)
   - 简介：Camouflaged Object Detection (COD) stands as a significant challenge in computer vision, dedicated to identifying and segmenting objects visually highly integrated with their backgrounds. Current mainstream methods have made progress in cross-layer feature fu...
   - 为什么值得读：直接关联伪装目标检测/分割，优先看方法和消融。

32. **Exploring Depth Contribution for Camouflaged Object Detection**
   - Source: arXiv, 2021-06-24
   - Authors: Mochu Xiang, Jing Zhang, Yunqiu Lv, Aixuan Li, Yiran Zhong et al.
   - Tags: COD, diffusion, depth/geometry, remote sensing
   - Links: [paper](http://arxiv.org/abs/2106.13217v3) / [pdf](http://arxiv.org/pdf/2106.13217v3)
   - 简介：Camouflaged object detection (COD) aims to segment camouflaged objects hiding in the environment, which is challenging due to the similar appearance of camouflaged objects and their surroundings. Research in biology suggests depth can provide useful object lo...
   - 为什么值得读：直接关联伪装目标检测/分割，优先看方法和消融。

33. **Hierarchical Consistency Learning for Test-time Adaptation in Camouflage Perception**
   - Source: arXiv, 2026-05-25
   - Authors: Mingfeng Zha, Tianyu Li, Guoqing Wang, Yunqiang Pei, Chaofan Qiao et al.
   - Tags: COD, diffusion, retrieval/prototype, boundary/frequency
   - Links: [paper](http://arxiv.org/abs/2605.25651v2) / [pdf](http://arxiv.org/pdf/2605.25651v2)
   - 简介：Camouflaged object detection (COD) aims to localize targets that exhibit minimal perceptual differences from backgrounds through physical attributes. Existing methods, constrained by the static train-then-freeze paradigm, suffer from domain rigidity and annot...
   - 为什么值得读：直接关联伪装目标检测/分割，优先看方法和消融。

34. **When W4A4 Breaks Camouflaged Object Detection: Token-Group Dual-Constraint Activation Quantization**
   - Source: arXiv, 2026-04-18
   - Authors: Tianqi Li, Wenyu Fang, Xin He, Xue Geng, Xu Cheng et al.
   - Tags: COD, boundary/frequency
   - Links: [paper](http://arxiv.org/abs/2604.16855v1) / [pdf](http://arxiv.org/pdf/2604.16855v1)
   - 简介：Camouflaged object detection (COD) segments objects that intentionally blend with the background, so predictions depend on subtle texture and boundary cues. COD is often needed under tight on-device memory and latency budgets, making low-bit inference highly...
   - 为什么值得读：直接关联伪装目标检测/分割，优先看方法和消融。

35. **Modality-Agnostic Prompt Learning for Multi-Modal Camouflaged Object Detection**
   - Source: arXiv, 2026-04-14
   - Authors: Hao Wang, Jiqing Zhang, Xin Yang, Baocai Yin, Lu Jiang et al.
   - Tags: COD, SAM, diffusion, boundary/frequency, depth/geometry
   - Links: [paper](http://arxiv.org/abs/2604.12380v1) / [pdf](http://arxiv.org/pdf/2604.12380v1)
   - 简介：Camouflaged Object Detection (COD) aims to segment objects that blend seamlessly into complex backgrounds, with growing interest in exploiting additional visual modalities to enhance robustness through complementary information. However, most existing approac...
   - 为什么值得读：直接关联伪装目标检测/分割，优先看方法和消融。

## 泛计算机视觉方法池

1. **SegRAG: Training-Free Retrieval-Augmented Semantic Segmentation**
   - Source: arXiv, 2026-05-17
   - Authors: Abderrahmene Boudiaf, Irfan Hussain, Sajid Javed
   - Tags: open-vocabulary, training-free, SAM, reasoning, retrieval/prototype
   - Links: [paper](http://arxiv.org/abs/2605.17630v2) / [pdf](http://arxiv.org/pdf/2605.17630v2)
   - 简介：Open-vocabulary segmentation models such as SAM3 perform well across broad categories via text prompting, yet degrade when target classes are visually underrepresented in pretraining or depart from canonical depictions-limitations text prompts cannot resolve...
   - 为什么值得读：适合迁移到开放词汇、零样本或无训练 COD。

2. **OVS-DINO: Open-Vocabulary Segmentation via Structure-Aligned SAM-DINO with Language Guidance**
   - Source: arXiv, 2026-04-09
   - Authors: Haoxi Zeng, Qiankun Liu, Yi Bin, Haiyue Zhang, Yujuan Ding et al.
   - Tags: open-vocabulary, unsupervised, SAM, boundary/frequency, remote sensing
   - Links: [paper](http://arxiv.org/abs/2604.08461v1) / [pdf](http://arxiv.org/pdf/2604.08461v1)
   - 简介：Open-Vocabulary Segmentation (OVS) aims to segment image regions beyond predefined category sets by leveraging semantic descriptions. While CLIP based approaches excel in semantic generalization, they frequently lack the fine-grained spatial awareness require...
   - 为什么值得读：适合迁移到开放词汇、零样本或无训练 COD。

3. **ARTEMIS: Agent-guided Reliability-aware Temporal Mask Evolution for Imperfectly Supervised Video Polyp Segmentation**
   - Source: arXiv, 2026-06-18
   - Authors: Tong Wang, Siwen Wang, Yaolei Qi, Jinxing Zhou, Yuting He et al.
   - Tags: SAM, VLM/MLLM, retrieval/prototype, boundary/frequency, depth/geometry, video
   - Links: [paper](http://arxiv.org/abs/2606.20161v1) / [pdf](http://arxiv.org/pdf/2606.20161v1)
   - 简介：Imperfectly supervised video polyp segmentation (VPS) aims to learn dense, temporally consistent masks from inexpensive supervision, including weak annotations (points, scribbles) and semi-supervision with few densely labeled frames. This setting is clinicall...
   - 为什么值得读：适合借鉴为 prompt 生成、mask 选择或视觉推理模块。

4. **ActiveSAM: Image-Conditional Class Pruning for Fast and Accurate Open-Vocabulary Segmentation**
   - Source: arXiv, 2026-06-15
   - Authors: Tran Dinh Tien, Zhiqiang Shen
   - Tags: open-vocabulary, training-free, SAM, diffusion, remote sensing
   - Links: [paper](http://arxiv.org/abs/2606.16996v1) / [pdf](http://arxiv.org/pdf/2606.16996v1)
   - 简介：Segment Anything Model 3 (SAM 3) provides a strong frozen backbone for concept-prompted segmentation, but applying it directly to open-vocabulary semantic segmentation (OVSS) is inefficient: full-resolution decoding is typically run over the entire dataset vo...
   - 为什么值得读：适合迁移到开放词汇、零样本或无训练 COD。

5. **Vision-Language Model Reasoning for Contextual Semantic Mapping in Intralogistics**
   - Source: arXiv, 2026-06-23
   - Authors: Marvin Rüdt, Hao Pang, Constantin Enke, Zäzilia Seibold, Kai Furmans
   - Tags: open-vocabulary, SAM, VLM/MLLM, reasoning, depth/geometry
   - Links: [paper](http://arxiv.org/abs/2606.24814v1) / [pdf](http://arxiv.org/pdf/2606.24814v1)
   - 简介：Autonomous mobile robots operating in intralogistics environments rely on geometric maps for localization and navigation, but lack semantic understanding of objects and their contextual properties. We present a contextual semantic mapping pipeline that combin...
   - 为什么值得读：适合迁移到开放词汇、零样本或无训练 COD。

6. **SegEarth-OV: Towards Training-Free Open-Vocabulary Segmentation for Remote Sensing Images**
   - Source: arXiv, 2024-10-02
   - Authors: Kaiyu Li, Ruixun Liu, Xiangyong Cao, Xueru Bai, Feng Zhou et al.
   - Tags: open-vocabulary, training-free, SAM, remote sensing, anomaly/OOD
   - Links: [paper](http://arxiv.org/abs/2410.01768v2) / [pdf](http://arxiv.org/pdf/2410.01768v2)
   - 简介：Remote sensing image plays an irreplaceable role in fields such as agriculture, water resources, military, and disaster relief. Pixel-level interpretation is a critical aspect of remote sensing image applications; however, a prevalent limitation remains the n...
   - 为什么值得读：适合迁移到开放词汇、零样本或无训练 COD。

7. **T-REN: Learning Text-Aligned Region Tokens Improves Dense Vision-Language Alignment and Scalability**
   - Source: arXiv, 2026-04-20
   - Authors: Savya Khosla, Sethuraman T, Aryan Chadha, Alex Schwing, Derek Hoiem
   - Tags: open-vocabulary, VLM/MLLM, diffusion, retrieval/prototype, depth/geometry, video
   - Links: [paper](http://arxiv.org/abs/2604.18573v1) / [pdf](http://arxiv.org/pdf/2604.18573v1)
   - 简介：Despite recent progress, vision-language encoders struggle with two core limitations: (1) weak alignment between language and dense vision features, which hurts tasks like open-vocabulary semantic segmentation; and (2) high token counts for fine-grained visua...
   - 为什么值得读：适合迁移到开放词汇、零样本或无训练 COD。

8. **MM-OVSeg:Multimodal Optical-SAR Fusion for Open-Vocabulary Segmentation in Remote Sensing**
   - Source: arXiv, 2026-03-18
   - Authors: Yimin Wei, Aoran Xiao, Hongruixuan Chen, Junshi Xia, Naoto Yokoya
   - Tags: open-vocabulary, VLM/MLLM, diffusion, remote sensing
   - Links: [paper](http://arxiv.org/abs/2603.17528v2) / [pdf](http://arxiv.org/pdf/2603.17528v2)
   - 简介：Open-vocabulary segmentation enables pixel-level recognition from an open set of textual categories, allowing generalization beyond fixed classes. Despite great potential in remote sensing, progress in this area remains largely limited to clear-sky optical da...
   - 为什么值得读：适合迁移到开放词汇、零样本或无训练 COD。

9. **Jolia: Concept-Level Vision-Language Alignment for 3D CT Contrastive Learning**
   - Source: arXiv, 2026-06-23
   - Authors: Julien Khlaut, Charles Corbière, Baptiste Callard, Amaury Prat, Leo Butsanets et al.
   - Tags: VLM/MLLM, depth/geometry
   - Links: [paper](http://arxiv.org/abs/2606.24570v2) / [pdf](http://arxiv.org/pdf/2606.24570v2)
   - 简介：Vision-language contrastive pretraining has become the dominant recipe for 3D medical foundation models, leveraging the large volumes of paired scans and reports produced in clinical practice. However, medical images usually span dozens of organs, and radiolo...
   - 为什么值得读：适合借鉴为 prompt 生成、mask 选择或视觉推理模块。

10. **HPP: Hierarchical Programmatic Probing for Long Video Understanding by Decoupling Perception and Reasoning**
   - Source: arXiv, 2026-06-19
   - Authors: Awais Rauf, Ahmed Hasssan, Greg Slabaugh
   - Tags: VLM/MLLM, reasoning, retrieval/prototype, video
   - Links: [paper](http://arxiv.org/abs/2606.21734v1) / [pdf](http://arxiv.org/pdf/2606.21734v1)
   - 简介：Understanding long videos requires fine-grained perception and multi-step, higher-order reasoning over complex, long-range spatio-temporal dynamics. Vision-language models (VLMs) encode video frames into visual tokens and attempt to perform both perception an...
   - 为什么值得读：适合借鉴为 prompt 生成、mask 选择或视觉推理模块。

11. **Object Tokens as a Bridge Between Segmentation and Visual Question Answering in Robotic Surgery**
   - Source: arXiv, 2026-06-14
   - Authors: Yiping Li, Ronald de Jong, Romy van Jaarsveld, Franco Badaloni, Gino Kuiper et al.
   - Tags: SAM, VLM/MLLM, reasoning
   - Links: [paper](http://arxiv.org/abs/2606.15861v1) / [pdf](http://arxiv.org/pdf/2606.15861v1)
   - 简介：Visual Question Answering (VQA) in robotic surgery, referred to as surgical VQA, requires high-level understanding of complex surgical scenes and the integration of visual perception with language reasoning, with the potential to support surgical training and...
   - 为什么值得读：适合借鉴为 prompt 生成、mask 选择或视觉推理模块。

12. **UniDrive: A Unified Vision-Language and Grounding Framework for Interpretable Risk Understanding in Autonomous Driving**
   - Source: arXiv, 2026-06-23
   - Authors: Xiaowei Gao, Pengxiang Li, Yitai Cheng, Ruihan Xu, James Haworth et al.
   - Tags: VLM/MLLM, reasoning, video
   - Links: [paper](http://arxiv.org/abs/2606.24759v1) / [pdf](http://arxiv.org/pdf/2606.24759v1)
   - 简介：Recent multimodal large language models (MLLMs) have shown strong potential for autonomous driving scene understanding, yet existing methods still face a fundamental trade-off between temporal reasoning and spatial precision. Models that rely on single-frame...
   - 为什么值得读：适合借鉴为 prompt 生成、mask 选择或视觉推理模块。

13. **EnTrust: Modeling Inter-Modal Conflict for Trustworthy Multimodal Medical Image Analysis**
   - Source: arXiv, 2026-06-19
   - Authors: Dwarikanath Mahapatra, Abhijit Das, Behzad Bozorgtabar, Zongyuan Ge, Sudipta Roy et al.
   - Tags: SAM, diffusion
   - Links: [paper](http://arxiv.org/abs/2606.21384v1) / [pdf](http://arxiv.org/pdf/2606.21384v1)
   - 简介：Multimodal medical imaging fuses complementary anatomical and functional information, yet modalities frequently disagree in pathologically heterogeneous regions. Current segmentation models handle this in one of two inadequate ways: deterministic fusion that...
   - 为什么值得读：适合借鉴为 prompt 生成、mask 选择或视觉推理模块。

14. **Annotation-Free Open-Vocabulary Segmentation for Remote-Sensing Images**
   - Source: arXiv, 2025-08-25
   - Authors: Kaiyu Li, Xiangyong Cao, Ruixun Liu, Shihong Wang, Zixuan Jiang et al.
   - Tags: open-vocabulary, SAM, boundary/frequency, remote sensing
   - Links: [paper](http://arxiv.org/abs/2508.18067v1) / [pdf](http://arxiv.org/pdf/2508.18067v1)
   - 简介：Semantic segmentation of remote sensing (RS) images is pivotal for comprehensive Earth observation, but the demand for interpreting new object categories, coupled with the high expense of manual annotation, poses significant challenges. Although open-vocabula...
   - 为什么值得读：适合迁移到开放词汇、零样本或无训练 COD。

15. **Diffusion Model as a Generalist Segmentation Learner**
   - Source: arXiv, 2026-04-27
   - Authors: Haoxiao Wang, Antao Xiang, Haiyang Sun, Peilin Sun, Changhao Pan et al.
   - Tags: open-vocabulary, diffusion, remote sensing, low-level
   - Links: [paper](http://arxiv.org/abs/2604.24575v1) / [pdf](http://arxiv.org/pdf/2604.24575v1)
   - 简介：Diffusion models are primarily trained for image synthesis, yet their denoising trajectories encode rich, spatially aligned visual priors. In this paper, we demonstrate that these priors can be utilized for text-conditioned semantic and open-vocabulary segmen...
   - 为什么值得读：适合迁移到开放词汇、零样本或无训练 COD。

16. **VesselSim: learning 3D blood vessel segmentation without expert annotations**
   - Source: arXiv, 2026-05-25
   - Authors: Erin Rainville, Melissa Ananian, Tristan Mirolla, Hassan Rivaz, Yiming Xiao
   - Tags: boundary/frequency, depth/geometry, anomaly/OOD
   - Links: [paper](http://arxiv.org/abs/2605.26277v2) / [pdf](http://arxiv.org/pdf/2605.26277v2)
   - 简介：Blood vessel segmentation is a core task in medical image analysis for the care of vascular diseases and surgical planning, yet the challenges of providing expert vascular annotations pose a major obstacle for the progress of related deep learning techniques....
   - 为什么值得读：适合补充伪装场景中的边界、纹理、几何先验。

17. **Binary Tracking for Spatial QA and Navigation with Open Vision-Language Models**
   - Source: arXiv, 2026-06-15
   - Authors: Dongbin Na, Chanwoo Kim, Soonbin Rho, Giyun Choi, Gangbok Lee et al.
   - Tags: SAM, VLM/MLLM, reasoning, diffusion, retrieval/prototype, video
   - Links: [paper](http://arxiv.org/abs/2606.16902v1) / [pdf](http://arxiv.org/pdf/2606.16902v1)
   - 简介：This work addresses spatial question answering for service robots traversing long egocentric routes. Given a query such as "where can I find a dry cleaner on the way back home?", the system returns a metric coordinate that downstream navigation components can...
   - 为什么值得读：适合借鉴为 prompt 生成、mask 选择或视觉推理模块。

18. **3D-PLOT-LLM: Part-Level Object Tokens for 3D Large Language Models**
   - Source: arXiv, 2026-06-18
   - Authors: Jintang Xue, Xinyu Wang, Yixing Wu, Jingwen Chen, C. -C. Jay Kuo
   - Tags: VLM/MLLM, diffusion, depth/geometry
   - Links: [paper](http://arxiv.org/abs/2606.19828v1) / [pdf](http://arxiv.org/pdf/2606.19828v1)
   - 简介：3D multimodal large language models (3D MLLMs) describe a 3D object as a whole but cannot address, name, or reason about its parts. Prior part-aware attempts add segmentation decoders, heavier 3D encoders, or bounding-box grammars at substantial parameter cos...
   - 为什么值得读：适合借鉴为 prompt 生成、mask 选择或视觉推理模块。

19. **High-Fidelity Synthetic Transmission Electron Microscopy Image Generation Using Diffusion Probabilistic Models for Data-Limited Semiconductor Metrology**
   - Source: arXiv, 2026-06-23
   - Authors: Johannes Boehm, Bappaditya Dey
   - Tags: SAM, diffusion, low-level
   - Links: [paper](http://arxiv.org/abs/2606.24817v1) / [pdf](http://arxiv.org/pdf/2606.24817v1)
   - 简介：Advanced semiconductor nodes drastically increased demand for Transmission Electron Microscopy (TEM), yet destructive sample preparation, slow imaging and high costs severely limit the availability of diverse datasets needed for downstream machine learning (M...
   - 为什么值得读：适合借鉴为 prompt 生成、mask 选择或视觉推理模块。

20. **Prob-BBDM: a Probabilistic Brownian Bridge Diffusion Model for MRI sequence image-to-image translation**
   - Source: arXiv, 2026-06-23
   - Authors: Martin Valls, Pascal Bourdon, Christine Fernandez-Maloigne, Guillaume Herpe, David Helbert
   - Tags: diffusion, depth/geometry
   - Links: [paper](http://arxiv.org/abs/2606.24313v1) / [pdf](http://arxiv.org/pdf/2606.24313v1)
   - 简介：AI-driven image-to-image synthesis is rapidly advancing, with growing applications in medical imaging. Multi-modal image analysis plays a crucial role in optimizing examination quality, yet acquiring multiple imaging modalities in clinical settings remains re...
   - 为什么值得读：适合补充伪装场景中的边界、纹理、几何先验。

21. **IMAGIN-4D: Image-Guided Controllable Interaction Generation**
   - Source: arXiv, 2026-06-22
   - Authors: Sai Kumar Dwivedi, Federica Bogo, Buğra Tekin, Chenhongyi Yang, Nadine Bertsch et al.
   - Tags: SAM, diffusion, depth/geometry, video
   - Links: [paper](http://arxiv.org/abs/2606.23675v1) / [pdf](http://arxiv.org/pdf/2606.23675v1)
   - 简介：Generating human-object interactions (HOI) is central to character animation, robotics, AR/VR, and embodied AI. Recent HOI generation methods synthesize motion from text, object geometry, and sparse waypoints, controlling action semantics and object trajector...
   - 为什么值得读：适合借鉴为 prompt 生成、mask 选择或视觉推理模块。

22. **Prompting Diffusion Models for Zero-Shot Instance Segmentation**
   - Source: arXiv, 2026-06-21
   - Authors: Irem Zeynep Alagöz, Nils Morbitzer, Andrea Ramazzina, Nassir Navab, Federico Tombari et al.
   - Tags: diffusion
   - Links: [paper](http://arxiv.org/abs/2606.22660v1) / [pdf](http://arxiv.org/pdf/2606.22660v1)
   - 简介：Several disruptive research directions have recently emerged in computer vision, including foundation models achieving previously unseen zero-shot performance in scene understanding, even interactively, and generative models that synthesize extremely realisti...
   - 为什么值得读：方法上可能可迁移，建议先读摘要和图 1。

23. **MMDiff: Extending Diffusion Transformers for Multi-Modal Generation**
   - Source: arXiv, 2026-06-15
   - Authors: Yagmur Akarken, Orest Kupyn, Christian Rupprecht
   - Tags: diffusion, depth/geometry, video, low-level
   - Links: [paper](http://arxiv.org/abs/2606.16673v1) / [pdf](http://arxiv.org/pdf/2606.16673v1)
   - 简介：Diffusion transformers have demonstrated remarkable generative capabilities, yet the rich perceptual representations computed across their denoising trajectory are discarded once the content is rendered. We present MMDiff, a framework that transforms a frozen...
   - 为什么值得读：适合补充伪装场景中的边界、纹理、几何先验。

24. **AD-DINOv3: Enhancing DINOv3 for Zero-Shot Anomaly Detection with Anomaly-Aware Calibration**
   - Source: arXiv, 2025-09-17
   - Authors: Jingyi Yuan, Jianxiong Ye, Wenkang Chen, Chenqiang Gao
   - Tags: VLM/MLLM, diffusion, anomaly/OOD
   - Links: [paper](http://arxiv.org/abs/2509.14084v2) / [pdf](http://arxiv.org/pdf/2509.14084v2)
   - 简介：Zero-Shot Anomaly Detection (ZSAD) seeks to identify anomalies from arbitrary novel categories, offering a scalable and annotation-efficient solution. Traditionally, most ZSAD works have been based on the CLIP model, which performs anomaly detection by calcul...
   - 为什么值得读：适合借鉴为 prompt 生成、mask 选择或视觉推理模块。

25. **FiLo++: Zero-/Few-Shot Anomaly Detection by Fused Fine-Grained Descriptions and Deformable Localization**
   - Source: arXiv, 2025-01-17
   - Authors: Zhaopeng Gu, Bingke Zhu, Guibo Zhu, Yingying Chen, Ming Tang et al.
   - Tags: SAM, reasoning, diffusion, anomaly/OOD
   - Links: [paper](http://arxiv.org/abs/2501.10067v2) / [pdf](http://arxiv.org/pdf/2501.10067v2)
   - 简介：Anomaly detection methods typically require extensive normal samples from the target class for training, limiting their applicability in scenarios that require rapid adaptation, such as cold start. Zero-shot and few-shot anomaly detection do not require label...
   - 为什么值得读：适合借鉴为 prompt 生成、mask 选择或视觉推理模块。

26. **Exploring Efficient Open-Vocabulary Segmentation in the Remote Sensing**
   - Source: arXiv, 2025-09-15
   - Authors: Bingyu Li, Haocheng Dong, Da Zhang, Zhiyuan Zhao, Junyu Gao et al.
   - Tags: open-vocabulary, SAM, VLM/MLLM, boundary/frequency, remote sensing
   - Links: [paper](http://arxiv.org/abs/2509.12040v2) / [pdf](http://arxiv.org/pdf/2509.12040v2)
   - 简介：Open-Vocabulary Remote Sensing Image Segmentation (OVRSIS), an emerging task that adapts Open-Vocabulary Segmentation (OVS) to the remote sensing (RS) domain, remains underexplored due to the absence of a unified evaluation benchmark and the domain gap betwee...
   - 为什么值得读：适合迁移到开放词汇、零样本或无训练 COD。

27. **TravExplorer: Cross-Floor Embodied Exploration via Traversability-Aware 3-D Planning**
   - Source: arXiv, 2026-05-19
   - Authors: Han Zheng, Zhe Chen, Yudong Huang, Haoran Liu, Jinghao Wang et al.
   - Tags: open-vocabulary, reasoning, depth/geometry, video
   - Links: [paper](http://arxiv.org/abs/2605.19958v1) / [pdf](http://arxiv.org/pdf/2605.19958v1)
   - 简介：Zero-shot Object Navigation (ZSON) has shown promise for open-vocabulary target search in unseen environments, yet most existing systems remain tied to planar representations and single-floor assumptions. These assumptions become inadequate in real buildings,...
   - 为什么值得读：适合迁移到开放词汇、零样本或无训练 COD。

28. **SparseSAM: Structured Sparsification of Activations in Segment Anything Models**
   - Source: arXiv, 2026-05-17
   - Authors: Hoai-Chau Tran, Chi H. Nguyen, Duy M. H. Nguyen, Mathias Niepert, Fan Lai et al.
   - Tags: open-vocabulary, training-free, SAM
   - Links: [paper](http://arxiv.org/abs/2605.17633v1) / [pdf](http://arxiv.org/pdf/2605.17633v1)
   - 简介：The Segment Anything Model (SAM) achieves strong open-vocabulary segmentation, but its ViT-based image encoders dominate inference latency and memory. Existing activation compression methods, such as token merging, reduce the token length to process, yet intr...
   - 为什么值得读：适合迁移到开放词汇、零样本或无训练 COD。

29. **Towards Realistic Open-Vocabulary Remote Sensing Segmentation: Benchmark and Baseline**
   - Source: arXiv, 2026-04-17
   - Authors: Bingyu Li, Tao Huo, Haocheng Dong, Da Zhang, Zhiyuan Zhao et al.
   - Tags: open-vocabulary, remote sensing, anomaly/OOD
   - Links: [paper](http://arxiv.org/abs/2604.15652v1) / [pdf](http://arxiv.org/pdf/2604.15652v1)
   - 简介：Open-vocabulary remote sensing image segmentation (OVRSIS) remains underexplored due to fragmented datasets, limited training diversity, and the lack of evaluation benchmarks that reflect realistic geospatial application demands. Our previous \textit{OVRSISBe...
   - 为什么值得读：适合迁移到开放词汇、零样本或无训练 COD。

30. **OV-Stitcher: A Global Context-Aware Framework for Training-Free Open-Vocabulary Semantic Segmentation**
   - Source: arXiv, 2026-04-09
   - Authors: Seungjae Moon, Seunghyun Oh, Youngmin Ro
   - Tags: open-vocabulary, training-free, VLM/MLLM, reasoning, diffusion, boundary/frequency
   - Links: [paper](http://arxiv.org/abs/2604.08110v2) / [pdf](http://arxiv.org/pdf/2604.08110v2)
   - 简介：Training-free open-vocabulary semantic segmentation(TF-OVSS) has recently attracted attention for its ability to perform dense prediction by leveraging the pretrained knowledge of large vision and vision-language models, without requiring additional training....
   - 为什么值得读：适合迁移到开放词汇、零样本或无训练 COD。

31. **TRACE: Evidence Grounding-Guided Multi-Video Event Understanding and Claim Generation**
   - Source: arXiv, 2026-05-16
   - Authors: Pengyu Yan, Akhil Gorugantu, Mahesh Bhosale, Abdul Wasi, Vishvesh Trivedi et al.
   - Tags: VLM/MLLM, reasoning, video
   - Links: [paper](http://arxiv.org/abs/2605.16740v2) / [pdf](http://arxiv.org/pdf/2605.16740v2)
   - 简介：Multi-video event understanding demands models that can locate and attribute query-relevant evidence scattered across long, heterogeneous video corpora. Existing large vision-language models (LVLMs) often underperform in this regime because they quickly exhau...
   - 为什么值得读：适合借鉴为 prompt 生成、mask 选择或视觉推理模块。

32. **Segmentation, Detection and Explanation: A Unified Framework for CT Appearance Reasoning**
   - Source: arXiv, 2026-05-15
   - Authors: Yuyuan Liu, Can Peng, Yingyu Yang, Qianye Yang, Cheng Ouyang et al.
   - Tags: VLM/MLLM, reasoning, diffusion
   - Links: [paper](http://arxiv.org/abs/2605.15997v1) / [pdf](http://arxiv.org/pdf/2605.15997v1)
   - 简介：Recent progress in deep learning has significantly advanced CT image analysis, particularly for segmentation tasks. However, these advances are largely confined to image-level pattern recognition, with most methods lacking explicit anatomical or contextual re...
   - 为什么值得读：适合借鉴为 prompt 生成、mask 选择或视觉推理模块。

33. **DeepTumorVQA: A Hierarchical 3D CT Benchmark for Stage-Wise Evaluation of Medical VLMs and Tool-Augmented Agents**
   - Source: arXiv, 2026-05-10
   - Authors: Yixiong Chen, Wenjie Xiao, Pedro R. A. S. Bassi, Boyan Wang, Liang He et al.
   - Tags: VLM/MLLM, reasoning, diffusion, boundary/frequency, depth/geometry
   - Links: [paper](http://arxiv.org/abs/2605.09679v1) / [pdf](http://arxiv.org/pdf/2605.09679v1)
   - 简介：Medical vision-language models (VLMs) and AI agents have made significant progress in learning to analyze and reason about clinical images. However, existing medical visual question answering (VQA) benchmarks collapse model capabilities into a single accuracy...
   - 为什么值得读：适合借鉴为 prompt 生成、mask 选择或视觉推理模块。

34. **SubspaceAD: Training-Free Few-Shot Anomaly Detection via Subspace Modeling**
   - Source: arXiv, 2026-02-26
   - Authors: Camile Lendering, Erkut Akdag, Egor Bondarev
   - Tags: training-free, VLM/MLLM, retrieval/prototype, remote sensing, anomaly/OOD
   - Links: [paper](http://arxiv.org/abs/2602.23013v3) / [pdf](http://arxiv.org/pdf/2602.23013v3)
   - 简介：Detecting visual anomalies in industrial inspection often requires training with only a few normal images per category. Recent few-shot methods achieve strong results employing foundation-model features, but typically rely on memory banks, auxiliary datasets,...
   - 为什么值得读：适合迁移到开放词汇、零样本或无训练 COD。

35. **V-Zero: Answer-Label-Free On-Policy Distillation with Contrastive Evidence Gating for Fine-Grained Visual Reasoning**
   - Source: arXiv, 2026-06-24
   - Authors: Haoxiang Sun, Zhihang Yi, Langxuan Deng, Yuhao Zhou, Peiqi Jia et al.
   - Tags: SAM, VLM/MLLM, reasoning
   - Links: [paper](http://arxiv.org/abs/2606.25319v1) / [pdf](http://arxiv.org/pdf/2606.25319v1)
   - 简介：Fine-grained visual reasoning requires multimodal large language models (MLLMs) to identify task-relevant visual evidence and ground their reasoning in local image regions. Existing agentic methods typically rely on reinforcement learning with verifiable rewa...
   - 为什么值得读：适合借鉴为 prompt 生成、mask 选择或视觉推理模块。

36. **Are We There Yet? Exploring the Capabilities of MLLMs in Assistive AI Applications**
   - Source: arXiv, 2026-06-23
   - Authors: Shayon Dasgupta, Avijit Dasgupta, C. V. Jawahar
   - Tags: VLM/MLLM, reasoning, anomaly/OOD
   - Links: [paper](http://arxiv.org/abs/2606.25084v1) / [pdf](http://arxiv.org/pdf/2606.25084v1)
   - 简介：Multimodal Large Language Models (MLLMs) have redefined visual understanding by combining vision encoders with large-scale language models. This unified architecture enables strong performance on tasks like image captioning, visual question answering, and mul...
   - 为什么值得读：适合借鉴为 prompt 生成、mask 选择或视觉推理模块。

37. **CineCap: Structured Reasoning with Spatio-Temporal Anchors for Cinematographic Video Captioning**
   - Source: arXiv, 2026-06-23
   - Authors: Xinyu Mao, Yuhui Zeng, Xiaokun Liu, Wenyu Qin, Meng Wang et al.
   - Tags: VLM/MLLM, reasoning, diffusion, depth/geometry, video
   - Links: [paper](http://arxiv.org/abs/2606.24636v1) / [pdf](http://arxiv.org/pdf/2606.24636v1)
   - 简介：Cinematographic captioning aims to describe how a video is filmed using professional film-language concepts such as camera movement, shot size, depth of field, composition, and shooting angle. This capability is important for fine-grained video understanding...
   - 为什么值得读：适合借鉴为 prompt 生成、mask 选择或视觉推理模块。

38. **Cross-Modality Structural Guidance in 3D Latent Diffusion for Robust FLAIR Super-Resolution**
   - Source: arXiv, 2026-06-24
   - Authors: Haoyu Lan, Jiazhen Zhang, John Onofrey, Bino Varghese, Nasim Sheikh-Bahaei et al.
   - Tags: SAM, diffusion, boundary/frequency, depth/geometry, low-level
   - Links: [paper](http://arxiv.org/abs/2606.25255v1) / [pdf](http://arxiv.org/pdf/2606.25255v1)
   - 简介：High-resolution (HR) MRI acquisition is often hampered by scan time constraints, resulting in anisotropic or low-resolution scans (e.g., thick-slice FLAIR) that limit diagnostic accuracy. While deep learning-based super-resolution (SR) methods show promise, t...
   - 为什么值得读：适合借鉴为 prompt 生成、mask 选择或视觉推理模块。

39. **NeuroSonic: Conditional Flow Matching for EEG-to-Speech Reconstruction**
   - Source: arXiv, 2026-06-23
   - Authors: Wenhao Gao, Yifan Wang, Yijia Ma, Carl Yang, Wen Li et al.
   - Tags: SAM, diffusion, video, low-level
   - Links: [paper](http://arxiv.org/abs/2606.24087v1) / [pdf](http://arxiv.org/pdf/2606.24087v1)
   - 简介：Reconstructing continuous speech from scalp electroencephalography (EEG) remains fundamentally challenging. EEG provides a weak, spatially diffuse, and highly variable measurement of distributed cortical activity, whereas speech is organized as a coherent aco...
   - 为什么值得读：适合借鉴为 prompt 生成、mask 选择或视觉推理模块。

40. **C^2GR: Coupled Comprehensive Generative Replay for a Continually Learnable Universal Segmentation Model**
   - Source: arXiv, 2026-06-22
   - Authors: Wei Li, Jingyang Zhang, Guoan Wang, Junzhi Ning, Yang Chen et al.
   - Tags: diffusion, low-level
   - Links: [paper](http://arxiv.org/abs/2606.23473v1) / [pdf](http://arxiv.org/pdf/2606.23473v1)
   - 简介：Universal segmentation models exhibit significant potential for diverse tasks involving different imaging modalities and segmentation objectives. Task-Incremental Learning provides a privacy-preserving approach to continually evolve a universal model on tasks...
   - 为什么值得读：方法上可能可迁移，建议先读摘要和图 1。

41. **BEV-Denoise: Learning Intrinsic Noise for Accurate Bird's-Eye-View Semantic Segmentation**
   - Source: arXiv, 2026-06-22
   - Authors: Dooseop Choi, Kyounghwan An, Kyoung-Wook Min
   - Tags: diffusion, low-level
   - Links: [paper](http://arxiv.org/abs/2606.22931v1) / [pdf](http://arxiv.org/pdf/2606.22931v1)
   - 简介：In this paper, we present a framework dubbed \textbf{BEV-Denoise} that estimates and removes intrinsic noise from learned Bird's-Eye-View (BEV) features to achieve accurate BEV semantic segmentation. Inspired by the noise estimation capability of Denoising Di...
   - 为什么值得读：方法上可能可迁移，建议先读摘要和图 1。

42. **ELDiff: When Evidential Learning Meets Text-to-Image Diffusion**
   - Source: arXiv, 2026-06-18
   - Authors: Qingtao Pan, Kai Ye, Zhihao Dou, Bing Ji, Shuo Li
   - Tags: diffusion, low-level
   - Links: [paper](http://arxiv.org/abs/2606.20924v1) / [pdf](http://arxiv.org/pdf/2606.20924v1)
   - 简介：In multi-object text-to-image (T2I) diffusion, ensuring semantic consistency between textual prompts and generated visual content is crucial for image synthesis. However, such consistency constraint is often underemphasized in the denoising process of diffusi...
   - 为什么值得读：方法上可能可迁移，建议先读摘要和图 1。

43. **Crane: Context-Guided Prompt Learning and Attention Refinement for Zero-Shot Anomaly Detection**
   - Source: arXiv, 2025-04-15
   - Authors: Alireza Salehi, Mohammadreza Salehi, Reshad Hosseini, Cees G. M. Snoek, Makoto Yamada et al.
   - Tags: SAM, diffusion, boundary/frequency, anomaly/OOD
   - Links: [paper](http://arxiv.org/abs/2504.11055v2) / [pdf](http://arxiv.org/pdf/2504.11055v2)
   - 简介：Anomaly Detection involves identifying deviations from normal data distributions and is critical in fields such as medical diagnostics and industrial defect detection. Traditional AD methods typically require the availability of normal training samples; howev...
   - 为什么值得读：适合借鉴为 prompt 生成、mask 选择或视觉推理模块。

44. **Taming SAM3 in the Wild: A Concept Bank for Open-Vocabulary Segmentation**
   - Source: arXiv, 2026-02-06
   - Authors: Gensheng Pei, Xiruo Jiang, Yazhou Yao, Xiangbo Shu, Fumin Shen et al.
   - Tags: open-vocabulary, SAM, diffusion, retrieval/prototype
   - Links: [paper](http://arxiv.org/abs/2602.06333v1) / [pdf](http://arxiv.org/pdf/2602.06333v1)
   - 简介：The recent introduction of \texttt{SAM3} has revolutionized Open-Vocabulary Segmentation (OVS) through \textit{promptable concept segmentation}, which grounds pixel predictions in flexible concept prompts. However, this reliance on pre-defined concepts makes...
   - 为什么值得读：适合迁移到开放词汇、零样本或无训练 COD。

45. **AerOSeg: Harnessing SAM for Open-Vocabulary Segmentation in Remote Sensing Images**
   - Source: arXiv, 2025-04-12
   - Authors: Saikat Dutta, Akhil Vasim, Siddhant Gole, Hamid Rezatofighi, Biplab Banerjee
   - Tags: open-vocabulary, SAM, diffusion, remote sensing
   - Links: [paper](http://arxiv.org/abs/2504.09203v1) / [pdf](http://arxiv.org/pdf/2504.09203v1)
   - 简介：Image segmentation beyond predefined categories is a key challenge in remote sensing, where novel and unseen classes often emerge during inference. Open-vocabulary image Segmentation addresses these generalization issues in traditional supervised segmentation...
   - 为什么值得读：适合迁移到开放词汇、零样本或无训练 COD。

46. **Decomposed Vision-Language Alignment for Fine-Grained Open-Vocabulary Segmentation**
   - Source: arXiv, 2026-05-15
   - Authors: Chenhao Wang, Yingrui Ji, Yu Meng, Yao Zhu
   - Tags: open-vocabulary, VLM/MLLM
   - Links: [paper](http://arxiv.org/abs/2605.15942v1) / [pdf](http://arxiv.org/pdf/2605.15942v1)
   - 简介：Open-vocabulary segmentation models often struggle to generalize to unseen combinations of object categories and attributes, because fine-grained descriptions are typically encoded as holistic sentences that entangle multiple semantic units. We propose a Deco...
   - 为什么值得读：适合迁移到开放词汇、零样本或无训练 COD。

47. **Making Training-Free Diffusion Segmentors Scale with the Generative Power**
   - Source: arXiv, 2026-03-06
   - Authors: Benyuan Meng, Qianqian Xu, Zitai Wang, Xiaochun Cao, Longtao Huang et al.
   - Tags: training-free, diffusion
   - Links: [paper](http://arxiv.org/abs/2603.06178v3) / [pdf](http://arxiv.org/pdf/2603.06178v3)
   - 简介：As powerful generative models, text-to-image diffusion models have recently been explored for discriminative tasks. A line of research focuses on adapting a pre-trained diffusion model to semantic segmentation without any further training, leading to training...
   - 为什么值得读：适合迁移到开放词汇、零样本或无训练 COD。

48. **R2AoP: Reliable and Robust Angle of Progression Estimation from Intrapartum Ultrasound**
   - Source: arXiv, 2026-05-20
   - Authors: Yuanhan Wang, Yifei Chen, Beining Wu, Mingxuan Liu, Xiaotian Hu et al.
   - Tags: diffusion, boundary/frequency, depth/geometry
   - Links: [paper](http://arxiv.org/abs/2605.21099v1) / [pdf](http://arxiv.org/pdf/2605.21099v1)
   - 简介：Accurate estimation of the Angle of Progression (AoP) from intrapartum transperineal ultrasound is critical for objective assessment of labor progression, yet remains highly sensitive to imaging noise, boundary ambiguities, and the geometric amplification of...
   - 为什么值得读：适合补充伪装场景中的边界、纹理、几何先验。

49. **VISTA: Variance-Gated Inter-Sequence Test-Time Adaptation for Multi-Sequence MRI Segmentation**
   - Source: arXiv, 2026-05-17
   - Authors: Zhipeng Deng, Jiale Zhou, Wenhan Jiang, Haolin Wang, Xun Lin et al.
   - Tags: boundary/frequency
   - Links: [paper](http://arxiv.org/abs/2605.17433v2) / [pdf](http://arxiv.org/pdf/2605.17433v2)
   - 简介：Deploying multi-sequence magnetic resonance imaging (MRI) segmentation models to new clinical environments is challenging due to variations in scanners and acquisition protocols. Although existing TTA methods handle basic per-modality shifts, they often fail...
   - 为什么值得读：适合补充伪装场景中的边界、纹理、几何先验。

50. **The Golden Subspace: Where Efficiency Meets Generalization in Continual Test-Time Adaptation**
   - Source: arXiv, 2026-03-23
   - Authors: Guannan Lai, Da-Wei Zhou, Zhenguo Li, Han-Jia Ye
   - Tags: SAM
   - Links: [paper](http://arxiv.org/abs/2603.21928v1) / [pdf](http://arxiv.org/pdf/2603.21928v1)
   - 简介：Continual Test-Time Adaptation (CTTA) aims to enable models to adapt online to unlabeled data streams under distribution shift without accessing source data. Existing CTTA methods face an efficiency-generalization trade-off: updating more parameters improves...
   - 为什么值得读：适合借鉴为 prompt 生成、mask 选择或视觉推理模块。

51. **Mind the Heads: Topological Representation Alignment for Multimodal LLMs**
   - Source: arXiv, 2026-06-22
   - Authors: Davide Caffagni, Alberto Compagnoni, Federico Melis, Sara Sarto, Pier Luigi Dovesi et al.
   - Tags: VLM/MLLM, anomaly/OOD
   - Links: [paper](http://arxiv.org/abs/2606.23885v1) / [pdf](http://arxiv.org/pdf/2606.23885v1)
   - 简介：Representation alignment has emerged as an effective approach to improve Multimodal Large Language Models (MLLMs) by regularizing their internal representations toward those of an external vision encoder. However, existing methods typically align a fixed laye...
   - 为什么值得读：适合借鉴为 prompt 生成、mask 选择或视觉推理模块。

52. **MLLMs Get It Right, Then Get It Wrong: Tracing and Correcting Late-Layer Textual Bias**
   - Source: arXiv, 2026-06-16
   - Authors: Xingming Li, Ao Cheng, Qiyao Sun, Xixiang He, Xuanyu Ji et al.
   - Tags: training-free, VLM/MLLM, reasoning, boundary/frequency
   - Links: [paper](http://arxiv.org/abs/2606.17953v1) / [pdf](http://arxiv.org/pdf/2606.17953v1)
   - 简介：When vision contradicts text, multimodal large language models (MLLMs) consistently favor text, even when images provide clear evidence otherwise. This bias poses risks for applications requiring visual grounding, yet its cause remains unclear.
   - 为什么值得读：适合迁移到开放词汇、零样本或无训练 COD。

53. **Gen-VCoT: Generative Visual Chain-of-Thought Reasoning via Diffusion-Based RGB Intermediate Representations**
   - Source: arXiv, 2026-06-15
   - Authors: Zhiqiang Zhou, Junliang Dai, Xu ling
   - Tags: SAM, VLM/MLLM, reasoning, diffusion, depth/geometry
   - Links: [paper](http://arxiv.org/abs/2606.16783v1) / [pdf](http://arxiv.org/pdf/2606.16783v1)
   - 简介：Multimodal large language models (MLLMs) excel at visual reasoning but rely on text-based chain-of-thought (CoT), lacking interpretable visual intermediates. Existing methods use opaque tokens or external tools, missing key properties.
   - 为什么值得读：适合借鉴为 prompt 生成、mask 选择或视觉推理模块。

54. **THREAD: Trajectory Planning for Hybrid Rigid-Soft Manipulators with Environment-Aware Diffusion**
   - Source: arXiv, 2026-06-19
   - Authors: Shivani Kamtikar, Pranav Asthana, Naveen Kumar Uppalapati, Girish Krishnan, Girish Chowdhary
   - Tags: diffusion, depth/geometry
   - Links: [paper](http://arxiv.org/abs/2606.21792v1) / [pdf](http://arxiv.org/pdf/2606.21792v1)
   - 简介：Manipulation in confined environments, such as threading a manipulator through narrow apertures, remains a fundamental challenge, especially for conventional rigid robots. Hybrid rigid-soft manipulators offer promise but face two compounding planning challeng...
   - 为什么值得读：适合补充伪装场景中的边界、纹理、几何先验。

55. **Search is All You Need for Few-shot Anomaly Detection**
   - Source: arXiv, 2025-04-16
   - Authors: Qishan Wang, Jia Guo, Shuyong Gao, Haofen Wang, Li Xiong et al.
   - Tags: training-free, SAM, retrieval/prototype, boundary/frequency, anomaly/OOD
   - Links: [paper](http://arxiv.org/abs/2504.11895v2) / [pdf](http://arxiv.org/pdf/2504.11895v2)
   - 简介：Few-shot anomaly detection (FSAD) has emerged as a crucial yet challenging task in industrial inspection, where normal distribution modeling must be accomplished with only a few normal images. While existing approaches typically employ multi-modal foundation...
   - 为什么值得读：适合迁移到开放词汇、零样本或无训练 COD。

56. **UniVAD: A Training-free Unified Model for Few-shot Visual Anomaly Detection**
   - Source: arXiv, 2024-12-04
   - Authors: Zhaopeng Gu, Bingke Zhu, Guibo Zhu, Yingying Chen, Ming Tang et al.
   - Tags: training-free, SAM, anomaly/OOD
   - Links: [paper](http://arxiv.org/abs/2412.03342v3) / [pdf](http://arxiv.org/pdf/2412.03342v3)
   - 简介：Visual Anomaly Detection (VAD) aims to identify abnormal samples in images that deviate from normal patterns, covering multiple domains, including industrial, logical, and medical fields. Due to the domain gaps between these fields, existing VAD methods are t...
   - 为什么值得读：适合迁移到开放词汇、零样本或无训练 COD。

57. **HD-TTA: Hypothesis-Driven Test-Time Adaptation for Safer Brain Tumor Segmentation**
   - Source: arXiv, 2026-02-23
   - Authors: Kartik Jhawar, Lipo Wang
   - Tags: SAM, diffusion, depth/geometry
   - Links: [paper](http://arxiv.org/abs/2602.19454v1) / [pdf](http://arxiv.org/pdf/2602.19454v1)
   - 简介：Standard Test-Time Adaptation (TTA) methods typically treat inference as a blind optimization task, applying generic objectives to all or filtered test samples. In safety-critical medical segmentation, this lack of selectivity often causes the tumor mask to s...
   - 为什么值得读：适合借鉴为 prompt 生成、mask 选择或视觉推理模块。

58. **Efficient Encoder-Free Fourier-based 3D Large Multimodal Model**
   - Source: CVPR 2026, 2026
   - Authors: Guofeng Mei, Wei Lin, Luigi Riz, Yujiao Wu, Yiming Wang et al.
   - Tags: depth/geometry
   - Links: [paper](https://openaccess.thecvf.com/content/CVPR2026/html/Mei_Efficient_Encoder-Free_Fourier-based_3D_Large_Multimodal_Model_CVPR_2026_paper.html) / [pdf](https://openaccess.thecvf.com/content/CVPR2026/papers/Mei_Efficient_Encoder-Free_Fourier-based_3D_Large_Multimodal_Model_CVPR_2026_paper.pdf)
   - 简介：CVF OpenAccess paper. Open the paper page for full abstract and method details.
   - 为什么值得读：适合补充伪装场景中的边界、纹理、几何先验。

59. **Seg-Agent: Test-Time Multimodal Reasoning for Training-Free Language-Guided Segmentation**
   - Source: arXiv, 2026-05-13
   - Authors: Chao Hao, Jun Xu, Ji Du, Shuo Ye, Ziyue Qiao et al.
   - Tags: training-free, SAM, VLM/MLLM, reasoning, diffusion
   - Links: [paper](http://arxiv.org/abs/2605.12953v1) / [pdf](http://arxiv.org/pdf/2605.12953v1)
   - 简介：Language-guided segmentation transcends the scope limitations of traditional semantic segmentation, enabling models to segment arbitrary target regions based on natural language instructions. Existing approaches typically adopt a two-stage framework: employin...
   - 为什么值得读：适合迁移到开放词汇、零样本或无训练 COD。

60. **SPEGC: Continual Test-Time Adaptation via Semantic-Prompt-Enhanced Graph Clustering for Medical Image Segmentation**
   - Source: arXiv, 2026-03-12
   - Authors: Xiaogang Du, Jiawei Zhang, Tongfei Liu, Tao Lei, Yingbo Wang
   - Tags: boundary/frequency, low-level
   - Links: [paper](http://arxiv.org/abs/2603.11492v1) / [pdf](http://arxiv.org/pdf/2603.11492v1)
   - 简介：In medical image segmentation tasks, the domain gap caused by the difference in data collection between training and testing data seriously hinders the deployment of pre-trained models in clinical practice. Continual Test-Time Adaptation (CTTA) aims to enable...
   - 为什么值得读：适合补充伪装场景中的边界、纹理、几何先验。

## 阅读记录模板

```text
论文：
任务设定：
核心假设：
方法模块：
对 COD / 我的课题的可迁移点：
我能改进的地方：
```

## 数据源

- arXiv API: recent preprints from COD and broad CV queries.
- CVF OpenAccess: CVPR 2026, WACV 2026, ICCV 2025 title-level scan.
