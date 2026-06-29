# Daily CV Paper Feed

Last updated: 2026-06-29 14:06 Asia/Shanghai
Archive days kept: 4

This page tracks new and useful computer-vision papers, with COD/camouflaged object detection kept as the primary reading thread and broader CV methods included for inspiration.

历史更新不会被删除；如果当天没看完，可以继续往下翻到对应日期。

## 今日优先读：近 30 天新文献优先

1. **A Retinomorphic Optical Spiking Neuron for Camouflaged Object Detection**
   - Source: arXiv, 2026-05-30
   - Authors: Srilagna Sahoo, Adwaaiit Pande, Kartikey Thakar, Shubham Sahay, Saurabh Lodha
   - Tags: COD, boundary/frequency
   - Links: [paper](http://arxiv.org/abs/2606.00818v1) / [pdf](http://arxiv.org/pdf/2606.00818v1)
   - 论文：A Retinomorphic Optical Spiking Neuron for Camouflaged Object Detection
   - 一句话总结：Advanced vision systems require retinomorphic, energy-efficient spike-based preprocessing of dynamic visual scenes. Here, we demonstrate multiple retinal preprocessing functionalities by leveraging a Hodgkin-H...
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：边界感知建模，适合改善伪装目标轮廓不清的问题。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；边界/频域增强模块。
   - 可改进点：可尝试引入基础模型、文本先验或更强的环境上下文建模。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

2. **Video Object Segmentation-Aware Audio Generation**
   - Source: Crossref / IJCV / CCF-A / 顶刊 / International Journal of Computer Vision, 2026-06-23
   - Authors: Ilpo Viertola, Vladimir Iashin, Esa Rahtu
   - Tags: diffusion, video, remote sensing
   - Links: [paper](https://doi.org/10.1007/s11263-026-02911-2)
   - 论文：Video Object Segmentation-Aware Audio Generation
   - 一句话总结：Abstract Existing multimodal audio generation models often lack precise user control, which limits their applicability in professional Foley workflows. In particular, these models focus on the entire video and...
   - 任务设定：遥感/大场景密集视觉任务，关注小目标、尺度变化和复杂背景。
   - 方法核心：扩散/生成式建模，可能用于数据合成、先验建模或掩码优化。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：不是 COD 直系论文，但可能提供可迁移的视觉表征、训练策略或评测思路。
   - 可借鉴点：任务建模、损失函数、消融组织方式。
   - 可改进点：可思考是否缺少 COD 场景验证、复杂背景失败分析或轻量化部署。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

3. **Understanding How MLLMs Describe Artworks Using Token Activation Maps**
   - Source: arXiv, 2026-06-26
   - Authors: Nicola Fanelli, Pasquale De Marinis, Raffaele Scaringi, Eva Cetinic, Gennaro Vessio et al.
   - Tags: open-vocabulary, SAM, VLM/MLLM, reasoning
   - Links: [paper](http://arxiv.org/abs/2606.27947v1) / [pdf](http://arxiv.org/pdf/2606.27947v1)
   - 论文：Understanding How MLLMs Describe Artworks Using Token Activation Maps
   - 一句话总结：Multimodal Large Language Models (MLLMs) describe artworks with remarkable fluency, yet the visual reasoning behind their outputs remains opaque. When an MLLM names a style, identifies a subject, or recognizes...
   - 任务设定：开放词汇视觉识别/分割，目标类别或文本提示在训练时未必出现。
   - 方法核心：提示学习或提示生成，重点看文本/视觉 prompt 如何约束定位。
   - 实验结论：摘要未给出强实验信号；先看实验表格和图 1，再决定是否精读。
   - 和我课题的关系：适合拓展到开放词汇、零样本或少标注 COD。
   - 可借鉴点：prompt 设计、类别文本构造、免训练迁移流程；候选 mask 生成、视觉-语言筛选、推理式定位。
   - 可改进点：可改进 prompt 自动生成、负样本约束和 mask 置信度校准。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

4. **Anatomy-Guided Residual Motion Diffusion for Controllable 4D Cardiac MRI Synthesis**
   - Source: arXiv, 2026-06-25
   - Authors: Yiheng Cao, Gustavo Andrade-Miranda, Jiatian Zhang, Lingxiao Zhao, Xin Gao
   - Tags: unsupervised, diffusion, boundary/frequency, depth/geometry, video, medical imaging
   - Links: [paper](http://arxiv.org/abs/2606.26764v1) / [pdf](http://arxiv.org/pdf/2606.26764v1)
   - 论文：Anatomy-Guided Residual Motion Diffusion for Controllable 4D Cardiac MRI Synthesis
   - 一句话总结：Developing robust artificial intelligence models for 4D (3D + time) medical imaging is constrained by limited annotated data, inter-device domain shifts, and privacy restrictions. To address this, we propose a...
   - 任务设定：医学影像分割/检测，常见弱边界、低对比和标注稀缺问题。
   - 方法核心：扩散/生成式建模，可能用于数据合成、先验建模或掩码优化。
   - 实验结论：可能包含新数据集/基准；适合看评测协议、失败案例和是否能服务 COD。
   - 和我课题的关系：可补充 COD 中纹理、边界、几何先验不足的问题。
   - 可借鉴点：边界/频域增强模块；深度或几何先验融合。
   - 可改进点：可结合多尺度语义上下文，避免只强化纹理导致误检。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

5. **Controllable Histopathology Image Synthesis with Training-free Structural Initialization and Textural Modulation**
   - Source: arXiv, 2026-06-26
   - Authors: Yuheng Qiu, Jingyi Luo, Chenfei Ye, Ting Ma, Jianfeng Cao
   - Tags: training-free, diffusion, boundary/frequency, medical imaging
   - Links: [paper](http://arxiv.org/abs/2606.27935v1) / [pdf](http://arxiv.org/pdf/2606.27935v1)
   - 论文：Controllable Histopathology Image Synthesis with Training-free Structural Initialization and Textural Modulation
   - 一句话总结：Deep learning has demonstrated remarkable success in high-throughput histopathology image analysis. However, the performance of learning-based models critically depends on the quality and size of annotations b...
   - 任务设定：免训练或少训练迁移设定，重点看 prompt、特征选择和后处理。
   - 方法核心：扩散/生成式建模，可能用于数据合成、先验建模或掩码优化。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：适合拓展到开放词汇、零样本或少标注 COD。
   - 可借鉴点：prompt 设计、类别文本构造、免训练迁移流程；边界/频域增强模块。
   - 可改进点：可改进 prompt 自动生成、负样本约束和 mask 置信度校准。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

6. **MLFFM-SegDiff: A Multi-Level Feature Fusion Diffusion Model for Skin Lesion Segmentation**
   - Source: arXiv, 2026-06-25
   - Authors: Jingjun Gu, Chaojie Shen, Yifeng Cao, Wei Zhang, Yiliu Li et al.
   - Tags: diffusion, boundary/frequency, low-level, saliency/transparent, medical imaging
   - Links: [paper](http://arxiv.org/abs/2606.26712v1) / [pdf](http://arxiv.org/pdf/2606.26712v1)
   - 论文：MLFFM-SegDiff: A Multi-Level Feature Fusion Diffusion Model for Skin Lesion Segmentation
   - 一句话总结：Skin lesion segmentation is a key task in computer-aided dermatological diagnosis, where accuracy directly impacts downstream analysis and disease classification. However, dermoscopic images are challenging du...
   - 任务设定：医学影像分割/检测，常见弱边界、低对比和标注稀缺问题。
   - 方法核心：扩散/生成式建模，可能用于数据合成、先验建模或掩码优化。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：和 COD 同属低显著/弱边界目标发现，可迁移目标-背景分离思想。
   - 可借鉴点：边界/频域增强模块。
   - 可改进点：可结合多尺度语义上下文，避免只强化纹理导致误检。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

7. **Vision-Language Model Reasoning for Contextual Semantic Mapping in Intralogistics**
   - Source: arXiv, 2026-06-23
   - Authors: Marvin Rüdt, Hao Pang, Constantin Enke, Zäzilia Seibold, Kai Furmans
   - Tags: open-vocabulary, SAM, VLM/MLLM, reasoning, depth/geometry
   - Links: [paper](http://arxiv.org/abs/2606.24814v1) / [pdf](http://arxiv.org/pdf/2606.24814v1)
   - 论文：Vision-Language Model Reasoning for Contextual Semantic Mapping in Intralogistics
   - 一句话总结：Autonomous mobile robots operating in intralogistics environments rely on geometric maps for localization and navigation, but lack semantic understanding of objects and their contextual properties. We present...
   - 任务设定：开放词汇视觉识别/分割，目标类别或文本提示在训练时未必出现。
   - 方法核心：提示学习或提示生成，重点看文本/视觉 prompt 如何约束定位。
   - 实验结论：摘要强调消融、鲁棒性或泛化；适合优先看实验设计和跨域表现。
   - 和我课题的关系：适合拓展到开放词汇、零样本或少标注 COD。
   - 可借鉴点：prompt 设计、类别文本构造、免训练迁移流程；候选 mask 生成、视觉-语言筛选、推理式定位；深度或几何先验融合。
   - 可改进点：可改进 prompt 自动生成、负样本约束和 mask 置信度校准。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

8. **Jolia: Concept-Level Vision-Language Alignment for 3D CT Contrastive Learning**
   - Source: arXiv, 2026-06-23
   - Authors: Julien Khlaut, Charles Corbière, Baptiste Callard, Amaury Prat, Leo Butsanets et al.
   - Tags: VLM/MLLM, depth/geometry, medical imaging
   - Links: [paper](http://arxiv.org/abs/2606.24570v2) / [pdf](http://arxiv.org/pdf/2606.24570v2)
   - 论文：Jolia: Concept-Level Vision-Language Alignment for 3D CT Contrastive Learning
   - 一句话总结：Vision-language contrastive pretraining has become the dominant recipe for 3D medical foundation models, leveraging the large volumes of paired scans and reports produced in clinical practice. However, medical...
   - 任务设定：基础模型驱动的视觉定位/分割/推理，可用于自动提示生成或 mask 筛选。
   - 方法核心：视觉-语言对齐，把语义文本信息引入检测或分割。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：可补充 COD 中纹理、边界、几何先验不足的问题。
   - 可借鉴点：候选 mask 生成、视觉-语言筛选、推理式定位；深度或几何先验融合。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

9. **Training-free Cross-domain Few-shot Segmentation via Robust Semantic Representation and Matching**
   - Source: arXiv, 2026-06-23
   - Authors: Sujun Sun, Mingwu Ren, Haofeng Zhang
   - Tags: training-free, diffusion, retrieval/prototype, boundary/frequency, low-level
   - Links: [paper](http://arxiv.org/abs/2606.24297v1) / [pdf](http://arxiv.org/pdf/2606.24297v1)
   - 论文：Training-free Cross-domain Few-shot Segmentation via Robust Semantic Representation and Matching
   - 一句话总结：Cross-domain Few-shot Segmentation (CD-FSS) aims to transfer knowledge learned from source domain to distinct target domains, segmenting unseen target classes with only a few annotated samples. Although existi...
   - 任务设定：免训练或少训练迁移设定，重点看 prompt、特征选择和后处理。
   - 方法核心：借助 SAM/基础分割模型产生候选 mask，再做筛选或适配。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：适合拓展到开放词汇、零样本或少标注 COD。
   - 可借鉴点：prompt 设计、类别文本构造、免训练迁移流程；边界/频域增强模块。
   - 可改进点：可改进 prompt 自动生成、负样本约束和 mask 置信度校准。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

10. **High-Fidelity Synthetic Transmission Electron Microscopy Image Generation Using Diffusion Probabilistic Models for Data-Limited Semiconductor Metrology**
   - Source: arXiv, 2026-06-23
   - Authors: Johannes Boehm, Bappaditya Dey
   - Tags: diffusion, low-level
   - Links: [paper](http://arxiv.org/abs/2606.24817v1) / [pdf](http://arxiv.org/pdf/2606.24817v1)
   - 论文：High-Fidelity Synthetic Transmission Electron Microscopy Image Generation Using Diffusion Probabilistic Models for Data-Limited Semiconductor Metrology
   - 一句话总结：Advanced semiconductor nodes drastically increased demand for Transmission Electron Microscopy (TEM), yet destructive sample preparation, slow imaging and high costs severely limit the availability of diverse...
   - 任务设定：通用计算机视觉任务，先判断是否能迁移到 COD 的感知、定位或分割环节。
   - 方法核心：扩散/生成式建模，可能用于数据合成、先验建模或掩码优化。
   - 实验结论：可能包含新数据集/基准；适合看评测协议、失败案例和是否能服务 COD。
   - 和我课题的关系：不是 COD 直系论文，但可能提供可迁移的视觉表征、训练策略或评测思路。
   - 可借鉴点：任务建模、损失函数、消融组织方式。
   - 可改进点：可思考是否缺少 COD 场景验证、复杂背景失败分析或轻量化部署。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

11. **ARTEMIS: Agent-guided Reliability-aware Temporal Mask Evolution for Imperfectly Supervised Video Polyp Segmentation**
   - Source: arXiv, 2026-06-18
   - Authors: Tong Wang, Siwen Wang, Yaolei Qi, Jinxing Zhou, Yuting He et al.
   - Tags: VLM/MLLM, retrieval/prototype, boundary/frequency, depth/geometry, video
   - Links: [paper](http://arxiv.org/abs/2606.20161v1) / [pdf](http://arxiv.org/pdf/2606.20161v1)
   - 论文：ARTEMIS: Agent-guided Reliability-aware Temporal Mask Evolution for Imperfectly Supervised Video Polyp Segmentation
   - 一句话总结：Imperfectly supervised video polyp segmentation (VPS) aims to learn dense, temporally consistent masks from inexpensive supervision, including weak annotations (points, scribbles) and semi-supervision with few...
   - 任务设定：基础模型驱动的视觉定位/分割/推理，可用于自动提示生成或 mask 筛选。
   - 方法核心：借助 SAM/基础分割模型产生候选 mask，再做筛选或适配。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：可补充 COD 中纹理、边界、几何先验不足的问题。
   - 可借鉴点：候选 mask 生成、视觉-语言筛选、推理式定位；边界/频域增强模块；深度或几何先验融合。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

12. **ActiveSAM: Image-Conditional Class Pruning for Fast and Accurate Open-Vocabulary Segmentation**
   - Source: arXiv, 2026-06-15
   - Authors: Tran Dinh Tien, Zhiqiang Shen
   - Tags: open-vocabulary, training-free, SAM, diffusion, remote sensing
   - Links: [paper](http://arxiv.org/abs/2606.16996v1) / [pdf](http://arxiv.org/pdf/2606.16996v1)
   - 论文：ActiveSAM: Image-Conditional Class Pruning for Fast and Accurate Open-Vocabulary Segmentation
   - 一句话总结：Segment Anything Model 3 (SAM 3) provides a strong frozen backbone for concept-prompted segmentation, but applying it directly to open-vocabulary semantic segmentation (OVSS) is inefficient: full-resolution de...
   - 任务设定：开放词汇视觉识别/分割，目标类别或文本提示在训练时未必出现。
   - 方法核心：提示学习或提示生成，重点看文本/视觉 prompt 如何约束定位。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：适合拓展到开放词汇、零样本或少标注 COD。
   - 可借鉴点：prompt 设计、类别文本构造、免训练迁移流程；候选 mask 生成、视觉-语言筛选、推理式定位。
   - 可改进点：可改进 prompt 自动生成、负样本约束和 mask 置信度校准。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

## 高质量来源优先读：CCF-A/B 与顶刊顶会

1. **VSCode: General Visual Salient and Camouflaged Object Detection with 2D Prompt Learning**
   - Source: CVPR 2024, 2024
   - Authors: Ziyang Luo, Nian Liu, Wangbo Zhao, Xuguang Yang, Dingwen Zhang et al.
   - Tags: COD, saliency/transparent
   - Links: [paper](https://openaccess.thecvf.com/content/CVPR2024/html/Luo_VSCode_General_Visual_Salient_and_Camouflaged_Object_Detection_with_2D_CVPR_2024_paper.html) / [pdf](https://openaccess.thecvf.com/content/CVPR2024/papers/Luo_VSCode_General_Visual_Salient_and_Camouflaged_Object_Detection_with_2D_CVPR_2024_paper.pdf)
   - 论文：VSCode: General Visual Salient and Camouflaged Object Detection with 2D Prompt Learning
   - 一句话总结：CVF OpenAccess paper. Open the paper page for full abstract and method details.
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：提示学习或提示生成，重点看文本/视觉 prompt 如何约束定位。
   - 实验结论：当前来源只提供标题级信息；需要打开论文页确认数据集、指标和消融。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析。
   - 可改进点：可尝试引入基础模型、文本先验或更强的环境上下文建模。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

2. **Training-Free Open-Vocabulary Camouflaged Object Segmentation via Fine-Grained Object Binding and Adaptive Hybrid Prompt**
   - Source: CVPR 2026, 2026
   - Authors: Peng Ren, Cheng Jiang, Chuande Yang, Fuming Sun, Tian Bai
   - Tags: COD, open-vocabulary, training-free
   - Links: [paper](https://openaccess.thecvf.com/content/CVPR2026/html/Ren_Training-Free_Open-Vocabulary_Camouflaged_Object_Segmentation_via_Fine-Grained_Object_Binding_and_CVPR_2026_paper.html) / [pdf](https://openaccess.thecvf.com/content/CVPR2026/papers/Ren_Training-Free_Open-Vocabulary_Camouflaged_Object_Segmentation_via_Fine-Grained_Object_Binding_and_CVPR_2026_paper.pdf)
   - 论文：Training-Free Open-Vocabulary Camouflaged Object Segmentation via Fine-Grained Object Binding and Adaptive Hybrid Prompt
   - 一句话总结：CVF OpenAccess paper. Open the paper page for full abstract and method details.
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：提示学习或提示生成，重点看文本/视觉 prompt 如何约束定位。
   - 实验结论：当前来源只提供标题级信息；需要打开论文页确认数据集、指标和消融。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；prompt 设计、类别文本构造、免训练迁移流程。
   - 可改进点：可尝试引入基础模型、文本先验或更强的环境上下文建模。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

3. **Video Object Segmentation-Aware Audio Generation**
   - Source: Crossref / IJCV / CCF-A / 顶刊 / International Journal of Computer Vision, 2026-06-23
   - Authors: Ilpo Viertola, Vladimir Iashin, Esa Rahtu
   - Tags: diffusion, video, remote sensing
   - Links: [paper](https://doi.org/10.1007/s11263-026-02911-2)
   - 论文：Video Object Segmentation-Aware Audio Generation
   - 一句话总结：Abstract Existing multimodal audio generation models often lack precise user control, which limits their applicability in professional Foley workflows. In particular, these models focus on the entire video and...
   - 任务设定：遥感/大场景密集视觉任务，关注小目标、尺度变化和复杂背景。
   - 方法核心：扩散/生成式建模，可能用于数据合成、先验建模或掩码优化。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：不是 COD 直系论文，但可能提供可迁移的视觉表征、训练策略或评测思路。
   - 可借鉴点：任务建模、损失函数、消融组织方式。
   - 可改进点：可思考是否缺少 COD 场景验证、复杂背景失败分析或轻量化部署。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

4. **Discover, Segment, and Select: A Progressive Mechanism for Zero-shot Camouflaged Object Segmentation**
   - Source: CVPR 2026, 2026
   - Authors: Yilong Yang, Jianxin Tian, Shengchuan Zhang, Liujuan Cao
   - Tags: COD
   - Links: [paper](https://openaccess.thecvf.com/content/CVPR2026/html/Yang_Discover_Segment_and_Select_A_Progressive_Mechanism_for_Zero-shot_Camouflaged_CVPR_2026_paper.html) / [pdf](https://openaccess.thecvf.com/content/CVPR2026/papers/Yang_Discover_Segment_and_Select_A_Progressive_Mechanism_for_Zero-shot_Camouflaged_CVPR_2026_paper.pdf)
   - 论文：Discover, Segment, and Select: A Progressive Mechanism for Zero-shot Camouflaged Object Segmentation
   - 一句话总结：CVF OpenAccess paper. Open the paper page for full abstract and method details.
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：摘要层面未显示明确模块，建议先看方法图确认 backbone、监督信号和损失设计。
   - 实验结论：当前来源只提供标题级信息；需要打开论文页确认数据集、指标和消融。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析。
   - 可改进点：可尝试引入基础模型、文本先验或更强的环境上下文建模。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

5. **Seeing Both Sides: Towards Bidirectional Semantic Alignment for Open-Vocabulary Camouflaged Object Segmentation**
   - Source: CVPR 2026, 2026
   - Authors: Guohui Zhang, Fuming Sun, Yu Zhao, Yuqiu Kong, Jing Sun et al.
   - Tags: COD, open-vocabulary
   - Links: [paper](https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_Seeing_Both_Sides_Towards_Bidirectional_Semantic_Alignment_for_Open-Vocabulary_Camouflaged_CVPR_2026_paper.html) / [pdf](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhang_Seeing_Both_Sides_Towards_Bidirectional_Semantic_Alignment_for_Open-Vocabulary_Camouflaged_CVPR_2026_paper.pdf)
   - 论文：Seeing Both Sides: Towards Bidirectional Semantic Alignment for Open-Vocabulary Camouflaged Object Segmentation
   - 一句话总结：CVF OpenAccess paper. Open the paper page for full abstract and method details.
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：摘要层面未显示明确模块，建议先看方法图确认 backbone、监督信号和损失设计。
   - 实验结论：当前来源只提供标题级信息；需要打开论文页确认数据集、指标和消融。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；prompt 设计、类别文本构造、免训练迁移流程。
   - 可改进点：可尝试引入基础模型、文本先验或更强的环境上下文建模。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

6. **Beyond Weak Supervision: MLLMs-Guided Graded Knowledge Distillation for Unsupervised Camouflaged Object Detection**
   - Source: CVPR 2026, 2026
   - Authors: Huafeng Chen, Chenguang Zhu, Yueming Lyu, Caifeng Shan
   - Tags: COD, unsupervised, VLM/MLLM, boundary/frequency
   - Links: [paper](https://openaccess.thecvf.com/content/CVPR2026/html/Chen_Beyond_Weak_Supervision_MLLMs-Guided_Graded_Knowledge_Distillation_for_Unsupervised_Camouflaged_CVPR_2026_paper.html) / [pdf](https://openaccess.thecvf.com/content/CVPR2026/papers/Chen_Beyond_Weak_Supervision_MLLMs-Guided_Graded_Knowledge_Distillation_for_Unsupervised_Camouflaged_CVPR_2026_paper.pdf)
   - 论文：Beyond Weak Supervision: MLLMs-Guided Graded Knowledge Distillation for Unsupervised Camouflaged Object Detection
   - 一句话总结：CVF OpenAccess paper. Open the paper page for full abstract and method details.
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：多模态大模型推理，可能用于目标描述、区域判断或链式推理。
   - 实验结论：当前来源只提供标题级信息；需要打开论文页确认数据集、指标和消融。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；候选 mask 生成、视觉-语言筛选、推理式定位；边界/频域增强模块。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

7. **Endow SAM with Keen Eyes: Temporal-spatial Prompt Learning for Video Camouflaged Object Detection**
   - Source: CVPR 2024, 2024
   - Authors: Wenjun Hui, Zhenfeng Zhu, Shuai Zheng, Yao Zhao
   - Tags: COD, SAM, video
   - Links: [paper](https://openaccess.thecvf.com/content/CVPR2024/html/Hui_Endow_SAM_with_Keen_Eyes_Temporal-spatial_Prompt_Learning_for_Video_CVPR_2024_paper.html) / [pdf](https://openaccess.thecvf.com/content/CVPR2024/papers/Hui_Endow_SAM_with_Keen_Eyes_Temporal-spatial_Prompt_Learning_for_Video_CVPR_2024_paper.pdf)
   - 论文：Endow SAM with Keen Eyes: Temporal-spatial Prompt Learning for Video Camouflaged Object Detection
   - 一句话总结：CVF OpenAccess paper. Open the paper page for full abstract and method details.
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：提示学习或提示生成，重点看文本/视觉 prompt 如何约束定位。
   - 实验结论：当前来源只提供标题级信息；需要打开论文页确认数据集、指标和消融。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；候选 mask 生成、视觉-语言筛选、推理式定位。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

8. **Seeing the Unseen: A Semantic Alignment and Context-Aware Prompt Framework for Open-Vocabulary Camouflaged Object Segmentation**
   - Source: ICCV 2025, 2025
   - Authors: Peng Ren, Tian Bai, Jing Sun, Fuming Sun
   - Tags: COD, open-vocabulary
   - Links: [paper](https://openaccess.thecvf.com/content/ICCV2025/html/Ren_Seeing_the_Unseen_A_Semantic_Alignment_and_Context-Aware_Prompt_Framework_ICCV_2025_paper.html) / [pdf](https://openaccess.thecvf.com/content/ICCV2025/papers/Ren_Seeing_the_Unseen_A_Semantic_Alignment_and_Context-Aware_Prompt_Framework_ICCV_2025_paper.pdf)
   - 论文：Seeing the Unseen: A Semantic Alignment and Context-Aware Prompt Framework for Open-Vocabulary Camouflaged Object Segmentation
   - 一句话总结：CVF OpenAccess paper. Open the paper page for full abstract and method details.
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：提示学习或提示生成，重点看文本/视觉 prompt 如何约束定位。
   - 实验结论：当前来源只提供标题级信息；需要打开论文页确认数据集、指标和消融。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；prompt 设计、类别文本构造、免训练迁移流程。
   - 可改进点：可尝试引入基础模型、文本先验或更强的环境上下文建模。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

9. **Beyond Appearance: Camouflaged Object Detection via Geometric Structure**
   - Source: CVPR 2026, 2026
   - Authors: Jinyu Han, Changguang Wu, Fuming Sun, Jinhui Tang
   - Tags: COD, depth/geometry
   - Links: [paper](https://openaccess.thecvf.com/content/CVPR2026/html/Han_Beyond_Appearance_Camouflaged_Object_Detection_via_Geometric_Structure_CVPR_2026_paper.html) / [pdf](https://openaccess.thecvf.com/content/CVPR2026/papers/Han_Beyond_Appearance_Camouflaged_Object_Detection_via_Geometric_Structure_CVPR_2026_paper.pdf)
   - 论文：Beyond Appearance: Camouflaged Object Detection via Geometric Structure
   - 一句话总结：CVF OpenAccess paper. Open the paper page for full abstract and method details.
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：摘要层面未显示明确模块，建议先看方法图确认 backbone、监督信号和损失设计。
   - 实验结论：当前来源只提供标题级信息；需要打开论文页确认数据集、指标和消融。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；深度或几何先验融合。
   - 可改进点：可尝试引入基础模型、文本先验或更强的环境上下文建模。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

10. **Shift the Lens: Environment-Aware Unsupervised Camouflaged Object Detection**
   - Source: CVPR 2025, 2025
   - Authors: Ji Du, Fangwei Hao, Mingyang Yu, Desheng Kong, Jiesheng Wu et al.
   - Tags: COD, unsupervised
   - Links: [paper](https://openaccess.thecvf.com/content/CVPR2025/html/Du_Shift_the_Lens_Environment-Aware_Unsupervised_Camouflaged_Object_Detection_CVPR_2025_paper.html) / [pdf](https://openaccess.thecvf.com/content/CVPR2025/papers/Du_Shift_the_Lens_Environment-Aware_Unsupervised_Camouflaged_Object_Detection_CVPR_2025_paper.pdf)
   - 论文：Shift the Lens: Environment-Aware Unsupervised Camouflaged Object Detection
   - 一句话总结：CVF OpenAccess paper. Open the paper page for full abstract and method details.
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：摘要层面未显示明确模块，建议先看方法图确认 backbone、监督信号和损失设计。
   - 实验结论：当前来源只提供标题级信息；需要打开论文页确认数据集、指标和消融。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析。
   - 可改进点：可尝试引入基础模型、文本先验或更强的环境上下文建模。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

11. **Rethinking Detecting Salient and Camouflaged Objects in Unconstrained Scenes**
   - Source: ICCV 2025, 2025
   - Authors: Zhangjun Zhou, Yiping Li, Chunlin Zhong, Jianuo Huang, Jialun Pei et al.
   - Tags: COD, saliency/transparent
   - Links: [paper](https://openaccess.thecvf.com/content/ICCV2025/html/Zhou_Rethinking_Detecting_Salient_and_Camouflaged_Objects_in_Unconstrained_Scenes_ICCV_2025_paper.html) / [pdf](https://openaccess.thecvf.com/content/ICCV2025/papers/Zhou_Rethinking_Detecting_Salient_and_Camouflaged_Objects_in_Unconstrained_Scenes_ICCV_2025_paper.pdf)
   - 论文：Rethinking Detecting Salient and Camouflaged Objects in Unconstrained Scenes
   - 一句话总结：CVF OpenAccess paper. Open the paper page for full abstract and method details.
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：摘要层面未显示明确模块，建议先看方法图确认 backbone、监督信号和损失设计。
   - 实验结论：当前来源只提供标题级信息；需要打开论文页确认数据集、指标和消融。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析。
   - 可改进点：可尝试引入基础模型、文本先验或更强的环境上下文建模。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

12. **ESCNet:Edge-Semantic Collaborative Network for Camouflaged Object Detection**
   - Source: ICCV 2025, 2025
   - Authors: Sheng Ye, Xin Chen, Yan Zhang, Xianming Lin, Liujuan Cao
   - Tags: COD, boundary/frequency
   - Links: [paper](https://openaccess.thecvf.com/content/ICCV2025/html/Ye_ESCNetEdge-Semantic_Collaborative_Network_for_Camouflaged_Object_Detection_ICCV_2025_paper.html) / [pdf](https://openaccess.thecvf.com/content/ICCV2025/papers/Ye_ESCNetEdge-Semantic_Collaborative_Network_for_Camouflaged_Object_Detection_ICCV_2025_paper.pdf)
   - 论文：ESCNet:Edge-Semantic Collaborative Network for Camouflaged Object Detection
   - 一句话总结：CVF OpenAccess paper. Open the paper page for full abstract and method details.
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：边界感知建模，适合改善伪装目标轮廓不清的问题。
   - 实验结论：当前来源只提供标题级信息；需要打开论文页确认数据集、指标和消融。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；边界/频域增强模块。
   - 可改进点：可尝试引入基础模型、文本先验或更强的环境上下文建模。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

13. **Enhancing Prompt Generation with Adaptive Refinement for Camouflaged Object Detection**
   - Source: ICCV 2025, 2025
   - Authors: Xuehan Chen, Guangyu Ren, Tianhong Dai, Tania Stathaki, Hengyan Liu
   - Tags: COD
   - Links: [paper](https://openaccess.thecvf.com/content/ICCV2025/html/Chen_Enhancing_Prompt_Generation_with_Adaptive_Refinement_for_Camouflaged_Object_Detection_ICCV_2025_paper.html) / [pdf](https://openaccess.thecvf.com/content/ICCV2025/papers/Chen_Enhancing_Prompt_Generation_with_Adaptive_Refinement_for_Camouflaged_Object_Detection_ICCV_2025_paper.pdf)
   - 论文：Enhancing Prompt Generation with Adaptive Refinement for Camouflaged Object Detection
   - 一句话总结：CVF OpenAccess paper. Open the paper page for full abstract and method details.
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：提示学习或提示生成，重点看文本/视觉 prompt 如何约束定位。
   - 实验结论：当前来源只提供标题级信息；需要打开论文页确认数据集、指标和消融。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析。
   - 可改进点：可尝试引入基础模型、文本先验或更强的环境上下文建模。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

14. **Multi-modal Segment Anything Model for Camouflaged Scene Segmentation**
   - Source: ICCV 2025, 2025
   - Authors: Guangyu Ren, Hengyan Liu, Michalis Lazarou, Tania Stathaki
   - Tags: COD, SAM
   - Links: [paper](https://openaccess.thecvf.com/content/ICCV2025/html/Ren_Multi-modal_Segment_Anything_Model_for_Camouflaged_Scene_Segmentation_ICCV_2025_paper.html) / [pdf](https://openaccess.thecvf.com/content/ICCV2025/papers/Ren_Multi-modal_Segment_Anything_Model_for_Camouflaged_Scene_Segmentation_ICCV_2025_paper.pdf)
   - 论文：Multi-modal Segment Anything Model for Camouflaged Scene Segmentation
   - 一句话总结：CVF OpenAccess paper. Open the paper page for full abstract and method details.
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：借助 SAM/基础分割模型产生候选 mask，再做筛选或适配。
   - 实验结论：当前来源只提供标题级信息；需要打开论文页确认数据集、指标和消融。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；候选 mask 生成、视觉-语言筛选、推理式定位。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

15. **LAKE-RED: Camouflaged Images Generation by Latent Background Knowledge Retrieval-Augmented Diffusion**
   - Source: CVPR 2024, 2024
   - Authors: Pancheng Zhao, Peng Xu, Pengda Qin, Deng-Ping Fan, Zhicheng Zhang et al.
   - Tags: COD, diffusion, retrieval/prototype, boundary/frequency
   - Links: [paper](https://openaccess.thecvf.com/content/CVPR2024/html/Zhao_LAKE-RED_Camouflaged_Images_Generation_by_Latent_Background_Knowledge_Retrieval-Augmented_Diffusion_CVPR_2024_paper.html) / [pdf](https://openaccess.thecvf.com/content/CVPR2024/papers/Zhao_LAKE-RED_Camouflaged_Images_Generation_by_Latent_Background_Knowledge_Retrieval-Augmented_Diffusion_CVPR_2024_paper.pdf)
   - 论文：LAKE-RED: Camouflaged Images Generation by Latent Background Knowledge Retrieval-Augmented Diffusion
   - 一句话总结：CVF OpenAccess paper. Open the paper page for full abstract and method details.
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：扩散/生成式建模，可能用于数据合成、先验建模或掩码优化。
   - 实验结论：当前来源只提供标题级信息；需要打开论文页确认数据集、指标和消融。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；边界/频域增强模块。
   - 可改进点：可尝试引入基础模型、文本先验或更强的环境上下文建模。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

16. **Scoring, Remember, and Reference: Catching Camouflaged Objects in Videos**
   - Source: ICCV 2025, 2025
   - Authors: Yu'ang Feng, Shuyong Gao, Fuzhen Yan, Yicheng Song, Lingyi Hong et al.
   - Tags: COD, video
   - Links: [paper](https://openaccess.thecvf.com/content/ICCV2025/html/Feng_Scoring_Remember_and_Reference_Catching_Camouflaged_Objects_in_Videos_ICCV_2025_paper.html) / [pdf](https://openaccess.thecvf.com/content/ICCV2025/papers/Feng_Scoring_Remember_and_Reference_Catching_Camouflaged_Objects_in_Videos_ICCV_2025_paper.pdf)
   - 论文：Scoring, Remember, and Reference: Catching Camouflaged Objects in Videos
   - 一句话总结：CVF OpenAccess paper. Open the paper page for full abstract and method details.
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：摘要层面未显示明确模块，建议先看方法图确认 backbone、监督信号和损失设计。
   - 实验结论：当前来源只提供标题级信息；需要打开论文页确认数据集、指标和消融。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析。
   - 可改进点：可尝试引入基础模型、文本先验或更强的环境上下文建模。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

17. **MAPSeg: Unified Unsupervised Domain Adaptation for Heterogeneous Medical Image Segmentation Based on 3D Masked Autoencoding and Pseudo-Labeling**
   - Source: CVPR 2024, 2024
   - Authors: Xuzhe Zhang, Yuhao Wu, Elsa Angelini, Ang Li, Jia Guo et al.
   - Tags: unsupervised, depth/geometry, domain adaptation, medical imaging
   - Links: [paper](https://openaccess.thecvf.com/content/CVPR2024/html/Zhang_MAPSeg_Unified_Unsupervised_Domain_Adaptation_for_Heterogeneous_Medical_Image_Segmentation_CVPR_2024_paper.html) / [pdf](https://openaccess.thecvf.com/content/CVPR2024/papers/Zhang_MAPSeg_Unified_Unsupervised_Domain_Adaptation_for_Heterogeneous_Medical_Image_Segmentation_CVPR_2024_paper.pdf)
   - 论文：MAPSeg: Unified Unsupervised Domain Adaptation for Heterogeneous Medical Image Segmentation Based on 3D Masked Autoencoding and Pseudo-Labeling
   - 一句话总结：CVF OpenAccess paper. Open the paper page for full abstract and method details.
   - 任务设定：医学影像分割/检测，常见弱边界、低对比和标注稀缺问题。
   - 方法核心：几何/深度线索建模，可能补充 RGB 外的结构先验。
   - 实验结论：当前来源只提供标题级信息；需要打开论文页确认数据集、指标和消融。
   - 和我课题的关系：可补充 COD 中纹理、边界、几何先验不足的问题。
   - 可借鉴点：深度或几何先验融合；跨域鲁棒性、不确定性或异常分数。
   - 可改进点：可验证在 COD 跨数据集上的泛化，加入目标缺失场景。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

18. **RAVEN: Radar Adaptive Vision Encoders for Efficient Chirp-wise Object Detection and Segmentation**
   - Source: CVPR 2026, 2026
   - Authors: Anuvab Sen, Mir Sayeed Mohammad, Saibal Mukhopadhyay
   - Tags: computer vision
   - Links: [paper](https://openaccess.thecvf.com/content/CVPR2026/html/Sen_RAVEN_Radar_Adaptive_Vision_Encoders_for_Efficient_Chirp-wise_Object_Detection_CVPR_2026_paper.html) / [pdf](https://openaccess.thecvf.com/content/CVPR2026/papers/Sen_RAVEN_Radar_Adaptive_Vision_Encoders_for_Efficient_Chirp-wise_Object_Detection_CVPR_2026_paper.pdf)
   - 论文：RAVEN: Radar Adaptive Vision Encoders for Efficient Chirp-wise Object Detection and Segmentation
   - 一句话总结：CVF OpenAccess paper. Open the paper page for full abstract and method details.
   - 任务设定：通用计算机视觉任务，先判断是否能迁移到 COD 的感知、定位或分割环节。
   - 方法核心：摘要层面未显示明确模块，建议先看方法图确认 backbone、监督信号和损失设计。
   - 实验结论：当前来源只提供标题级信息；需要打开论文页确认数据集、指标和消融。
   - 和我课题的关系：不是 COD 直系论文，但可能提供可迁移的视觉表征、训练策略或评测思路。
   - 可借鉴点：任务建模、损失函数、消融组织方式。
   - 可改进点：可思考是否缺少 COD 场景验证、复杂背景失败分析或轻量化部署。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

19. **Hierarchical Point-Patch Fusion with Adaptive Patch Codebook for 3D Shape Anomaly Detection**
   - Source: CVPR 2026, 2026
   - Authors: Xueyang Kang, Zizhao Li, Tian Lan, Dong Gong, Kourosh Khoshelham et al.
   - Tags: depth/geometry, anomaly/OOD
   - Links: [paper](https://openaccess.thecvf.com/content/CVPR2026/html/Kang_Hierarchical_Point-Patch_Fusion_with_Adaptive_Patch_Codebook_for_3D_Shape_CVPR_2026_paper.html) / [pdf](https://openaccess.thecvf.com/content/CVPR2026/papers/Kang_Hierarchical_Point-Patch_Fusion_with_Adaptive_Patch_Codebook_for_3D_Shape_CVPR_2026_paper.pdf)
   - 论文：Hierarchical Point-Patch Fusion with Adaptive Patch Codebook for 3D Shape Anomaly Detection
   - 一句话总结：CVF OpenAccess paper. Open the paper page for full abstract and method details.
   - 任务设定：异常检测或分布外识别，可类比伪装目标的弱异常发现。
   - 方法核心：几何/深度线索建模，可能补充 RGB 外的结构先验。
   - 实验结论：当前来源只提供标题级信息；需要打开论文页确认数据集、指标和消融。
   - 和我课题的关系：可补充 COD 中纹理、边界、几何先验不足的问题。
   - 可借鉴点：深度或几何先验融合；跨域鲁棒性、不确定性或异常分数。
   - 可改进点：可思考是否缺少 COD 场景验证、复杂背景失败分析或轻量化部署。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

20. **HyPiDecoder: Hybrid Pixel Decoder for Efficient Segmentation and Detection**
   - Source: ICCV 2025, 2025
   - Authors: Fengzhe Zhou, Humphrey Shi
   - Tags: computer vision
   - Links: [paper](https://openaccess.thecvf.com/content/ICCV2025/html/Zhou_HyPiDecoder_Hybrid_Pixel_Decoder_for_Efficient_Segmentation_and_Detection_ICCV_2025_paper.html) / [pdf](https://openaccess.thecvf.com/content/ICCV2025/papers/Zhou_HyPiDecoder_Hybrid_Pixel_Decoder_for_Efficient_Segmentation_and_Detection_ICCV_2025_paper.pdf)
   - 论文：HyPiDecoder: Hybrid Pixel Decoder for Efficient Segmentation and Detection
   - 一句话总结：CVF OpenAccess paper. Open the paper page for full abstract and method details.
   - 任务设定：通用计算机视觉任务，先判断是否能迁移到 COD 的感知、定位或分割环节。
   - 方法核心：摘要层面未显示明确模块，建议先看方法图确认 backbone、监督信号和损失设计。
   - 实验结论：当前来源只提供标题级信息；需要打开论文页确认数据集、指标和消融。
   - 和我课题的关系：不是 COD 直系论文，但可能提供可迁移的视觉表征、训练策略或评测思路。
   - 可借鉴点：任务建模、损失函数、消融组织方式。
   - 可改进点：可思考是否缺少 COD 场景验证、复杂背景失败分析或轻量化部署。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

21. **Efficient Encoder-Free Fourier-based 3D Large Multimodal Model**
   - Source: CVPR 2026, 2026
   - Authors: Guofeng Mei, Wei Lin, Luigi Riz, Yujiao Wu, Yiming Wang et al.
   - Tags: depth/geometry
   - Links: [paper](https://openaccess.thecvf.com/content/CVPR2026/html/Mei_Efficient_Encoder-Free_Fourier-based_3D_Large_Multimodal_Model_CVPR_2026_paper.html) / [pdf](https://openaccess.thecvf.com/content/CVPR2026/papers/Mei_Efficient_Encoder-Free_Fourier-based_3D_Large_Multimodal_Model_CVPR_2026_paper.pdf)
   - 论文：Efficient Encoder-Free Fourier-based 3D Large Multimodal Model
   - 一句话总结：CVF OpenAccess paper. Open the paper page for full abstract and method details.
   - 任务设定：通用计算机视觉任务，先判断是否能迁移到 COD 的感知、定位或分割环节。
   - 方法核心：视觉-语言对齐，把语义文本信息引入检测或分割。
   - 实验结论：当前来源只提供标题级信息；需要打开论文页确认数据集、指标和消融。
   - 和我课题的关系：可补充 COD 中纹理、边界、几何先验不足的问题。
   - 可借鉴点：深度或几何先验融合。
   - 可改进点：可思考是否缺少 COD 场景验证、复杂背景失败分析或轻量化部署。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

22. **Rethinking Decoder Design: Improving Biomarker Segmentation Using Depth-to-Space Restoration and Residual Linear Attention**
   - Source: CVPR 2025, 2025
   - Authors: Saad Wazir, Daeyoung Kim
   - Tags: depth/geometry, low-level
   - Links: [paper](https://openaccess.thecvf.com/content/CVPR2025/html/Wazir_Rethinking_Decoder_Design_Improving_Biomarker_Segmentation_Using_Depth-to-Space_Restoration_and_CVPR_2025_paper.html) / [pdf](https://openaccess.thecvf.com/content/CVPR2025/papers/Wazir_Rethinking_Decoder_Design_Improving_Biomarker_Segmentation_Using_Depth-to-Space_Restoration_and_CVPR_2025_paper.pdf)
   - 论文：Rethinking Decoder Design: Improving Biomarker Segmentation Using Depth-to-Space Restoration and Residual Linear Attention
   - 一句话总结：CVF OpenAccess paper. Open the paper page for full abstract and method details.
   - 任务设定：通用计算机视觉任务，先判断是否能迁移到 COD 的感知、定位或分割环节。
   - 方法核心：几何/深度线索建模，可能补充 RGB 外的结构先验。
   - 实验结论：当前来源只提供标题级信息；需要打开论文页确认数据集、指标和消融。
   - 和我课题的关系：可补充 COD 中纹理、边界、几何先验不足的问题。
   - 可借鉴点：深度或几何先验融合。
   - 可改进点：可思考是否缺少 COD 场景验证、复杂背景失败分析或轻量化部署。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

23. **EffiDec3D: An Optimized Decoder for High-Performance and Efficient 3D Medical Image Segmentation**
   - Source: CVPR 2025, 2025
   - Authors: Md Mostafijur Rahman, Radu Marculescu
   - Tags: depth/geometry, medical imaging
   - Links: [paper](https://openaccess.thecvf.com/content/CVPR2025/html/Rahman_EffiDec3D_An_Optimized_Decoder_for_High-Performance_and_Efficient_3D_Medical_CVPR_2025_paper.html) / [pdf](https://openaccess.thecvf.com/content/CVPR2025/papers/Rahman_EffiDec3D_An_Optimized_Decoder_for_High-Performance_and_Efficient_3D_Medical_CVPR_2025_paper.pdf)
   - 论文：EffiDec3D: An Optimized Decoder for High-Performance and Efficient 3D Medical Image Segmentation
   - 一句话总结：CVF OpenAccess paper. Open the paper page for full abstract and method details.
   - 任务设定：医学影像分割/检测，常见弱边界、低对比和标注稀缺问题。
   - 方法核心：几何/深度线索建模，可能补充 RGB 外的结构先验。
   - 实验结论：当前来源只提供标题级信息；需要打开论文页确认数据集、指标和消融。
   - 和我课题的关系：可补充 COD 中纹理、边界、几何先验不足的问题。
   - 可借鉴点：深度或几何先验融合。
   - 可改进点：可思考是否缺少 COD 场景验证、复杂背景失败分析或轻量化部署。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

24. **Noise-Resistant Video Anomaly Detection via RGB Error-Guided Multiscale Predictive Coding and Dynamic Memory**
   - Source: CVPR 2025, 2025
   - Authors: Han Hu, Wenli Du, Peng Liao, Bing Wang, Siyuan Fan
   - Tags: video, anomaly/OOD
   - Links: [paper](https://openaccess.thecvf.com/content/CVPR2025/html/Hu_Noise-Resistant_Video_Anomaly_Detection_via_RGB_Error-Guided_Multiscale_Predictive_Coding_CVPR_2025_paper.html) / [pdf](https://openaccess.thecvf.com/content/CVPR2025/papers/Hu_Noise-Resistant_Video_Anomaly_Detection_via_RGB_Error-Guided_Multiscale_Predictive_Coding_CVPR_2025_paper.pdf)
   - 论文：Noise-Resistant Video Anomaly Detection via RGB Error-Guided Multiscale Predictive Coding and Dynamic Memory
   - 一句话总结：CVF OpenAccess paper. Open the paper page for full abstract and method details.
   - 任务设定：异常检测或分布外识别，可类比伪装目标的弱异常发现。
   - 方法核心：异常/OOD 建模，把目标从复杂背景中作为低概率区域凸显出来。
   - 实验结论：当前来源只提供标题级信息；需要打开论文页确认数据集、指标和消融。
   - 和我课题的关系：可把伪装目标看作复杂背景中的弱异常区域来借鉴。
   - 可借鉴点：跨域鲁棒性、不确定性或异常分数。
   - 可改进点：可思考是否缺少 COD 场景验证、复杂背景失败分析或轻量化部署。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

25. **AEROBLADE: Training-Free Detection of Latent Diffusion Images Using Autoencoder Reconstruction Error**
   - Source: CVPR 2024, 2024
   - Authors: Jonas Ricker, Denis Lukovnikov, Asja Fischer
   - Tags: training-free, diffusion
   - Links: [paper](https://openaccess.thecvf.com/content/CVPR2024/html/Ricker_AEROBLADE_Training-Free_Detection_of_Latent_Diffusion_Images_Using_Autoencoder_Reconstruction_CVPR_2024_paper.html) / [pdf](https://openaccess.thecvf.com/content/CVPR2024/papers/Ricker_AEROBLADE_Training-Free_Detection_of_Latent_Diffusion_Images_Using_Autoencoder_Reconstruction_CVPR_2024_paper.pdf)
   - 论文：AEROBLADE: Training-Free Detection of Latent Diffusion Images Using Autoencoder Reconstruction Error
   - 一句话总结：CVF OpenAccess paper. Open the paper page for full abstract and method details.
   - 任务设定：免训练或少训练迁移设定，重点看 prompt、特征选择和后处理。
   - 方法核心：扩散/生成式建模，可能用于数据合成、先验建模或掩码优化。
   - 实验结论：当前来源只提供标题级信息；需要打开论文页确认数据集、指标和消融。
   - 和我课题的关系：适合拓展到开放词汇、零样本或少标注 COD。
   - 可借鉴点：prompt 设计、类别文本构造、免训练迁移流程。
   - 可改进点：可改进 prompt 自动生成、负样本约束和 mask 置信度校准。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

26. **Describe, Adapt and Combine: Empowering CLIP Encoders for Open-set 3D Object Retrieval**
   - Source: ICCV 2025, 2025
   - Authors: Zhichuan Wang, Yang Zhou, Zhe Liu, Rui Yu, Song Bai et al.
   - Tags: retrieval/prototype, depth/geometry
   - Links: [paper](https://openaccess.thecvf.com/content/ICCV2025/html/Wang_Describe_Adapt_and_Combine_Empowering_CLIP_Encoders_for_Open-set_3D_ICCV_2025_paper.html) / [pdf](https://openaccess.thecvf.com/content/ICCV2025/papers/Wang_Describe_Adapt_and_Combine_Empowering_CLIP_Encoders_for_Open-set_3D_ICCV_2025_paper.pdf)
   - 论文：Describe, Adapt and Combine: Empowering CLIP Encoders for Open-set 3D Object Retrieval
   - 一句话总结：CVF OpenAccess paper. Open the paper page for full abstract and method details.
   - 任务设定：通用计算机视觉任务，先判断是否能迁移到 COD 的感知、定位或分割环节。
   - 方法核心：视觉-语言对齐，把语义文本信息引入检测或分割。
   - 实验结论：当前来源只提供标题级信息；需要打开论文页确认数据集、指标和消融。
   - 和我课题的关系：可补充 COD 中纹理、边界、几何先验不足的问题。
   - 可借鉴点：深度或几何先验融合。
   - 可改进点：可思考是否缺少 COD 场景验证、复杂背景失败分析或轻量化部署。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

27. **GeoFormer: Geometry Point Encoder for 3D Object Detection with Graph-based Transformer**
   - Source: ICCV 2025, 2025
   - Authors: Xin Jin, Haisheng Su, Cong Ma, Kai Liu, Wei Wu et al.
   - Tags: depth/geometry
   - Links: [paper](https://openaccess.thecvf.com/content/ICCV2025/html/Jin_GeoFormer_Geometry_Point_Encoder_for_3D_Object_Detection_with_Graph-based_ICCV_2025_paper.html) / [pdf](https://openaccess.thecvf.com/content/ICCV2025/papers/Jin_GeoFormer_Geometry_Point_Encoder_for_3D_Object_Detection_with_Graph-based_ICCV_2025_paper.pdf)
   - 论文：GeoFormer: Geometry Point Encoder for 3D Object Detection with Graph-based Transformer
   - 一句话总结：CVF OpenAccess paper. Open the paper page for full abstract and method details.
   - 任务设定：通用计算机视觉任务，先判断是否能迁移到 COD 的感知、定位或分割环节。
   - 方法核心：几何/深度线索建模，可能补充 RGB 外的结构先验。
   - 实验结论：当前来源只提供标题级信息；需要打开论文页确认数据集、指标和消融。
   - 和我课题的关系：可补充 COD 中纹理、边界、几何先验不足的问题。
   - 可借鉴点：深度或几何先验融合。
   - 可改进点：可思考是否缺少 COD 场景验证、复杂背景失败分析或轻量化部署。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

28. **3D Gaussian Splatting Driven Multi-View Robust Physical Adversarial Camouflage Generation**
   - Source: ICCV 2025, 2025
   - Authors: Tianrui Lou, Xiaojun Jia, Siyuan Liang, Jiawei Liang, Ming Zhang et al.
   - Tags: COD, depth/geometry, remote sensing
   - Links: [paper](https://openaccess.thecvf.com/content/ICCV2025/html/Lou_3D_Gaussian_Splatting_Driven_Multi-View_Robust_Physical_Adversarial_Camouflage_Generation_ICCV_2025_paper.html) / [pdf](https://openaccess.thecvf.com/content/ICCV2025/papers/Lou_3D_Gaussian_Splatting_Driven_Multi-View_Robust_Physical_Adversarial_Camouflage_Generation_ICCV_2025_paper.pdf)
   - 论文：3D Gaussian Splatting Driven Multi-View Robust Physical Adversarial Camouflage Generation
   - 一句话总结：CVF OpenAccess paper. Open the paper page for full abstract and method details.
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：几何/深度线索建模，可能补充 RGB 外的结构先验。
   - 实验结论：当前来源只提供标题级信息；需要打开论文页确认数据集、指标和消融。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；深度或几何先验融合。
   - 可改进点：可尝试引入基础模型、文本先验或更强的环境上下文建模。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

29. **Gradient-Reweighted Adversarial Camouflage for Physical Object Detection Evasion**
   - Source: ICCV 2025, 2025
   - Authors: Jiawei Liang, Siyuan Liang, Tianrui Lou, Ming Zhang, Wenjin Li et al.
   - Tags: COD, remote sensing
   - Links: [paper](https://openaccess.thecvf.com/content/ICCV2025/html/Liang_Gradient-Reweighted_Adversarial_Camouflage_for_Physical_Object_Detection_Evasion_ICCV_2025_paper.html) / [pdf](https://openaccess.thecvf.com/content/ICCV2025/papers/Liang_Gradient-Reweighted_Adversarial_Camouflage_for_Physical_Object_Detection_Evasion_ICCV_2025_paper.pdf)
   - 论文：Gradient-Reweighted Adversarial Camouflage for Physical Object Detection Evasion
   - 一句话总结：CVF OpenAccess paper. Open the paper page for full abstract and method details.
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：摘要层面未显示明确模块，建议先看方法图确认 backbone、监督信号和损失设计。
   - 实验结论：当前来源只提供标题级信息；需要打开论文页确认数据集、指标和消融。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析。
   - 可改进点：可尝试引入基础模型、文本先验或更强的环境上下文建模。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

30. **FE-CLIP: Frequency Enhanced CLIP Model for Zero-Shot Anomaly Detection and Segmentation**
   - Source: ICCV 2025, 2025
   - Authors: Tao Gong, Qi Chu, Bin Liu, Wei Zhou, Nenghai Yu
   - Tags: boundary/frequency, anomaly/OOD
   - Links: [paper](https://openaccess.thecvf.com/content/ICCV2025/html/Gong_FE-CLIP_Frequency_Enhanced_CLIP_Model_for_Zero-Shot_Anomaly_Detection_and_ICCV_2025_paper.html) / [pdf](https://openaccess.thecvf.com/content/ICCV2025/papers/Gong_FE-CLIP_Frequency_Enhanced_CLIP_Model_for_Zero-Shot_Anomaly_Detection_and_ICCV_2025_paper.pdf)
   - 论文：FE-CLIP: Frequency Enhanced CLIP Model for Zero-Shot Anomaly Detection and Segmentation
   - 一句话总结：CVF OpenAccess paper. Open the paper page for full abstract and method details.
   - 任务设定：异常检测或分布外识别，可类比伪装目标的弱异常发现。
   - 方法核心：视觉-语言对齐，把语义文本信息引入检测或分割。
   - 实验结论：当前来源只提供标题级信息；需要打开论文页确认数据集、指标和消融。
   - 和我课题的关系：可补充 COD 中纹理、边界、几何先验不足的问题。
   - 可借鉴点：边界/频域增强模块；跨域鲁棒性、不确定性或异常分数。
   - 可改进点：可结合多尺度语义上下文，避免只强化纹理导致误检。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

## COD / 伪装目标检测相关

1. **Open-Vocabulary Camouflaged Object Segmentation**
   - Source: arXiv, 2023-11-19
   - Authors: Youwei Pang, Xiaoqi Zhao, Jiaming Zuo, Lihe Zhang, Huchuan Lu
   - Tags: COD, open-vocabulary, VLM/MLLM, boundary/frequency, depth/geometry, low-level
   - Links: [paper](http://arxiv.org/abs/2311.11241v3) / [pdf](http://arxiv.org/pdf/2311.11241v3)
   - 论文：Open-Vocabulary Camouflaged Object Segmentation
   - 一句话总结：Recently, the emergence of the large-scale vision-language model (VLM), such as CLIP, has opened the way towards open-world object perception. Many works have explored the utilization of pre-trained VLM for th...
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：视觉-语言对齐，把语义文本信息引入检测或分割。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；prompt 设计、类别文本构造、免训练迁移流程；候选 mask 生成、视觉-语言筛选、推理式定位；边界/频域增强模块；深度或几何先验融合。
   - 可改进点：可改进 prompt 自动生成、负样本约束和 mask 置信度校准。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

2. **Debate-Enhanced Pseudo Labeling and Frequency-Aware Progressive Debiasing for Weakly-Supervised Camouflaged Object Detection with Scribble Annotations**
   - Source: arXiv, 2025-12-23
   - Authors: Jiawei Ge, Jiuxin Cao, Xinyi Li, Xuelin Zhu, Chang Liu et al.
   - Tags: COD, unsupervised, SAM, boundary/frequency
   - Links: [paper](http://arxiv.org/abs/2512.20260v5) / [pdf](http://arxiv.org/pdf/2512.20260v5)
   - 论文：Debate-Enhanced Pseudo Labeling and Frequency-Aware Progressive Debiasing for Weakly-Supervised Camouflaged Object Detection with Scribble Annotations
   - 一句话总结：Weakly-Supervised Camouflaged Object Detection (WSCOD) aims to locate and segment objects that are visually concealed within their surrounding scenes, relying solely on sparse supervision such as scribble anno...
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：借助 SAM/基础分割模型产生候选 mask，再做筛选或适配。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；候选 mask 生成、视觉-语言筛选、推理式定位；边界/频域增强模块。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

3. **SAM3-Adapter: Efficient Adaptation of Segment Anything 3 for Camouflage Object Segmentation, Shadow Detection, and Medical Image Segmentation**
   - Source: arXiv, 2025-11-24
   - Authors: Tianrun Chen, Runlong Cao, Xinda Yu, Lanyun Zhu, Chaotao Ding et al.
   - Tags: COD, SAM, medical imaging
   - Links: [paper](http://arxiv.org/abs/2511.19425v1) / [pdf](http://arxiv.org/pdf/2511.19425v1)
   - 论文：SAM3-Adapter: Efficient Adaptation of Segment Anything 3 for Camouflage Object Segmentation, Shadow Detection, and Medical Image Segmentation
   - 一句话总结：The rapid rise of large-scale foundation models has reshaped the landscape of image segmentation, with models such as Segment Anything achieving unprecedented versatility across diverse vision tasks. However,...
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：借助 SAM/基础分割模型产生候选 mask，再做筛选或适配。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；候选 mask 生成、视觉-语言筛选、推理式定位。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

4. **SAM2-Adapter: Evaluating & Adapting Segment Anything 2 in Downstream Tasks: Camouflage, Shadow, Medical Image Segmentation, and More**
   - Source: arXiv, 2024-08-08
   - Authors: Tianrun Chen, Ankang Lu, Lanyun Zhu, Chaotao Ding, Chunan Yu et al.
   - Tags: COD, SAM, medical imaging
   - Links: [paper](http://arxiv.org/abs/2408.04579v2) / [pdf](http://arxiv.org/pdf/2408.04579v2)
   - 论文：SAM2-Adapter: Evaluating & Adapting Segment Anything 2 in Downstream Tasks: Camouflage, Shadow, Medical Image Segmentation, and More
   - 一句话总结：The advent of large models, also known as foundation models, has significantly transformed the AI research landscape, with models like Segment Anything (SAM) achieving notable success in diverse image segmenta...
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：借助 SAM/基础分割模型产生候选 mask，再做筛选或适配。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；候选 mask 生成、视觉-语言筛选、推理式定位。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

5. **UCOD-DPL: Unsupervised Camouflaged Object Detection via Dynamic Pseudo-label Learning**
   - Source: arXiv, 2025-06-08
   - Authors: Weiqi Yan, Lvhai Chen, Huaijia Kou, Shengchuan Zhang, Yan Zhang et al.
   - Tags: COD, unsupervised, boundary/frequency, remote sensing
   - Links: [paper](http://arxiv.org/abs/2506.07087v1) / [pdf](http://arxiv.org/pdf/2506.07087v1)
   - 论文：UCOD-DPL: Unsupervised Camouflaged Object Detection via Dynamic Pseudo-label Learning
   - 一句话总结：Unsupervised Camoflaged Object Detection (UCOD) has gained attention since it doesn't need to rely on extensive pixel-level labels. Existing UCOD methods typically generate pseudo-labels using fixed strategies...
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：边界感知建模，适合改善伪装目标轮廓不清的问题。
   - 实验结论：摘要未给出强实验信号；先看实验表格和图 1，再决定是否精读。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；边界/频域增强模块。
   - 可改进点：可尝试引入基础模型、文本先验或更强的环境上下文建模。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

6. **High-Resolution Underwater Camouflaged Object Detection: GBU-UCOD Dataset and Topology-Aware and Frequency-Decoupled Networks**
   - Source: arXiv, 2026-02-03
   - Authors: Wenji Wu, Shuo Ye, Yiyu Liu, Jiguang He, Zhuo Wang et al.
   - Tags: COD, diffusion, boundary/frequency, depth/geometry, saliency/transparent
   - Links: [paper](http://arxiv.org/abs/2602.03591v1) / [pdf](http://arxiv.org/pdf/2602.03591v1)
   - 论文：High-Resolution Underwater Camouflaged Object Detection: GBU-UCOD Dataset and Topology-Aware and Frequency-Decoupled Networks
   - 一句话总结：Underwater Camouflaged Object Detection (UCOD) is a challenging task due to the extreme visual similarity between targets and backgrounds across varying marine depths. Existing methods often struggle with topo...
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：借助 SAM/基础分割模型产生候选 mask，再做筛选或适配。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；边界/频域增强模块；深度或几何先验融合。
   - 可改进点：可尝试引入基础模型、文本先验或更强的环境上下文建模。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

7. **EReCu: Pseudo-label Evolution Fusion and Refinement with Multi-Cue Learning for Unsupervised Camouflage Detection**
   - Source: arXiv, 2026-03-12
   - Authors: Shuo Jiang, Gaojia Zhang, Min Tan, Yufei Yin, Gang Pan
   - Tags: COD, unsupervised, diffusion, boundary/frequency, depth/geometry, low-level
   - Links: [paper](http://arxiv.org/abs/2603.11521v1) / [pdf](http://arxiv.org/pdf/2603.11521v1)
   - 论文：EReCu: Pseudo-label Evolution Fusion and Refinement with Multi-Cue Learning for Unsupervised Camouflage Detection
   - 一句话总结：Unsupervised Camouflaged Object Detection (UCOD) remains a challenging task due to the high intrinsic similarity between target objects and their surroundings, as well as the reliance on noisy pseudo-labels th...
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：边界感知建模，适合改善伪装目标轮廓不清的问题。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；边界/频域增强模块；深度或几何先验融合。
   - 可改进点：可尝试引入基础模型、文本先验或更强的环境上下文建模。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

8. **A Survey of Camouflaged Object Detection and Beyond**
   - Source: arXiv, 2024-08-26
   - Authors: Fengyang Xiao, Sujie Hu, Yuqi Shen, Chengyu Fang, Jinfa Huang et al.
   - Tags: COD, diffusion, video
   - Links: [paper](http://arxiv.org/abs/2408.14562v1) / [pdf](http://arxiv.org/pdf/2408.14562v1)
   - 论文：A Survey of Camouflaged Object Detection and Beyond
   - 一句话总结：Camouflaged Object Detection (COD) refers to the task of identifying and segmenting objects that blend seamlessly into their surroundings, posing a significant challenge for computer vision systems. In recent...
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：摘要层面未显示明确模块，建议先看方法图确认 backbone、监督信号和损失设计。
   - 实验结论：可能包含新数据集/基准；适合看评测协议、失败案例和是否能服务 COD。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析。
   - 可改进点：可尝试引入基础模型、文本先验或更强的环境上下文建模。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

9. **Concealed Object Segmentation with Hierarchical Coherence Modeling**
   - Source: arXiv, 2024-01-22
   - Authors: Fengyang Xiao, Pan Zhang, Chunming He, Runze Hu, Yutao Liu
   - Tags: COD, diffusion, saliency/transparent
   - Links: [paper](http://arxiv.org/abs/2401.11767v1) / [pdf](http://arxiv.org/pdf/2401.11767v1)
   - 论文：Concealed Object Segmentation with Hierarchical Coherence Modeling
   - 一句话总结：Concealed object segmentation (COS) is a challenging task that involves localizing and segmenting those concealed objects that are visually blended with their surrounding environments. Despite achieving remark...
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：摘要层面未显示明确模块，建议先看方法图确认 backbone、监督信号和损失设计。
   - 实验结论：摘要未给出强实验信号；先看实验表格和图 1，再决定是否精读。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析。
   - 可改进点：可尝试引入基础模型、文本先验或更强的环境上下文建模。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

10. **First RAG, Second SEG: A Training-Free Paradigm for Camouflaged Object Detection**
   - Source: arXiv, 2025-08-21
   - Authors: Wutao Liu, YiDan Wang, Pan Gao
   - Tags: COD, training-free, unsupervised, SAM, retrieval/prototype, anomaly/OOD, saliency/transparent
   - Links: [paper](http://arxiv.org/abs/2508.15313v2) / [pdf](http://arxiv.org/pdf/2508.15313v2)
   - 论文：First RAG, Second SEG: A Training-Free Paradigm for Camouflaged Object Detection
   - 一句话总结：Camouflaged object detection (COD) poses a significant challenge in computer vision due to the high similarity between objects and their backgrounds. Existing approaches often rely on heavy training and large...
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：提示学习或提示生成，重点看文本/视觉 prompt 如何约束定位。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；prompt 设计、类别文本构造、免训练迁移流程；候选 mask 生成、视觉-语言筛选、推理式定位；跨域鲁棒性、不确定性或异常分数。
   - 可改进点：可改进 prompt 自动生成、负样本约束和 mask 置信度校准。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

11. **ZS-VCOS: Zero-Shot Video Camouflaged Object Segmentation By Optical Flow and Open Vocabulary Object Detection**
   - Source: arXiv, 2025-04-10
   - Authors: Wenqi Guo, Mohamed Shehata, Shan Du
   - Tags: COD, open-vocabulary, unsupervised, SAM, VLM/MLLM, diffusion, video
   - Links: [paper](http://arxiv.org/abs/2505.01431v2) / [pdf](http://arxiv.org/pdf/2505.01431v2)
   - 论文：ZS-VCOS: Zero-Shot Video Camouflaged Object Segmentation By Optical Flow and Open Vocabulary Object Detection
   - 一句话总结：Camouflaged object segmentation presents unique challenges compared to traditional segmentation tasks, primarily due to the high similarity in patterns and colors between camouflaged objects and their backgrou...
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：借助 SAM/基础分割模型产生候选 mask，再做筛选或适配。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；prompt 设计、类别文本构造、免训练迁移流程；候选 mask 生成、视觉-语言筛选、推理式定位。
   - 可改进点：可改进 prompt 自动生成、负样本约束和 mask 置信度校准。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

12. **BED-SAM2: Boundary-Enhanced-Depth SAM2 via Monocular Geometric Priors**
   - Source: arXiv, 2026-05-24
   - Authors: Tyler Rust, Dara McNally, Kyle O'Donnell, Colin Kelly, Chandra Kambhamettu
   - Tags: COD, boundary/frequency, depth/geometry, saliency/transparent
   - Links: [paper](http://arxiv.org/abs/2605.24893v1) / [pdf](http://arxiv.org/pdf/2605.24893v1)
   - 论文：BED-SAM2: Boundary-Enhanced-Depth SAM2 via Monocular Geometric Priors
   - 一句话总结：Building upon the SAM2 vision foundation model for downstream segmentation, this study introduces Boundary Enhanced Depth (BED)-SAM2. The SAM2 Hiera encoder architecture is modified to directly encode monocula...
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：借助 SAM/基础分割模型产生候选 mask，再做筛选或适配。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；边界/频域增强模块；深度或几何先验融合。
   - 可改进点：可尝试引入基础模型、文本先验或更强的环境上下文建模。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

13. **SAM2-UNeXT: An Improved High-Resolution Baseline for Adapting Foundation Models to Downstream Segmentation Tasks**
   - Source: arXiv, 2025-08-05
   - Authors: Xinyu Xiong, Zihuang Wu, Lei Zhang, Lei Lu, Ming Li et al.
   - Tags: COD, SAM, remote sensing, saliency/transparent
   - Links: [paper](http://arxiv.org/abs/2508.03566v1) / [pdf](http://arxiv.org/pdf/2508.03566v1)
   - 论文：SAM2-UNeXT: An Improved High-Resolution Baseline for Adapting Foundation Models to Downstream Segmentation Tasks
   - 一句话总结：Recent studies have highlighted the potential of adapting the Segment Anything Model (SAM) for various downstream tasks. However, constructing a more powerful and generalizable encoder to further enhance perfo...
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：借助 SAM/基础分割模型产生候选 mask，再做筛选或适配。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；候选 mask 生成、视觉-语言筛选、推理式定位。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

14. **COMPrompter: reconceptualized segment anything model with multiprompt network for camouflaged object detection**
   - Source: arXiv, 2024-11-28
   - Authors: Xiaoqin Zhang, Zhenni Yu, Li Zhao, Deng-Ping Fan, Guobao Xiao
   - Tags: COD, SAM, boundary/frequency
   - Links: [paper](http://arxiv.org/abs/2411.18858v1) / [pdf](http://arxiv.org/pdf/2411.18858v1)
   - 论文：COMPrompter: reconceptualized segment anything model with multiprompt network for camouflaged object detection
   - 一句话总结：We rethink the segment anything model (SAM) and propose a novel multiprompt network called COMPrompter for camouflaged object detection (COD). SAM has zero-shot generalization ability beyond other models and c...
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：提示学习或提示生成，重点看文本/视觉 prompt 如何约束定位。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；候选 mask 生成、视觉-语言筛选、推理式定位；边界/频域增强模块。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

15. **Assisted Refinement Network Based on Channel Information Interaction for Camouflaged and Salient Object Detection**
   - Source: arXiv, 2025-12-12
   - Authors: Kuan Wang, Yanjun Qin, Mengge Lu, Liejun Wang, Xiaoming Tao
   - Tags: COD, diffusion, boundary/frequency, low-level, saliency/transparent
   - Links: [paper](http://arxiv.org/abs/2512.11369v1) / [pdf](http://arxiv.org/pdf/2512.11369v1)
   - 论文：Assisted Refinement Network Based on Channel Information Interaction for Camouflaged and Salient Object Detection
   - 一句话总结：Camouflaged Object Detection (COD) stands as a significant challenge in computer vision, dedicated to identifying and segmenting objects visually highly integrated with their backgrounds. Current mainstream me...
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：借助 SAM/基础分割模型产生候选 mask，再做筛选或适配。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；边界/频域增强模块。
   - 可改进点：可尝试引入基础模型、文本先验或更强的环境上下文建模。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

16. **Depth-guided Texture Diffusion for Image Semantic Segmentation**
   - Source: arXiv, 2024-08-17
   - Authors: Wei Sun, Yuan Li, Qixiang Ye, Jianbin Jiao, Yanzhao Zhou
   - Tags: COD, diffusion, boundary/frequency, depth/geometry, saliency/transparent
   - Links: [paper](http://arxiv.org/abs/2408.09097v1) / [pdf](http://arxiv.org/pdf/2408.09097v1)
   - 论文：Depth-guided Texture Diffusion for Image Semantic Segmentation
   - 一句话总结：Depth information provides valuable insights into the 3D structure especially the outline of objects, which can be utilized to improve the semantic segmentation tasks. However, a naive fusion of depth informat...
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：扩散/生成式建模，可能用于数据合成、先验建模或掩码优化。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；边界/频域增强模块；深度或几何先验融合。
   - 可改进点：可尝试引入基础模型、文本先验或更强的环境上下文建模。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

17. **Exploring Deeper! Segment Anything Model with Depth Perception for Camouflaged Object Detection**
   - Source: arXiv, 2024-07-17
   - Authors: Zhenni Yu, Xiaoqin Zhang, Li Zhao, Yi Bin, Guobao Xiao
   - Tags: COD, SAM, boundary/frequency, depth/geometry
   - Links: [paper](http://arxiv.org/abs/2407.12339v1) / [pdf](http://arxiv.org/pdf/2407.12339v1)
   - 论文：Exploring Deeper! Segment Anything Model with Depth Perception for Camouflaged Object Detection
   - 一句话总结：This paper introduces a new Segment Anything Model with Depth Perception (DSAM) for Camouflaged Object Detection (COD). DSAM exploits the zero-shot capability of SAM to realize precise segmentation in the RGB-...
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：提示学习或提示生成，重点看文本/视觉 prompt 如何约束定位。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；候选 mask 生成、视觉-语言筛选、推理式定位；边界/频域增强模块；深度或几何先验融合。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

18. **RIDE: Retinex-Informed Decoupling for Exposing Concealed Objects**
   - Source: arXiv, 2026-05-14
   - Authors: Chunming He, Rihan Zhang, Dingming Zhang, Chengyu Fang, Longxiang Tang et al.
   - Tags: COD, boundary/frequency, saliency/transparent
   - Links: [paper](http://arxiv.org/abs/2605.15450v1) / [pdf](http://arxiv.org/pdf/2605.15450v1)
   - 论文：RIDE: Retinex-Informed Decoupling for Exposing Concealed Objects
   - 一句话总结：Concealed Object Segmentation (COS) encompasses a family of dense-prediction tasks, including camouflaged object detection, polyp segmentation, transparent object detection, and industrial defect inspection, w...
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：借助 SAM/基础分割模型产生候选 mask，再做筛选或适配。
   - 实验结论：摘要未给出强实验信号；先看实验表格和图 1，再决定是否精读。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；边界/频域增强模块。
   - 可改进点：可尝试引入基础模型、文本先验或更强的环境上下文建模。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

19. **FCL-COD: Weakly Supervised Camouflaged Object Detection with Frequency-aware and Contrastive Learning**
   - Source: arXiv, 2026-03-24
   - Authors: Jingchen Ni, Quan Zhang, Dan Jiang, Keyu Lv, Ke Zhang et al.
   - Tags: COD, unsupervised, SAM, diffusion, boundary/frequency
   - Links: [paper](http://arxiv.org/abs/2603.22969v1) / [pdf](http://arxiv.org/pdf/2603.22969v1)
   - 论文：FCL-COD: Weakly Supervised Camouflaged Object Detection with Frequency-aware and Contrastive Learning
   - 一句话总结：Existing camouflage object detection (COD) methods typically rely on fully-supervised learning guided by mask annotations. However, obtaining mask annotations is time-consuming and labor-intensive.
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：借助 SAM/基础分割模型产生候选 mask，再做筛选或适配。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；候选 mask 生成、视觉-语言筛选、推理式定位；边界/频域增强模块。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

20. **When SAM2 Meets Video Camouflaged Object Segmentation: A Comprehensive Evaluation and Adaptation**
   - Source: arXiv, 2024-09-27
   - Authors: Yuli Zhou, Guolei Sun, Yawei Li, Guo-Sen Xie, Luca Benini et al.
   - Tags: COD, SAM, VLM/MLLM, diffusion, video
   - Links: [paper](http://arxiv.org/abs/2409.18653v2) / [pdf](http://arxiv.org/pdf/2409.18653v2)
   - 论文：When SAM2 Meets Video Camouflaged Object Segmentation: A Comprehensive Evaluation and Adaptation
   - 一句话总结：This study investigates the application and performance of the Segment Anything Model 2 (SAM2) in the challenging task of video camouflaged object segmentation (VCOS). VCOS involves detecting objects that blen...
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：提示学习或提示生成，重点看文本/视觉 prompt 如何约束定位。
   - 实验结论：可能包含新数据集/基准；适合看评测协议、失败案例和是否能服务 COD。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；候选 mask 生成、视觉-语言筛选、推理式定位。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

21. **SAM Fails to Segment Anything? -- SAM-Adapter: Adapting SAM in Underperformed Scenes: Camouflage, Shadow, Medical Image Segmentation, and More**
   - Source: arXiv, 2023-04-18
   - Authors: Tianrun Chen, Lanyun Zhu, Chaotao Ding, Runlong Cao, Yan Wang et al.
   - Tags: COD, SAM, boundary/frequency, remote sensing, medical imaging
   - Links: [paper](http://arxiv.org/abs/2304.09148v3) / [pdf](http://arxiv.org/pdf/2304.09148v3)
   - 论文：SAM Fails to Segment Anything? -- SAM-Adapter: Adapting SAM in Underperformed Scenes: Camouflage, Shadow, Medical Image Segmentation, and More
   - 一句话总结：The emergence of large models, also known as foundation models, has brought significant advancements to AI research. One such model is Segment Anything (SAM), which is designed for image segmentation tasks.
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：提示学习或提示生成，重点看文本/视觉 prompt 如何约束定位。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；候选 mask 生成、视觉-语言筛选、推理式定位；边界/频域增强模块。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

22. **C3Net: Context-Contrast Network for Camouflaged Object Detection**
   - Source: arXiv, 2025-11-16
   - Authors: Baber Jan, Aiman H. El-Maleh, Abdul Jabbar Siddiqui, Abdul Bais, Saeed Anwar
   - Tags: COD, diffusion, boundary/frequency, low-level, saliency/transparent
   - Links: [paper](http://arxiv.org/abs/2511.12627v1) / [pdf](http://arxiv.org/pdf/2511.12627v1)
   - 论文：C3Net: Context-Contrast Network for Camouflaged Object Detection
   - 一句话总结：Camouflaged object detection identifies objects that blend seamlessly with their surroundings through similar colors, textures, and patterns. This task challenges both traditional segmentation methods and mode...
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：借助 SAM/基础分割模型产生候选 mask，再做筛选或适配。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；边界/频域增强模块。
   - 可改进点：可尝试引入基础模型、文本先验或更强的环境上下文建模。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

23. **SAM2-UNet: Segment Anything 2 Makes Strong Encoder for Natural and Medical Image Segmentation**
   - Source: arXiv, 2024-08-16
   - Authors: Xinyu Xiong, Zihuang Wu, Shuangyi Tan, Wenxue Li, Feilong Tang et al.
   - Tags: COD, SAM, diffusion, saliency/transparent, medical imaging
   - Links: [paper](http://arxiv.org/abs/2408.08870v1) / [pdf](http://arxiv.org/pdf/2408.08870v1)
   - 论文：SAM2-UNet: Segment Anything 2 Makes Strong Encoder for Natural and Medical Image Segmentation
   - 一句话总结：Image segmentation plays an important role in vision understanding. Recently, the emerging vision foundation models continuously achieved superior performance on various tasks.
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：借助 SAM/基础分割模型产生候选 mask，再做筛选或适配。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；候选 mask 生成、视觉-语言筛选、推理式定位。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

24. **Weakly Supervised Camouflaged Object Detection Based on the SAM Model and Mask Guidance**
   - Source: arXiv, 2026-05-25
   - Authors: Xia Li, Xinran Liu, Lin Qi, Junyu Dong
   - Tags: COD, unsupervised, SAM, boundary/frequency, low-level
   - Links: [paper](http://arxiv.org/abs/2605.25385v1) / [pdf](http://arxiv.org/pdf/2605.25385v1)
   - 论文：Weakly Supervised Camouflaged Object Detection Based on the SAM Model and Mask Guidance
   - 一句话总结：Camouflaged object detection (COD) from a single image is a challenging task due to the high similarity between objects and their surroundings. Existing fully supervised methods require labor-intensive pixel-l...
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：提示学习或提示生成，重点看文本/视觉 prompt 如何约束定位。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；候选 mask 生成、视觉-语言筛选、推理式定位；边界/频域增强模块。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

25. **Exploring Boundary-Aware Spatial-Frequency Fusion for Camouflaged Object Detection**
   - Source: arXiv, 2026-04-20
   - Authors: Song Yu, Yang Hu, Haokang Ding, Zhifang Liao, Yucheng Song
   - Tags: COD, diffusion, boundary/frequency
   - Links: [paper](http://arxiv.org/abs/2604.17879v1) / [pdf](http://arxiv.org/pdf/2604.17879v1)
   - 论文：Exploring Boundary-Aware Spatial-Frequency Fusion for Camouflaged Object Detection
   - 一句话总结：Camouflaged Object Detection is challenging due to the high degree of similarity between camouflaged objects and their surrounding backgrounds. Current COD methods mainly rely on edge extraction in the spatial...
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：频域/纹理特征增强，适合处理伪装背景与目标细粒度差异。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；边界/频域增强模块。
   - 可改进点：可尝试引入基础模型、文本先验或更强的环境上下文建模。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

26. **IP-SAM: Prompt-Space Conditioning for Prompt-Absent Camouflaged Object Detection**
   - Source: arXiv, 2026-03-28
   - Authors: Huiyao Zhang, Jin Bai, Rui Guo, JianWen Tan, HongFei Wang et al.
   - Tags: COD, SAM, diffusion
   - Links: [paper](http://arxiv.org/abs/2603.27250v1) / [pdf](http://arxiv.org/pdf/2603.27250v1)
   - 论文：IP-SAM: Prompt-Space Conditioning for Prompt-Absent Camouflaged Object Detection
   - 一句话总结：Prompt-conditioned foundation segmenters have emerged as a dominant paradigm for image segmentation, where explicit spatial prompts (e.g., points, boxes, masks) guide mask decoding. However, many real-world de...
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：提示学习或提示生成，重点看文本/视觉 prompt 如何约束定位。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；候选 mask 生成、视觉-语言筛选、推理式定位。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

27. **Language-Guided Structure-Aware Network for Camouflaged Object Detection**
   - Source: arXiv, 2026-03-25
   - Authors: Min Zhang
   - Tags: COD, boundary/frequency, low-level
   - Links: [paper](http://arxiv.org/abs/2603.24355v1) / [pdf](http://arxiv.org/pdf/2603.24355v1)
   - 论文：Language-Guided Structure-Aware Network for Camouflaged Object Detection
   - 一句话总结：Camouflaged Object Detection (COD) aims to segment objects that are highly integrated with the background in terms of color, texture, and structure, making it a highly challenging task in computer vision. Alth...
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：提示学习或提示生成，重点看文本/视觉 prompt 如何约束定位。
   - 实验结论：可能包含新数据集/基准；适合看评测协议、失败案例和是否能服务 COD。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；边界/频域增强模块。
   - 可改进点：可尝试引入基础模型、文本先验或更强的环境上下文建模。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

28. **Beyond Single Images: Retrieval Self-Augmented Unsupervised Camouflaged Object Detection**
   - Source: arXiv, 2025-10-21
   - Authors: Ji Du, Xin Wang, Fangwei Hao, Mingyang Yu, Chunyuan Chen et al.
   - Tags: COD, unsupervised, retrieval/prototype
   - Links: [paper](http://arxiv.org/abs/2510.18437v1) / [pdf](http://arxiv.org/pdf/2510.18437v1)
   - 论文：Beyond Single Images: Retrieval Self-Augmented Unsupervised Camouflaged Object Detection
   - 一句话总结：At the core of Camouflaged Object Detection (COD) lies segmenting objects from their highly similar surroundings. Previous efforts navigate this challenge primarily through image-level modeling or annotation-b...
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：提示学习或提示生成，重点看文本/视觉 prompt 如何约束定位。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析。
   - 可改进点：可尝试引入基础模型、文本先验或更强的环境上下文建模。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

29. **HyperCOD: The First Challenging Benchmark and Baseline for Hyperspectral Camouflaged Object Detection**
   - Source: arXiv, 2026-01-07
   - Authors: Shuyan Bai, Tingfa Xu, Peifu Liu, Yuhao Qiu, Huiyan Bai et al.
   - Tags: COD, SAM, remote sensing, saliency/transparent
   - Links: [paper](http://arxiv.org/abs/2601.03736v1) / [pdf](http://arxiv.org/pdf/2601.03736v1)
   - 论文：HyperCOD: The First Challenging Benchmark and Baseline for Hyperspectral Camouflaged Object Detection
   - 一句话总结：RGB-based camouflaged object detection struggles in real-world scenarios where color and texture cues are ambiguous. While hyperspectral image offers a powerful alternative by capturing fine-grained spectral s...
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：提示学习或提示生成，重点看文本/视觉 prompt 如何约束定位。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；候选 mask 生成、视觉-语言筛选、推理式定位。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

30. **DGA-Net: Enhancing SAM with Depth Prompting and Graph-Anchor Guidance for Camouflaged Object Detection**
   - Source: arXiv, 2026-01-06
   - Authors: Yuetong Li, Qing Zhang, Yilin Zhao, Gongyang Li, Zeming Liu
   - Tags: COD, SAM, depth/geometry, low-level
   - Links: [paper](http://arxiv.org/abs/2601.02831v1) / [pdf](http://arxiv.org/pdf/2601.02831v1)
   - 论文：DGA-Net: Enhancing SAM with Depth Prompting and Graph-Anchor Guidance for Camouflaged Object Detection
   - 一句话总结：To fully exploit depth cues in Camouflaged Object Detection (COD), we present DGA-Net, a specialized framework that adapts the Segment Anything Model (SAM) via a novel ``depth prompting" paradigm. Distinguishe...
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：提示学习或提示生成，重点看文本/视觉 prompt 如何约束定位。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；候选 mask 生成、视觉-语言筛选、推理式定位；深度或几何先验融合。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

31. **Phantom-Insight: Adaptive Multi-cue Fusion for Video Camouflaged Object Detection with Multimodal LLM**
   - Source: arXiv, 2025-09-08
   - Authors: Hua Zhang, Changjiang Luo, Ruoyu Chen
   - Tags: COD, SAM, VLM/MLLM, diffusion, boundary/frequency, video
   - Links: [paper](http://arxiv.org/abs/2509.06422v1) / [pdf](http://arxiv.org/pdf/2509.06422v1)
   - 论文：Phantom-Insight: Adaptive Multi-cue Fusion for Video Camouflaged Object Detection with Multimodal LLM
   - 一句话总结：Video camouflaged object detection (VCOD) is challenging due to dynamic environments. Existing methods face two main issues: (1) SAM-based methods struggle to separate camouflaged object edges due to model fre...
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：提示学习或提示生成，重点看文本/视觉 prompt 如何约束定位。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；候选 mask 生成、视觉-语言筛选、推理式定位；边界/频域增强模块。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

32. **Improving SAM for Camouflaged Object Detection via Dual Stream Adapters**
   - Source: arXiv, 2025-03-08
   - Authors: Jiaming Liu, Linghe Kong, Guihai Chen
   - Tags: COD, SAM, diffusion, boundary/frequency, depth/geometry
   - Links: [paper](http://arxiv.org/abs/2503.06042v2) / [pdf](http://arxiv.org/pdf/2503.06042v2)
   - 论文：Improving SAM for Camouflaged Object Detection via Dual Stream Adapters
   - 一句话总结：Segment anything model (SAM) has shown impressive general-purpose segmentation performance on natural images, but its performance on camouflaged object detection (COD) is unsatisfactory. In this paper, we prop...
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：提示学习或提示生成，重点看文本/视觉 prompt 如何约束定位。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；候选 mask 生成、视觉-语言筛选、推理式定位；边界/频域增强模块；深度或几何先验融合。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

33. **Refining Context-Entangled Content Segmentation via Curriculum Selection and Anti-Curriculum Promotion**
   - Source: arXiv, 2026-02-01
   - Authors: Chunming He, Rihan Zhang, Fengyang Xiao, Dingming Zhang, Zhiwen Cao et al.
   - Tags: COD, boundary/frequency, video, low-level
   - Links: [paper](http://arxiv.org/abs/2602.01183v2) / [pdf](http://arxiv.org/pdf/2602.01183v2)
   - 论文：Refining Context-Entangled Content Segmentation via Curriculum Selection and Anti-Curriculum Promotion
   - 一句话总结：Biological learning proceeds from easy to difficult tasks, gradually reinforcing perception and robustness. Inspired by this principle, we address Context-Entangled Content Segmentation (CECS), a challenging s...
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：借助 SAM/基础分割模型产生候选 mask，再做筛选或适配。
   - 实验结论：可能包含新数据集/基准；适合看评测协议、失败案例和是否能服务 COD。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；边界/频域增强模块。
   - 可改进点：可尝试引入基础模型、文本先验或更强的环境上下文建模。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

34. **Exploring Depth Contribution for Camouflaged Object Detection**
   - Source: arXiv, 2021-06-24
   - Authors: Mochu Xiang, Jing Zhang, Yunqiu Lv, Aixuan Li, Yiran Zhong et al.
   - Tags: COD, diffusion, depth/geometry, remote sensing
   - Links: [paper](http://arxiv.org/abs/2106.13217v3) / [pdf](http://arxiv.org/pdf/2106.13217v3)
   - 论文：Exploring Depth Contribution for Camouflaged Object Detection
   - 一句话总结：Camouflaged object detection (COD) aims to segment camouflaged objects hiding in the environment, which is challenging due to the similar appearance of camouflaged objects and their surroundings. Research in b...
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：扩散/生成式建模，可能用于数据合成、先验建模或掩码优化。
   - 实验结论：可能包含新数据集/基准；适合看评测协议、失败案例和是否能服务 COD。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；深度或几何先验融合。
   - 可改进点：可尝试引入基础模型、文本先验或更强的环境上下文建模。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

35. **FakeMix Augmentation Improves Transparent Object Detection**
   - Source: arXiv, 2021-03-24
   - Authors: Yang Cao, Zhengqiang Zhang, Enze Xie, Qibin Hou, Kai Zhao et al.
   - Tags: COD, boundary/frequency, saliency/transparent
   - Links: [paper](http://arxiv.org/abs/2103.13279v2) / [pdf](http://arxiv.org/pdf/2103.13279v2)
   - 论文：FakeMix Augmentation Improves Transparent Object Detection
   - 一句话总结：Detecting transparent objects in natural scenes is challenging due to the low contrast in texture, brightness and colors. Recent deep-learning-based works reveal that it is effective to leverage boundaries for...
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：借助 SAM/基础分割模型产生候选 mask，再做筛选或适配。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；边界/频域增强模块。
   - 可改进点：可尝试引入基础模型、文本先验或更强的环境上下文建模。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

## 泛计算机视觉方法池

1. **Video Object Segmentation-Aware Audio Generation**
   - Source: Crossref / IJCV / CCF-A / 顶刊 / International Journal of Computer Vision, 2026-06-23
   - Authors: Ilpo Viertola, Vladimir Iashin, Esa Rahtu
   - Tags: diffusion, video, remote sensing
   - Links: [paper](https://doi.org/10.1007/s11263-026-02911-2)
   - 论文：Video Object Segmentation-Aware Audio Generation
   - 一句话总结：Abstract Existing multimodal audio generation models often lack precise user control, which limits their applicability in professional Foley workflows. In particular, these models focus on the entire video and...
   - 任务设定：遥感/大场景密集视觉任务，关注小目标、尺度变化和复杂背景。
   - 方法核心：扩散/生成式建模，可能用于数据合成、先验建模或掩码优化。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：不是 COD 直系论文，但可能提供可迁移的视觉表征、训练策略或评测思路。
   - 可借鉴点：任务建模、损失函数、消融组织方式。
   - 可改进点：可思考是否缺少 COD 场景验证、复杂背景失败分析或轻量化部署。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

2. **SegRAG: Training-Free Retrieval-Augmented Semantic Segmentation**
   - Source: arXiv, 2026-05-17
   - Authors: Abderrahmene Boudiaf, Irfan Hussain, Sajid Javed
   - Tags: open-vocabulary, training-free, reasoning, retrieval/prototype
   - Links: [paper](http://arxiv.org/abs/2605.17630v2) / [pdf](http://arxiv.org/pdf/2605.17630v2)
   - 论文：SegRAG: Training-Free Retrieval-Augmented Semantic Segmentation
   - 一句话总结：Open-vocabulary segmentation models such as SAM3 perform well across broad categories via text prompting, yet degrade when target classes are visually underrepresented in pretraining or depart from canonical d...
   - 任务设定：开放词汇视觉识别/分割，目标类别或文本提示在训练时未必出现。
   - 方法核心：提示学习或提示生成，重点看文本/视觉 prompt 如何约束定位。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：适合拓展到开放词汇、零样本或少标注 COD。
   - 可借鉴点：prompt 设计、类别文本构造、免训练迁移流程。
   - 可改进点：可改进 prompt 自动生成、负样本约束和 mask 置信度校准。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

3. **OVS-DINO: Open-Vocabulary Segmentation via Structure-Aligned SAM-DINO with Language Guidance**
   - Source: arXiv, 2026-04-09
   - Authors: Haoxi Zeng, Qiankun Liu, Yi Bin, Haiyue Zhang, Yujuan Ding et al.
   - Tags: open-vocabulary, unsupervised, SAM, boundary/frequency, remote sensing
   - Links: [paper](http://arxiv.org/abs/2604.08461v1) / [pdf](http://arxiv.org/pdf/2604.08461v1)
   - 论文：OVS-DINO: Open-Vocabulary Segmentation via Structure-Aligned SAM-DINO with Language Guidance
   - 一句话总结：Open-Vocabulary Segmentation (OVS) aims to segment image regions beyond predefined category sets by leveraging semantic descriptions. While CLIP based approaches excel in semantic generalization, they frequent...
   - 任务设定：开放词汇视觉识别/分割，目标类别或文本提示在训练时未必出现。
   - 方法核心：借助 SAM/基础分割模型产生候选 mask，再做筛选或适配。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：适合拓展到开放词汇、零样本或少标注 COD。
   - 可借鉴点：prompt 设计、类别文本构造、免训练迁移流程；候选 mask 生成、视觉-语言筛选、推理式定位；边界/频域增强模块。
   - 可改进点：可改进 prompt 自动生成、负样本约束和 mask 置信度校准。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

4. **SegEarth-OV: Towards Training-Free Open-Vocabulary Segmentation for Remote Sensing Images**
   - Source: arXiv, 2024-10-02
   - Authors: Kaiyu Li, Ruixun Liu, Xiangyong Cao, Xueru Bai, Feng Zhou et al.
   - Tags: open-vocabulary, training-free, remote sensing, anomaly/OOD
   - Links: [paper](http://arxiv.org/abs/2410.01768v2) / [pdf](http://arxiv.org/pdf/2410.01768v2)
   - 论文：SegEarth-OV: Towards Training-Free Open-Vocabulary Segmentation for Remote Sensing Images
   - 一句话总结：Remote sensing image plays an irreplaceable role in fields such as agriculture, water resources, military, and disaster relief. Pixel-level interpretation is a critical aspect of remote sensing image applicati...
   - 任务设定：开放词汇视觉识别/分割，目标类别或文本提示在训练时未必出现。
   - 方法核心：借助 SAM/基础分割模型产生候选 mask，再做筛选或适配。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：适合拓展到开放词汇、零样本或少标注 COD。
   - 可借鉴点：prompt 设计、类别文本构造、免训练迁移流程；跨域鲁棒性、不确定性或异常分数。
   - 可改进点：可改进 prompt 自动生成、负样本约束和 mask 置信度校准。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

5. **TF-SSD: A Strong Pipeline via Synergic Mask Filter for Training-free Co-salient Object Detection**
   - Source: arXiv, 2026-04-01
   - Authors: Zhijin He, Shuo Jin, Siyue Yu, Shuwei Wu, Bingfeng Zhang et al.
   - Tags: training-free, SAM, retrieval/prototype, saliency/transparent
   - Links: [paper](http://arxiv.org/abs/2604.00549v1) / [pdf](http://arxiv.org/pdf/2604.00549v1)
   - 论文：TF-SSD: A Strong Pipeline via Synergic Mask Filter for Training-free Co-salient Object Detection
   - 一句话总结：Co-salient Object Detection (CoSOD) aims to segment salient objects that consistently appear across a group of related images. Despite the notable progress achieved by recent training-based approaches, they st...
   - 任务设定：免训练或少训练迁移设定，重点看 prompt、特征选择和后处理。
   - 方法核心：借助 SAM/基础分割模型产生候选 mask，再做筛选或适配。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：和 COD 同属低显著/弱边界目标发现，可迁移目标-背景分离思想。
   - 可借鉴点：prompt 设计、类别文本构造、免训练迁移流程；候选 mask 生成、视觉-语言筛选、推理式定位。
   - 可改进点：可改进 prompt 自动生成、负样本约束和 mask 置信度校准。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

6. **Understanding How MLLMs Describe Artworks Using Token Activation Maps**
   - Source: arXiv, 2026-06-26
   - Authors: Nicola Fanelli, Pasquale De Marinis, Raffaele Scaringi, Eva Cetinic, Gennaro Vessio et al.
   - Tags: open-vocabulary, SAM, VLM/MLLM, reasoning
   - Links: [paper](http://arxiv.org/abs/2606.27947v1) / [pdf](http://arxiv.org/pdf/2606.27947v1)
   - 论文：Understanding How MLLMs Describe Artworks Using Token Activation Maps
   - 一句话总结：Multimodal Large Language Models (MLLMs) describe artworks with remarkable fluency, yet the visual reasoning behind their outputs remains opaque. When an MLLM names a style, identifies a subject, or recognizes...
   - 任务设定：开放词汇视觉识别/分割，目标类别或文本提示在训练时未必出现。
   - 方法核心：提示学习或提示生成，重点看文本/视觉 prompt 如何约束定位。
   - 实验结论：摘要未给出强实验信号；先看实验表格和图 1，再决定是否精读。
   - 和我课题的关系：适合拓展到开放词汇、零样本或少标注 COD。
   - 可借鉴点：prompt 设计、类别文本构造、免训练迁移流程；候选 mask 生成、视觉-语言筛选、推理式定位。
   - 可改进点：可改进 prompt 自动生成、负样本约束和 mask 置信度校准。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

7. **Anatomy-Guided Residual Motion Diffusion for Controllable 4D Cardiac MRI Synthesis**
   - Source: arXiv, 2026-06-25
   - Authors: Yiheng Cao, Gustavo Andrade-Miranda, Jiatian Zhang, Lingxiao Zhao, Xin Gao
   - Tags: unsupervised, diffusion, boundary/frequency, depth/geometry, video, medical imaging
   - Links: [paper](http://arxiv.org/abs/2606.26764v1) / [pdf](http://arxiv.org/pdf/2606.26764v1)
   - 论文：Anatomy-Guided Residual Motion Diffusion for Controllable 4D Cardiac MRI Synthesis
   - 一句话总结：Developing robust artificial intelligence models for 4D (3D + time) medical imaging is constrained by limited annotated data, inter-device domain shifts, and privacy restrictions. To address this, we propose a...
   - 任务设定：医学影像分割/检测，常见弱边界、低对比和标注稀缺问题。
   - 方法核心：扩散/生成式建模，可能用于数据合成、先验建模或掩码优化。
   - 实验结论：可能包含新数据集/基准；适合看评测协议、失败案例和是否能服务 COD。
   - 和我课题的关系：可补充 COD 中纹理、边界、几何先验不足的问题。
   - 可借鉴点：边界/频域增强模块；深度或几何先验融合。
   - 可改进点：可结合多尺度语义上下文，避免只强化纹理导致误检。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

8. **M$^4$-SAM: Multi-Modal Mixture-of-Experts with Memory-Augmented SAM for RGB-D Video Salient Object Detection**
   - Source: arXiv, 2026-05-12
   - Authors: Jiyuan Liu, Jia Lin, Xiaofei Zhou, Runmin Cong, Deyang Liu et al.
   - Tags: SAM, retrieval/prototype, video, saliency/transparent
   - Links: [paper](http://arxiv.org/abs/2605.11760v1) / [pdf](http://arxiv.org/pdf/2605.11760v1)
   - 论文：M$^4$-SAM: Multi-Modal Mixture-of-Experts with Memory-Augmented SAM for RGB-D Video Salient Object Detection
   - 一句话总结：The Segment Anything Model 2 (SAM2) has emerged as a foundation model for universal segmentation. Owing to its generalizable visual representations, SAM2 has been successfully applied to various downstream tas...
   - 任务设定：基础模型驱动的视觉定位/分割/推理，可用于自动提示生成或 mask 筛选。
   - 方法核心：提示学习或提示生成，重点看文本/视觉 prompt 如何约束定位。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：和 COD 同属低显著/弱边界目标发现，可迁移目标-背景分离思想。
   - 可借鉴点：候选 mask 生成、视觉-语言筛选、推理式定位。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

9. **SOCO: Benchmarking Semantic Object Correspondence in Vision Foundation Models**
   - Source: arXiv, 2026-05-29
   - Authors: Olaf Dünkel, Basavaraj Sunagad, Haoran Wang, David T. Hoffmann, Christian Theobalt et al.
   - Tags: VLM/MLLM, diffusion, depth/geometry, video
   - Links: [paper](http://arxiv.org/abs/2605.31597v2) / [pdf](http://arxiv.org/pdf/2605.31597v2)
   - 论文：SOCO: Benchmarking Semantic Object Correspondence in Vision Foundation Models
   - 一句话总结：Measuring structured object understanding in vision foundation models remains challenging due to inconsistent evaluation protocols and limited part-level supervision. Semantic correspondence (SC) evaluates thi...
   - 任务设定：基础模型驱动的视觉定位/分割/推理，可用于自动提示生成或 mask 筛选。
   - 方法核心：提示学习或提示生成，重点看文本/视觉 prompt 如何约束定位。
   - 实验结论：可能包含新数据集/基准；适合看评测协议、失败案例和是否能服务 COD。
   - 和我课题的关系：可补充 COD 中纹理、边界、几何先验不足的问题。
   - 可借鉴点：候选 mask 生成、视觉-语言筛选、推理式定位；深度或几何先验融合。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

10. **VesselSim: learning 3D blood vessel segmentation without expert annotations**
   - Source: arXiv, 2026-05-25
   - Authors: Erin Rainville, Melissa Ananian, Tristan Mirolla, Hassan Rivaz, Yiming Xiao
   - Tags: boundary/frequency, depth/geometry, anomaly/OOD, domain adaptation, medical imaging
   - Links: [paper](http://arxiv.org/abs/2605.26277v2) / [pdf](http://arxiv.org/pdf/2605.26277v2)
   - 论文：VesselSim: learning 3D blood vessel segmentation without expert annotations
   - 一句话总结：Blood vessel segmentation is a core task in medical image analysis for the care of vascular diseases and surgical planning, yet the challenges of providing expert vascular annotations pose a major obstacle for...
   - 任务设定：异常检测或分布外识别，可类比伪装目标的弱异常发现。
   - 方法核心：边界感知建模，适合改善伪装目标轮廓不清的问题。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：可补充 COD 中纹理、边界、几何先验不足的问题。
   - 可借鉴点：边界/频域增强模块；深度或几何先验融合；跨域鲁棒性、不确定性或异常分数。
   - 可改进点：可结合多尺度语义上下文，避免只强化纹理导致误检。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

11. **MM-OVSeg:Multimodal Optical-SAR Fusion for Open-Vocabulary Segmentation in Remote Sensing**
   - Source: arXiv, 2026-03-18
   - Authors: Yimin Wei, Aoran Xiao, Hongruixuan Chen, Junshi Xia, Naoto Yokoya
   - Tags: open-vocabulary, VLM/MLLM, diffusion, remote sensing
   - Links: [paper](http://arxiv.org/abs/2603.17528v2) / [pdf](http://arxiv.org/pdf/2603.17528v2)
   - 论文：MM-OVSeg:Multimodal Optical-SAR Fusion for Open-Vocabulary Segmentation in Remote Sensing
   - 一句话总结：Open-vocabulary segmentation enables pixel-level recognition from an open set of textual categories, allowing generalization beyond fixed classes. Despite great potential in remote sensing, progress in this ar...
   - 任务设定：开放词汇视觉识别/分割，目标类别或文本提示在训练时未必出现。
   - 方法核心：视觉-语言对齐，把语义文本信息引入检测或分割。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：适合拓展到开放词汇、零样本或少标注 COD。
   - 可借鉴点：prompt 设计、类别文本构造、免训练迁移流程；候选 mask 生成、视觉-语言筛选、推理式定位。
   - 可改进点：可改进 prompt 自动生成、负样本约束和 mask 置信度校准。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

12. **ActiveSAM: Image-Conditional Class Pruning for Fast and Accurate Open-Vocabulary Segmentation**
   - Source: arXiv, 2026-06-15
   - Authors: Tran Dinh Tien, Zhiqiang Shen
   - Tags: open-vocabulary, training-free, SAM, diffusion, remote sensing
   - Links: [paper](http://arxiv.org/abs/2606.16996v1) / [pdf](http://arxiv.org/pdf/2606.16996v1)
   - 论文：ActiveSAM: Image-Conditional Class Pruning for Fast and Accurate Open-Vocabulary Segmentation
   - 一句话总结：Segment Anything Model 3 (SAM 3) provides a strong frozen backbone for concept-prompted segmentation, but applying it directly to open-vocabulary semantic segmentation (OVSS) is inefficient: full-resolution de...
   - 任务设定：开放词汇视觉识别/分割，目标类别或文本提示在训练时未必出现。
   - 方法核心：提示学习或提示生成，重点看文本/视觉 prompt 如何约束定位。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：适合拓展到开放词汇、零样本或少标注 COD。
   - 可借鉴点：prompt 设计、类别文本构造、免训练迁移流程；候选 mask 生成、视觉-语言筛选、推理式定位。
   - 可改进点：可改进 prompt 自动生成、负样本约束和 mask 置信度校准。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

13. **Vision-Language Model Reasoning for Contextual Semantic Mapping in Intralogistics**
   - Source: arXiv, 2026-06-23
   - Authors: Marvin Rüdt, Hao Pang, Constantin Enke, Zäzilia Seibold, Kai Furmans
   - Tags: open-vocabulary, SAM, VLM/MLLM, reasoning, depth/geometry
   - Links: [paper](http://arxiv.org/abs/2606.24814v1) / [pdf](http://arxiv.org/pdf/2606.24814v1)
   - 论文：Vision-Language Model Reasoning for Contextual Semantic Mapping in Intralogistics
   - 一句话总结：Autonomous mobile robots operating in intralogistics environments rely on geometric maps for localization and navigation, but lack semantic understanding of objects and their contextual properties. We present...
   - 任务设定：开放词汇视觉识别/分割，目标类别或文本提示在训练时未必出现。
   - 方法核心：提示学习或提示生成，重点看文本/视觉 prompt 如何约束定位。
   - 实验结论：摘要强调消融、鲁棒性或泛化；适合优先看实验设计和跨域表现。
   - 和我课题的关系：适合拓展到开放词汇、零样本或少标注 COD。
   - 可借鉴点：prompt 设计、类别文本构造、免训练迁移流程；候选 mask 生成、视觉-语言筛选、推理式定位；深度或几何先验融合。
   - 可改进点：可改进 prompt 自动生成、负样本约束和 mask 置信度校准。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

14. **Jolia: Concept-Level Vision-Language Alignment for 3D CT Contrastive Learning**
   - Source: arXiv, 2026-06-23
   - Authors: Julien Khlaut, Charles Corbière, Baptiste Callard, Amaury Prat, Leo Butsanets et al.
   - Tags: VLM/MLLM, depth/geometry, medical imaging
   - Links: [paper](http://arxiv.org/abs/2606.24570v2) / [pdf](http://arxiv.org/pdf/2606.24570v2)
   - 论文：Jolia: Concept-Level Vision-Language Alignment for 3D CT Contrastive Learning
   - 一句话总结：Vision-language contrastive pretraining has become the dominant recipe for 3D medical foundation models, leveraging the large volumes of paired scans and reports produced in clinical practice. However, medical...
   - 任务设定：基础模型驱动的视觉定位/分割/推理，可用于自动提示生成或 mask 筛选。
   - 方法核心：视觉-语言对齐，把语义文本信息引入检测或分割。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：可补充 COD 中纹理、边界、几何先验不足的问题。
   - 可借鉴点：候选 mask 生成、视觉-语言筛选、推理式定位；深度或几何先验融合。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

15. **ARTEMIS: Agent-guided Reliability-aware Temporal Mask Evolution for Imperfectly Supervised Video Polyp Segmentation**
   - Source: arXiv, 2026-06-18
   - Authors: Tong Wang, Siwen Wang, Yaolei Qi, Jinxing Zhou, Yuting He et al.
   - Tags: VLM/MLLM, retrieval/prototype, boundary/frequency, depth/geometry, video
   - Links: [paper](http://arxiv.org/abs/2606.20161v1) / [pdf](http://arxiv.org/pdf/2606.20161v1)
   - 论文：ARTEMIS: Agent-guided Reliability-aware Temporal Mask Evolution for Imperfectly Supervised Video Polyp Segmentation
   - 一句话总结：Imperfectly supervised video polyp segmentation (VPS) aims to learn dense, temporally consistent masks from inexpensive supervision, including weak annotations (points, scribbles) and semi-supervision with few...
   - 任务设定：基础模型驱动的视觉定位/分割/推理，可用于自动提示生成或 mask 筛选。
   - 方法核心：借助 SAM/基础分割模型产生候选 mask，再做筛选或适配。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：可补充 COD 中纹理、边界、几何先验不足的问题。
   - 可借鉴点：候选 mask 生成、视觉-语言筛选、推理式定位；边界/频域增强模块；深度或几何先验融合。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

16. **Training-free Cross-domain Few-shot Segmentation via Robust Semantic Representation and Matching**
   - Source: arXiv, 2026-06-23
   - Authors: Sujun Sun, Mingwu Ren, Haofeng Zhang
   - Tags: training-free, diffusion, retrieval/prototype, boundary/frequency, low-level
   - Links: [paper](http://arxiv.org/abs/2606.24297v1) / [pdf](http://arxiv.org/pdf/2606.24297v1)
   - 论文：Training-free Cross-domain Few-shot Segmentation via Robust Semantic Representation and Matching
   - 一句话总结：Cross-domain Few-shot Segmentation (CD-FSS) aims to transfer knowledge learned from source domain to distinct target domains, segmenting unseen target classes with only a few annotated samples. Although existi...
   - 任务设定：免训练或少训练迁移设定，重点看 prompt、特征选择和后处理。
   - 方法核心：借助 SAM/基础分割模型产生候选 mask，再做筛选或适配。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：适合拓展到开放词汇、零样本或少标注 COD。
   - 可借鉴点：prompt 设计、类别文本构造、免训练迁移流程；边界/频域增强模块。
   - 可改进点：可改进 prompt 自动生成、负样本约束和 mask 置信度校准。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

17. **SWARD: Stochastic Window-Attention-Based Relational Distillation for Cross-Architectural Semantic Segmentation**
   - Source: arXiv, 2026-05-31
   - Authors: Aditya Makineni, Qing Tian
   - Tags: retrieval/prototype, boundary/frequency, medical imaging
   - Links: [paper](http://arxiv.org/abs/2606.00999v1) / [pdf](http://arxiv.org/pdf/2606.00999v1)
   - 论文：SWARD: Stochastic Window-Attention-Based Relational Distillation for Cross-Architectural Semantic Segmentation
   - 一句话总结：Large-scale vision foundation models have driven substantial gains on dense prediction tasks such as semantic segmentation, but their size makes deployment impractical in resource-constrained settings, motivat...
   - 任务设定：医学影像分割/检测，常见弱边界、低对比和标注稀缺问题。
   - 方法核心：借助 SAM/基础分割模型产生候选 mask，再做筛选或适配。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：可补充 COD 中纹理、边界、几何先验不足的问题。
   - 可借鉴点：边界/频域增强模块。
   - 可改进点：可结合多尺度语义上下文，避免只强化纹理导致误检。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

18. **Controllable Histopathology Image Synthesis with Training-free Structural Initialization and Textural Modulation**
   - Source: arXiv, 2026-06-26
   - Authors: Yuheng Qiu, Jingyi Luo, Chenfei Ye, Ting Ma, Jianfeng Cao
   - Tags: training-free, diffusion, boundary/frequency, medical imaging
   - Links: [paper](http://arxiv.org/abs/2606.27935v1) / [pdf](http://arxiv.org/pdf/2606.27935v1)
   - 论文：Controllable Histopathology Image Synthesis with Training-free Structural Initialization and Textural Modulation
   - 一句话总结：Deep learning has demonstrated remarkable success in high-throughput histopathology image analysis. However, the performance of learning-based models critically depends on the quality and size of annotations b...
   - 任务设定：免训练或少训练迁移设定，重点看 prompt、特征选择和后处理。
   - 方法核心：扩散/生成式建模，可能用于数据合成、先验建模或掩码优化。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：适合拓展到开放词汇、零样本或少标注 COD。
   - 可借鉴点：prompt 设计、类别文本构造、免训练迁移流程；边界/频域增强模块。
   - 可改进点：可改进 prompt 自动生成、负样本约束和 mask 置信度校准。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

19. **MLFFM-SegDiff: A Multi-Level Feature Fusion Diffusion Model for Skin Lesion Segmentation**
   - Source: arXiv, 2026-06-25
   - Authors: Jingjun Gu, Chaojie Shen, Yifeng Cao, Wei Zhang, Yiliu Li et al.
   - Tags: diffusion, boundary/frequency, low-level, saliency/transparent, medical imaging
   - Links: [paper](http://arxiv.org/abs/2606.26712v1) / [pdf](http://arxiv.org/pdf/2606.26712v1)
   - 论文：MLFFM-SegDiff: A Multi-Level Feature Fusion Diffusion Model for Skin Lesion Segmentation
   - 一句话总结：Skin lesion segmentation is a key task in computer-aided dermatological diagnosis, where accuracy directly impacts downstream analysis and disease classification. However, dermoscopic images are challenging du...
   - 任务设定：医学影像分割/检测，常见弱边界、低对比和标注稀缺问题。
   - 方法核心：扩散/生成式建模，可能用于数据合成、先验建模或掩码优化。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：和 COD 同属低显著/弱边界目标发现，可迁移目标-背景分离思想。
   - 可借鉴点：边界/频域增强模块。
   - 可改进点：可结合多尺度语义上下文，避免只强化纹理导致误检。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

20. **High-Fidelity Synthetic Transmission Electron Microscopy Image Generation Using Diffusion Probabilistic Models for Data-Limited Semiconductor Metrology**
   - Source: arXiv, 2026-06-23
   - Authors: Johannes Boehm, Bappaditya Dey
   - Tags: diffusion, low-level
   - Links: [paper](http://arxiv.org/abs/2606.24817v1) / [pdf](http://arxiv.org/pdf/2606.24817v1)
   - 论文：High-Fidelity Synthetic Transmission Electron Microscopy Image Generation Using Diffusion Probabilistic Models for Data-Limited Semiconductor Metrology
   - 一句话总结：Advanced semiconductor nodes drastically increased demand for Transmission Electron Microscopy (TEM), yet destructive sample preparation, slow imaging and high costs severely limit the availability of diverse...
   - 任务设定：通用计算机视觉任务，先判断是否能迁移到 COD 的感知、定位或分割环节。
   - 方法核心：扩散/生成式建模，可能用于数据合成、先验建模或掩码优化。
   - 实验结论：可能包含新数据集/基准；适合看评测协议、失败案例和是否能服务 COD。
   - 和我课题的关系：不是 COD 直系论文，但可能提供可迁移的视觉表征、训练策略或评测思路。
   - 可借鉴点：任务建模、损失函数、消融组织方式。
   - 可改进点：可思考是否缺少 COD 场景验证、复杂背景失败分析或轻量化部署。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

21. **Harnessing Vision Foundation Models for High-Performance, Training-Free Open Vocabulary Segmentation**
   - Source: Semantic Scholar / IEEE International Conference on Computer Vision / citations 37, 2024-11-14
   - Authors: Yuheng Shi, Minjing Dong, Chang Xu
   - Tags: open-vocabulary, training-free, SAM, VLM/MLLM
   - Links: [paper](https://www.semanticscholar.org/paper/9dadb571b26ea7bd387b9273b34263fd2c2e981b)
   - 论文：Harnessing Vision Foundation Models for High-Performance, Training-Free Open Vocabulary Segmentation
   - 一句话总结：While CLIP has advanced open-vocabulary predictions, its performance on semantic segmentation remains suboptimal. This shortfall primarily stems from its spatialinvariant semantic features and constrained reso...
   - 任务设定：开放词汇视觉识别/分割，目标类别或文本提示在训练时未必出现。
   - 方法核心：提示学习或提示生成，重点看文本/视觉 prompt 如何约束定位。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：适合拓展到开放词汇、零样本或少标注 COD。
   - 可借鉴点：prompt 设计、类别文本构造、免训练迁移流程；候选 mask 生成、视觉-语言筛选、推理式定位。
   - 可改进点：可改进 prompt 自动生成、负样本约束和 mask 置信度校准。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

22. **SAM-DAQ: Segment Anything Model with Depth-guided Adaptive Queries for RGB-D Video Salient Object Detection**
   - Source: arXiv, 2025-11-13
   - Authors: Jia Lin, Xiaofei Zhou, Jiyuan Liu, Runmin Cong, Guodao Zhang et al.
   - Tags: SAM, diffusion, retrieval/prototype, depth/geometry, video, saliency/transparent
   - Links: [paper](http://arxiv.org/abs/2511.09870v1) / [pdf](http://arxiv.org/pdf/2511.09870v1)
   - 论文：SAM-DAQ: Segment Anything Model with Depth-guided Adaptive Queries for RGB-D Video Salient Object Detection
   - 一句话总结：Recently segment anything model (SAM) has attracted widespread concerns, and it is often treated as a vision foundation model for universal segmentation. Some researchers have attempted to directly apply the f...
   - 任务设定：基础模型驱动的视觉定位/分割/推理，可用于自动提示生成或 mask 筛选。
   - 方法核心：提示学习或提示生成，重点看文本/视觉 prompt 如何约束定位。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：和 COD 同属低显著/弱边界目标发现，可迁移目标-背景分离思想。
   - 可借鉴点：候选 mask 生成、视觉-语言筛选、推理式定位；深度或几何先验融合。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

23. **AD-DINOv3: Enhancing DINOv3 for Zero-Shot Anomaly Detection with Anomaly-Aware Calibration**
   - Source: arXiv, 2025-09-17
   - Authors: Jingyi Yuan, Jianxiong Ye, Wenkang Chen, Chenqiang Gao
   - Tags: VLM/MLLM, diffusion, anomaly/OOD
   - Links: [paper](http://arxiv.org/abs/2509.14084v2) / [pdf](http://arxiv.org/pdf/2509.14084v2)
   - 论文：AD-DINOv3: Enhancing DINOv3 for Zero-Shot Anomaly Detection with Anomaly-Aware Calibration
   - 一句话总结：Zero-Shot Anomaly Detection (ZSAD) seeks to identify anomalies from arbitrary novel categories, offering a scalable and annotation-efficient solution. Traditionally, most ZSAD works have been based on the CLIP...
   - 任务设定：基础模型驱动的视觉定位/分割/推理，可用于自动提示生成或 mask 筛选。
   - 方法核心：提示学习或提示生成，重点看文本/视觉 prompt 如何约束定位。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：可用于伪装目标的语义描述、环境理解和候选区域判断。
   - 可借鉴点：候选 mask 生成、视觉-语言筛选、推理式定位；跨域鲁棒性、不确定性或异常分数。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

24. **FiLo++: Zero-/Few-Shot Anomaly Detection by Fused Fine-Grained Descriptions and Deformable Localization**
   - Source: arXiv, 2025-01-17
   - Authors: Zhaopeng Gu, Bingke Zhu, Guibo Zhu, Yingying Chen, Ming Tang et al.
   - Tags: reasoning, diffusion, anomaly/OOD
   - Links: [paper](http://arxiv.org/abs/2501.10067v2) / [pdf](http://arxiv.org/pdf/2501.10067v2)
   - 论文：FiLo++: Zero-/Few-Shot Anomaly Detection by Fused Fine-Grained Descriptions and Deformable Localization
   - 一句话总结：Anomaly detection methods typically require extensive normal samples from the target class for training, limiting their applicability in scenarios that require rapid adaptation, such as cold start. Zero-shot a...
   - 任务设定：异常检测或分布外识别，可类比伪装目标的弱异常发现。
   - 方法核心：提示学习或提示生成，重点看文本/视觉 prompt 如何约束定位。
   - 实验结论：可能包含新数据集/基准；适合看评测协议、失败案例和是否能服务 COD。
   - 和我课题的关系：可用于伪装目标的语义描述、环境理解和候选区域判断。
   - 可借鉴点：跨域鲁棒性、不确定性或异常分数。
   - 可改进点：可思考是否缺少 COD 场景验证、复杂背景失败分析或轻量化部署。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

25. **MAPSeg: Unified Unsupervised Domain Adaptation for Heterogeneous Medical Image Segmentation Based on 3D Masked Autoencoding and Pseudo-Labeling**
   - Source: CVPR 2024, 2024
   - Authors: Xuzhe Zhang, Yuhao Wu, Elsa Angelini, Ang Li, Jia Guo et al.
   - Tags: unsupervised, depth/geometry, domain adaptation, medical imaging
   - Links: [paper](https://openaccess.thecvf.com/content/CVPR2024/html/Zhang_MAPSeg_Unified_Unsupervised_Domain_Adaptation_for_Heterogeneous_Medical_Image_Segmentation_CVPR_2024_paper.html) / [pdf](https://openaccess.thecvf.com/content/CVPR2024/papers/Zhang_MAPSeg_Unified_Unsupervised_Domain_Adaptation_for_Heterogeneous_Medical_Image_Segmentation_CVPR_2024_paper.pdf)
   - 论文：MAPSeg: Unified Unsupervised Domain Adaptation for Heterogeneous Medical Image Segmentation Based on 3D Masked Autoencoding and Pseudo-Labeling
   - 一句话总结：CVF OpenAccess paper. Open the paper page for full abstract and method details.
   - 任务设定：医学影像分割/检测，常见弱边界、低对比和标注稀缺问题。
   - 方法核心：几何/深度线索建模，可能补充 RGB 外的结构先验。
   - 实验结论：当前来源只提供标题级信息；需要打开论文页确认数据集、指标和消融。
   - 和我课题的关系：可补充 COD 中纹理、边界、几何先验不足的问题。
   - 可借鉴点：深度或几何先验融合；跨域鲁棒性、不确定性或异常分数。
   - 可改进点：可验证在 COD 跨数据集上的泛化，加入目标缺失场景。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

26. **T-REN: Learning Text-Aligned Region Tokens Improves Dense Vision-Language Alignment and Scalability**
   - Source: arXiv, 2026-04-20
   - Authors: Savya Khosla, Sethuraman T, Aryan Chadha, Alex Schwing, Derek Hoiem
   - Tags: open-vocabulary, VLM/MLLM, diffusion, retrieval/prototype, depth/geometry, video
   - Links: [paper](http://arxiv.org/abs/2604.18573v1) / [pdf](http://arxiv.org/pdf/2604.18573v1)
   - 论文：T-REN: Learning Text-Aligned Region Tokens Improves Dense Vision-Language Alignment and Scalability
   - 一句话总结：Despite recent progress, vision-language encoders struggle with two core limitations: (1) weak alignment between language and dense vision features, which hurts tasks like open-vocabulary semantic segmentation...
   - 任务设定：开放词汇视觉识别/分割，目标类别或文本提示在训练时未必出现。
   - 方法核心：视觉-语言对齐，把语义文本信息引入检测或分割。
   - 实验结论：摘要未给出强实验信号；先看实验表格和图 1，再决定是否精读。
   - 和我课题的关系：适合拓展到开放词汇、零样本或少标注 COD。
   - 可借鉴点：prompt 设计、类别文本构造、免训练迁移流程；候选 mask 生成、视觉-语言筛选、推理式定位；深度或几何先验融合。
   - 可改进点：可改进 prompt 自动生成、负样本约束和 mask 置信度校准。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

27. **Towards Realistic Open-Vocabulary Remote Sensing Segmentation: Benchmark and Baseline**
   - Source: arXiv, 2026-04-17
   - Authors: Bingyu Li, Tao Huo, Haocheng Dong, Da Zhang, Zhiyuan Zhao et al.
   - Tags: open-vocabulary, remote sensing, anomaly/OOD
   - Links: [paper](http://arxiv.org/abs/2604.15652v1) / [pdf](http://arxiv.org/pdf/2604.15652v1)
   - 论文：Towards Realistic Open-Vocabulary Remote Sensing Segmentation: Benchmark and Baseline
   - 一句话总结：Open-vocabulary remote sensing image segmentation (OVRSIS) remains underexplored due to fragmented datasets, limited training diversity, and the lack of evaluation benchmarks that reflect realistic geospatial...
   - 任务设定：开放词汇视觉识别/分割，目标类别或文本提示在训练时未必出现。
   - 方法核心：异常/OOD 建模，把目标从复杂背景中作为低概率区域凸显出来。
   - 实验结论：可能包含新数据集/基准；适合看评测协议、失败案例和是否能服务 COD。
   - 和我课题的关系：适合拓展到开放词汇、零样本或少标注 COD。
   - 可借鉴点：prompt 设计、类别文本构造、免训练迁移流程；跨域鲁棒性、不确定性或异常分数。
   - 可改进点：可改进 prompt 自动生成、负样本约束和 mask 置信度校准。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

28. **TRACE: Evidence Grounding-Guided Multi-Video Event Understanding and Claim Generation**
   - Source: arXiv, 2026-05-16
   - Authors: Pengyu Yan, Akhil Gorugantu, Mahesh Bhosale, Abdul Wasi, Vishvesh Trivedi et al.
   - Tags: VLM/MLLM, reasoning, video
   - Links: [paper](http://arxiv.org/abs/2605.16740v2) / [pdf](http://arxiv.org/pdf/2605.16740v2)
   - 论文：TRACE: Evidence Grounding-Guided Multi-Video Event Understanding and Claim Generation
   - 一句话总结：Multi-video event understanding demands models that can locate and attribute query-relevant evidence scattered across long, heterogeneous video corpora. Existing large vision-language models (LVLMs) often unde...
   - 任务设定：基础模型驱动的视觉定位/分割/推理，可用于自动提示生成或 mask 筛选。
   - 方法核心：视觉-语言对齐，把语义文本信息引入检测或分割。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：可用于伪装目标的语义描述、环境理解和候选区域判断。
   - 可借鉴点：候选 mask 生成、视觉-语言筛选、推理式定位。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

29. **Segmentation, Detection and Explanation: A Unified Framework for CT Appearance Reasoning**
   - Source: arXiv, 2026-05-15
   - Authors: Yuyuan Liu, Can Peng, Yingyu Yang, Qianye Yang, Cheng Ouyang et al.
   - Tags: VLM/MLLM, reasoning, diffusion, medical imaging
   - Links: [paper](http://arxiv.org/abs/2605.15997v1) / [pdf](http://arxiv.org/pdf/2605.15997v1)
   - 论文：Segmentation, Detection and Explanation: A Unified Framework for CT Appearance Reasoning
   - 一句话总结：Recent progress in deep learning has significantly advanced CT image analysis, particularly for segmentation tasks. However, these advances are largely confined to image-level pattern recognition, with most me...
   - 任务设定：基础模型驱动的视觉定位/分割/推理，可用于自动提示生成或 mask 筛选。
   - 方法核心：提示学习或提示生成，重点看文本/视觉 prompt 如何约束定位。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：可用于伪装目标的语义描述、环境理解和候选区域判断。
   - 可借鉴点：候选 mask 生成、视觉-语言筛选、推理式定位。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

30. **ModuSeg: Decoupling Object Discovery and Semantic Retrieval for Training-Free Weakly Supervised Segmentation**
   - Source: arXiv, 2026-04-08
   - Authors: Qingze He, Fagui Liu, Dengke Zhang, Qingmao Wei, Quan Tang
   - Tags: training-free, unsupervised, retrieval/prototype, boundary/frequency, depth/geometry
   - Links: [paper](http://arxiv.org/abs/2604.07021v2) / [pdf](http://arxiv.org/pdf/2604.07021v2)
   - 论文：ModuSeg: Decoupling Object Discovery and Semantic Retrieval for Training-Free Weakly Supervised Segmentation
   - 一句话总结：Weakly supervised semantic segmentation aims to achieve pixel-level predictions using image-level labels. Existing methods typically entangle semantic recognition and object localization, which often leads mod...
   - 任务设定：免训练或少训练迁移设定，重点看 prompt、特征选择和后处理。
   - 方法核心：边界感知建模，适合改善伪装目标轮廓不清的问题。
   - 实验结论：可能包含新数据集/基准；适合看评测协议、失败案例和是否能服务 COD。
   - 和我课题的关系：适合拓展到开放词汇、零样本或少标注 COD。
   - 可借鉴点：prompt 设计、类别文本构造、免训练迁移流程；边界/频域增强模块；深度或几何先验融合。
   - 可改进点：可改进 prompt 自动生成、负样本约束和 mask 置信度校准。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

31. **Frequency Adapter with SAM for Generalized Medical Image Segmentation**
   - Source: arXiv, 2026-05-11
   - Authors: Phuoc-Nguyen Bui, Van-Nguyen Pham, Duc-Tai Le, Junghyun Bum, Hyunseung Choo
   - Tags: SAM, diffusion, boundary/frequency, remote sensing, domain adaptation, medical imaging
   - Links: [paper](http://arxiv.org/abs/2605.09925v1) / [pdf](http://arxiv.org/pdf/2605.09925v1)
   - 论文：Frequency Adapter with SAM for Generalized Medical Image Segmentation
   - 一句话总结：Medical image segmentation is a critical task in computer-aided diagnosis and treatment planning. However, deep learning models often struggle to generalize across datasets due to domain shifts arising from va...
   - 任务设定：基础模型驱动的视觉定位/分割/推理，可用于自动提示生成或 mask 筛选。
   - 方法核心：借助 SAM/基础分割模型产生候选 mask，再做筛选或适配。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：可补充 COD 中纹理、边界、几何先验不足的问题。
   - 可借鉴点：候选 mask 生成、视觉-语言筛选、推理式定位；边界/频域增强模块；跨域鲁棒性、不确定性或异常分数。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

32. **Flood Mapping from RGB imagery using a Vision Foundation Model**
   - Source: arXiv, 2026-06-23
   - Authors: Vladyslav Polushko, Tilman Bucher, Ronald Rösch, Thomas März, Markus Rauhut et al.
   - Tags: depth/geometry, remote sensing, anomaly/OOD
   - Links: [paper](http://arxiv.org/abs/2606.24120v1) / [pdf](http://arxiv.org/pdf/2606.24120v1)
   - 论文：Flood Mapping from RGB imagery using a Vision Foundation Model
   - 一句话总结：Timely, high-resolution maps of flood extent around settlements are essential for emergency response and damage assessment. We consider airborne RGB imagery for flood mapping as it can be collected rapidly at...
   - 任务设定：异常检测或分布外识别，可类比伪装目标的弱异常发现。
   - 方法核心：几何/深度线索建模，可能补充 RGB 外的结构先验。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：可补充 COD 中纹理、边界、几何先验不足的问题。
   - 可借鉴点：深度或几何先验融合；跨域鲁棒性、不确定性或异常分数。
   - 可改进点：可思考是否缺少 COD 场景验证、复杂背景失败分析或轻量化部署。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

33. **UniDrive: A Unified Vision-Language and Grounding Framework for Interpretable Risk Understanding in Autonomous Driving**
   - Source: arXiv, 2026-06-23
   - Authors: Xiaowei Gao, Pengxiang Li, Yitai Cheng, Ruihan Xu, James Haworth et al.
   - Tags: VLM/MLLM, reasoning, video
   - Links: [paper](http://arxiv.org/abs/2606.24759v1) / [pdf](http://arxiv.org/pdf/2606.24759v1)
   - 论文：UniDrive: A Unified Vision-Language and Grounding Framework for Interpretable Risk Understanding in Autonomous Driving
   - 一句话总结：Recent multimodal large language models (MLLMs) have shown strong potential for autonomous driving scene understanding, yet existing methods still face a fundamental trade-off between temporal reasoning and sp...
   - 任务设定：基础模型驱动的视觉定位/分割/推理，可用于自动提示生成或 mask 筛选。
   - 方法核心：视觉-语言对齐，把语义文本信息引入检测或分割。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：可用于伪装目标的语义描述、环境理解和候选区域判断。
   - 可借鉴点：候选 mask 生成、视觉-语言筛选、推理式定位。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

34. **Object Tokens as a Bridge Between Segmentation and Visual Question Answering in Robotic Surgery**
   - Source: arXiv, 2026-06-14
   - Authors: Yiping Li, Ronald de Jong, Romy van Jaarsveld, Franco Badaloni, Gino Kuiper et al.
   - Tags: SAM, VLM/MLLM, reasoning
   - Links: [paper](http://arxiv.org/abs/2606.15861v1) / [pdf](http://arxiv.org/pdf/2606.15861v1)
   - 论文：Object Tokens as a Bridge Between Segmentation and Visual Question Answering in Robotic Surgery
   - 一句话总结：Visual Question Answering (VQA) in robotic surgery, referred to as surgical VQA, requires high-level understanding of complex surgical scenes and the integration of visual perception with language reasoning, w...
   - 任务设定：基础模型驱动的视觉定位/分割/推理，可用于自动提示生成或 mask 筛选。
   - 方法核心：借助 SAM/基础分割模型产生候选 mask，再做筛选或适配。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：可用于伪装目标的语义描述、环境理解和候选区域判断。
   - 可借鉴点：候选 mask 生成、视觉-语言筛选、推理式定位。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

35. **Prob-BBDM: a Probabilistic Brownian Bridge Diffusion Model for MRI sequence image-to-image translation**
   - Source: arXiv, 2026-06-23
   - Authors: Martin Valls, Pascal Bourdon, Christine Fernandez-Maloigne, Guillaume Herpe, David Helbert
   - Tags: diffusion, depth/geometry, medical imaging
   - Links: [paper](http://arxiv.org/abs/2606.24313v1) / [pdf](http://arxiv.org/pdf/2606.24313v1)
   - 论文：Prob-BBDM: a Probabilistic Brownian Bridge Diffusion Model for MRI sequence image-to-image translation
   - 一句话总结：AI-driven image-to-image synthesis is rapidly advancing, with growing applications in medical imaging. Multi-modal image analysis plays a crucial role in optimizing examination quality, yet acquiring multiple...
   - 任务设定：医学影像分割/检测，常见弱边界、低对比和标注稀缺问题。
   - 方法核心：扩散/生成式建模，可能用于数据合成、先验建模或掩码优化。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：可补充 COD 中纹理、边界、几何先验不足的问题。
   - 可借鉴点：深度或几何先验融合。
   - 可改进点：可思考是否缺少 COD 场景验证、复杂背景失败分析或轻量化部署。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

36. **EnTrust: Modeling Inter-Modal Conflict for Trustworthy Multimodal Medical Image Analysis**
   - Source: arXiv, 2026-06-19
   - Authors: Dwarikanath Mahapatra, Abhijit Das, Behzad Bozorgtabar, Zongyuan Ge, Sudipta Roy et al.
   - Tags: diffusion, medical imaging
   - Links: [paper](http://arxiv.org/abs/2606.21384v1) / [pdf](http://arxiv.org/pdf/2606.21384v1)
   - 论文：EnTrust: Modeling Inter-Modal Conflict for Trustworthy Multimodal Medical Image Analysis
   - 一句话总结：Multimodal medical imaging fuses complementary anatomical and functional information, yet modalities frequently disagree in pathologically heterogeneous regions. Current segmentation models handle this in one...
   - 任务设定：医学影像分割/检测，常见弱边界、低对比和标注稀缺问题。
   - 方法核心：扩散/生成式建模，可能用于数据合成、先验建模或掩码优化。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：不是 COD 直系论文，但可能提供可迁移的视觉表征、训练策略或评测思路。
   - 可借鉴点：任务建模、损失函数、消融组织方式。
   - 可改进点：可思考是否缺少 COD 场景验证、复杂背景失败分析或轻量化部署。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

37. **SegmentAnyTreeV2: Scaling Transformer-Based Tree Instance Segmentation Across Sensors, Platforms, and Forests**
   - Source: arXiv, 2026-06-06
   - Authors: Maciej Wielgosz, Stefano Puliti, Rasmus Astrup
   - Tags: domain adaptation
   - Links: [paper](http://arxiv.org/abs/2606.08206v2) / [pdf](http://arxiv.org/pdf/2606.08206v2)
   - 论文：SegmentAnyTreeV2: Scaling Transformer-Based Tree Instance Segmentation Across Sensors, Platforms, and Forests
   - 一句话总结：We present SegmentAnyTreeV2, a sensor- and platform-agnostic framework for semantic and instance segmentation of forest point clouds. The model combines a serialization-based Point Transformer v3 backbone with...
   - 任务设定：通用计算机视觉任务，先判断是否能迁移到 COD 的感知、定位或分割环节。
   - 方法核心：测试时适配或域泛化，重点看跨数据集鲁棒性。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：不是 COD 直系论文，但可能提供可迁移的视觉表征、训练策略或评测思路。
   - 可借鉴点：跨域鲁棒性、不确定性或异常分数。
   - 可改进点：可验证在 COD 跨数据集上的泛化，加入目标缺失场景。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

38. **RAVEN: Radar Adaptive Vision Encoders for Efficient Chirp-wise Object Detection and Segmentation**
   - Source: CVPR 2026, 2026
   - Authors: Anuvab Sen, Mir Sayeed Mohammad, Saibal Mukhopadhyay
   - Tags: computer vision
   - Links: [paper](https://openaccess.thecvf.com/content/CVPR2026/html/Sen_RAVEN_Radar_Adaptive_Vision_Encoders_for_Efficient_Chirp-wise_Object_Detection_CVPR_2026_paper.html) / [pdf](https://openaccess.thecvf.com/content/CVPR2026/papers/Sen_RAVEN_Radar_Adaptive_Vision_Encoders_for_Efficient_Chirp-wise_Object_Detection_CVPR_2026_paper.pdf)
   - 论文：RAVEN: Radar Adaptive Vision Encoders for Efficient Chirp-wise Object Detection and Segmentation
   - 一句话总结：CVF OpenAccess paper. Open the paper page for full abstract and method details.
   - 任务设定：通用计算机视觉任务，先判断是否能迁移到 COD 的感知、定位或分割环节。
   - 方法核心：摘要层面未显示明确模块，建议先看方法图确认 backbone、监督信号和损失设计。
   - 实验结论：当前来源只提供标题级信息；需要打开论文页确认数据集、指标和消融。
   - 和我课题的关系：不是 COD 直系论文，但可能提供可迁移的视觉表征、训练策略或评测思路。
   - 可借鉴点：任务建模、损失函数、消融组织方式。
   - 可改进点：可思考是否缺少 COD 场景验证、复杂背景失败分析或轻量化部署。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

39. **Hierarchical Point-Patch Fusion with Adaptive Patch Codebook for 3D Shape Anomaly Detection**
   - Source: CVPR 2026, 2026
   - Authors: Xueyang Kang, Zizhao Li, Tian Lan, Dong Gong, Kourosh Khoshelham et al.
   - Tags: depth/geometry, anomaly/OOD
   - Links: [paper](https://openaccess.thecvf.com/content/CVPR2026/html/Kang_Hierarchical_Point-Patch_Fusion_with_Adaptive_Patch_Codebook_for_3D_Shape_CVPR_2026_paper.html) / [pdf](https://openaccess.thecvf.com/content/CVPR2026/papers/Kang_Hierarchical_Point-Patch_Fusion_with_Adaptive_Patch_Codebook_for_3D_Shape_CVPR_2026_paper.pdf)
   - 论文：Hierarchical Point-Patch Fusion with Adaptive Patch Codebook for 3D Shape Anomaly Detection
   - 一句话总结：CVF OpenAccess paper. Open the paper page for full abstract and method details.
   - 任务设定：异常检测或分布外识别，可类比伪装目标的弱异常发现。
   - 方法核心：几何/深度线索建模，可能补充 RGB 外的结构先验。
   - 实验结论：当前来源只提供标题级信息；需要打开论文页确认数据集、指标和消融。
   - 和我课题的关系：可补充 COD 中纹理、边界、几何先验不足的问题。
   - 可借鉴点：深度或几何先验融合；跨域鲁棒性、不确定性或异常分数。
   - 可改进点：可思考是否缺少 COD 场景验证、复杂背景失败分析或轻量化部署。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

40. **SubspaceAD: Training-Free Few-Shot Anomaly Detection via Subspace Modeling**
   - Source: arXiv, 2026-02-26
   - Authors: Camile Lendering, Erkut Akdag, Egor Bondarev
   - Tags: training-free, VLM/MLLM, retrieval/prototype, remote sensing, anomaly/OOD
   - Links: [paper](http://arxiv.org/abs/2602.23013v3) / [pdf](http://arxiv.org/pdf/2602.23013v3)
   - 论文：SubspaceAD: Training-Free Few-Shot Anomaly Detection via Subspace Modeling
   - 一句话总结：Detecting visual anomalies in industrial inspection often requires training with only a few normal images per category. Recent few-shot methods achieve strong results employing foundation-model features, but t...
   - 任务设定：免训练或少训练迁移设定，重点看 prompt、特征选择和后处理。
   - 方法核心：提示学习或提示生成，重点看文本/视觉 prompt 如何约束定位。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：适合拓展到开放词汇、零样本或少标注 COD。
   - 可借鉴点：prompt 设计、类别文本构造、免训练迁移流程；候选 mask 生成、视觉-语言筛选、推理式定位；跨域鲁棒性、不确定性或异常分数。
   - 可改进点：可改进 prompt 自动生成、负样本约束和 mask 置信度校准。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

41. **Crane: Context-Guided Prompt Learning and Attention Refinement for Zero-Shot Anomaly Detection**
   - Source: arXiv, 2025-04-15
   - Authors: Alireza Salehi, Mohammadreza Salehi, Reshad Hosseini, Cees G. M. Snoek, Makoto Yamada et al.
   - Tags: diffusion, boundary/frequency, anomaly/OOD
   - Links: [paper](http://arxiv.org/abs/2504.11055v2) / [pdf](http://arxiv.org/pdf/2504.11055v2)
   - 论文：Crane: Context-Guided Prompt Learning and Attention Refinement for Zero-Shot Anomaly Detection
   - 一句话总结：Anomaly Detection involves identifying deviations from normal data distributions and is critical in fields such as medical diagnostics and industrial defect detection. Traditional AD methods typically require...
   - 任务设定：异常检测或分布外识别，可类比伪装目标的弱异常发现。
   - 方法核心：提示学习或提示生成，重点看文本/视觉 prompt 如何约束定位。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：可补充 COD 中纹理、边界、几何先验不足的问题。
   - 可借鉴点：边界/频域增强模块；跨域鲁棒性、不确定性或异常分数。
   - 可改进点：可结合多尺度语义上下文，避免只强化纹理导致误检。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

42. **Exploring Efficient Open-Vocabulary Segmentation in the Remote Sensing**
   - Source: arXiv, 2025-09-15
   - Authors: Bingyu Li, Haocheng Dong, Da Zhang, Zhiyuan Zhao, Junyu Gao et al.
   - Tags: open-vocabulary, VLM/MLLM, boundary/frequency, remote sensing, domain adaptation
   - Links: [paper](http://arxiv.org/abs/2509.12040v2) / [pdf](http://arxiv.org/pdf/2509.12040v2)
   - 论文：Exploring Efficient Open-Vocabulary Segmentation in the Remote Sensing
   - 一句话总结：Open-Vocabulary Remote Sensing Image Segmentation (OVRSIS), an emerging task that adapts Open-Vocabulary Segmentation (OVS) to the remote sensing (RS) domain, remains underexplored due to the absence of a unif...
   - 任务设定：开放词汇视觉识别/分割，目标类别或文本提示在训练时未必出现。
   - 方法核心：借助 SAM/基础分割模型产生候选 mask，再做筛选或适配。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：适合拓展到开放词汇、零样本或少标注 COD。
   - 可借鉴点：prompt 设计、类别文本构造、免训练迁移流程；候选 mask 生成、视觉-语言筛选、推理式定位；边界/频域增强模块；跨域鲁棒性、不确定性或异常分数。
   - 可改进点：可改进 prompt 自动生成、负样本约束和 mask 置信度校准。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

43. **Annotation-Free Open-Vocabulary Segmentation for Remote-Sensing Images**
   - Source: arXiv, 2025-08-25
   - Authors: Kaiyu Li, Xiangyong Cao, Ruixun Liu, Shihong Wang, Zixuan Jiang et al.
   - Tags: open-vocabulary, boundary/frequency, remote sensing
   - Links: [paper](http://arxiv.org/abs/2508.18067v1) / [pdf](http://arxiv.org/pdf/2508.18067v1)
   - 论文：Annotation-Free Open-Vocabulary Segmentation for Remote-Sensing Images
   - 一句话总结：Semantic segmentation of remote sensing (RS) images is pivotal for comprehensive Earth observation, but the demand for interpreting new object categories, coupled with the high expense of manual annotation, po...
   - 任务设定：开放词汇视觉识别/分割，目标类别或文本提示在训练时未必出现。
   - 方法核心：借助 SAM/基础分割模型产生候选 mask，再做筛选或适配。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：适合拓展到开放词汇、零样本或少标注 COD。
   - 可借鉴点：prompt 设计、类别文本构造、免训练迁移流程；边界/频域增强模块。
   - 可改进点：可改进 prompt 自动生成、负样本约束和 mask 置信度校准。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

44. **Diffusion Model as a Generalist Segmentation Learner**
   - Source: arXiv, 2026-04-27
   - Authors: Haoxiao Wang, Antao Xiang, Haiyang Sun, Peilin Sun, Changhao Pan et al.
   - Tags: open-vocabulary, diffusion, remote sensing, low-level
   - Links: [paper](http://arxiv.org/abs/2604.24575v1) / [pdf](http://arxiv.org/pdf/2604.24575v1)
   - 论文：Diffusion Model as a Generalist Segmentation Learner
   - 一句话总结：Diffusion models are primarily trained for image synthesis, yet their denoising trajectories encode rich, spatially aligned visual priors. In this paper, we demonstrate that these priors can be utilized for te...
   - 任务设定：开放词汇视觉识别/分割，目标类别或文本提示在训练时未必出现。
   - 方法核心：扩散/生成式建模，可能用于数据合成、先验建模或掩码优化。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：适合拓展到开放词汇、零样本或少标注 COD。
   - 可借鉴点：prompt 设计、类别文本构造、免训练迁移流程。
   - 可改进点：可改进 prompt 自动生成、负样本约束和 mask 置信度校准。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

45. **Cross-Modal-Domain Generalization Through Semantically Aligned Discrete Representations**
   - Source: arXiv, 2026-05-12
   - Authors: Souptik Sen, Raneen Younis, Zahra Ahmadi
   - Tags: retrieval/prototype, video, domain adaptation
   - Links: [paper](http://arxiv.org/abs/2605.12145v2) / [pdf](http://arxiv.org/pdf/2605.12145v2)
   - 论文：Cross-Modal-Domain Generalization Through Semantically Aligned Discrete Representations
   - 一句话总结：Multimodal learning seeks to integrate information across diverse sensory sources, yet current approaches struggle to balance cross-modal generalizability with modality-specific structure. Continuous (implicit...
   - 任务设定：视频/时序视觉任务，关注跨帧一致性、运动线索和长期上下文。
   - 方法核心：视觉-语言对齐，把语义文本信息引入检测或分割。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：不是 COD 直系论文，但可能提供可迁移的视觉表征、训练策略或评测思路。
   - 可借鉴点：跨域鲁棒性、不确定性或异常分数。
   - 可改进点：可验证在 COD 跨数据集上的泛化，加入目标缺失场景。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

46. **EDGER: EDge-Guided with HEatmap Refinement for Generalizable Image Forgery Localization**
   - Source: arXiv, 2026-05-12
   - Authors: Minh-Khoa Le-Phan, Minh-Hoang Le, Minh-Triet Tran, Trong-Le Do
   - Tags: boundary/frequency, domain adaptation
   - Links: [paper](http://arxiv.org/abs/2605.12002v1) / [pdf](http://arxiv.org/pdf/2605.12002v1)
   - 论文：EDGER: EDge-Guided with HEatmap Refinement for Generalizable Image Forgery Localization
   - 一句话总结：Text-guided inpainting has made image forgery increasingly realistic, challenging both SID and IFL. However, existing methods often struggle to point out suspicious signals across domains.
   - 任务设定：通用计算机视觉任务，先判断是否能迁移到 COD 的感知、定位或分割环节。
   - 方法核心：视觉-语言对齐，把语义文本信息引入检测或分割。
   - 实验结论：摘要强调消融、鲁棒性或泛化；适合优先看实验设计和跨域表现。
   - 和我课题的关系：可补充 COD 中纹理、边界、几何先验不足的问题。
   - 可借鉴点：边界/频域增强模块；跨域鲁棒性、不确定性或异常分数。
   - 可改进点：可结合多尺度语义上下文，避免只强化纹理导致误检。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

47. **CrossPan: A Comprehensive Benchmark for Cross-Sequence Pancreas MRI Segmentation and Generalization**
   - Source: arXiv, 2026-04-20
   - Authors: Linkai Peng, Cuiling Sun, Zheyuan Zhang, Wanying Dou, Halil Ertugrul Aktas et al.
   - Tags: unsupervised, depth/geometry, domain adaptation, medical imaging
   - Links: [paper](http://arxiv.org/abs/2604.18797v1) / [pdf](http://arxiv.org/pdf/2604.18797v1)
   - 论文：CrossPan: A Comprehensive Benchmark for Cross-Sequence Pancreas MRI Segmentation and Generalization
   - 一句话总结：Automatic pancreas segmentation is fundamental to abdominal MRI analysis, yet deep learning models trained on one MRI sequence often fail catastrophically when applied to another-a challenge that has received...
   - 任务设定：医学影像分割/检测，常见弱边界、低对比和标注稀缺问题。
   - 方法核心：借助 SAM/基础分割模型产生候选 mask，再做筛选或适配。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：可补充 COD 中纹理、边界、几何先验不足的问题。
   - 可借鉴点：深度或几何先验融合；跨域鲁棒性、不确定性或异常分数。
   - 可改进点：可验证在 COD 跨数据集上的泛化，加入目标缺失场景。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

48. **SemiSAM-O1: How far can we push the boundary of annotation-efficient medical image segmentation?**
   - Source: arXiv, 2026-04-27
   - Authors: Yichi Zhang, Le Xue, Bichun Xu, Judong Luo, Zhigang Wu et al.
   - Tags: unsupervised, retrieval/prototype, boundary/frequency, medical imaging
   - Links: [paper](http://arxiv.org/abs/2604.24109v1) / [pdf](http://arxiv.org/pdf/2604.24109v1)
   - 论文：SemiSAM-O1: How far can we push the boundary of annotation-efficient medical image segmentation?
   - 一句话总结：Semi-supervised learning (SSL) has become a promising solution to alleviate the annotation burden of deep learning-based medical image segmentation models. While recent advances in foundation model-driven SSL...
   - 任务设定：医学影像分割/检测，常见弱边界、低对比和标注稀缺问题。
   - 方法核心：提示学习或提示生成，重点看文本/视觉 prompt 如何约束定位。
   - 实验结论：摘要强调消融、鲁棒性或泛化；适合优先看实验设计和跨域表现。
   - 和我课题的关系：可补充 COD 中纹理、边界、几何先验不足的问题。
   - 可借鉴点：边界/频域增强模块。
   - 可改进点：可结合多尺度语义上下文，避免只强化纹理导致误检。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

49. **Adapting Foundation Models for Annotation-Efficient Adnexal Mass Segmentation in Cine Images**
   - Source: arXiv, 2026-04-09
   - Authors: Francesca Fati, Alberto Rota, Adriana V. Gregory, Anna Catozzo, Maria C. Giuliano et al.
   - Tags: diffusion, boundary/frequency, medical imaging
   - Links: [paper](http://arxiv.org/abs/2604.08045v1) / [pdf](http://arxiv.org/pdf/2604.08045v1)
   - 论文：Adapting Foundation Models for Annotation-Efficient Adnexal Mass Segmentation in Cine Images
   - 一句话总结：Adnexal mass evaluation via ultrasound is a challenging clinical task, often hindered by subjective interpretation and significant inter-observer variability. While automated segmentation is a foundational ste...
   - 任务设定：医学影像分割/检测，常见弱边界、低对比和标注稀缺问题。
   - 方法核心：边界感知建模，适合改善伪装目标轮廓不清的问题。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：可补充 COD 中纹理、边界、几何先验不足的问题。
   - 可借鉴点：边界/频域增强模块。
   - 可改进点：可结合多尺度语义上下文，避免只强化纹理导致误检。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

50. **HyPiDecoder: Hybrid Pixel Decoder for Efficient Segmentation and Detection**
   - Source: ICCV 2025, 2025
   - Authors: Fengzhe Zhou, Humphrey Shi
   - Tags: computer vision
   - Links: [paper](https://openaccess.thecvf.com/content/ICCV2025/html/Zhou_HyPiDecoder_Hybrid_Pixel_Decoder_for_Efficient_Segmentation_and_Detection_ICCV_2025_paper.html) / [pdf](https://openaccess.thecvf.com/content/ICCV2025/papers/Zhou_HyPiDecoder_Hybrid_Pixel_Decoder_for_Efficient_Segmentation_and_Detection_ICCV_2025_paper.pdf)
   - 论文：HyPiDecoder: Hybrid Pixel Decoder for Efficient Segmentation and Detection
   - 一句话总结：CVF OpenAccess paper. Open the paper page for full abstract and method details.
   - 任务设定：通用计算机视觉任务，先判断是否能迁移到 COD 的感知、定位或分割环节。
   - 方法核心：摘要层面未显示明确模块，建议先看方法图确认 backbone、监督信号和损失设计。
   - 实验结论：当前来源只提供标题级信息；需要打开论文页确认数据集、指标和消融。
   - 和我课题的关系：不是 COD 直系论文，但可能提供可迁移的视觉表征、训练策略或评测思路。
   - 可借鉴点：任务建模、损失函数、消融组织方式。
   - 可改进点：可思考是否缺少 COD 场景验证、复杂背景失败分析或轻量化部署。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

51. **SVHighlights: Towards Extremely Long Sport Video Highlight Detection**
   - Source: arXiv, 2026-06-05
   - Authors: Donggyu Lee, Youngbin Ki, Jeonghun Kang, Taehwan Kim
   - Tags: training-free, reasoning, boundary/frequency, video, saliency/transparent
   - Links: [paper](http://arxiv.org/abs/2606.06926v2) / [pdf](http://arxiv.org/pdf/2606.06926v2)
   - 论文：SVHighlights: Towards Extremely Long Sport Video Highlight Detection
   - 一句话总结：While highlight detection for long-form videos is of great practical importance, most existing methods remain limited to short-form content, largely due to the absence of a suitable benchmark. To bridge this g...
   - 任务设定：免训练或少训练迁移设定，重点看 prompt、特征选择和后处理。
   - 方法核心：借助 SAM/基础分割模型产生候选 mask，再做筛选或适配。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：和 COD 同属低显著/弱边界目标发现，可迁移目标-背景分离思想。
   - 可借鉴点：prompt 设计、类别文本构造、免训练迁移流程；边界/频域增强模块。
   - 可改进点：可改进 prompt 自动生成、负样本约束和 mask 置信度校准。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

52. **HPP: Hierarchical Programmatic Probing for Long Video Understanding by Decoupling Perception and Reasoning**
   - Source: arXiv, 2026-06-19
   - Authors: Awais Rauf, Ahmed Hasssan, Greg Slabaugh
   - Tags: VLM/MLLM, reasoning, retrieval/prototype, video
   - Links: [paper](http://arxiv.org/abs/2606.21734v1) / [pdf](http://arxiv.org/pdf/2606.21734v1)
   - 论文：HPP: Hierarchical Programmatic Probing for Long Video Understanding by Decoupling Perception and Reasoning
   - 一句话总结：Understanding long videos requires fine-grained perception and multi-step, higher-order reasoning over complex, long-range spatio-temporal dynamics. Vision-language models (VLMs) encode video frames into visua...
   - 任务设定：基础模型驱动的视觉定位/分割/推理，可用于自动提示生成或 mask 筛选。
   - 方法核心：视觉-语言对齐，把语义文本信息引入检测或分割。
   - 实验结论：可能包含新数据集/基准；适合看评测协议、失败案例和是否能服务 COD。
   - 和我课题的关系：可用于伪装目标的语义描述、环境理解和候选区域判断。
   - 可借鉴点：候选 mask 生成、视觉-语言筛选、推理式定位。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

53. **Binary Tracking for Spatial QA and Navigation with Open Vision-Language Models**
   - Source: arXiv, 2026-06-15
   - Authors: Dongbin Na, Chanwoo Kim, Soonbin Rho, Giyun Choi, Gangbok Lee et al.
   - Tags: VLM/MLLM, reasoning, diffusion, retrieval/prototype, video
   - Links: [paper](http://arxiv.org/abs/2606.16902v1) / [pdf](http://arxiv.org/pdf/2606.16902v1)
   - 论文：Binary Tracking for Spatial QA and Navigation with Open Vision-Language Models
   - 一句话总结：This work addresses spatial question answering for service robots traversing long egocentric routes. Given a query such as "where can I find a dry cleaner on the way back home?", the system returns a metric co...
   - 任务设定：基础模型驱动的视觉定位/分割/推理，可用于自动提示生成或 mask 筛选。
   - 方法核心：借助 SAM/基础分割模型产生候选 mask，再做筛选或适配。
   - 实验结论：可能包含新数据集/基准；适合看评测协议、失败案例和是否能服务 COD。
   - 和我课题的关系：可用于伪装目标的语义描述、环境理解和候选区域判断。
   - 可借鉴点：候选 mask 生成、视觉-语言筛选、推理式定位。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

54. **ReasonCLIP-58M: Visually Grounded Commonsense Reasoning Supervision for CLIP**
   - Source: arXiv, 2026-06-25
   - Authors: Sicheng Zhang, Muzammal Naseer, Binzhu Xie, Naufal Suryanto, Shi Qiu et al.
   - Tags: VLM/MLLM, reasoning, diffusion, retrieval/prototype
   - Links: [paper](http://arxiv.org/abs/2606.26794v1) / [pdf](http://arxiv.org/pdf/2606.26794v1)
   - 论文：ReasonCLIP-58M: Visually Grounded Commonsense Reasoning Supervision for CLIP
   - 一句话总结：CLIP and its variants are widely adopted visual backbones in multimodal systems, but their pretraining remains dominated by descriptive image-text alignment. As downstream applications increasingly demand visu...
   - 任务设定：基础模型驱动的视觉定位/分割/推理，可用于自动提示生成或 mask 筛选。
   - 方法核心：视觉-语言对齐，把语义文本信息引入检测或分割。
   - 实验结论：可能包含新数据集/基准；适合看评测协议、失败案例和是否能服务 COD。
   - 和我课题的关系：可用于伪装目标的语义描述、环境理解和候选区域判断。
   - 可借鉴点：候选 mask 生成、视觉-语言筛选、推理式定位。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

55. **IMAGIN-4D: Image-Guided Controllable Interaction Generation**
   - Source: arXiv, 2026-06-22
   - Authors: Sai Kumar Dwivedi, Federica Bogo, Buğra Tekin, Chenhongyi Yang, Nadine Bertsch et al.
   - Tags: diffusion, depth/geometry, video
   - Links: [paper](http://arxiv.org/abs/2606.23675v1) / [pdf](http://arxiv.org/pdf/2606.23675v1)
   - 论文：IMAGIN-4D: Image-Guided Controllable Interaction Generation
   - 一句话总结：Generating human-object interactions (HOI) is central to character animation, robotics, AR/VR, and embodied AI. Recent HOI generation methods synthesize motion from text, object geometry, and sparse waypoints,...
   - 任务设定：视频/时序视觉任务，关注跨帧一致性、运动线索和长期上下文。
   - 方法核心：扩散/生成式建模，可能用于数据合成、先验建模或掩码优化。
   - 实验结论：可能包含新数据集/基准；适合看评测协议、失败案例和是否能服务 COD。
   - 和我课题的关系：可补充 COD 中纹理、边界、几何先验不足的问题。
   - 可借鉴点：深度或几何先验融合。
   - 可改进点：可思考是否缺少 COD 场景验证、复杂背景失败分析或轻量化部署。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

56. **SARIF: Segment Anything for Robust Image Forensics**
   - Source: arXiv, 2026-06-19
   - Authors: Dong-Hyun Moon, Ju-Hyeon Nam, Sang-Chul Lee
   - Tags: SAM, remote sensing, domain adaptation
   - Links: [paper](http://arxiv.org/abs/2606.21108v1) / [pdf](http://arxiv.org/pdf/2606.21108v1)
   - 论文：SARIF: Segment Anything for Robust Image Forensics
   - 一句话总结：Image forgery localization remains challenging due to diverse manipulation techniques and distribution shifts. Existing forgery localization models achieve high accuracy on benchmarks but often struggle with c...
   - 任务设定：基础模型驱动的视觉定位/分割/推理，可用于自动提示生成或 mask 筛选。
   - 方法核心：提示学习或提示生成，重点看文本/视觉 prompt 如何约束定位。
   - 实验结论：可能包含新数据集/基准；适合看评测协议、失败案例和是否能服务 COD。
   - 和我课题的关系：不是 COD 直系论文，但可能提供可迁移的视觉表征、训练策略或评测思路。
   - 可借鉴点：候选 mask 生成、视觉-语言筛选、推理式定位；跨域鲁棒性、不确定性或异常分数。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

57. **SL-S4Wave: Self-Supervised Learning of Physiological Waveforms with Structured State Space Models**
   - Source: arXiv, 2026-06-18
   - Authors: Feng Wu, Harsh Deep, Eric Lehman, Sanyam Kapoor, Guoshuai Zhao et al.
   - Tags: diffusion, video, domain adaptation
   - Links: [paper](http://arxiv.org/abs/2606.19888v1) / [pdf](http://arxiv.org/pdf/2606.19888v1)
   - 论文：SL-S4Wave: Self-Supervised Learning of Physiological Waveforms with Structured State Space Models
   - 一句话总结：Modeling long-sequence medical time series data, such as electrocardiograms (ECG), poses significant challenges due to high sampling rates, multichannel signal complexity, inherent noise, and limited labeled d...
   - 任务设定：视频/时序视觉任务，关注跨帧一致性、运动线索和长期上下文。
   - 方法核心：借助 SAM/基础分割模型产生候选 mask，再做筛选或适配。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：不是 COD 直系论文，但可能提供可迁移的视觉表征、训练策略或评测思路。
   - 可借鉴点：跨域鲁棒性、不确定性或异常分数。
   - 可改进点：可验证在 COD 跨数据集上的泛化，加入目标缺失场景。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

58. **VTOS: Learning to Orchestrate Vision Tools by Co-Searching Solutions and Observers**
   - Source: arXiv, 2026-06-17
   - Authors: Jinchao Ge, Lingqiao Liu, Shuwen Zhao, Lei Wang
   - Tags: open-vocabulary, SAM, reasoning, diffusion, boundary/frequency, anomaly/OOD, domain adaptation
   - Links: [paper](http://arxiv.org/abs/2606.20728v1) / [pdf](http://arxiv.org/pdf/2606.20728v1)
   - 论文：VTOS: Learning to Orchestrate Vision Tools by Co-Searching Solutions and Observers
   - 一句话总结：Vision foundation tools such as open-vocabulary detectors, segmentation models, and post-processing operators are powerful building blocks for computer vision, but their effectiveness depends heavily on how th...
   - 任务设定：开放词汇视觉识别/分割，目标类别或文本提示在训练时未必出现。
   - 方法核心：借助 SAM/基础分割模型产生候选 mask，再做筛选或适配。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：适合拓展到开放词汇、零样本或少标注 COD。
   - 可借鉴点：prompt 设计、类别文本构造、免训练迁移流程；候选 mask 生成、视觉-语言筛选、推理式定位；边界/频域增强模块；跨域鲁棒性、不确定性或异常分数。
   - 可改进点：可改进 prompt 自动生成、负样本约束和 mask 置信度校准。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

59. **Efficient Encoder-Free Fourier-based 3D Large Multimodal Model**
   - Source: CVPR 2026, 2026
   - Authors: Guofeng Mei, Wei Lin, Luigi Riz, Yujiao Wu, Yiming Wang et al.
   - Tags: depth/geometry
   - Links: [paper](https://openaccess.thecvf.com/content/CVPR2026/html/Mei_Efficient_Encoder-Free_Fourier-based_3D_Large_Multimodal_Model_CVPR_2026_paper.html) / [pdf](https://openaccess.thecvf.com/content/CVPR2026/papers/Mei_Efficient_Encoder-Free_Fourier-based_3D_Large_Multimodal_Model_CVPR_2026_paper.pdf)
   - 论文：Efficient Encoder-Free Fourier-based 3D Large Multimodal Model
   - 一句话总结：CVF OpenAccess paper. Open the paper page for full abstract and method details.
   - 任务设定：通用计算机视觉任务，先判断是否能迁移到 COD 的感知、定位或分割环节。
   - 方法核心：视觉-语言对齐，把语义文本信息引入检测或分割。
   - 实验结论：当前来源只提供标题级信息；需要打开论文页确认数据集、指标和消融。
   - 和我课题的关系：可补充 COD 中纹理、边界、几何先验不足的问题。
   - 可借鉴点：深度或几何先验融合。
   - 可改进点：可思考是否缺少 COD 场景验证、复杂背景失败分析或轻量化部署。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

60. **Boosting Salient Object Detection with Knowledge Distillated from Large Foundation Models**
   - Source: arXiv, 2025-01-08
   - Authors: Miaoyang He, Shuyong Gao, Tsui Qin Mok, Weifeng Ge, Wengqiang Zhang
   - Tags: unsupervised, diffusion, boundary/frequency, saliency/transparent
   - Links: [paper](http://arxiv.org/abs/2501.04582v1) / [pdf](http://arxiv.org/pdf/2501.04582v1)
   - 论文：Boosting Salient Object Detection with Knowledge Distillated from Large Foundation Models
   - 一句话总结：Salient Object Detection (SOD) aims to identify and segment prominent regions within a scene. Traditional models rely on manually annotated pseudo labels with precise pixel-level accuracy, which is time-consum...
   - 任务设定：通用计算机视觉任务，先判断是否能迁移到 COD 的感知、定位或分割环节。
   - 方法核心：提示学习或提示生成，重点看文本/视觉 prompt 如何约束定位。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：和 COD 同属低显著/弱边界目标发现，可迁移目标-背景分离思想。
   - 可借鉴点：边界/频域增强模块。
   - 可改进点：可结合多尺度语义上下文，避免只强化纹理导致误检。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

## 历史更新归档

## 2026-06-26 23:47 更新

Selected papers: 8487

### 当日优先读

1. **CFCamo: A Counterfactual Detect-or-Abstain Framework for Camouflaged Object Detection**
   - Source: arXiv, 2026-05-28
   - Authors: Suhang Li, Osamu Yoshie, Yuya Ieiri
   - Tags: COD, VLM/MLLM
   - Links: [paper](http://arxiv.org/abs/2606.11231v1) / [pdf](http://arxiv.org/pdf/2606.11231v1)
   - 论文：CFCamo: A Counterfactual Detect-or-Abstain Framework for Camouflaged Object Detection
   - 一句话总结：Vision-language reinforcement learning has recently shown strong target-present localization for camouflaged object detection (COD). Yet localization is only one side of the decision: when the agent faces an o...
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：反事实建模/拒识机制，用来降低误检或判断目标是否存在。
   - 实验结论：可能包含新数据集/基准；适合看评测协议、失败案例和是否能服务 COD。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；候选 mask 生成、视觉-语言筛选、推理式定位。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

2. **A Retinomorphic Optical Spiking Neuron for Camouflaged Object Detection**
   - Source: arXiv, 2026-05-30
   - Authors: Srilagna Sahoo, Adwaaiit Pande, Kartikey Thakar, Shubham Sahay, Saurabh Lodha
   - Tags: COD, boundary/frequency
   - Links: [paper](http://arxiv.org/abs/2606.00818v1) / [pdf](http://arxiv.org/pdf/2606.00818v1)
   - 论文：A Retinomorphic Optical Spiking Neuron for Camouflaged Object Detection
   - 一句话总结：Advanced vision systems require retinomorphic, energy-efficient spike-based preprocessing of dynamic visual scenes. Here, we demonstrate multiple retinal preprocessing functionalities by leveraging a Hodgkin-H...
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：边界感知建模，适合改善伪装目标轮廓不清的问题。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；边界/频域增强模块。
   - 可改进点：可尝试引入基础模型、文本先验或更强的环境上下文建模。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

3. **Video Object Segmentation-Aware Audio Generation**
   - Source: Crossref / IJCV / CCF-A / 顶刊 / International Journal of Computer Vision, 2026-06-23
   - Authors: Ilpo Viertola, Vladimir Iashin, Esa Rahtu
   - Tags: diffusion, video, remote sensing
   - Links: [paper](https://doi.org/10.1007/s11263-026-02911-2)
   - 论文：Video Object Segmentation-Aware Audio Generation
   - 一句话总结：Abstract Existing multimodal audio generation models often lack precise user control, which limits their applicability in professional Foley workflows. In particular, these models focus on the entire video and...
   - 任务设定：遥感/大场景密集视觉任务，关注小目标、尺度变化和复杂背景。
   - 方法核心：扩散/生成式建模，可能用于数据合成、先验建模或掩码优化。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：不是 COD 直系论文，但可能提供可迁移的视觉表征、训练策略或评测思路。
   - 可借鉴点：任务建模、损失函数、消融组织方式。
   - 可改进点：可思考是否缺少 COD 场景验证、复杂背景失败分析或轻量化部署。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

4. **Anatomy-Guided Residual Motion Diffusion for Controllable 4D Cardiac MRI Synthesis**
   - Source: arXiv, 2026-06-25
   - Authors: Yiheng Cao, Gustavo Andrade-Miranda, Jiatian Zhang, Lingxiao Zhao, Xin Gao
   - Tags: unsupervised, diffusion, boundary/frequency, depth/geometry, video, medical imaging
   - Links: [paper](http://arxiv.org/abs/2606.26764v1) / [pdf](http://arxiv.org/pdf/2606.26764v1)
   - 论文：Anatomy-Guided Residual Motion Diffusion for Controllable 4D Cardiac MRI Synthesis
   - 一句话总结：Developing robust artificial intelligence models for 4D (3D + time) medical imaging is constrained by limited annotated data, inter-device domain shifts, and privacy restrictions. To address this, we propose a...
   - 任务设定：医学影像分割/检测，常见弱边界、低对比和标注稀缺问题。
   - 方法核心：扩散/生成式建模，可能用于数据合成、先验建模或掩码优化。
   - 实验结论：可能包含新数据集/基准；适合看评测协议、失败案例和是否能服务 COD。
   - 和我课题的关系：可补充 COD 中纹理、边界、几何先验不足的问题。
   - 可借鉴点：边界/频域增强模块；深度或几何先验融合。
   - 可改进点：可结合多尺度语义上下文，避免只强化纹理导致误检。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

5. **SOCO: Benchmarking Semantic Object Correspondence in Vision Foundation Models**
   - Source: arXiv, 2026-05-29
   - Authors: Olaf Dünkel, Basavaraj Sunagad, Haoran Wang, David T. Hoffmann, Christian Theobalt et al.
   - Tags: VLM/MLLM, diffusion, depth/geometry, video
   - Links: [paper](http://arxiv.org/abs/2605.31597v2) / [pdf](http://arxiv.org/pdf/2605.31597v2)
   - 论文：SOCO: Benchmarking Semantic Object Correspondence in Vision Foundation Models
   - 一句话总结：Measuring structured object understanding in vision foundation models remains challenging due to inconsistent evaluation protocols and limited part-level supervision. Semantic correspondence (SC) evaluates thi...
   - 任务设定：基础模型驱动的视觉定位/分割/推理，可用于自动提示生成或 mask 筛选。
   - 方法核心：提示学习或提示生成，重点看文本/视觉 prompt 如何约束定位。
   - 实验结论：可能包含新数据集/基准；适合看评测协议、失败案例和是否能服务 COD。
   - 和我课题的关系：可补充 COD 中纹理、边界、几何先验不足的问题。
   - 可借鉴点：候选 mask 生成、视觉-语言筛选、推理式定位；深度或几何先验融合。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

6. **MLFFM-SegDiff: A Multi-Level Feature Fusion Diffusion Model for Skin Lesion Segmentation**
   - Source: arXiv, 2026-06-25
   - Authors: Jingjun Gu, Chaojie Shen, Yifeng Cao, Wei Zhang, Yiliu Li et al.
   - Tags: diffusion, boundary/frequency, low-level, saliency/transparent, medical imaging
   - Links: [paper](http://arxiv.org/abs/2606.26712v1) / [pdf](http://arxiv.org/pdf/2606.26712v1)
   - 论文：MLFFM-SegDiff: A Multi-Level Feature Fusion Diffusion Model for Skin Lesion Segmentation
   - 一句话总结：Skin lesion segmentation is a key task in computer-aided dermatological diagnosis, where accuracy directly impacts downstream analysis and disease classification. However, dermoscopic images are challenging du...
   - 任务设定：医学影像分割/检测，常见弱边界、低对比和标注稀缺问题。
   - 方法核心：扩散/生成式建模，可能用于数据合成、先验建模或掩码优化。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：和 COD 同属低显著/弱边界目标发现，可迁移目标-背景分离思想。
   - 可借鉴点：边界/频域增强模块。
   - 可改进点：可结合多尺度语义上下文，避免只强化纹理导致误检。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

7. **Vision-Language Model Reasoning for Contextual Semantic Mapping in Intralogistics**
   - Source: arXiv, 2026-06-23
   - Authors: Marvin Rüdt, Hao Pang, Constantin Enke, Zäzilia Seibold, Kai Furmans
   - Tags: open-vocabulary, SAM, VLM/MLLM, reasoning, depth/geometry
   - Links: [paper](http://arxiv.org/abs/2606.24814v1) / [pdf](http://arxiv.org/pdf/2606.24814v1)
   - 论文：Vision-Language Model Reasoning for Contextual Semantic Mapping in Intralogistics
   - 一句话总结：Autonomous mobile robots operating in intralogistics environments rely on geometric maps for localization and navigation, but lack semantic understanding of objects and their contextual properties. We present...
   - 任务设定：开放词汇视觉识别/分割，目标类别或文本提示在训练时未必出现。
   - 方法核心：提示学习或提示生成，重点看文本/视觉 prompt 如何约束定位。
   - 实验结论：摘要强调消融、鲁棒性或泛化；适合优先看实验设计和跨域表现。
   - 和我课题的关系：适合拓展到开放词汇、零样本或少标注 COD。
   - 可借鉴点：prompt 设计、类别文本构造、免训练迁移流程；候选 mask 生成、视觉-语言筛选、推理式定位；深度或几何先验融合。
   - 可改进点：可改进 prompt 自动生成、负样本约束和 mask 置信度校准。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

8. **Jolia: Concept-Level Vision-Language Alignment for 3D CT Contrastive Learning**
   - Source: arXiv, 2026-06-23
   - Authors: Julien Khlaut, Charles Corbière, Baptiste Callard, Amaury Prat, Leo Butsanets et al.
   - Tags: VLM/MLLM, depth/geometry, medical imaging
   - Links: [paper](http://arxiv.org/abs/2606.24570v2) / [pdf](http://arxiv.org/pdf/2606.24570v2)
   - 论文：Jolia: Concept-Level Vision-Language Alignment for 3D CT Contrastive Learning
   - 一句话总结：Vision-language contrastive pretraining has become the dominant recipe for 3D medical foundation models, leveraging the large volumes of paired scans and reports produced in clinical practice. However, medical...
   - 任务设定：基础模型驱动的视觉定位/分割/推理，可用于自动提示生成或 mask 筛选。
   - 方法核心：视觉-语言对齐，把语义文本信息引入检测或分割。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：可补充 COD 中纹理、边界、几何先验不足的问题。
   - 可借鉴点：候选 mask 生成、视觉-语言筛选、推理式定位；深度或几何先验融合。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

9. **Training-free Cross-domain Few-shot Segmentation via Robust Semantic Representation and Matching**
   - Source: arXiv, 2026-06-23
   - Authors: Sujun Sun, Mingwu Ren, Haofeng Zhang
   - Tags: training-free, diffusion, retrieval/prototype, boundary/frequency, low-level
   - Links: [paper](http://arxiv.org/abs/2606.24297v1) / [pdf](http://arxiv.org/pdf/2606.24297v1)
   - 论文：Training-free Cross-domain Few-shot Segmentation via Robust Semantic Representation and Matching
   - 一句话总结：Cross-domain Few-shot Segmentation (CD-FSS) aims to transfer knowledge learned from source domain to distinct target domains, segmenting unseen target classes with only a few annotated samples. Although existi...
   - 任务设定：免训练或少训练迁移设定，重点看 prompt、特征选择和后处理。
   - 方法核心：借助 SAM/基础分割模型产生候选 mask，再做筛选或适配。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：适合拓展到开放词汇、零样本或少标注 COD。
   - 可借鉴点：prompt 设计、类别文本构造、免训练迁移流程；边界/频域增强模块。
   - 可改进点：可改进 prompt 自动生成、负样本约束和 mask 置信度校准。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

10. **High-Fidelity Synthetic Transmission Electron Microscopy Image Generation Using Diffusion Probabilistic Models for Data-Limited Semiconductor Metrology**
   - Source: arXiv, 2026-06-23
   - Authors: Johannes Boehm, Bappaditya Dey
   - Tags: diffusion, low-level
   - Links: [paper](http://arxiv.org/abs/2606.24817v1) / [pdf](http://arxiv.org/pdf/2606.24817v1)
   - 论文：High-Fidelity Synthetic Transmission Electron Microscopy Image Generation Using Diffusion Probabilistic Models for Data-Limited Semiconductor Metrology
   - 一句话总结：Advanced semiconductor nodes drastically increased demand for Transmission Electron Microscopy (TEM), yet destructive sample preparation, slow imaging and high costs severely limit the availability of diverse...
   - 任务设定：通用计算机视觉任务，先判断是否能迁移到 COD 的感知、定位或分割环节。
   - 方法核心：扩散/生成式建模，可能用于数据合成、先验建模或掩码优化。
   - 实验结论：可能包含新数据集/基准；适合看评测协议、失败案例和是否能服务 COD。
   - 和我课题的关系：不是 COD 直系论文，但可能提供可迁移的视觉表征、训练策略或评测思路。
   - 可借鉴点：任务建模、损失函数、消融组织方式。
   - 可改进点：可思考是否缺少 COD 场景验证、复杂背景失败分析或轻量化部署。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

11. **EnTrust: Modeling Inter-Modal Conflict for Trustworthy Multimodal Medical Image Analysis**
   - Source: arXiv, 2026-06-19
   - Authors: Dwarikanath Mahapatra, Abhijit Das, Behzad Bozorgtabar, Zongyuan Ge, Sudipta Roy et al.
   - Tags: diffusion, medical imaging
   - Links: [paper](http://arxiv.org/abs/2606.21384v1) / [pdf](http://arxiv.org/pdf/2606.21384v1)
   - 论文：EnTrust: Modeling Inter-Modal Conflict for Trustworthy Multimodal Medical Image Analysis
   - 一句话总结：Multimodal medical imaging fuses complementary anatomical and functional information, yet modalities frequently disagree in pathologically heterogeneous regions. Current segmentation models handle this in one...
   - 任务设定：医学影像分割/检测，常见弱边界、低对比和标注稀缺问题。
   - 方法核心：扩散/生成式建模，可能用于数据合成、先验建模或掩码优化。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：不是 COD 直系论文，但可能提供可迁移的视觉表征、训练策略或评测思路。
   - 可借鉴点：任务建模、损失函数、消融组织方式。
   - 可改进点：可思考是否缺少 COD 场景验证、复杂背景失败分析或轻量化部署。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

12. **ARTEMIS: Agent-guided Reliability-aware Temporal Mask Evolution for Imperfectly Supervised Video Polyp Segmentation**
   - Source: arXiv, 2026-06-18
   - Authors: Tong Wang, Siwen Wang, Yaolei Qi, Jinxing Zhou, Yuting He et al.
   - Tags: VLM/MLLM, retrieval/prototype, boundary/frequency, depth/geometry, video
   - Links: [paper](http://arxiv.org/abs/2606.20161v1) / [pdf](http://arxiv.org/pdf/2606.20161v1)
   - 论文：ARTEMIS: Agent-guided Reliability-aware Temporal Mask Evolution for Imperfectly Supervised Video Polyp Segmentation
   - 一句话总结：Imperfectly supervised video polyp segmentation (VPS) aims to learn dense, temporally consistent masks from inexpensive supervision, including weak annotations (points, scribbles) and semi-supervision with few...
   - 任务设定：基础模型驱动的视觉定位/分割/推理，可用于自动提示生成或 mask 筛选。
   - 方法核心：借助 SAM/基础分割模型产生候选 mask，再做筛选或适配。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：可补充 COD 中纹理、边界、几何先验不足的问题。
   - 可借鉴点：候选 mask 生成、视觉-语言筛选、推理式定位；边界/频域增强模块；深度或几何先验融合。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

### 当日高质量来源优先读

1. **VSCode: General Visual Salient and Camouflaged Object Detection with 2D Prompt Learning**
   - Source: CVPR 2024, 2024
   - Authors: Ziyang Luo, Nian Liu, Wangbo Zhao, Xuguang Yang, Dingwen Zhang et al.
   - Tags: COD, saliency/transparent
   - Links: [paper](https://openaccess.thecvf.com/content/CVPR2024/html/Luo_VSCode_General_Visual_Salient_and_Camouflaged_Object_Detection_with_2D_CVPR_2024_paper.html) / [pdf](https://openaccess.thecvf.com/content/CVPR2024/papers/Luo_VSCode_General_Visual_Salient_and_Camouflaged_Object_Detection_with_2D_CVPR_2024_paper.pdf)
   - 论文：VSCode: General Visual Salient and Camouflaged Object Detection with 2D Prompt Learning
   - 一句话总结：CVF OpenAccess paper. Open the paper page for full abstract and method details.
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：提示学习或提示生成，重点看文本/视觉 prompt 如何约束定位。
   - 实验结论：当前来源只提供标题级信息；需要打开论文页确认数据集、指标和消融。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析。
   - 可改进点：可尝试引入基础模型、文本先验或更强的环境上下文建模。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

2. **Training-Free Open-Vocabulary Camouflaged Object Segmentation via Fine-Grained Object Binding and Adaptive Hybrid Prompt**
   - Source: CVPR 2026, 2026
   - Authors: Peng Ren, Cheng Jiang, Chuande Yang, Fuming Sun, Tian Bai
   - Tags: COD, open-vocabulary, training-free
   - Links: [paper](https://openaccess.thecvf.com/content/CVPR2026/html/Ren_Training-Free_Open-Vocabulary_Camouflaged_Object_Segmentation_via_Fine-Grained_Object_Binding_and_CVPR_2026_paper.html) / [pdf](https://openaccess.thecvf.com/content/CVPR2026/papers/Ren_Training-Free_Open-Vocabulary_Camouflaged_Object_Segmentation_via_Fine-Grained_Object_Binding_and_CVPR_2026_paper.pdf)
   - 论文：Training-Free Open-Vocabulary Camouflaged Object Segmentation via Fine-Grained Object Binding and Adaptive Hybrid Prompt
   - 一句话总结：CVF OpenAccess paper. Open the paper page for full abstract and method details.
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：提示学习或提示生成，重点看文本/视觉 prompt 如何约束定位。
   - 实验结论：当前来源只提供标题级信息；需要打开论文页确认数据集、指标和消融。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；prompt 设计、类别文本构造、免训练迁移流程。
   - 可改进点：可尝试引入基础模型、文本先验或更强的环境上下文建模。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

3. **Video Object Segmentation-Aware Audio Generation**
   - Source: Crossref / IJCV / CCF-A / 顶刊 / International Journal of Computer Vision, 2026-06-23
   - Authors: Ilpo Viertola, Vladimir Iashin, Esa Rahtu
   - Tags: diffusion, video, remote sensing
   - Links: [paper](https://doi.org/10.1007/s11263-026-02911-2)
   - 论文：Video Object Segmentation-Aware Audio Generation
   - 一句话总结：Abstract Existing multimodal audio generation models often lack precise user control, which limits their applicability in professional Foley workflows. In particular, these models focus on the entire video and...
   - 任务设定：遥感/大场景密集视觉任务，关注小目标、尺度变化和复杂背景。
   - 方法核心：扩散/生成式建模，可能用于数据合成、先验建模或掩码优化。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：不是 COD 直系论文，但可能提供可迁移的视觉表征、训练策略或评测思路。
   - 可借鉴点：任务建模、损失函数、消融组织方式。
   - 可改进点：可思考是否缺少 COD 场景验证、复杂背景失败分析或轻量化部署。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

4. **Discover, Segment, and Select: A Progressive Mechanism for Zero-shot Camouflaged Object Segmentation**
   - Source: CVPR 2026, 2026
   - Authors: Yilong Yang, Jianxin Tian, Shengchuan Zhang, Liujuan Cao
   - Tags: COD
   - Links: [paper](https://openaccess.thecvf.com/content/CVPR2026/html/Yang_Discover_Segment_and_Select_A_Progressive_Mechanism_for_Zero-shot_Camouflaged_CVPR_2026_paper.html) / [pdf](https://openaccess.thecvf.com/content/CVPR2026/papers/Yang_Discover_Segment_and_Select_A_Progressive_Mechanism_for_Zero-shot_Camouflaged_CVPR_2026_paper.pdf)
   - 论文：Discover, Segment, and Select: A Progressive Mechanism for Zero-shot Camouflaged Object Segmentation
   - 一句话总结：CVF OpenAccess paper. Open the paper page for full abstract and method details.
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：摘要层面未显示明确模块，建议先看方法图确认 backbone、监督信号和损失设计。
   - 实验结论：当前来源只提供标题级信息；需要打开论文页确认数据集、指标和消融。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析。
   - 可改进点：可尝试引入基础模型、文本先验或更强的环境上下文建模。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

5. **Seeing Both Sides: Towards Bidirectional Semantic Alignment for Open-Vocabulary Camouflaged Object Segmentation**
   - Source: CVPR 2026, 2026
   - Authors: Guohui Zhang, Fuming Sun, Yu Zhao, Yuqiu Kong, Jing Sun et al.
   - Tags: COD, open-vocabulary
   - Links: [paper](https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_Seeing_Both_Sides_Towards_Bidirectional_Semantic_Alignment_for_Open-Vocabulary_Camouflaged_CVPR_2026_paper.html) / [pdf](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhang_Seeing_Both_Sides_Towards_Bidirectional_Semantic_Alignment_for_Open-Vocabulary_Camouflaged_CVPR_2026_paper.pdf)
   - 论文：Seeing Both Sides: Towards Bidirectional Semantic Alignment for Open-Vocabulary Camouflaged Object Segmentation
   - 一句话总结：CVF OpenAccess paper. Open the paper page for full abstract and method details.
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：摘要层面未显示明确模块，建议先看方法图确认 backbone、监督信号和损失设计。
   - 实验结论：当前来源只提供标题级信息；需要打开论文页确认数据集、指标和消融。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；prompt 设计、类别文本构造、免训练迁移流程。
   - 可改进点：可尝试引入基础模型、文本先验或更强的环境上下文建模。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

6. **Beyond Weak Supervision: MLLMs-Guided Graded Knowledge Distillation for Unsupervised Camouflaged Object Detection**
   - Source: CVPR 2026, 2026
   - Authors: Huafeng Chen, Chenguang Zhu, Yueming Lyu, Caifeng Shan
   - Tags: COD, unsupervised, VLM/MLLM, boundary/frequency
   - Links: [paper](https://openaccess.thecvf.com/content/CVPR2026/html/Chen_Beyond_Weak_Supervision_MLLMs-Guided_Graded_Knowledge_Distillation_for_Unsupervised_Camouflaged_CVPR_2026_paper.html) / [pdf](https://openaccess.thecvf.com/content/CVPR2026/papers/Chen_Beyond_Weak_Supervision_MLLMs-Guided_Graded_Knowledge_Distillation_for_Unsupervised_Camouflaged_CVPR_2026_paper.pdf)
   - 论文：Beyond Weak Supervision: MLLMs-Guided Graded Knowledge Distillation for Unsupervised Camouflaged Object Detection
   - 一句话总结：CVF OpenAccess paper. Open the paper page for full abstract and method details.
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：多模态大模型推理，可能用于目标描述、区域判断或链式推理。
   - 实验结论：当前来源只提供标题级信息；需要打开论文页确认数据集、指标和消融。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；候选 mask 生成、视觉-语言筛选、推理式定位；边界/频域增强模块。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

7. **Endow SAM with Keen Eyes: Temporal-spatial Prompt Learning for Video Camouflaged Object Detection**
   - Source: CVPR 2024, 2024
   - Authors: Wenjun Hui, Zhenfeng Zhu, Shuai Zheng, Yao Zhao
   - Tags: COD, SAM, video
   - Links: [paper](https://openaccess.thecvf.com/content/CVPR2024/html/Hui_Endow_SAM_with_Keen_Eyes_Temporal-spatial_Prompt_Learning_for_Video_CVPR_2024_paper.html) / [pdf](https://openaccess.thecvf.com/content/CVPR2024/papers/Hui_Endow_SAM_with_Keen_Eyes_Temporal-spatial_Prompt_Learning_for_Video_CVPR_2024_paper.pdf)
   - 论文：Endow SAM with Keen Eyes: Temporal-spatial Prompt Learning for Video Camouflaged Object Detection
   - 一句话总结：CVF OpenAccess paper. Open the paper page for full abstract and method details.
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：提示学习或提示生成，重点看文本/视觉 prompt 如何约束定位。
   - 实验结论：当前来源只提供标题级信息；需要打开论文页确认数据集、指标和消融。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；候选 mask 生成、视觉-语言筛选、推理式定位。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

8. **Seeing the Unseen: A Semantic Alignment and Context-Aware Prompt Framework for Open-Vocabulary Camouflaged Object Segmentation**
   - Source: ICCV 2025, 2025
   - Authors: Peng Ren, Tian Bai, Jing Sun, Fuming Sun
   - Tags: COD, open-vocabulary
   - Links: [paper](https://openaccess.thecvf.com/content/ICCV2025/html/Ren_Seeing_the_Unseen_A_Semantic_Alignment_and_Context-Aware_Prompt_Framework_ICCV_2025_paper.html) / [pdf](https://openaccess.thecvf.com/content/ICCV2025/papers/Ren_Seeing_the_Unseen_A_Semantic_Alignment_and_Context-Aware_Prompt_Framework_ICCV_2025_paper.pdf)
   - 论文：Seeing the Unseen: A Semantic Alignment and Context-Aware Prompt Framework for Open-Vocabulary Camouflaged Object Segmentation
   - 一句话总结：CVF OpenAccess paper. Open the paper page for full abstract and method details.
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：提示学习或提示生成，重点看文本/视觉 prompt 如何约束定位。
   - 实验结论：当前来源只提供标题级信息；需要打开论文页确认数据集、指标和消融。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；prompt 设计、类别文本构造、免训练迁移流程。
   - 可改进点：可尝试引入基础模型、文本先验或更强的环境上下文建模。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

9. **Beyond Appearance: Camouflaged Object Detection via Geometric Structure**
   - Source: CVPR 2026, 2026
   - Authors: Jinyu Han, Changguang Wu, Fuming Sun, Jinhui Tang
   - Tags: COD, depth/geometry
   - Links: [paper](https://openaccess.thecvf.com/content/CVPR2026/html/Han_Beyond_Appearance_Camouflaged_Object_Detection_via_Geometric_Structure_CVPR_2026_paper.html) / [pdf](https://openaccess.thecvf.com/content/CVPR2026/papers/Han_Beyond_Appearance_Camouflaged_Object_Detection_via_Geometric_Structure_CVPR_2026_paper.pdf)
   - 论文：Beyond Appearance: Camouflaged Object Detection via Geometric Structure
   - 一句话总结：CVF OpenAccess paper. Open the paper page for full abstract and method details.
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：摘要层面未显示明确模块，建议先看方法图确认 backbone、监督信号和损失设计。
   - 实验结论：当前来源只提供标题级信息；需要打开论文页确认数据集、指标和消融。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；深度或几何先验融合。
   - 可改进点：可尝试引入基础模型、文本先验或更强的环境上下文建模。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

10. **Shift the Lens: Environment-Aware Unsupervised Camouflaged Object Detection**
   - Source: CVPR 2025, 2025
   - Authors: Ji Du, Fangwei Hao, Mingyang Yu, Desheng Kong, Jiesheng Wu et al.
   - Tags: COD, unsupervised
   - Links: [paper](https://openaccess.thecvf.com/content/CVPR2025/html/Du_Shift_the_Lens_Environment-Aware_Unsupervised_Camouflaged_Object_Detection_CVPR_2025_paper.html) / [pdf](https://openaccess.thecvf.com/content/CVPR2025/papers/Du_Shift_the_Lens_Environment-Aware_Unsupervised_Camouflaged_Object_Detection_CVPR_2025_paper.pdf)
   - 论文：Shift the Lens: Environment-Aware Unsupervised Camouflaged Object Detection
   - 一句话总结：CVF OpenAccess paper. Open the paper page for full abstract and method details.
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：摘要层面未显示明确模块，建议先看方法图确认 backbone、监督信号和损失设计。
   - 实验结论：当前来源只提供标题级信息；需要打开论文页确认数据集、指标和消融。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析。
   - 可改进点：可尝试引入基础模型、文本先验或更强的环境上下文建模。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

11. **Rethinking Detecting Salient and Camouflaged Objects in Unconstrained Scenes**
   - Source: ICCV 2025, 2025
   - Authors: Zhangjun Zhou, Yiping Li, Chunlin Zhong, Jianuo Huang, Jialun Pei et al.
   - Tags: COD, saliency/transparent
   - Links: [paper](https://openaccess.thecvf.com/content/ICCV2025/html/Zhou_Rethinking_Detecting_Salient_and_Camouflaged_Objects_in_Unconstrained_Scenes_ICCV_2025_paper.html) / [pdf](https://openaccess.thecvf.com/content/ICCV2025/papers/Zhou_Rethinking_Detecting_Salient_and_Camouflaged_Objects_in_Unconstrained_Scenes_ICCV_2025_paper.pdf)
   - 论文：Rethinking Detecting Salient and Camouflaged Objects in Unconstrained Scenes
   - 一句话总结：CVF OpenAccess paper. Open the paper page for full abstract and method details.
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：摘要层面未显示明确模块，建议先看方法图确认 backbone、监督信号和损失设计。
   - 实验结论：当前来源只提供标题级信息；需要打开论文页确认数据集、指标和消融。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析。
   - 可改进点：可尝试引入基础模型、文本先验或更强的环境上下文建模。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

12. **ESCNet:Edge-Semantic Collaborative Network for Camouflaged Object Detection**
   - Source: ICCV 2025, 2025
   - Authors: Sheng Ye, Xin Chen, Yan Zhang, Xianming Lin, Liujuan Cao
   - Tags: COD, boundary/frequency
   - Links: [paper](https://openaccess.thecvf.com/content/ICCV2025/html/Ye_ESCNetEdge-Semantic_Collaborative_Network_for_Camouflaged_Object_Detection_ICCV_2025_paper.html) / [pdf](https://openaccess.thecvf.com/content/ICCV2025/papers/Ye_ESCNetEdge-Semantic_Collaborative_Network_for_Camouflaged_Object_Detection_ICCV_2025_paper.pdf)
   - 论文：ESCNet:Edge-Semantic Collaborative Network for Camouflaged Object Detection
   - 一句话总结：CVF OpenAccess paper. Open the paper page for full abstract and method details.
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：边界感知建模，适合改善伪装目标轮廓不清的问题。
   - 实验结论：当前来源只提供标题级信息；需要打开论文页确认数据集、指标和消融。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；边界/频域增强模块。
   - 可改进点：可尝试引入基础模型、文本先验或更强的环境上下文建模。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

13. **Enhancing Prompt Generation with Adaptive Refinement for Camouflaged Object Detection**
   - Source: ICCV 2025, 2025
   - Authors: Xuehan Chen, Guangyu Ren, Tianhong Dai, Tania Stathaki, Hengyan Liu
   - Tags: COD
   - Links: [paper](https://openaccess.thecvf.com/content/ICCV2025/html/Chen_Enhancing_Prompt_Generation_with_Adaptive_Refinement_for_Camouflaged_Object_Detection_ICCV_2025_paper.html) / [pdf](https://openaccess.thecvf.com/content/ICCV2025/papers/Chen_Enhancing_Prompt_Generation_with_Adaptive_Refinement_for_Camouflaged_Object_Detection_ICCV_2025_paper.pdf)
   - 论文：Enhancing Prompt Generation with Adaptive Refinement for Camouflaged Object Detection
   - 一句话总结：CVF OpenAccess paper. Open the paper page for full abstract and method details.
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：提示学习或提示生成，重点看文本/视觉 prompt 如何约束定位。
   - 实验结论：当前来源只提供标题级信息；需要打开论文页确认数据集、指标和消融。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析。
   - 可改进点：可尝试引入基础模型、文本先验或更强的环境上下文建模。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

14. **Multi-modal Segment Anything Model for Camouflaged Scene Segmentation**
   - Source: ICCV 2025, 2025
   - Authors: Guangyu Ren, Hengyan Liu, Michalis Lazarou, Tania Stathaki
   - Tags: COD, SAM
   - Links: [paper](https://openaccess.thecvf.com/content/ICCV2025/html/Ren_Multi-modal_Segment_Anything_Model_for_Camouflaged_Scene_Segmentation_ICCV_2025_paper.html) / [pdf](https://openaccess.thecvf.com/content/ICCV2025/papers/Ren_Multi-modal_Segment_Anything_Model_for_Camouflaged_Scene_Segmentation_ICCV_2025_paper.pdf)
   - 论文：Multi-modal Segment Anything Model for Camouflaged Scene Segmentation
   - 一句话总结：CVF OpenAccess paper. Open the paper page for full abstract and method details.
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：借助 SAM/基础分割模型产生候选 mask，再做筛选或适配。
   - 实验结论：当前来源只提供标题级信息；需要打开论文页确认数据集、指标和消融。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；候选 mask 生成、视觉-语言筛选、推理式定位。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

15. **LAKE-RED: Camouflaged Images Generation by Latent Background Knowledge Retrieval-Augmented Diffusion**
   - Source: CVPR 2024, 2024
   - Authors: Pancheng Zhao, Peng Xu, Pengda Qin, Deng-Ping Fan, Zhicheng Zhang et al.
   - Tags: COD, diffusion, retrieval/prototype, boundary/frequency
   - Links: [paper](https://openaccess.thecvf.com/content/CVPR2024/html/Zhao_LAKE-RED_Camouflaged_Images_Generation_by_Latent_Background_Knowledge_Retrieval-Augmented_Diffusion_CVPR_2024_paper.html) / [pdf](https://openaccess.thecvf.com/content/CVPR2024/papers/Zhao_LAKE-RED_Camouflaged_Images_Generation_by_Latent_Background_Knowledge_Retrieval-Augmented_Diffusion_CVPR_2024_paper.pdf)
   - 论文：LAKE-RED: Camouflaged Images Generation by Latent Background Knowledge Retrieval-Augmented Diffusion
   - 一句话总结：CVF OpenAccess paper. Open the paper page for full abstract and method details.
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：扩散/生成式建模，可能用于数据合成、先验建模或掩码优化。
   - 实验结论：当前来源只提供标题级信息；需要打开论文页确认数据集、指标和消融。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；边界/频域增强模块。
   - 可改进点：可尝试引入基础模型、文本先验或更强的环境上下文建模。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

16. **Scoring, Remember, and Reference: Catching Camouflaged Objects in Videos**
   - Source: ICCV 2025, 2025
   - Authors: Yu'ang Feng, Shuyong Gao, Fuzhen Yan, Yicheng Song, Lingyi Hong et al.
   - Tags: COD, video
   - Links: [paper](https://openaccess.thecvf.com/content/ICCV2025/html/Feng_Scoring_Remember_and_Reference_Catching_Camouflaged_Objects_in_Videos_ICCV_2025_paper.html) / [pdf](https://openaccess.thecvf.com/content/ICCV2025/papers/Feng_Scoring_Remember_and_Reference_Catching_Camouflaged_Objects_in_Videos_ICCV_2025_paper.pdf)
   - 论文：Scoring, Remember, and Reference: Catching Camouflaged Objects in Videos
   - 一句话总结：CVF OpenAccess paper. Open the paper page for full abstract and method details.
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：摘要层面未显示明确模块，建议先看方法图确认 backbone、监督信号和损失设计。
   - 实验结论：当前来源只提供标题级信息；需要打开论文页确认数据集、指标和消融。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析。
   - 可改进点：可尝试引入基础模型、文本先验或更强的环境上下文建模。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

17. **MAPSeg: Unified Unsupervised Domain Adaptation for Heterogeneous Medical Image Segmentation Based on 3D Masked Autoencoding and Pseudo-Labeling**
   - Source: CVPR 2024, 2024
   - Authors: Xuzhe Zhang, Yuhao Wu, Elsa Angelini, Ang Li, Jia Guo et al.
   - Tags: unsupervised, depth/geometry, domain adaptation, medical imaging
   - Links: [paper](https://openaccess.thecvf.com/content/CVPR2024/html/Zhang_MAPSeg_Unified_Unsupervised_Domain_Adaptation_for_Heterogeneous_Medical_Image_Segmentation_CVPR_2024_paper.html) / [pdf](https://openaccess.thecvf.com/content/CVPR2024/papers/Zhang_MAPSeg_Unified_Unsupervised_Domain_Adaptation_for_Heterogeneous_Medical_Image_Segmentation_CVPR_2024_paper.pdf)
   - 论文：MAPSeg: Unified Unsupervised Domain Adaptation for Heterogeneous Medical Image Segmentation Based on 3D Masked Autoencoding and Pseudo-Labeling
   - 一句话总结：CVF OpenAccess paper. Open the paper page for full abstract and method details.
   - 任务设定：医学影像分割/检测，常见弱边界、低对比和标注稀缺问题。
   - 方法核心：几何/深度线索建模，可能补充 RGB 外的结构先验。
   - 实验结论：当前来源只提供标题级信息；需要打开论文页确认数据集、指标和消融。
   - 和我课题的关系：可补充 COD 中纹理、边界、几何先验不足的问题。
   - 可借鉴点：深度或几何先验融合；跨域鲁棒性、不确定性或异常分数。
   - 可改进点：可验证在 COD 跨数据集上的泛化，加入目标缺失场景。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

18. **RAVEN: Radar Adaptive Vision Encoders for Efficient Chirp-wise Object Detection and Segmentation**
   - Source: CVPR 2026, 2026
   - Authors: Anuvab Sen, Mir Sayeed Mohammad, Saibal Mukhopadhyay
   - Tags: computer vision
   - Links: [paper](https://openaccess.thecvf.com/content/CVPR2026/html/Sen_RAVEN_Radar_Adaptive_Vision_Encoders_for_Efficient_Chirp-wise_Object_Detection_CVPR_2026_paper.html) / [pdf](https://openaccess.thecvf.com/content/CVPR2026/papers/Sen_RAVEN_Radar_Adaptive_Vision_Encoders_for_Efficient_Chirp-wise_Object_Detection_CVPR_2026_paper.pdf)
   - 论文：RAVEN: Radar Adaptive Vision Encoders for Efficient Chirp-wise Object Detection and Segmentation
   - 一句话总结：CVF OpenAccess paper. Open the paper page for full abstract and method details.
   - 任务设定：通用计算机视觉任务，先判断是否能迁移到 COD 的感知、定位或分割环节。
   - 方法核心：摘要层面未显示明确模块，建议先看方法图确认 backbone、监督信号和损失设计。
   - 实验结论：当前来源只提供标题级信息；需要打开论文页确认数据集、指标和消融。
   - 和我课题的关系：不是 COD 直系论文，但可能提供可迁移的视觉表征、训练策略或评测思路。
   - 可借鉴点：任务建模、损失函数、消融组织方式。
   - 可改进点：可思考是否缺少 COD 场景验证、复杂背景失败分析或轻量化部署。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

19. **Hierarchical Point-Patch Fusion with Adaptive Patch Codebook for 3D Shape Anomaly Detection**
   - Source: CVPR 2026, 2026
   - Authors: Xueyang Kang, Zizhao Li, Tian Lan, Dong Gong, Kourosh Khoshelham et al.
   - Tags: depth/geometry, anomaly/OOD
   - Links: [paper](https://openaccess.thecvf.com/content/CVPR2026/html/Kang_Hierarchical_Point-Patch_Fusion_with_Adaptive_Patch_Codebook_for_3D_Shape_CVPR_2026_paper.html) / [pdf](https://openaccess.thecvf.com/content/CVPR2026/papers/Kang_Hierarchical_Point-Patch_Fusion_with_Adaptive_Patch_Codebook_for_3D_Shape_CVPR_2026_paper.pdf)
   - 论文：Hierarchical Point-Patch Fusion with Adaptive Patch Codebook for 3D Shape Anomaly Detection
   - 一句话总结：CVF OpenAccess paper. Open the paper page for full abstract and method details.
   - 任务设定：异常检测或分布外识别，可类比伪装目标的弱异常发现。
   - 方法核心：几何/深度线索建模，可能补充 RGB 外的结构先验。
   - 实验结论：当前来源只提供标题级信息；需要打开论文页确认数据集、指标和消融。
   - 和我课题的关系：可补充 COD 中纹理、边界、几何先验不足的问题。
   - 可借鉴点：深度或几何先验融合；跨域鲁棒性、不确定性或异常分数。
   - 可改进点：可思考是否缺少 COD 场景验证、复杂背景失败分析或轻量化部署。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

20. **HyPiDecoder: Hybrid Pixel Decoder for Efficient Segmentation and Detection**
   - Source: ICCV 2025, 2025
   - Authors: Fengzhe Zhou, Humphrey Shi
   - Tags: computer vision
   - Links: [paper](https://openaccess.thecvf.com/content/ICCV2025/html/Zhou_HyPiDecoder_Hybrid_Pixel_Decoder_for_Efficient_Segmentation_and_Detection_ICCV_2025_paper.html) / [pdf](https://openaccess.thecvf.com/content/ICCV2025/papers/Zhou_HyPiDecoder_Hybrid_Pixel_Decoder_for_Efficient_Segmentation_and_Detection_ICCV_2025_paper.pdf)
   - 论文：HyPiDecoder: Hybrid Pixel Decoder for Efficient Segmentation and Detection
   - 一句话总结：CVF OpenAccess paper. Open the paper page for full abstract and method details.
   - 任务设定：通用计算机视觉任务，先判断是否能迁移到 COD 的感知、定位或分割环节。
   - 方法核心：摘要层面未显示明确模块，建议先看方法图确认 backbone、监督信号和损失设计。
   - 实验结论：当前来源只提供标题级信息；需要打开论文页确认数据集、指标和消融。
   - 和我课题的关系：不是 COD 直系论文，但可能提供可迁移的视觉表征、训练策略或评测思路。
   - 可借鉴点：任务建模、损失函数、消融组织方式。
   - 可改进点：可思考是否缺少 COD 场景验证、复杂背景失败分析或轻量化部署。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

21. **Efficient Encoder-Free Fourier-based 3D Large Multimodal Model**
   - Source: CVPR 2026, 2026
   - Authors: Guofeng Mei, Wei Lin, Luigi Riz, Yujiao Wu, Yiming Wang et al.
   - Tags: depth/geometry
   - Links: [paper](https://openaccess.thecvf.com/content/CVPR2026/html/Mei_Efficient_Encoder-Free_Fourier-based_3D_Large_Multimodal_Model_CVPR_2026_paper.html) / [pdf](https://openaccess.thecvf.com/content/CVPR2026/papers/Mei_Efficient_Encoder-Free_Fourier-based_3D_Large_Multimodal_Model_CVPR_2026_paper.pdf)
   - 论文：Efficient Encoder-Free Fourier-based 3D Large Multimodal Model
   - 一句话总结：CVF OpenAccess paper. Open the paper page for full abstract and method details.
   - 任务设定：通用计算机视觉任务，先判断是否能迁移到 COD 的感知、定位或分割环节。
   - 方法核心：视觉-语言对齐，把语义文本信息引入检测或分割。
   - 实验结论：当前来源只提供标题级信息；需要打开论文页确认数据集、指标和消融。
   - 和我课题的关系：可补充 COD 中纹理、边界、几何先验不足的问题。
   - 可借鉴点：深度或几何先验融合。
   - 可改进点：可思考是否缺少 COD 场景验证、复杂背景失败分析或轻量化部署。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

22. **Rethinking Decoder Design: Improving Biomarker Segmentation Using Depth-to-Space Restoration and Residual Linear Attention**
   - Source: CVPR 2025, 2025
   - Authors: Saad Wazir, Daeyoung Kim
   - Tags: depth/geometry, low-level
   - Links: [paper](https://openaccess.thecvf.com/content/CVPR2025/html/Wazir_Rethinking_Decoder_Design_Improving_Biomarker_Segmentation_Using_Depth-to-Space_Restoration_and_CVPR_2025_paper.html) / [pdf](https://openaccess.thecvf.com/content/CVPR2025/papers/Wazir_Rethinking_Decoder_Design_Improving_Biomarker_Segmentation_Using_Depth-to-Space_Restoration_and_CVPR_2025_paper.pdf)
   - 论文：Rethinking Decoder Design: Improving Biomarker Segmentation Using Depth-to-Space Restoration and Residual Linear Attention
   - 一句话总结：CVF OpenAccess paper. Open the paper page for full abstract and method details.
   - 任务设定：通用计算机视觉任务，先判断是否能迁移到 COD 的感知、定位或分割环节。
   - 方法核心：几何/深度线索建模，可能补充 RGB 外的结构先验。
   - 实验结论：当前来源只提供标题级信息；需要打开论文页确认数据集、指标和消融。
   - 和我课题的关系：可补充 COD 中纹理、边界、几何先验不足的问题。
   - 可借鉴点：深度或几何先验融合。
   - 可改进点：可思考是否缺少 COD 场景验证、复杂背景失败分析或轻量化部署。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

23. **EffiDec3D: An Optimized Decoder for High-Performance and Efficient 3D Medical Image Segmentation**
   - Source: CVPR 2025, 2025
   - Authors: Md Mostafijur Rahman, Radu Marculescu
   - Tags: depth/geometry, medical imaging
   - Links: [paper](https://openaccess.thecvf.com/content/CVPR2025/html/Rahman_EffiDec3D_An_Optimized_Decoder_for_High-Performance_and_Efficient_3D_Medical_CVPR_2025_paper.html) / [pdf](https://openaccess.thecvf.com/content/CVPR2025/papers/Rahman_EffiDec3D_An_Optimized_Decoder_for_High-Performance_and_Efficient_3D_Medical_CVPR_2025_paper.pdf)
   - 论文：EffiDec3D: An Optimized Decoder for High-Performance and Efficient 3D Medical Image Segmentation
   - 一句话总结：CVF OpenAccess paper. Open the paper page for full abstract and method details.
   - 任务设定：医学影像分割/检测，常见弱边界、低对比和标注稀缺问题。
   - 方法核心：几何/深度线索建模，可能补充 RGB 外的结构先验。
   - 实验结论：当前来源只提供标题级信息；需要打开论文页确认数据集、指标和消融。
   - 和我课题的关系：可补充 COD 中纹理、边界、几何先验不足的问题。
   - 可借鉴点：深度或几何先验融合。
   - 可改进点：可思考是否缺少 COD 场景验证、复杂背景失败分析或轻量化部署。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

24. **Noise-Resistant Video Anomaly Detection via RGB Error-Guided Multiscale Predictive Coding and Dynamic Memory**
   - Source: CVPR 2025, 2025
   - Authors: Han Hu, Wenli Du, Peng Liao, Bing Wang, Siyuan Fan
   - Tags: video, anomaly/OOD
   - Links: [paper](https://openaccess.thecvf.com/content/CVPR2025/html/Hu_Noise-Resistant_Video_Anomaly_Detection_via_RGB_Error-Guided_Multiscale_Predictive_Coding_CVPR_2025_paper.html) / [pdf](https://openaccess.thecvf.com/content/CVPR2025/papers/Hu_Noise-Resistant_Video_Anomaly_Detection_via_RGB_Error-Guided_Multiscale_Predictive_Coding_CVPR_2025_paper.pdf)
   - 论文：Noise-Resistant Video Anomaly Detection via RGB Error-Guided Multiscale Predictive Coding and Dynamic Memory
   - 一句话总结：CVF OpenAccess paper. Open the paper page for full abstract and method details.
   - 任务设定：异常检测或分布外识别，可类比伪装目标的弱异常发现。
   - 方法核心：异常/OOD 建模，把目标从复杂背景中作为低概率区域凸显出来。
   - 实验结论：当前来源只提供标题级信息；需要打开论文页确认数据集、指标和消融。
   - 和我课题的关系：可把伪装目标看作复杂背景中的弱异常区域来借鉴。
   - 可借鉴点：跨域鲁棒性、不确定性或异常分数。
   - 可改进点：可思考是否缺少 COD 场景验证、复杂背景失败分析或轻量化部署。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

25. **AEROBLADE: Training-Free Detection of Latent Diffusion Images Using Autoencoder Reconstruction Error**
   - Source: CVPR 2024, 2024
   - Authors: Jonas Ricker, Denis Lukovnikov, Asja Fischer
   - Tags: training-free, diffusion
   - Links: [paper](https://openaccess.thecvf.com/content/CVPR2024/html/Ricker_AEROBLADE_Training-Free_Detection_of_Latent_Diffusion_Images_Using_Autoencoder_Reconstruction_CVPR_2024_paper.html) / [pdf](https://openaccess.thecvf.com/content/CVPR2024/papers/Ricker_AEROBLADE_Training-Free_Detection_of_Latent_Diffusion_Images_Using_Autoencoder_Reconstruction_CVPR_2024_paper.pdf)
   - 论文：AEROBLADE: Training-Free Detection of Latent Diffusion Images Using Autoencoder Reconstruction Error
   - 一句话总结：CVF OpenAccess paper. Open the paper page for full abstract and method details.
   - 任务设定：免训练或少训练迁移设定，重点看 prompt、特征选择和后处理。
   - 方法核心：扩散/生成式建模，可能用于数据合成、先验建模或掩码优化。
   - 实验结论：当前来源只提供标题级信息；需要打开论文页确认数据集、指标和消融。
   - 和我课题的关系：适合拓展到开放词汇、零样本或少标注 COD。
   - 可借鉴点：prompt 设计、类别文本构造、免训练迁移流程。
   - 可改进点：可改进 prompt 自动生成、负样本约束和 mask 置信度校准。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

26. **Describe, Adapt and Combine: Empowering CLIP Encoders for Open-set 3D Object Retrieval**
   - Source: ICCV 2025, 2025
   - Authors: Zhichuan Wang, Yang Zhou, Zhe Liu, Rui Yu, Song Bai et al.
   - Tags: retrieval/prototype, depth/geometry
   - Links: [paper](https://openaccess.thecvf.com/content/ICCV2025/html/Wang_Describe_Adapt_and_Combine_Empowering_CLIP_Encoders_for_Open-set_3D_ICCV_2025_paper.html) / [pdf](https://openaccess.thecvf.com/content/ICCV2025/papers/Wang_Describe_Adapt_and_Combine_Empowering_CLIP_Encoders_for_Open-set_3D_ICCV_2025_paper.pdf)
   - 论文：Describe, Adapt and Combine: Empowering CLIP Encoders for Open-set 3D Object Retrieval
   - 一句话总结：CVF OpenAccess paper. Open the paper page for full abstract and method details.
   - 任务设定：通用计算机视觉任务，先判断是否能迁移到 COD 的感知、定位或分割环节。
   - 方法核心：视觉-语言对齐，把语义文本信息引入检测或分割。
   - 实验结论：当前来源只提供标题级信息；需要打开论文页确认数据集、指标和消融。
   - 和我课题的关系：可补充 COD 中纹理、边界、几何先验不足的问题。
   - 可借鉴点：深度或几何先验融合。
   - 可改进点：可思考是否缺少 COD 场景验证、复杂背景失败分析或轻量化部署。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

27. **GeoFormer: Geometry Point Encoder for 3D Object Detection with Graph-based Transformer**
   - Source: ICCV 2025, 2025
   - Authors: Xin Jin, Haisheng Su, Cong Ma, Kai Liu, Wei Wu et al.
   - Tags: depth/geometry
   - Links: [paper](https://openaccess.thecvf.com/content/ICCV2025/html/Jin_GeoFormer_Geometry_Point_Encoder_for_3D_Object_Detection_with_Graph-based_ICCV_2025_paper.html) / [pdf](https://openaccess.thecvf.com/content/ICCV2025/papers/Jin_GeoFormer_Geometry_Point_Encoder_for_3D_Object_Detection_with_Graph-based_ICCV_2025_paper.pdf)
   - 论文：GeoFormer: Geometry Point Encoder for 3D Object Detection with Graph-based Transformer
   - 一句话总结：CVF OpenAccess paper. Open the paper page for full abstract and method details.
   - 任务设定：通用计算机视觉任务，先判断是否能迁移到 COD 的感知、定位或分割环节。
   - 方法核心：几何/深度线索建模，可能补充 RGB 外的结构先验。
   - 实验结论：当前来源只提供标题级信息；需要打开论文页确认数据集、指标和消融。
   - 和我课题的关系：可补充 COD 中纹理、边界、几何先验不足的问题。
   - 可借鉴点：深度或几何先验融合。
   - 可改进点：可思考是否缺少 COD 场景验证、复杂背景失败分析或轻量化部署。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

28. **3D Gaussian Splatting Driven Multi-View Robust Physical Adversarial Camouflage Generation**
   - Source: ICCV 2025, 2025
   - Authors: Tianrui Lou, Xiaojun Jia, Siyuan Liang, Jiawei Liang, Ming Zhang et al.
   - Tags: COD, depth/geometry, remote sensing
   - Links: [paper](https://openaccess.thecvf.com/content/ICCV2025/html/Lou_3D_Gaussian_Splatting_Driven_Multi-View_Robust_Physical_Adversarial_Camouflage_Generation_ICCV_2025_paper.html) / [pdf](https://openaccess.thecvf.com/content/ICCV2025/papers/Lou_3D_Gaussian_Splatting_Driven_Multi-View_Robust_Physical_Adversarial_Camouflage_Generation_ICCV_2025_paper.pdf)
   - 论文：3D Gaussian Splatting Driven Multi-View Robust Physical Adversarial Camouflage Generation
   - 一句话总结：CVF OpenAccess paper. Open the paper page for full abstract and method details.
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：几何/深度线索建模，可能补充 RGB 外的结构先验。
   - 实验结论：当前来源只提供标题级信息；需要打开论文页确认数据集、指标和消融。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；深度或几何先验融合。
   - 可改进点：可尝试引入基础模型、文本先验或更强的环境上下文建模。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

29. **Gradient-Reweighted Adversarial Camouflage for Physical Object Detection Evasion**
   - Source: ICCV 2025, 2025
   - Authors: Jiawei Liang, Siyuan Liang, Tianrui Lou, Ming Zhang, Wenjin Li et al.
   - Tags: COD, remote sensing
   - Links: [paper](https://openaccess.thecvf.com/content/ICCV2025/html/Liang_Gradient-Reweighted_Adversarial_Camouflage_for_Physical_Object_Detection_Evasion_ICCV_2025_paper.html) / [pdf](https://openaccess.thecvf.com/content/ICCV2025/papers/Liang_Gradient-Reweighted_Adversarial_Camouflage_for_Physical_Object_Detection_Evasion_ICCV_2025_paper.pdf)
   - 论文：Gradient-Reweighted Adversarial Camouflage for Physical Object Detection Evasion
   - 一句话总结：CVF OpenAccess paper. Open the paper page for full abstract and method details.
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：摘要层面未显示明确模块，建议先看方法图确认 backbone、监督信号和损失设计。
   - 实验结论：当前来源只提供标题级信息；需要打开论文页确认数据集、指标和消融。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析。
   - 可改进点：可尝试引入基础模型、文本先验或更强的环境上下文建模。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

30. **FE-CLIP: Frequency Enhanced CLIP Model for Zero-Shot Anomaly Detection and Segmentation**
   - Source: ICCV 2025, 2025
   - Authors: Tao Gong, Qi Chu, Bin Liu, Wei Zhou, Nenghai Yu
   - Tags: boundary/frequency, anomaly/OOD
   - Links: [paper](https://openaccess.thecvf.com/content/ICCV2025/html/Gong_FE-CLIP_Frequency_Enhanced_CLIP_Model_for_Zero-Shot_Anomaly_Detection_and_ICCV_2025_paper.html) / [pdf](https://openaccess.thecvf.com/content/ICCV2025/papers/Gong_FE-CLIP_Frequency_Enhanced_CLIP_Model_for_Zero-Shot_Anomaly_Detection_and_ICCV_2025_paper.pdf)
   - 论文：FE-CLIP: Frequency Enhanced CLIP Model for Zero-Shot Anomaly Detection and Segmentation
   - 一句话总结：CVF OpenAccess paper. Open the paper page for full abstract and method details.
   - 任务设定：异常检测或分布外识别，可类比伪装目标的弱异常发现。
   - 方法核心：视觉-语言对齐，把语义文本信息引入检测或分割。
   - 实验结论：当前来源只提供标题级信息；需要打开论文页确认数据集、指标和消融。
   - 和我课题的关系：可补充 COD 中纹理、边界、几何先验不足的问题。
   - 可借鉴点：边界/频域增强模块；跨域鲁棒性、不确定性或异常分数。
   - 可改进点：可结合多尺度语义上下文，避免只强化纹理导致误检。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

### 当日 COD / 伪装目标检测相关

1. **Open-Vocabulary Camouflaged Object Segmentation**
   - Source: arXiv, 2023-11-19
   - Authors: Youwei Pang, Xiaoqi Zhao, Jiaming Zuo, Lihe Zhang, Huchuan Lu
   - Tags: COD, open-vocabulary, VLM/MLLM, boundary/frequency, depth/geometry, low-level
   - Links: [paper](http://arxiv.org/abs/2311.11241v3) / [pdf](http://arxiv.org/pdf/2311.11241v3)
   - 论文：Open-Vocabulary Camouflaged Object Segmentation
   - 一句话总结：Recently, the emergence of the large-scale vision-language model (VLM), such as CLIP, has opened the way towards open-world object perception. Many works have explored the utilization of pre-trained VLM for th...
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：视觉-语言对齐，把语义文本信息引入检测或分割。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；prompt 设计、类别文本构造、免训练迁移流程；候选 mask 生成、视觉-语言筛选、推理式定位；边界/频域增强模块；深度或几何先验融合。
   - 可改进点：可改进 prompt 自动生成、负样本约束和 mask 置信度校准。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

2. **Debate-Enhanced Pseudo Labeling and Frequency-Aware Progressive Debiasing for Weakly-Supervised Camouflaged Object Detection with Scribble Annotations**
   - Source: arXiv, 2025-12-23
   - Authors: Jiawei Ge, Jiuxin Cao, Xinyi Li, Xuelin Zhu, Chang Liu et al.
   - Tags: COD, unsupervised, SAM, boundary/frequency
   - Links: [paper](http://arxiv.org/abs/2512.20260v5) / [pdf](http://arxiv.org/pdf/2512.20260v5)
   - 论文：Debate-Enhanced Pseudo Labeling and Frequency-Aware Progressive Debiasing for Weakly-Supervised Camouflaged Object Detection with Scribble Annotations
   - 一句话总结：Weakly-Supervised Camouflaged Object Detection (WSCOD) aims to locate and segment objects that are visually concealed within their surrounding scenes, relying solely on sparse supervision such as scribble anno...
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：借助 SAM/基础分割模型产生候选 mask，再做筛选或适配。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；候选 mask 生成、视觉-语言筛选、推理式定位；边界/频域增强模块。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

3. **SAM3-Adapter: Efficient Adaptation of Segment Anything 3 for Camouflage Object Segmentation, Shadow Detection, and Medical Image Segmentation**
   - Source: arXiv, 2025-11-24
   - Authors: Tianrun Chen, Runlong Cao, Xinda Yu, Lanyun Zhu, Chaotao Ding et al.
   - Tags: COD, SAM, medical imaging
   - Links: [paper](http://arxiv.org/abs/2511.19425v1) / [pdf](http://arxiv.org/pdf/2511.19425v1)
   - 论文：SAM3-Adapter: Efficient Adaptation of Segment Anything 3 for Camouflage Object Segmentation, Shadow Detection, and Medical Image Segmentation
   - 一句话总结：The rapid rise of large-scale foundation models has reshaped the landscape of image segmentation, with models such as Segment Anything achieving unprecedented versatility across diverse vision tasks. However,...
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：借助 SAM/基础分割模型产生候选 mask，再做筛选或适配。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；候选 mask 生成、视觉-语言筛选、推理式定位。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

4. **SAM2-Adapter: Evaluating & Adapting Segment Anything 2 in Downstream Tasks: Camouflage, Shadow, Medical Image Segmentation, and More**
   - Source: arXiv, 2024-08-08
   - Authors: Tianrun Chen, Ankang Lu, Lanyun Zhu, Chaotao Ding, Chunan Yu et al.
   - Tags: COD, SAM, medical imaging
   - Links: [paper](http://arxiv.org/abs/2408.04579v2) / [pdf](http://arxiv.org/pdf/2408.04579v2)
   - 论文：SAM2-Adapter: Evaluating & Adapting Segment Anything 2 in Downstream Tasks: Camouflage, Shadow, Medical Image Segmentation, and More
   - 一句话总结：The advent of large models, also known as foundation models, has significantly transformed the AI research landscape, with models like Segment Anything (SAM) achieving notable success in diverse image segmenta...
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：借助 SAM/基础分割模型产生候选 mask，再做筛选或适配。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；候选 mask 生成、视觉-语言筛选、推理式定位。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

5. **UCOD-DPL: Unsupervised Camouflaged Object Detection via Dynamic Pseudo-label Learning**
   - Source: arXiv, 2025-06-08
   - Authors: Weiqi Yan, Lvhai Chen, Huaijia Kou, Shengchuan Zhang, Yan Zhang et al.
   - Tags: COD, unsupervised, boundary/frequency, remote sensing
   - Links: [paper](http://arxiv.org/abs/2506.07087v1) / [pdf](http://arxiv.org/pdf/2506.07087v1)
   - 论文：UCOD-DPL: Unsupervised Camouflaged Object Detection via Dynamic Pseudo-label Learning
   - 一句话总结：Unsupervised Camoflaged Object Detection (UCOD) has gained attention since it doesn't need to rely on extensive pixel-level labels. Existing UCOD methods typically generate pseudo-labels using fixed strategies...
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：边界感知建模，适合改善伪装目标轮廓不清的问题。
   - 实验结论：摘要未给出强实验信号；先看实验表格和图 1，再决定是否精读。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；边界/频域增强模块。
   - 可改进点：可尝试引入基础模型、文本先验或更强的环境上下文建模。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

6. **High-Resolution Underwater Camouflaged Object Detection: GBU-UCOD Dataset and Topology-Aware and Frequency-Decoupled Networks**
   - Source: arXiv, 2026-02-03
   - Authors: Wenji Wu, Shuo Ye, Yiyu Liu, Jiguang He, Zhuo Wang et al.
   - Tags: COD, diffusion, boundary/frequency, depth/geometry, saliency/transparent
   - Links: [paper](http://arxiv.org/abs/2602.03591v1) / [pdf](http://arxiv.org/pdf/2602.03591v1)
   - 论文：High-Resolution Underwater Camouflaged Object Detection: GBU-UCOD Dataset and Topology-Aware and Frequency-Decoupled Networks
   - 一句话总结：Underwater Camouflaged Object Detection (UCOD) is a challenging task due to the extreme visual similarity between targets and backgrounds across varying marine depths. Existing methods often struggle with topo...
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：借助 SAM/基础分割模型产生候选 mask，再做筛选或适配。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；边界/频域增强模块；深度或几何先验融合。
   - 可改进点：可尝试引入基础模型、文本先验或更强的环境上下文建模。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

7. **EReCu: Pseudo-label Evolution Fusion and Refinement with Multi-Cue Learning for Unsupervised Camouflage Detection**
   - Source: arXiv, 2026-03-12
   - Authors: Shuo Jiang, Gaojia Zhang, Min Tan, Yufei Yin, Gang Pan
   - Tags: COD, unsupervised, diffusion, boundary/frequency, depth/geometry, low-level
   - Links: [paper](http://arxiv.org/abs/2603.11521v1) / [pdf](http://arxiv.org/pdf/2603.11521v1)
   - 论文：EReCu: Pseudo-label Evolution Fusion and Refinement with Multi-Cue Learning for Unsupervised Camouflage Detection
   - 一句话总结：Unsupervised Camouflaged Object Detection (UCOD) remains a challenging task due to the high intrinsic similarity between target objects and their surroundings, as well as the reliance on noisy pseudo-labels th...
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：边界感知建模，适合改善伪装目标轮廓不清的问题。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；边界/频域增强模块；深度或几何先验融合。
   - 可改进点：可尝试引入基础模型、文本先验或更强的环境上下文建模。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

8. **A Survey of Camouflaged Object Detection and Beyond**
   - Source: arXiv, 2024-08-26
   - Authors: Fengyang Xiao, Sujie Hu, Yuqi Shen, Chengyu Fang, Jinfa Huang et al.
   - Tags: COD, diffusion, video
   - Links: [paper](http://arxiv.org/abs/2408.14562v1) / [pdf](http://arxiv.org/pdf/2408.14562v1)
   - 论文：A Survey of Camouflaged Object Detection and Beyond
   - 一句话总结：Camouflaged Object Detection (COD) refers to the task of identifying and segmenting objects that blend seamlessly into their surroundings, posing a significant challenge for computer vision systems. In recent...
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：摘要层面未显示明确模块，建议先看方法图确认 backbone、监督信号和损失设计。
   - 实验结论：可能包含新数据集/基准；适合看评测协议、失败案例和是否能服务 COD。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析。
   - 可改进点：可尝试引入基础模型、文本先验或更强的环境上下文建模。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

9. **Concealed Object Segmentation with Hierarchical Coherence Modeling**
   - Source: arXiv, 2024-01-22
   - Authors: Fengyang Xiao, Pan Zhang, Chunming He, Runze Hu, Yutao Liu
   - Tags: COD, diffusion, saliency/transparent
   - Links: [paper](http://arxiv.org/abs/2401.11767v1) / [pdf](http://arxiv.org/pdf/2401.11767v1)
   - 论文：Concealed Object Segmentation with Hierarchical Coherence Modeling
   - 一句话总结：Concealed object segmentation (COS) is a challenging task that involves localizing and segmenting those concealed objects that are visually blended with their surrounding environments. Despite achieving remark...
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：摘要层面未显示明确模块，建议先看方法图确认 backbone、监督信号和损失设计。
   - 实验结论：摘要未给出强实验信号；先看实验表格和图 1，再决定是否精读。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析。
   - 可改进点：可尝试引入基础模型、文本先验或更强的环境上下文建模。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

10. **First RAG, Second SEG: A Training-Free Paradigm for Camouflaged Object Detection**
   - Source: arXiv, 2025-08-21
   - Authors: Wutao Liu, YiDan Wang, Pan Gao
   - Tags: COD, training-free, unsupervised, SAM, retrieval/prototype, anomaly/OOD, saliency/transparent
   - Links: [paper](http://arxiv.org/abs/2508.15313v2) / [pdf](http://arxiv.org/pdf/2508.15313v2)
   - 论文：First RAG, Second SEG: A Training-Free Paradigm for Camouflaged Object Detection
   - 一句话总结：Camouflaged object detection (COD) poses a significant challenge in computer vision due to the high similarity between objects and their backgrounds. Existing approaches often rely on heavy training and large...
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：提示学习或提示生成，重点看文本/视觉 prompt 如何约束定位。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；prompt 设计、类别文本构造、免训练迁移流程；候选 mask 生成、视觉-语言筛选、推理式定位；跨域鲁棒性、不确定性或异常分数。
   - 可改进点：可改进 prompt 自动生成、负样本约束和 mask 置信度校准。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

11. **ZS-VCOS: Zero-Shot Video Camouflaged Object Segmentation By Optical Flow and Open Vocabulary Object Detection**
   - Source: arXiv, 2025-04-10
   - Authors: Wenqi Guo, Mohamed Shehata, Shan Du
   - Tags: COD, open-vocabulary, unsupervised, SAM, VLM/MLLM, diffusion, video
   - Links: [paper](http://arxiv.org/abs/2505.01431v2) / [pdf](http://arxiv.org/pdf/2505.01431v2)
   - 论文：ZS-VCOS: Zero-Shot Video Camouflaged Object Segmentation By Optical Flow and Open Vocabulary Object Detection
   - 一句话总结：Camouflaged object segmentation presents unique challenges compared to traditional segmentation tasks, primarily due to the high similarity in patterns and colors between camouflaged objects and their backgrou...
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：借助 SAM/基础分割模型产生候选 mask，再做筛选或适配。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；prompt 设计、类别文本构造、免训练迁移流程；候选 mask 生成、视觉-语言筛选、推理式定位。
   - 可改进点：可改进 prompt 自动生成、负样本约束和 mask 置信度校准。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

12. **BED-SAM2: Boundary-Enhanced-Depth SAM2 via Monocular Geometric Priors**
   - Source: arXiv, 2026-05-24
   - Authors: Tyler Rust, Dara McNally, Kyle O'Donnell, Colin Kelly, Chandra Kambhamettu
   - Tags: COD, boundary/frequency, depth/geometry, saliency/transparent
   - Links: [paper](http://arxiv.org/abs/2605.24893v1) / [pdf](http://arxiv.org/pdf/2605.24893v1)
   - 论文：BED-SAM2: Boundary-Enhanced-Depth SAM2 via Monocular Geometric Priors
   - 一句话总结：Building upon the SAM2 vision foundation model for downstream segmentation, this study introduces Boundary Enhanced Depth (BED)-SAM2. The SAM2 Hiera encoder architecture is modified to directly encode monocula...
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：借助 SAM/基础分割模型产生候选 mask，再做筛选或适配。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；边界/频域增强模块；深度或几何先验融合。
   - 可改进点：可尝试引入基础模型、文本先验或更强的环境上下文建模。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

13. **SAM2-UNeXT: An Improved High-Resolution Baseline for Adapting Foundation Models to Downstream Segmentation Tasks**
   - Source: arXiv, 2025-08-05
   - Authors: Xinyu Xiong, Zihuang Wu, Lei Zhang, Lei Lu, Ming Li et al.
   - Tags: COD, SAM, remote sensing, saliency/transparent
   - Links: [paper](http://arxiv.org/abs/2508.03566v1) / [pdf](http://arxiv.org/pdf/2508.03566v1)
   - 论文：SAM2-UNeXT: An Improved High-Resolution Baseline for Adapting Foundation Models to Downstream Segmentation Tasks
   - 一句话总结：Recent studies have highlighted the potential of adapting the Segment Anything Model (SAM) for various downstream tasks. However, constructing a more powerful and generalizable encoder to further enhance perfo...
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：借助 SAM/基础分割模型产生候选 mask，再做筛选或适配。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；候选 mask 生成、视觉-语言筛选、推理式定位。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

14. **COMPrompter: reconceptualized segment anything model with multiprompt network for camouflaged object detection**
   - Source: arXiv, 2024-11-28
   - Authors: Xiaoqin Zhang, Zhenni Yu, Li Zhao, Deng-Ping Fan, Guobao Xiao
   - Tags: COD, SAM, boundary/frequency
   - Links: [paper](http://arxiv.org/abs/2411.18858v1) / [pdf](http://arxiv.org/pdf/2411.18858v1)
   - 论文：COMPrompter: reconceptualized segment anything model with multiprompt network for camouflaged object detection
   - 一句话总结：We rethink the segment anything model (SAM) and propose a novel multiprompt network called COMPrompter for camouflaged object detection (COD). SAM has zero-shot generalization ability beyond other models and c...
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：提示学习或提示生成，重点看文本/视觉 prompt 如何约束定位。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；候选 mask 生成、视觉-语言筛选、推理式定位；边界/频域增强模块。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

15. **Assisted Refinement Network Based on Channel Information Interaction for Camouflaged and Salient Object Detection**
   - Source: arXiv, 2025-12-12
   - Authors: Kuan Wang, Yanjun Qin, Mengge Lu, Liejun Wang, Xiaoming Tao
   - Tags: COD, diffusion, boundary/frequency, low-level, saliency/transparent
   - Links: [paper](http://arxiv.org/abs/2512.11369v1) / [pdf](http://arxiv.org/pdf/2512.11369v1)
   - 论文：Assisted Refinement Network Based on Channel Information Interaction for Camouflaged and Salient Object Detection
   - 一句话总结：Camouflaged Object Detection (COD) stands as a significant challenge in computer vision, dedicated to identifying and segmenting objects visually highly integrated with their backgrounds. Current mainstream me...
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：借助 SAM/基础分割模型产生候选 mask，再做筛选或适配。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；边界/频域增强模块。
   - 可改进点：可尝试引入基础模型、文本先验或更强的环境上下文建模。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

16. **Depth-guided Texture Diffusion for Image Semantic Segmentation**
   - Source: arXiv, 2024-08-17
   - Authors: Wei Sun, Yuan Li, Qixiang Ye, Jianbin Jiao, Yanzhao Zhou
   - Tags: COD, diffusion, boundary/frequency, depth/geometry, saliency/transparent
   - Links: [paper](http://arxiv.org/abs/2408.09097v1) / [pdf](http://arxiv.org/pdf/2408.09097v1)
   - 论文：Depth-guided Texture Diffusion for Image Semantic Segmentation
   - 一句话总结：Depth information provides valuable insights into the 3D structure especially the outline of objects, which can be utilized to improve the semantic segmentation tasks. However, a naive fusion of depth informat...
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：扩散/生成式建模，可能用于数据合成、先验建模或掩码优化。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；边界/频域增强模块；深度或几何先验融合。
   - 可改进点：可尝试引入基础模型、文本先验或更强的环境上下文建模。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

17. **Exploring Deeper! Segment Anything Model with Depth Perception for Camouflaged Object Detection**
   - Source: arXiv, 2024-07-17
   - Authors: Zhenni Yu, Xiaoqin Zhang, Li Zhao, Yi Bin, Guobao Xiao
   - Tags: COD, SAM, boundary/frequency, depth/geometry
   - Links: [paper](http://arxiv.org/abs/2407.12339v1) / [pdf](http://arxiv.org/pdf/2407.12339v1)
   - 论文：Exploring Deeper! Segment Anything Model with Depth Perception for Camouflaged Object Detection
   - 一句话总结：This paper introduces a new Segment Anything Model with Depth Perception (DSAM) for Camouflaged Object Detection (COD). DSAM exploits the zero-shot capability of SAM to realize precise segmentation in the RGB-...
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：提示学习或提示生成，重点看文本/视觉 prompt 如何约束定位。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；候选 mask 生成、视觉-语言筛选、推理式定位；边界/频域增强模块；深度或几何先验融合。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

18. **RIDE: Retinex-Informed Decoupling for Exposing Concealed Objects**
   - Source: arXiv, 2026-05-14
   - Authors: Chunming He, Rihan Zhang, Dingming Zhang, Chengyu Fang, Longxiang Tang et al.
   - Tags: COD, boundary/frequency, saliency/transparent
   - Links: [paper](http://arxiv.org/abs/2605.15450v1) / [pdf](http://arxiv.org/pdf/2605.15450v1)
   - 论文：RIDE: Retinex-Informed Decoupling for Exposing Concealed Objects
   - 一句话总结：Concealed Object Segmentation (COS) encompasses a family of dense-prediction tasks, including camouflaged object detection, polyp segmentation, transparent object detection, and industrial defect inspection, w...
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：借助 SAM/基础分割模型产生候选 mask，再做筛选或适配。
   - 实验结论：摘要未给出强实验信号；先看实验表格和图 1，再决定是否精读。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；边界/频域增强模块。
   - 可改进点：可尝试引入基础模型、文本先验或更强的环境上下文建模。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

19. **FCL-COD: Weakly Supervised Camouflaged Object Detection with Frequency-aware and Contrastive Learning**
   - Source: arXiv, 2026-03-24
   - Authors: Jingchen Ni, Quan Zhang, Dan Jiang, Keyu Lv, Ke Zhang et al.
   - Tags: COD, unsupervised, SAM, diffusion, boundary/frequency
   - Links: [paper](http://arxiv.org/abs/2603.22969v1) / [pdf](http://arxiv.org/pdf/2603.22969v1)
   - 论文：FCL-COD: Weakly Supervised Camouflaged Object Detection with Frequency-aware and Contrastive Learning
   - 一句话总结：Existing camouflage object detection (COD) methods typically rely on fully-supervised learning guided by mask annotations. However, obtaining mask annotations is time-consuming and labor-intensive.
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：借助 SAM/基础分割模型产生候选 mask，再做筛选或适配。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；候选 mask 生成、视觉-语言筛选、推理式定位；边界/频域增强模块。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

20. **When SAM2 Meets Video Camouflaged Object Segmentation: A Comprehensive Evaluation and Adaptation**
   - Source: arXiv, 2024-09-27
   - Authors: Yuli Zhou, Guolei Sun, Yawei Li, Guo-Sen Xie, Luca Benini et al.
   - Tags: COD, SAM, VLM/MLLM, diffusion, video
   - Links: [paper](http://arxiv.org/abs/2409.18653v2) / [pdf](http://arxiv.org/pdf/2409.18653v2)
   - 论文：When SAM2 Meets Video Camouflaged Object Segmentation: A Comprehensive Evaluation and Adaptation
   - 一句话总结：This study investigates the application and performance of the Segment Anything Model 2 (SAM2) in the challenging task of video camouflaged object segmentation (VCOS). VCOS involves detecting objects that blen...
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：提示学习或提示生成，重点看文本/视觉 prompt 如何约束定位。
   - 实验结论：可能包含新数据集/基准；适合看评测协议、失败案例和是否能服务 COD。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；候选 mask 生成、视觉-语言筛选、推理式定位。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

21. **SAM Fails to Segment Anything? -- SAM-Adapter: Adapting SAM in Underperformed Scenes: Camouflage, Shadow, Medical Image Segmentation, and More**
   - Source: arXiv, 2023-04-18
   - Authors: Tianrun Chen, Lanyun Zhu, Chaotao Ding, Runlong Cao, Yan Wang et al.
   - Tags: COD, SAM, boundary/frequency, remote sensing, medical imaging
   - Links: [paper](http://arxiv.org/abs/2304.09148v3) / [pdf](http://arxiv.org/pdf/2304.09148v3)
   - 论文：SAM Fails to Segment Anything? -- SAM-Adapter: Adapting SAM in Underperformed Scenes: Camouflage, Shadow, Medical Image Segmentation, and More
   - 一句话总结：The emergence of large models, also known as foundation models, has brought significant advancements to AI research. One such model is Segment Anything (SAM), which is designed for image segmentation tasks.
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：提示学习或提示生成，重点看文本/视觉 prompt 如何约束定位。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；候选 mask 生成、视觉-语言筛选、推理式定位；边界/频域增强模块。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

22. **C3Net: Context-Contrast Network for Camouflaged Object Detection**
   - Source: arXiv, 2025-11-16
   - Authors: Baber Jan, Aiman H. El-Maleh, Abdul Jabbar Siddiqui, Abdul Bais, Saeed Anwar
   - Tags: COD, diffusion, boundary/frequency, low-level, saliency/transparent
   - Links: [paper](http://arxiv.org/abs/2511.12627v1) / [pdf](http://arxiv.org/pdf/2511.12627v1)
   - 论文：C3Net: Context-Contrast Network for Camouflaged Object Detection
   - 一句话总结：Camouflaged object detection identifies objects that blend seamlessly with their surroundings through similar colors, textures, and patterns. This task challenges both traditional segmentation methods and mode...
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：借助 SAM/基础分割模型产生候选 mask，再做筛选或适配。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；边界/频域增强模块。
   - 可改进点：可尝试引入基础模型、文本先验或更强的环境上下文建模。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

23. **SAM2-UNet: Segment Anything 2 Makes Strong Encoder for Natural and Medical Image Segmentation**
   - Source: arXiv, 2024-08-16
   - Authors: Xinyu Xiong, Zihuang Wu, Shuangyi Tan, Wenxue Li, Feilong Tang et al.
   - Tags: COD, SAM, diffusion, saliency/transparent, medical imaging
   - Links: [paper](http://arxiv.org/abs/2408.08870v1) / [pdf](http://arxiv.org/pdf/2408.08870v1)
   - 论文：SAM2-UNet: Segment Anything 2 Makes Strong Encoder for Natural and Medical Image Segmentation
   - 一句话总结：Image segmentation plays an important role in vision understanding. Recently, the emerging vision foundation models continuously achieved superior performance on various tasks.
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：借助 SAM/基础分割模型产生候选 mask，再做筛选或适配。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；候选 mask 生成、视觉-语言筛选、推理式定位。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

24. **Weakly Supervised Camouflaged Object Detection Based on the SAM Model and Mask Guidance**
   - Source: arXiv, 2026-05-25
   - Authors: Xia Li, Xinran Liu, Lin Qi, Junyu Dong
   - Tags: COD, unsupervised, SAM, boundary/frequency, low-level
   - Links: [paper](http://arxiv.org/abs/2605.25385v1) / [pdf](http://arxiv.org/pdf/2605.25385v1)
   - 论文：Weakly Supervised Camouflaged Object Detection Based on the SAM Model and Mask Guidance
   - 一句话总结：Camouflaged object detection (COD) from a single image is a challenging task due to the high similarity between objects and their surroundings. Existing fully supervised methods require labor-intensive pixel-l...
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：提示学习或提示生成，重点看文本/视觉 prompt 如何约束定位。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；候选 mask 生成、视觉-语言筛选、推理式定位；边界/频域增强模块。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

25. **Exploring Boundary-Aware Spatial-Frequency Fusion for Camouflaged Object Detection**
   - Source: arXiv, 2026-04-20
   - Authors: Song Yu, Yang Hu, Haokang Ding, Zhifang Liao, Yucheng Song
   - Tags: COD, diffusion, boundary/frequency
   - Links: [paper](http://arxiv.org/abs/2604.17879v1) / [pdf](http://arxiv.org/pdf/2604.17879v1)
   - 论文：Exploring Boundary-Aware Spatial-Frequency Fusion for Camouflaged Object Detection
   - 一句话总结：Camouflaged Object Detection is challenging due to the high degree of similarity between camouflaged objects and their surrounding backgrounds. Current COD methods mainly rely on edge extraction in the spatial...
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：频域/纹理特征增强，适合处理伪装背景与目标细粒度差异。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；边界/频域增强模块。
   - 可改进点：可尝试引入基础模型、文本先验或更强的环境上下文建模。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

26. **IP-SAM: Prompt-Space Conditioning for Prompt-Absent Camouflaged Object Detection**
   - Source: arXiv, 2026-03-28
   - Authors: Huiyao Zhang, Jin Bai, Rui Guo, JianWen Tan, HongFei Wang et al.
   - Tags: COD, SAM, diffusion
   - Links: [paper](http://arxiv.org/abs/2603.27250v1) / [pdf](http://arxiv.org/pdf/2603.27250v1)
   - 论文：IP-SAM: Prompt-Space Conditioning for Prompt-Absent Camouflaged Object Detection
   - 一句话总结：Prompt-conditioned foundation segmenters have emerged as a dominant paradigm for image segmentation, where explicit spatial prompts (e.g., points, boxes, masks) guide mask decoding. However, many real-world de...
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：提示学习或提示生成，重点看文本/视觉 prompt 如何约束定位。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；候选 mask 生成、视觉-语言筛选、推理式定位。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

27. **Language-Guided Structure-Aware Network for Camouflaged Object Detection**
   - Source: arXiv, 2026-03-25
   - Authors: Min Zhang
   - Tags: COD, boundary/frequency, low-level
   - Links: [paper](http://arxiv.org/abs/2603.24355v1) / [pdf](http://arxiv.org/pdf/2603.24355v1)
   - 论文：Language-Guided Structure-Aware Network for Camouflaged Object Detection
   - 一句话总结：Camouflaged Object Detection (COD) aims to segment objects that are highly integrated with the background in terms of color, texture, and structure, making it a highly challenging task in computer vision. Alth...
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：提示学习或提示生成，重点看文本/视觉 prompt 如何约束定位。
   - 实验结论：可能包含新数据集/基准；适合看评测协议、失败案例和是否能服务 COD。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；边界/频域增强模块。
   - 可改进点：可尝试引入基础模型、文本先验或更强的环境上下文建模。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

28. **Beyond Single Images: Retrieval Self-Augmented Unsupervised Camouflaged Object Detection**
   - Source: arXiv, 2025-10-21
   - Authors: Ji Du, Xin Wang, Fangwei Hao, Mingyang Yu, Chunyuan Chen et al.
   - Tags: COD, unsupervised, retrieval/prototype
   - Links: [paper](http://arxiv.org/abs/2510.18437v1) / [pdf](http://arxiv.org/pdf/2510.18437v1)
   - 论文：Beyond Single Images: Retrieval Self-Augmented Unsupervised Camouflaged Object Detection
   - 一句话总结：At the core of Camouflaged Object Detection (COD) lies segmenting objects from their highly similar surroundings. Previous efforts navigate this challenge primarily through image-level modeling or annotation-b...
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：提示学习或提示生成，重点看文本/视觉 prompt 如何约束定位。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析。
   - 可改进点：可尝试引入基础模型、文本先验或更强的环境上下文建模。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

29. **HyperCOD: The First Challenging Benchmark and Baseline for Hyperspectral Camouflaged Object Detection**
   - Source: arXiv, 2026-01-07
   - Authors: Shuyan Bai, Tingfa Xu, Peifu Liu, Yuhao Qiu, Huiyan Bai et al.
   - Tags: COD, SAM, remote sensing, saliency/transparent
   - Links: [paper](http://arxiv.org/abs/2601.03736v1) / [pdf](http://arxiv.org/pdf/2601.03736v1)
   - 论文：HyperCOD: The First Challenging Benchmark and Baseline for Hyperspectral Camouflaged Object Detection
   - 一句话总结：RGB-based camouflaged object detection struggles in real-world scenarios where color and texture cues are ambiguous. While hyperspectral image offers a powerful alternative by capturing fine-grained spectral s...
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：提示学习或提示生成，重点看文本/视觉 prompt 如何约束定位。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；候选 mask 生成、视觉-语言筛选、推理式定位。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

30. **DGA-Net: Enhancing SAM with Depth Prompting and Graph-Anchor Guidance for Camouflaged Object Detection**
   - Source: arXiv, 2026-01-06
   - Authors: Yuetong Li, Qing Zhang, Yilin Zhao, Gongyang Li, Zeming Liu
   - Tags: COD, SAM, depth/geometry, low-level
   - Links: [paper](http://arxiv.org/abs/2601.02831v1) / [pdf](http://arxiv.org/pdf/2601.02831v1)
   - 论文：DGA-Net: Enhancing SAM with Depth Prompting and Graph-Anchor Guidance for Camouflaged Object Detection
   - 一句话总结：To fully exploit depth cues in Camouflaged Object Detection (COD), we present DGA-Net, a specialized framework that adapts the Segment Anything Model (SAM) via a novel ``depth prompting" paradigm. Distinguishe...
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：提示学习或提示生成，重点看文本/视觉 prompt 如何约束定位。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；候选 mask 生成、视觉-语言筛选、推理式定位；深度或几何先验融合。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

31. **Phantom-Insight: Adaptive Multi-cue Fusion for Video Camouflaged Object Detection with Multimodal LLM**
   - Source: arXiv, 2025-09-08
   - Authors: Hua Zhang, Changjiang Luo, Ruoyu Chen
   - Tags: COD, SAM, VLM/MLLM, diffusion, boundary/frequency, video
   - Links: [paper](http://arxiv.org/abs/2509.06422v1) / [pdf](http://arxiv.org/pdf/2509.06422v1)
   - 论文：Phantom-Insight: Adaptive Multi-cue Fusion for Video Camouflaged Object Detection with Multimodal LLM
   - 一句话总结：Video camouflaged object detection (VCOD) is challenging due to dynamic environments. Existing methods face two main issues: (1) SAM-based methods struggle to separate camouflaged object edges due to model fre...
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：提示学习或提示生成，重点看文本/视觉 prompt 如何约束定位。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；候选 mask 生成、视觉-语言筛选、推理式定位；边界/频域增强模块。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

32. **Improving SAM for Camouflaged Object Detection via Dual Stream Adapters**
   - Source: arXiv, 2025-03-08
   - Authors: Jiaming Liu, Linghe Kong, Guihai Chen
   - Tags: COD, SAM, diffusion, boundary/frequency, depth/geometry
   - Links: [paper](http://arxiv.org/abs/2503.06042v2) / [pdf](http://arxiv.org/pdf/2503.06042v2)
   - 论文：Improving SAM for Camouflaged Object Detection via Dual Stream Adapters
   - 一句话总结：Segment anything model (SAM) has shown impressive general-purpose segmentation performance on natural images, but its performance on camouflaged object detection (COD) is unsatisfactory. In this paper, we prop...
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：提示学习或提示生成，重点看文本/视觉 prompt 如何约束定位。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；候选 mask 生成、视觉-语言筛选、推理式定位；边界/频域增强模块；深度或几何先验融合。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

33. **Refining Context-Entangled Content Segmentation via Curriculum Selection and Anti-Curriculum Promotion**
   - Source: arXiv, 2026-02-01
   - Authors: Chunming He, Rihan Zhang, Fengyang Xiao, Dingming Zhang, Zhiwen Cao et al.
   - Tags: COD, boundary/frequency, video, low-level
   - Links: [paper](http://arxiv.org/abs/2602.01183v2) / [pdf](http://arxiv.org/pdf/2602.01183v2)
   - 论文：Refining Context-Entangled Content Segmentation via Curriculum Selection and Anti-Curriculum Promotion
   - 一句话总结：Biological learning proceeds from easy to difficult tasks, gradually reinforcing perception and robustness. Inspired by this principle, we address Context-Entangled Content Segmentation (CECS), a challenging s...
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：借助 SAM/基础分割模型产生候选 mask，再做筛选或适配。
   - 实验结论：可能包含新数据集/基准；适合看评测协议、失败案例和是否能服务 COD。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；边界/频域增强模块。
   - 可改进点：可尝试引入基础模型、文本先验或更强的环境上下文建模。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

34. **Exploring Depth Contribution for Camouflaged Object Detection**
   - Source: arXiv, 2021-06-24
   - Authors: Mochu Xiang, Jing Zhang, Yunqiu Lv, Aixuan Li, Yiran Zhong et al.
   - Tags: COD, diffusion, depth/geometry, remote sensing
   - Links: [paper](http://arxiv.org/abs/2106.13217v3) / [pdf](http://arxiv.org/pdf/2106.13217v3)
   - 论文：Exploring Depth Contribution for Camouflaged Object Detection
   - 一句话总结：Camouflaged object detection (COD) aims to segment camouflaged objects hiding in the environment, which is challenging due to the similar appearance of camouflaged objects and their surroundings. Research in b...
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：扩散/生成式建模，可能用于数据合成、先验建模或掩码优化。
   - 实验结论：可能包含新数据集/基准；适合看评测协议、失败案例和是否能服务 COD。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；深度或几何先验融合。
   - 可改进点：可尝试引入基础模型、文本先验或更强的环境上下文建模。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

35. **FakeMix Augmentation Improves Transparent Object Detection**
   - Source: arXiv, 2021-03-24
   - Authors: Yang Cao, Zhengqiang Zhang, Enze Xie, Qibin Hou, Kai Zhao et al.
   - Tags: COD, boundary/frequency, saliency/transparent
   - Links: [paper](http://arxiv.org/abs/2103.13279v2) / [pdf](http://arxiv.org/pdf/2103.13279v2)
   - 论文：FakeMix Augmentation Improves Transparent Object Detection
   - 一句话总结：Detecting transparent objects in natural scenes is challenging due to the low contrast in texture, brightness and colors. Recent deep-learning-based works reveal that it is effective to leverage boundaries for...
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：借助 SAM/基础分割模型产生候选 mask，再做筛选或适配。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；边界/频域增强模块。
   - 可改进点：可尝试引入基础模型、文本先验或更强的环境上下文建模。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

### 当日泛计算机视觉方法池

1. **Video Object Segmentation-Aware Audio Generation**
   - Source: Crossref / IJCV / CCF-A / 顶刊 / International Journal of Computer Vision, 2026-06-23
   - Authors: Ilpo Viertola, Vladimir Iashin, Esa Rahtu
   - Tags: diffusion, video, remote sensing
   - Links: [paper](https://doi.org/10.1007/s11263-026-02911-2)
   - 论文：Video Object Segmentation-Aware Audio Generation
   - 一句话总结：Abstract Existing multimodal audio generation models often lack precise user control, which limits their applicability in professional Foley workflows. In particular, these models focus on the entire video and...
   - 任务设定：遥感/大场景密集视觉任务，关注小目标、尺度变化和复杂背景。
   - 方法核心：扩散/生成式建模，可能用于数据合成、先验建模或掩码优化。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：不是 COD 直系论文，但可能提供可迁移的视觉表征、训练策略或评测思路。
   - 可借鉴点：任务建模、损失函数、消融组织方式。
   - 可改进点：可思考是否缺少 COD 场景验证、复杂背景失败分析或轻量化部署。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

2. **SegRAG: Training-Free Retrieval-Augmented Semantic Segmentation**
   - Source: arXiv, 2026-05-17
   - Authors: Abderrahmene Boudiaf, Irfan Hussain, Sajid Javed
   - Tags: open-vocabulary, training-free, reasoning, retrieval/prototype
   - Links: [paper](http://arxiv.org/abs/2605.17630v2) / [pdf](http://arxiv.org/pdf/2605.17630v2)
   - 论文：SegRAG: Training-Free Retrieval-Augmented Semantic Segmentation
   - 一句话总结：Open-vocabulary segmentation models such as SAM3 perform well across broad categories via text prompting, yet degrade when target classes are visually underrepresented in pretraining or depart from canonical d...
   - 任务设定：开放词汇视觉识别/分割，目标类别或文本提示在训练时未必出现。
   - 方法核心：提示学习或提示生成，重点看文本/视觉 prompt 如何约束定位。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：适合拓展到开放词汇、零样本或少标注 COD。
   - 可借鉴点：prompt 设计、类别文本构造、免训练迁移流程。
   - 可改进点：可改进 prompt 自动生成、负样本约束和 mask 置信度校准。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

3. **OVS-DINO: Open-Vocabulary Segmentation via Structure-Aligned SAM-DINO with Language Guidance**
   - Source: arXiv, 2026-04-09
   - Authors: Haoxi Zeng, Qiankun Liu, Yi Bin, Haiyue Zhang, Yujuan Ding et al.
   - Tags: open-vocabulary, unsupervised, SAM, boundary/frequency, remote sensing
   - Links: [paper](http://arxiv.org/abs/2604.08461v1) / [pdf](http://arxiv.org/pdf/2604.08461v1)
   - 论文：OVS-DINO: Open-Vocabulary Segmentation via Structure-Aligned SAM-DINO with Language Guidance
   - 一句话总结：Open-Vocabulary Segmentation (OVS) aims to segment image regions beyond predefined category sets by leveraging semantic descriptions. While CLIP based approaches excel in semantic generalization, they frequent...
   - 任务设定：开放词汇视觉识别/分割，目标类别或文本提示在训练时未必出现。
   - 方法核心：借助 SAM/基础分割模型产生候选 mask，再做筛选或适配。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：适合拓展到开放词汇、零样本或少标注 COD。
   - 可借鉴点：prompt 设计、类别文本构造、免训练迁移流程；候选 mask 生成、视觉-语言筛选、推理式定位；边界/频域增强模块。
   - 可改进点：可改进 prompt 自动生成、负样本约束和 mask 置信度校准。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

4. **SegEarth-OV: Towards Training-Free Open-Vocabulary Segmentation for Remote Sensing Images**
   - Source: arXiv, 2024-10-02
   - Authors: Kaiyu Li, Ruixun Liu, Xiangyong Cao, Xueru Bai, Feng Zhou et al.
   - Tags: open-vocabulary, training-free, remote sensing, anomaly/OOD
   - Links: [paper](http://arxiv.org/abs/2410.01768v2) / [pdf](http://arxiv.org/pdf/2410.01768v2)
   - 论文：SegEarth-OV: Towards Training-Free Open-Vocabulary Segmentation for Remote Sensing Images
   - 一句话总结：Remote sensing image plays an irreplaceable role in fields such as agriculture, water resources, military, and disaster relief. Pixel-level interpretation is a critical aspect of remote sensing image applicati...
   - 任务设定：开放词汇视觉识别/分割，目标类别或文本提示在训练时未必出现。
   - 方法核心：借助 SAM/基础分割模型产生候选 mask，再做筛选或适配。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：适合拓展到开放词汇、零样本或少标注 COD。
   - 可借鉴点：prompt 设计、类别文本构造、免训练迁移流程；跨域鲁棒性、不确定性或异常分数。
   - 可改进点：可改进 prompt 自动生成、负样本约束和 mask 置信度校准。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

5. **TF-SSD: A Strong Pipeline via Synergic Mask Filter for Training-free Co-salient Object Detection**
   - Source: arXiv, 2026-04-01
   - Authors: Zhijin He, Shuo Jin, Siyue Yu, Shuwei Wu, Bingfeng Zhang et al.
   - Tags: training-free, SAM, retrieval/prototype, saliency/transparent
   - Links: [paper](http://arxiv.org/abs/2604.00549v1) / [pdf](http://arxiv.org/pdf/2604.00549v1)
   - 论文：TF-SSD: A Strong Pipeline via Synergic Mask Filter for Training-free Co-salient Object Detection
   - 一句话总结：Co-salient Object Detection (CoSOD) aims to segment salient objects that consistently appear across a group of related images. Despite the notable progress achieved by recent training-based approaches, they st...
   - 任务设定：免训练或少训练迁移设定，重点看 prompt、特征选择和后处理。
   - 方法核心：借助 SAM/基础分割模型产生候选 mask，再做筛选或适配。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：和 COD 同属低显著/弱边界目标发现，可迁移目标-背景分离思想。
   - 可借鉴点：prompt 设计、类别文本构造、免训练迁移流程；候选 mask 生成、视觉-语言筛选、推理式定位。
   - 可改进点：可改进 prompt 自动生成、负样本约束和 mask 置信度校准。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

6. **SOCO: Benchmarking Semantic Object Correspondence in Vision Foundation Models**
   - Source: arXiv, 2026-05-29
   - Authors: Olaf Dünkel, Basavaraj Sunagad, Haoran Wang, David T. Hoffmann, Christian Theobalt et al.
   - Tags: VLM/MLLM, diffusion, depth/geometry, video
   - Links: [paper](http://arxiv.org/abs/2605.31597v2) / [pdf](http://arxiv.org/pdf/2605.31597v2)
   - 论文：SOCO: Benchmarking Semantic Object Correspondence in Vision Foundation Models
   - 一句话总结：Measuring structured object understanding in vision foundation models remains challenging due to inconsistent evaluation protocols and limited part-level supervision. Semantic correspondence (SC) evaluates thi...
   - 任务设定：基础模型驱动的视觉定位/分割/推理，可用于自动提示生成或 mask 筛选。
   - 方法核心：提示学习或提示生成，重点看文本/视觉 prompt 如何约束定位。
   - 实验结论：可能包含新数据集/基准；适合看评测协议、失败案例和是否能服务 COD。
   - 和我课题的关系：可补充 COD 中纹理、边界、几何先验不足的问题。
   - 可借鉴点：候选 mask 生成、视觉-语言筛选、推理式定位；深度或几何先验融合。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

7. **Anatomy-Guided Residual Motion Diffusion for Controllable 4D Cardiac MRI Synthesis**
   - Source: arXiv, 2026-06-25
   - Authors: Yiheng Cao, Gustavo Andrade-Miranda, Jiatian Zhang, Lingxiao Zhao, Xin Gao
   - Tags: unsupervised, diffusion, boundary/frequency, depth/geometry, video, medical imaging
   - Links: [paper](http://arxiv.org/abs/2606.26764v1) / [pdf](http://arxiv.org/pdf/2606.26764v1)
   - 论文：Anatomy-Guided Residual Motion Diffusion for Controllable 4D Cardiac MRI Synthesis
   - 一句话总结：Developing robust artificial intelligence models for 4D (3D + time) medical imaging is constrained by limited annotated data, inter-device domain shifts, and privacy restrictions. To address this, we propose a...
   - 任务设定：医学影像分割/检测，常见弱边界、低对比和标注稀缺问题。
   - 方法核心：扩散/生成式建模，可能用于数据合成、先验建模或掩码优化。
   - 实验结论：可能包含新数据集/基准；适合看评测协议、失败案例和是否能服务 COD。
   - 和我课题的关系：可补充 COD 中纹理、边界、几何先验不足的问题。
   - 可借鉴点：边界/频域增强模块；深度或几何先验融合。
   - 可改进点：可结合多尺度语义上下文，避免只强化纹理导致误检。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

8. **M$^4$-SAM: Multi-Modal Mixture-of-Experts with Memory-Augmented SAM for RGB-D Video Salient Object Detection**
   - Source: arXiv, 2026-05-12
   - Authors: Jiyuan Liu, Jia Lin, Xiaofei Zhou, Runmin Cong, Deyang Liu et al.
   - Tags: SAM, retrieval/prototype, video, saliency/transparent
   - Links: [paper](http://arxiv.org/abs/2605.11760v1) / [pdf](http://arxiv.org/pdf/2605.11760v1)
   - 论文：M$^4$-SAM: Multi-Modal Mixture-of-Experts with Memory-Augmented SAM for RGB-D Video Salient Object Detection
   - 一句话总结：The Segment Anything Model 2 (SAM2) has emerged as a foundation model for universal segmentation. Owing to its generalizable visual representations, SAM2 has been successfully applied to various downstream tas...
   - 任务设定：基础模型驱动的视觉定位/分割/推理，可用于自动提示生成或 mask 筛选。
   - 方法核心：提示学习或提示生成，重点看文本/视觉 prompt 如何约束定位。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：和 COD 同属低显著/弱边界目标发现，可迁移目标-背景分离思想。
   - 可借鉴点：候选 mask 生成、视觉-语言筛选、推理式定位。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

9. **VesselSim: learning 3D blood vessel segmentation without expert annotations**
   - Source: arXiv, 2026-05-25
   - Authors: Erin Rainville, Melissa Ananian, Tristan Mirolla, Hassan Rivaz, Yiming Xiao
   - Tags: boundary/frequency, depth/geometry, anomaly/OOD, domain adaptation, medical imaging
   - Links: [paper](http://arxiv.org/abs/2605.26277v2) / [pdf](http://arxiv.org/pdf/2605.26277v2)
   - 论文：VesselSim: learning 3D blood vessel segmentation without expert annotations
   - 一句话总结：Blood vessel segmentation is a core task in medical image analysis for the care of vascular diseases and surgical planning, yet the challenges of providing expert vascular annotations pose a major obstacle for...
   - 任务设定：异常检测或分布外识别，可类比伪装目标的弱异常发现。
   - 方法核心：边界感知建模，适合改善伪装目标轮廓不清的问题。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：可补充 COD 中纹理、边界、几何先验不足的问题。
   - 可借鉴点：边界/频域增强模块；深度或几何先验融合；跨域鲁棒性、不确定性或异常分数。
   - 可改进点：可结合多尺度语义上下文，避免只强化纹理导致误检。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

10. **MM-OVSeg:Multimodal Optical-SAR Fusion for Open-Vocabulary Segmentation in Remote Sensing**
   - Source: arXiv, 2026-03-18
   - Authors: Yimin Wei, Aoran Xiao, Hongruixuan Chen, Junshi Xia, Naoto Yokoya
   - Tags: open-vocabulary, VLM/MLLM, diffusion, remote sensing
   - Links: [paper](http://arxiv.org/abs/2603.17528v2) / [pdf](http://arxiv.org/pdf/2603.17528v2)
   - 论文：MM-OVSeg:Multimodal Optical-SAR Fusion for Open-Vocabulary Segmentation in Remote Sensing
   - 一句话总结：Open-vocabulary segmentation enables pixel-level recognition from an open set of textual categories, allowing generalization beyond fixed classes. Despite great potential in remote sensing, progress in this ar...
   - 任务设定：开放词汇视觉识别/分割，目标类别或文本提示在训练时未必出现。
   - 方法核心：视觉-语言对齐，把语义文本信息引入检测或分割。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：适合拓展到开放词汇、零样本或少标注 COD。
   - 可借鉴点：prompt 设计、类别文本构造、免训练迁移流程；候选 mask 生成、视觉-语言筛选、推理式定位。
   - 可改进点：可改进 prompt 自动生成、负样本约束和 mask 置信度校准。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

11. **ActiveSAM: Image-Conditional Class Pruning for Fast and Accurate Open-Vocabulary Segmentation**
   - Source: arXiv, 2026-06-15
   - Authors: Tran Dinh Tien, Zhiqiang Shen
   - Tags: open-vocabulary, training-free, SAM, diffusion, remote sensing
   - Links: [paper](http://arxiv.org/abs/2606.16996v1) / [pdf](http://arxiv.org/pdf/2606.16996v1)
   - 论文：ActiveSAM: Image-Conditional Class Pruning for Fast and Accurate Open-Vocabulary Segmentation
   - 一句话总结：Segment Anything Model 3 (SAM 3) provides a strong frozen backbone for concept-prompted segmentation, but applying it directly to open-vocabulary semantic segmentation (OVSS) is inefficient: full-resolution de...
   - 任务设定：开放词汇视觉识别/分割，目标类别或文本提示在训练时未必出现。
   - 方法核心：提示学习或提示生成，重点看文本/视觉 prompt 如何约束定位。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：适合拓展到开放词汇、零样本或少标注 COD。
   - 可借鉴点：prompt 设计、类别文本构造、免训练迁移流程；候选 mask 生成、视觉-语言筛选、推理式定位。
   - 可改进点：可改进 prompt 自动生成、负样本约束和 mask 置信度校准。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

12. **Vision-Language Model Reasoning for Contextual Semantic Mapping in Intralogistics**
   - Source: arXiv, 2026-06-23
   - Authors: Marvin Rüdt, Hao Pang, Constantin Enke, Zäzilia Seibold, Kai Furmans
   - Tags: open-vocabulary, SAM, VLM/MLLM, reasoning, depth/geometry
   - Links: [paper](http://arxiv.org/abs/2606.24814v1) / [pdf](http://arxiv.org/pdf/2606.24814v1)
   - 论文：Vision-Language Model Reasoning for Contextual Semantic Mapping in Intralogistics
   - 一句话总结：Autonomous mobile robots operating in intralogistics environments rely on geometric maps for localization and navigation, but lack semantic understanding of objects and their contextual properties. We present...
   - 任务设定：开放词汇视觉识别/分割，目标类别或文本提示在训练时未必出现。
   - 方法核心：提示学习或提示生成，重点看文本/视觉 prompt 如何约束定位。
   - 实验结论：摘要强调消融、鲁棒性或泛化；适合优先看实验设计和跨域表现。
   - 和我课题的关系：适合拓展到开放词汇、零样本或少标注 COD。
   - 可借鉴点：prompt 设计、类别文本构造、免训练迁移流程；候选 mask 生成、视觉-语言筛选、推理式定位；深度或几何先验融合。
   - 可改进点：可改进 prompt 自动生成、负样本约束和 mask 置信度校准。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

13. **Jolia: Concept-Level Vision-Language Alignment for 3D CT Contrastive Learning**
   - Source: arXiv, 2026-06-23
   - Authors: Julien Khlaut, Charles Corbière, Baptiste Callard, Amaury Prat, Leo Butsanets et al.
   - Tags: VLM/MLLM, depth/geometry, medical imaging
   - Links: [paper](http://arxiv.org/abs/2606.24570v2) / [pdf](http://arxiv.org/pdf/2606.24570v2)
   - 论文：Jolia: Concept-Level Vision-Language Alignment for 3D CT Contrastive Learning
   - 一句话总结：Vision-language contrastive pretraining has become the dominant recipe for 3D medical foundation models, leveraging the large volumes of paired scans and reports produced in clinical practice. However, medical...
   - 任务设定：基础模型驱动的视觉定位/分割/推理，可用于自动提示生成或 mask 筛选。
   - 方法核心：视觉-语言对齐，把语义文本信息引入检测或分割。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：可补充 COD 中纹理、边界、几何先验不足的问题。
   - 可借鉴点：候选 mask 生成、视觉-语言筛选、推理式定位；深度或几何先验融合。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

14. **ARTEMIS: Agent-guided Reliability-aware Temporal Mask Evolution for Imperfectly Supervised Video Polyp Segmentation**
   - Source: arXiv, 2026-06-18
   - Authors: Tong Wang, Siwen Wang, Yaolei Qi, Jinxing Zhou, Yuting He et al.
   - Tags: VLM/MLLM, retrieval/prototype, boundary/frequency, depth/geometry, video
   - Links: [paper](http://arxiv.org/abs/2606.20161v1) / [pdf](http://arxiv.org/pdf/2606.20161v1)
   - 论文：ARTEMIS: Agent-guided Reliability-aware Temporal Mask Evolution for Imperfectly Supervised Video Polyp Segmentation
   - 一句话总结：Imperfectly supervised video polyp segmentation (VPS) aims to learn dense, temporally consistent masks from inexpensive supervision, including weak annotations (points, scribbles) and semi-supervision with few...
   - 任务设定：基础模型驱动的视觉定位/分割/推理，可用于自动提示生成或 mask 筛选。
   - 方法核心：借助 SAM/基础分割模型产生候选 mask，再做筛选或适配。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：可补充 COD 中纹理、边界、几何先验不足的问题。
   - 可借鉴点：候选 mask 生成、视觉-语言筛选、推理式定位；边界/频域增强模块；深度或几何先验融合。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

15. **Training-free Cross-domain Few-shot Segmentation via Robust Semantic Representation and Matching**
   - Source: arXiv, 2026-06-23
   - Authors: Sujun Sun, Mingwu Ren, Haofeng Zhang
   - Tags: training-free, diffusion, retrieval/prototype, boundary/frequency, low-level
   - Links: [paper](http://arxiv.org/abs/2606.24297v1) / [pdf](http://arxiv.org/pdf/2606.24297v1)
   - 论文：Training-free Cross-domain Few-shot Segmentation via Robust Semantic Representation and Matching
   - 一句话总结：Cross-domain Few-shot Segmentation (CD-FSS) aims to transfer knowledge learned from source domain to distinct target domains, segmenting unseen target classes with only a few annotated samples. Although existi...
   - 任务设定：免训练或少训练迁移设定，重点看 prompt、特征选择和后处理。
   - 方法核心：借助 SAM/基础分割模型产生候选 mask，再做筛选或适配。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：适合拓展到开放词汇、零样本或少标注 COD。
   - 可借鉴点：prompt 设计、类别文本构造、免训练迁移流程；边界/频域增强模块。
   - 可改进点：可改进 prompt 自动生成、负样本约束和 mask 置信度校准。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

16. **SWARD: Stochastic Window-Attention-Based Relational Distillation for Cross-Architectural Semantic Segmentation**
   - Source: arXiv, 2026-05-31
   - Authors: Aditya Makineni, Qing Tian
   - Tags: retrieval/prototype, boundary/frequency, medical imaging
   - Links: [paper](http://arxiv.org/abs/2606.00999v1) / [pdf](http://arxiv.org/pdf/2606.00999v1)
   - 论文：SWARD: Stochastic Window-Attention-Based Relational Distillation for Cross-Architectural Semantic Segmentation
   - 一句话总结：Large-scale vision foundation models have driven substantial gains on dense prediction tasks such as semantic segmentation, but their size makes deployment impractical in resource-constrained settings, motivat...
   - 任务设定：医学影像分割/检测，常见弱边界、低对比和标注稀缺问题。
   - 方法核心：借助 SAM/基础分割模型产生候选 mask，再做筛选或适配。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：可补充 COD 中纹理、边界、几何先验不足的问题。
   - 可借鉴点：边界/频域增强模块。
   - 可改进点：可结合多尺度语义上下文，避免只强化纹理导致误检。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

17. **MLFFM-SegDiff: A Multi-Level Feature Fusion Diffusion Model for Skin Lesion Segmentation**
   - Source: arXiv, 2026-06-25
   - Authors: Jingjun Gu, Chaojie Shen, Yifeng Cao, Wei Zhang, Yiliu Li et al.
   - Tags: diffusion, boundary/frequency, low-level, saliency/transparent, medical imaging
   - Links: [paper](http://arxiv.org/abs/2606.26712v1) / [pdf](http://arxiv.org/pdf/2606.26712v1)
   - 论文：MLFFM-SegDiff: A Multi-Level Feature Fusion Diffusion Model for Skin Lesion Segmentation
   - 一句话总结：Skin lesion segmentation is a key task in computer-aided dermatological diagnosis, where accuracy directly impacts downstream analysis and disease classification. However, dermoscopic images are challenging du...
   - 任务设定：医学影像分割/检测，常见弱边界、低对比和标注稀缺问题。
   - 方法核心：扩散/生成式建模，可能用于数据合成、先验建模或掩码优化。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：和 COD 同属低显著/弱边界目标发现，可迁移目标-背景分离思想。
   - 可借鉴点：边界/频域增强模块。
   - 可改进点：可结合多尺度语义上下文，避免只强化纹理导致误检。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

18. **High-Fidelity Synthetic Transmission Electron Microscopy Image Generation Using Diffusion Probabilistic Models for Data-Limited Semiconductor Metrology**
   - Source: arXiv, 2026-06-23
   - Authors: Johannes Boehm, Bappaditya Dey
   - Tags: diffusion, low-level
   - Links: [paper](http://arxiv.org/abs/2606.24817v1) / [pdf](http://arxiv.org/pdf/2606.24817v1)
   - 论文：High-Fidelity Synthetic Transmission Electron Microscopy Image Generation Using Diffusion Probabilistic Models for Data-Limited Semiconductor Metrology
   - 一句话总结：Advanced semiconductor nodes drastically increased demand for Transmission Electron Microscopy (TEM), yet destructive sample preparation, slow imaging and high costs severely limit the availability of diverse...
   - 任务设定：通用计算机视觉任务，先判断是否能迁移到 COD 的感知、定位或分割环节。
   - 方法核心：扩散/生成式建模，可能用于数据合成、先验建模或掩码优化。
   - 实验结论：可能包含新数据集/基准；适合看评测协议、失败案例和是否能服务 COD。
   - 和我课题的关系：不是 COD 直系论文，但可能提供可迁移的视觉表征、训练策略或评测思路。
   - 可借鉴点：任务建模、损失函数、消融组织方式。
   - 可改进点：可思考是否缺少 COD 场景验证、复杂背景失败分析或轻量化部署。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

19. **EnTrust: Modeling Inter-Modal Conflict for Trustworthy Multimodal Medical Image Analysis**
   - Source: arXiv, 2026-06-19
   - Authors: Dwarikanath Mahapatra, Abhijit Das, Behzad Bozorgtabar, Zongyuan Ge, Sudipta Roy et al.
   - Tags: diffusion, medical imaging
   - Links: [paper](http://arxiv.org/abs/2606.21384v1) / [pdf](http://arxiv.org/pdf/2606.21384v1)
   - 论文：EnTrust: Modeling Inter-Modal Conflict for Trustworthy Multimodal Medical Image Analysis
   - 一句话总结：Multimodal medical imaging fuses complementary anatomical and functional information, yet modalities frequently disagree in pathologically heterogeneous regions. Current segmentation models handle this in one...
   - 任务设定：医学影像分割/检测，常见弱边界、低对比和标注稀缺问题。
   - 方法核心：扩散/生成式建模，可能用于数据合成、先验建模或掩码优化。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：不是 COD 直系论文，但可能提供可迁移的视觉表征、训练策略或评测思路。
   - 可借鉴点：任务建模、损失函数、消融组织方式。
   - 可改进点：可思考是否缺少 COD 场景验证、复杂背景失败分析或轻量化部署。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

20. **SAM-DAQ: Segment Anything Model with Depth-guided Adaptive Queries for RGB-D Video Salient Object Detection**
   - Source: arXiv, 2025-11-13
   - Authors: Jia Lin, Xiaofei Zhou, Jiyuan Liu, Runmin Cong, Guodao Zhang et al.
   - Tags: SAM, diffusion, retrieval/prototype, depth/geometry, video, saliency/transparent
   - Links: [paper](http://arxiv.org/abs/2511.09870v1) / [pdf](http://arxiv.org/pdf/2511.09870v1)
   - 论文：SAM-DAQ: Segment Anything Model with Depth-guided Adaptive Queries for RGB-D Video Salient Object Detection
   - 一句话总结：Recently segment anything model (SAM) has attracted widespread concerns, and it is often treated as a vision foundation model for universal segmentation. Some researchers have attempted to directly apply the f...
   - 任务设定：基础模型驱动的视觉定位/分割/推理，可用于自动提示生成或 mask 筛选。
   - 方法核心：提示学习或提示生成，重点看文本/视觉 prompt 如何约束定位。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：和 COD 同属低显著/弱边界目标发现，可迁移目标-背景分离思想。
   - 可借鉴点：候选 mask 生成、视觉-语言筛选、推理式定位；深度或几何先验融合。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

21. **AD-DINOv3: Enhancing DINOv3 for Zero-Shot Anomaly Detection with Anomaly-Aware Calibration**
   - Source: arXiv, 2025-09-17
   - Authors: Jingyi Yuan, Jianxiong Ye, Wenkang Chen, Chenqiang Gao
   - Tags: VLM/MLLM, diffusion, anomaly/OOD
   - Links: [paper](http://arxiv.org/abs/2509.14084v2) / [pdf](http://arxiv.org/pdf/2509.14084v2)
   - 论文：AD-DINOv3: Enhancing DINOv3 for Zero-Shot Anomaly Detection with Anomaly-Aware Calibration
   - 一句话总结：Zero-Shot Anomaly Detection (ZSAD) seeks to identify anomalies from arbitrary novel categories, offering a scalable and annotation-efficient solution. Traditionally, most ZSAD works have been based on the CLIP...
   - 任务设定：基础模型驱动的视觉定位/分割/推理，可用于自动提示生成或 mask 筛选。
   - 方法核心：提示学习或提示生成，重点看文本/视觉 prompt 如何约束定位。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：可用于伪装目标的语义描述、环境理解和候选区域判断。
   - 可借鉴点：候选 mask 生成、视觉-语言筛选、推理式定位；跨域鲁棒性、不确定性或异常分数。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

22. **FiLo++: Zero-/Few-Shot Anomaly Detection by Fused Fine-Grained Descriptions and Deformable Localization**
   - Source: arXiv, 2025-01-17
   - Authors: Zhaopeng Gu, Bingke Zhu, Guibo Zhu, Yingying Chen, Ming Tang et al.
   - Tags: reasoning, diffusion, anomaly/OOD
   - Links: [paper](http://arxiv.org/abs/2501.10067v2) / [pdf](http://arxiv.org/pdf/2501.10067v2)
   - 论文：FiLo++: Zero-/Few-Shot Anomaly Detection by Fused Fine-Grained Descriptions and Deformable Localization
   - 一句话总结：Anomaly detection methods typically require extensive normal samples from the target class for training, limiting their applicability in scenarios that require rapid adaptation, such as cold start. Zero-shot a...
   - 任务设定：异常检测或分布外识别，可类比伪装目标的弱异常发现。
   - 方法核心：提示学习或提示生成，重点看文本/视觉 prompt 如何约束定位。
   - 实验结论：可能包含新数据集/基准；适合看评测协议、失败案例和是否能服务 COD。
   - 和我课题的关系：可用于伪装目标的语义描述、环境理解和候选区域判断。
   - 可借鉴点：跨域鲁棒性、不确定性或异常分数。
   - 可改进点：可思考是否缺少 COD 场景验证、复杂背景失败分析或轻量化部署。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

23. **MAPSeg: Unified Unsupervised Domain Adaptation for Heterogeneous Medical Image Segmentation Based on 3D Masked Autoencoding and Pseudo-Labeling**
   - Source: CVPR 2024, 2024
   - Authors: Xuzhe Zhang, Yuhao Wu, Elsa Angelini, Ang Li, Jia Guo et al.
   - Tags: unsupervised, depth/geometry, domain adaptation, medical imaging
   - Links: [paper](https://openaccess.thecvf.com/content/CVPR2024/html/Zhang_MAPSeg_Unified_Unsupervised_Domain_Adaptation_for_Heterogeneous_Medical_Image_Segmentation_CVPR_2024_paper.html) / [pdf](https://openaccess.thecvf.com/content/CVPR2024/papers/Zhang_MAPSeg_Unified_Unsupervised_Domain_Adaptation_for_Heterogeneous_Medical_Image_Segmentation_CVPR_2024_paper.pdf)
   - 论文：MAPSeg: Unified Unsupervised Domain Adaptation for Heterogeneous Medical Image Segmentation Based on 3D Masked Autoencoding and Pseudo-Labeling
   - 一句话总结：CVF OpenAccess paper. Open the paper page for full abstract and method details.
   - 任务设定：医学影像分割/检测，常见弱边界、低对比和标注稀缺问题。
   - 方法核心：几何/深度线索建模，可能补充 RGB 外的结构先验。
   - 实验结论：当前来源只提供标题级信息；需要打开论文页确认数据集、指标和消融。
   - 和我课题的关系：可补充 COD 中纹理、边界、几何先验不足的问题。
   - 可借鉴点：深度或几何先验融合；跨域鲁棒性、不确定性或异常分数。
   - 可改进点：可验证在 COD 跨数据集上的泛化，加入目标缺失场景。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

24. **T-REN: Learning Text-Aligned Region Tokens Improves Dense Vision-Language Alignment and Scalability**
   - Source: arXiv, 2026-04-20
   - Authors: Savya Khosla, Sethuraman T, Aryan Chadha, Alex Schwing, Derek Hoiem
   - Tags: open-vocabulary, VLM/MLLM, diffusion, retrieval/prototype, depth/geometry, video
   - Links: [paper](http://arxiv.org/abs/2604.18573v1) / [pdf](http://arxiv.org/pdf/2604.18573v1)
   - 论文：T-REN: Learning Text-Aligned Region Tokens Improves Dense Vision-Language Alignment and Scalability
   - 一句话总结：Despite recent progress, vision-language encoders struggle with two core limitations: (1) weak alignment between language and dense vision features, which hurts tasks like open-vocabulary semantic segmentation...
   - 任务设定：开放词汇视觉识别/分割，目标类别或文本提示在训练时未必出现。
   - 方法核心：视觉-语言对齐，把语义文本信息引入检测或分割。
   - 实验结论：摘要未给出强实验信号；先看实验表格和图 1，再决定是否精读。
   - 和我课题的关系：适合拓展到开放词汇、零样本或少标注 COD。
   - 可借鉴点：prompt 设计、类别文本构造、免训练迁移流程；候选 mask 生成、视觉-语言筛选、推理式定位；深度或几何先验融合。
   - 可改进点：可改进 prompt 自动生成、负样本约束和 mask 置信度校准。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

25. **Towards Realistic Open-Vocabulary Remote Sensing Segmentation: Benchmark and Baseline**
   - Source: arXiv, 2026-04-17
   - Authors: Bingyu Li, Tao Huo, Haocheng Dong, Da Zhang, Zhiyuan Zhao et al.
   - Tags: open-vocabulary, remote sensing, anomaly/OOD
   - Links: [paper](http://arxiv.org/abs/2604.15652v1) / [pdf](http://arxiv.org/pdf/2604.15652v1)
   - 论文：Towards Realistic Open-Vocabulary Remote Sensing Segmentation: Benchmark and Baseline
   - 一句话总结：Open-vocabulary remote sensing image segmentation (OVRSIS) remains underexplored due to fragmented datasets, limited training diversity, and the lack of evaluation benchmarks that reflect realistic geospatial...
   - 任务设定：开放词汇视觉识别/分割，目标类别或文本提示在训练时未必出现。
   - 方法核心：异常/OOD 建模，把目标从复杂背景中作为低概率区域凸显出来。
   - 实验结论：可能包含新数据集/基准；适合看评测协议、失败案例和是否能服务 COD。
   - 和我课题的关系：适合拓展到开放词汇、零样本或少标注 COD。
   - 可借鉴点：prompt 设计、类别文本构造、免训练迁移流程；跨域鲁棒性、不确定性或异常分数。
   - 可改进点：可改进 prompt 自动生成、负样本约束和 mask 置信度校准。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

26. **TRACE: Evidence Grounding-Guided Multi-Video Event Understanding and Claim Generation**
   - Source: arXiv, 2026-05-16
   - Authors: Pengyu Yan, Akhil Gorugantu, Mahesh Bhosale, Abdul Wasi, Vishvesh Trivedi et al.
   - Tags: VLM/MLLM, reasoning, video
   - Links: [paper](http://arxiv.org/abs/2605.16740v2) / [pdf](http://arxiv.org/pdf/2605.16740v2)
   - 论文：TRACE: Evidence Grounding-Guided Multi-Video Event Understanding and Claim Generation
   - 一句话总结：Multi-video event understanding demands models that can locate and attribute query-relevant evidence scattered across long, heterogeneous video corpora. Existing large vision-language models (LVLMs) often unde...
   - 任务设定：基础模型驱动的视觉定位/分割/推理，可用于自动提示生成或 mask 筛选。
   - 方法核心：视觉-语言对齐，把语义文本信息引入检测或分割。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：可用于伪装目标的语义描述、环境理解和候选区域判断。
   - 可借鉴点：候选 mask 生成、视觉-语言筛选、推理式定位。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

27. **Segmentation, Detection and Explanation: A Unified Framework for CT Appearance Reasoning**
   - Source: arXiv, 2026-05-15
   - Authors: Yuyuan Liu, Can Peng, Yingyu Yang, Qianye Yang, Cheng Ouyang et al.
   - Tags: VLM/MLLM, reasoning, diffusion, medical imaging
   - Links: [paper](http://arxiv.org/abs/2605.15997v1) / [pdf](http://arxiv.org/pdf/2605.15997v1)
   - 论文：Segmentation, Detection and Explanation: A Unified Framework for CT Appearance Reasoning
   - 一句话总结：Recent progress in deep learning has significantly advanced CT image analysis, particularly for segmentation tasks. However, these advances are largely confined to image-level pattern recognition, with most me...
   - 任务设定：基础模型驱动的视觉定位/分割/推理，可用于自动提示生成或 mask 筛选。
   - 方法核心：提示学习或提示生成，重点看文本/视觉 prompt 如何约束定位。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：可用于伪装目标的语义描述、环境理解和候选区域判断。
   - 可借鉴点：候选 mask 生成、视觉-语言筛选、推理式定位。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

28. **SubspaceAD: Training-Free Few-Shot Anomaly Detection via Subspace Modeling**
   - Source: arXiv, 2026-02-26
   - Authors: Camile Lendering, Erkut Akdag, Egor Bondarev
   - Tags: training-free, VLM/MLLM, retrieval/prototype, remote sensing, anomaly/OOD
   - Links: [paper](http://arxiv.org/abs/2602.23013v3) / [pdf](http://arxiv.org/pdf/2602.23013v3)
   - 论文：SubspaceAD: Training-Free Few-Shot Anomaly Detection via Subspace Modeling
   - 一句话总结：Detecting visual anomalies in industrial inspection often requires training with only a few normal images per category. Recent few-shot methods achieve strong results employing foundation-model features, but t...
   - 任务设定：免训练或少训练迁移设定，重点看 prompt、特征选择和后处理。
   - 方法核心：提示学习或提示生成，重点看文本/视觉 prompt 如何约束定位。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：适合拓展到开放词汇、零样本或少标注 COD。
   - 可借鉴点：prompt 设计、类别文本构造、免训练迁移流程；候选 mask 生成、视觉-语言筛选、推理式定位；跨域鲁棒性、不确定性或异常分数。
   - 可改进点：可改进 prompt 自动生成、负样本约束和 mask 置信度校准。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

29. **ModuSeg: Decoupling Object Discovery and Semantic Retrieval for Training-Free Weakly Supervised Segmentation**
   - Source: arXiv, 2026-04-08
   - Authors: Qingze He, Fagui Liu, Dengke Zhang, Qingmao Wei, Quan Tang
   - Tags: training-free, unsupervised, retrieval/prototype, boundary/frequency, depth/geometry
   - Links: [paper](http://arxiv.org/abs/2604.07021v2) / [pdf](http://arxiv.org/pdf/2604.07021v2)
   - 论文：ModuSeg: Decoupling Object Discovery and Semantic Retrieval for Training-Free Weakly Supervised Segmentation
   - 一句话总结：Weakly supervised semantic segmentation aims to achieve pixel-level predictions using image-level labels. Existing methods typically entangle semantic recognition and object localization, which often leads mod...
   - 任务设定：免训练或少训练迁移设定，重点看 prompt、特征选择和后处理。
   - 方法核心：边界感知建模，适合改善伪装目标轮廓不清的问题。
   - 实验结论：可能包含新数据集/基准；适合看评测协议、失败案例和是否能服务 COD。
   - 和我课题的关系：适合拓展到开放词汇、零样本或少标注 COD。
   - 可借鉴点：prompt 设计、类别文本构造、免训练迁移流程；边界/频域增强模块；深度或几何先验融合。
   - 可改进点：可改进 prompt 自动生成、负样本约束和 mask 置信度校准。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

30. **Frequency Adapter with SAM for Generalized Medical Image Segmentation**
   - Source: arXiv, 2026-05-11
   - Authors: Phuoc-Nguyen Bui, Van-Nguyen Pham, Duc-Tai Le, Junghyun Bum, Hyunseung Choo
   - Tags: SAM, diffusion, boundary/frequency, remote sensing, domain adaptation, medical imaging
   - Links: [paper](http://arxiv.org/abs/2605.09925v1) / [pdf](http://arxiv.org/pdf/2605.09925v1)
   - 论文：Frequency Adapter with SAM for Generalized Medical Image Segmentation
   - 一句话总结：Medical image segmentation is a critical task in computer-aided diagnosis and treatment planning. However, deep learning models often struggle to generalize across datasets due to domain shifts arising from va...
   - 任务设定：基础模型驱动的视觉定位/分割/推理，可用于自动提示生成或 mask 筛选。
   - 方法核心：借助 SAM/基础分割模型产生候选 mask，再做筛选或适配。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：可补充 COD 中纹理、边界、几何先验不足的问题。
   - 可借鉴点：候选 mask 生成、视觉-语言筛选、推理式定位；边界/频域增强模块；跨域鲁棒性、不确定性或异常分数。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

31. **HPP: Hierarchical Programmatic Probing for Long Video Understanding by Decoupling Perception and Reasoning**
   - Source: arXiv, 2026-06-19
   - Authors: Awais Rauf, Ahmed Hasssan, Greg Slabaugh
   - Tags: VLM/MLLM, reasoning, retrieval/prototype, video
   - Links: [paper](http://arxiv.org/abs/2606.21734v1) / [pdf](http://arxiv.org/pdf/2606.21734v1)
   - 论文：HPP: Hierarchical Programmatic Probing for Long Video Understanding by Decoupling Perception and Reasoning
   - 一句话总结：Understanding long videos requires fine-grained perception and multi-step, higher-order reasoning over complex, long-range spatio-temporal dynamics. Vision-language models (VLMs) encode video frames into visua...
   - 任务设定：基础模型驱动的视觉定位/分割/推理，可用于自动提示生成或 mask 筛选。
   - 方法核心：视觉-语言对齐，把语义文本信息引入检测或分割。
   - 实验结论：可能包含新数据集/基准；适合看评测协议、失败案例和是否能服务 COD。
   - 和我课题的关系：可用于伪装目标的语义描述、环境理解和候选区域判断。
   - 可借鉴点：候选 mask 生成、视觉-语言筛选、推理式定位。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

32. **Flood Mapping from RGB imagery using a Vision Foundation Model**
   - Source: arXiv, 2026-06-23
   - Authors: Vladyslav Polushko, Tilman Bucher, Ronald Rösch, Thomas März, Markus Rauhut et al.
   - Tags: depth/geometry, remote sensing, anomaly/OOD
   - Links: [paper](http://arxiv.org/abs/2606.24120v1) / [pdf](http://arxiv.org/pdf/2606.24120v1)
   - 论文：Flood Mapping from RGB imagery using a Vision Foundation Model
   - 一句话总结：Timely, high-resolution maps of flood extent around settlements are essential for emergency response and damage assessment. We consider airborne RGB imagery for flood mapping as it can be collected rapidly at...
   - 任务设定：异常检测或分布外识别，可类比伪装目标的弱异常发现。
   - 方法核心：几何/深度线索建模，可能补充 RGB 外的结构先验。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：可补充 COD 中纹理、边界、几何先验不足的问题。
   - 可借鉴点：深度或几何先验融合；跨域鲁棒性、不确定性或异常分数。
   - 可改进点：可思考是否缺少 COD 场景验证、复杂背景失败分析或轻量化部署。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

33. **UniDrive: A Unified Vision-Language and Grounding Framework for Interpretable Risk Understanding in Autonomous Driving**
   - Source: arXiv, 2026-06-23
   - Authors: Xiaowei Gao, Pengxiang Li, Yitai Cheng, Ruihan Xu, James Haworth et al.
   - Tags: VLM/MLLM, reasoning, video
   - Links: [paper](http://arxiv.org/abs/2606.24759v1) / [pdf](http://arxiv.org/pdf/2606.24759v1)
   - 论文：UniDrive: A Unified Vision-Language and Grounding Framework for Interpretable Risk Understanding in Autonomous Driving
   - 一句话总结：Recent multimodal large language models (MLLMs) have shown strong potential for autonomous driving scene understanding, yet existing methods still face a fundamental trade-off between temporal reasoning and sp...
   - 任务设定：基础模型驱动的视觉定位/分割/推理，可用于自动提示生成或 mask 筛选。
   - 方法核心：视觉-语言对齐，把语义文本信息引入检测或分割。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：可用于伪装目标的语义描述、环境理解和候选区域判断。
   - 可借鉴点：候选 mask 生成、视觉-语言筛选、推理式定位。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

34. **Object Tokens as a Bridge Between Segmentation and Visual Question Answering in Robotic Surgery**
   - Source: arXiv, 2026-06-14
   - Authors: Yiping Li, Ronald de Jong, Romy van Jaarsveld, Franco Badaloni, Gino Kuiper et al.
   - Tags: SAM, VLM/MLLM, reasoning
   - Links: [paper](http://arxiv.org/abs/2606.15861v1) / [pdf](http://arxiv.org/pdf/2606.15861v1)
   - 论文：Object Tokens as a Bridge Between Segmentation and Visual Question Answering in Robotic Surgery
   - 一句话总结：Visual Question Answering (VQA) in robotic surgery, referred to as surgical VQA, requires high-level understanding of complex surgical scenes and the integration of visual perception with language reasoning, w...
   - 任务设定：基础模型驱动的视觉定位/分割/推理，可用于自动提示生成或 mask 筛选。
   - 方法核心：借助 SAM/基础分割模型产生候选 mask，再做筛选或适配。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：可用于伪装目标的语义描述、环境理解和候选区域判断。
   - 可借鉴点：候选 mask 生成、视觉-语言筛选、推理式定位。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

35. **Prob-BBDM: a Probabilistic Brownian Bridge Diffusion Model for MRI sequence image-to-image translation**
   - Source: arXiv, 2026-06-23
   - Authors: Martin Valls, Pascal Bourdon, Christine Fernandez-Maloigne, Guillaume Herpe, David Helbert
   - Tags: diffusion, depth/geometry, medical imaging
   - Links: [paper](http://arxiv.org/abs/2606.24313v1) / [pdf](http://arxiv.org/pdf/2606.24313v1)
   - 论文：Prob-BBDM: a Probabilistic Brownian Bridge Diffusion Model for MRI sequence image-to-image translation
   - 一句话总结：AI-driven image-to-image synthesis is rapidly advancing, with growing applications in medical imaging. Multi-modal image analysis plays a crucial role in optimizing examination quality, yet acquiring multiple...
   - 任务设定：医学影像分割/检测，常见弱边界、低对比和标注稀缺问题。
   - 方法核心：扩散/生成式建模，可能用于数据合成、先验建模或掩码优化。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：可补充 COD 中纹理、边界、几何先验不足的问题。
   - 可借鉴点：深度或几何先验融合。
   - 可改进点：可思考是否缺少 COD 场景验证、复杂背景失败分析或轻量化部署。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

36. **SARIF: Segment Anything for Robust Image Forensics**
   - Source: arXiv, 2026-06-19
   - Authors: Dong-Hyun Moon, Ju-Hyeon Nam, Sang-Chul Lee
   - Tags: SAM, remote sensing, domain adaptation
   - Links: [paper](http://arxiv.org/abs/2606.21108v1) / [pdf](http://arxiv.org/pdf/2606.21108v1)
   - 论文：SARIF: Segment Anything for Robust Image Forensics
   - 一句话总结：Image forgery localization remains challenging due to diverse manipulation techniques and distribution shifts. Existing forgery localization models achieve high accuracy on benchmarks but often struggle with c...
   - 任务设定：基础模型驱动的视觉定位/分割/推理，可用于自动提示生成或 mask 筛选。
   - 方法核心：提示学习或提示生成，重点看文本/视觉 prompt 如何约束定位。
   - 实验结论：可能包含新数据集/基准；适合看评测协议、失败案例和是否能服务 COD。
   - 和我课题的关系：不是 COD 直系论文，但可能提供可迁移的视觉表征、训练策略或评测思路。
   - 可借鉴点：候选 mask 生成、视觉-语言筛选、推理式定位；跨域鲁棒性、不确定性或异常分数。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

37. **SegmentAnyTreeV2: Scaling Transformer-Based Tree Instance Segmentation Across Sensors, Platforms, and Forests**
   - Source: arXiv, 2026-06-06
   - Authors: Maciej Wielgosz, Stefano Puliti, Rasmus Astrup
   - Tags: domain adaptation
   - Links: [paper](http://arxiv.org/abs/2606.08206v2) / [pdf](http://arxiv.org/pdf/2606.08206v2)
   - 论文：SegmentAnyTreeV2: Scaling Transformer-Based Tree Instance Segmentation Across Sensors, Platforms, and Forests
   - 一句话总结：We present SegmentAnyTreeV2, a sensor- and platform-agnostic framework for semantic and instance segmentation of forest point clouds. The model combines a serialization-based Point Transformer v3 backbone with...
   - 任务设定：通用计算机视觉任务，先判断是否能迁移到 COD 的感知、定位或分割环节。
   - 方法核心：测试时适配或域泛化，重点看跨数据集鲁棒性。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：不是 COD 直系论文，但可能提供可迁移的视觉表征、训练策略或评测思路。
   - 可借鉴点：跨域鲁棒性、不确定性或异常分数。
   - 可改进点：可验证在 COD 跨数据集上的泛化，加入目标缺失场景。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

38. **RAVEN: Radar Adaptive Vision Encoders for Efficient Chirp-wise Object Detection and Segmentation**
   - Source: CVPR 2026, 2026
   - Authors: Anuvab Sen, Mir Sayeed Mohammad, Saibal Mukhopadhyay
   - Tags: computer vision
   - Links: [paper](https://openaccess.thecvf.com/content/CVPR2026/html/Sen_RAVEN_Radar_Adaptive_Vision_Encoders_for_Efficient_Chirp-wise_Object_Detection_CVPR_2026_paper.html) / [pdf](https://openaccess.thecvf.com/content/CVPR2026/papers/Sen_RAVEN_Radar_Adaptive_Vision_Encoders_for_Efficient_Chirp-wise_Object_Detection_CVPR_2026_paper.pdf)
   - 论文：RAVEN: Radar Adaptive Vision Encoders for Efficient Chirp-wise Object Detection and Segmentation
   - 一句话总结：CVF OpenAccess paper. Open the paper page for full abstract and method details.
   - 任务设定：通用计算机视觉任务，先判断是否能迁移到 COD 的感知、定位或分割环节。
   - 方法核心：摘要层面未显示明确模块，建议先看方法图确认 backbone、监督信号和损失设计。
   - 实验结论：当前来源只提供标题级信息；需要打开论文页确认数据集、指标和消融。
   - 和我课题的关系：不是 COD 直系论文，但可能提供可迁移的视觉表征、训练策略或评测思路。
   - 可借鉴点：任务建模、损失函数、消融组织方式。
   - 可改进点：可思考是否缺少 COD 场景验证、复杂背景失败分析或轻量化部署。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

39. **Hierarchical Point-Patch Fusion with Adaptive Patch Codebook for 3D Shape Anomaly Detection**
   - Source: CVPR 2026, 2026
   - Authors: Xueyang Kang, Zizhao Li, Tian Lan, Dong Gong, Kourosh Khoshelham et al.
   - Tags: depth/geometry, anomaly/OOD
   - Links: [paper](https://openaccess.thecvf.com/content/CVPR2026/html/Kang_Hierarchical_Point-Patch_Fusion_with_Adaptive_Patch_Codebook_for_3D_Shape_CVPR_2026_paper.html) / [pdf](https://openaccess.thecvf.com/content/CVPR2026/papers/Kang_Hierarchical_Point-Patch_Fusion_with_Adaptive_Patch_Codebook_for_3D_Shape_CVPR_2026_paper.pdf)
   - 论文：Hierarchical Point-Patch Fusion with Adaptive Patch Codebook for 3D Shape Anomaly Detection
   - 一句话总结：CVF OpenAccess paper. Open the paper page for full abstract and method details.
   - 任务设定：异常检测或分布外识别，可类比伪装目标的弱异常发现。
   - 方法核心：几何/深度线索建模，可能补充 RGB 外的结构先验。
   - 实验结论：当前来源只提供标题级信息；需要打开论文页确认数据集、指标和消融。
   - 和我课题的关系：可补充 COD 中纹理、边界、几何先验不足的问题。
   - 可借鉴点：深度或几何先验融合；跨域鲁棒性、不确定性或异常分数。
   - 可改进点：可思考是否缺少 COD 场景验证、复杂背景失败分析或轻量化部署。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

40. **Crane: Context-Guided Prompt Learning and Attention Refinement for Zero-Shot Anomaly Detection**
   - Source: arXiv, 2025-04-15
   - Authors: Alireza Salehi, Mohammadreza Salehi, Reshad Hosseini, Cees G. M. Snoek, Makoto Yamada et al.
   - Tags: diffusion, boundary/frequency, anomaly/OOD
   - Links: [paper](http://arxiv.org/abs/2504.11055v2) / [pdf](http://arxiv.org/pdf/2504.11055v2)
   - 论文：Crane: Context-Guided Prompt Learning and Attention Refinement for Zero-Shot Anomaly Detection
   - 一句话总结：Anomaly Detection involves identifying deviations from normal data distributions and is critical in fields such as medical diagnostics and industrial defect detection. Traditional AD methods typically require...
   - 任务设定：异常检测或分布外识别，可类比伪装目标的弱异常发现。
   - 方法核心：提示学习或提示生成，重点看文本/视觉 prompt 如何约束定位。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：可补充 COD 中纹理、边界、几何先验不足的问题。
   - 可借鉴点：边界/频域增强模块；跨域鲁棒性、不确定性或异常分数。
   - 可改进点：可结合多尺度语义上下文，避免只强化纹理导致误检。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

41. **Exploring Efficient Open-Vocabulary Segmentation in the Remote Sensing**
   - Source: arXiv, 2025-09-15
   - Authors: Bingyu Li, Haocheng Dong, Da Zhang, Zhiyuan Zhao, Junyu Gao et al.
   - Tags: open-vocabulary, VLM/MLLM, boundary/frequency, remote sensing, domain adaptation
   - Links: [paper](http://arxiv.org/abs/2509.12040v2) / [pdf](http://arxiv.org/pdf/2509.12040v2)
   - 论文：Exploring Efficient Open-Vocabulary Segmentation in the Remote Sensing
   - 一句话总结：Open-Vocabulary Remote Sensing Image Segmentation (OVRSIS), an emerging task that adapts Open-Vocabulary Segmentation (OVS) to the remote sensing (RS) domain, remains underexplored due to the absence of a unif...
   - 任务设定：开放词汇视觉识别/分割，目标类别或文本提示在训练时未必出现。
   - 方法核心：借助 SAM/基础分割模型产生候选 mask，再做筛选或适配。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：适合拓展到开放词汇、零样本或少标注 COD。
   - 可借鉴点：prompt 设计、类别文本构造、免训练迁移流程；候选 mask 生成、视觉-语言筛选、推理式定位；边界/频域增强模块；跨域鲁棒性、不确定性或异常分数。
   - 可改进点：可改进 prompt 自动生成、负样本约束和 mask 置信度校准。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

42. **Annotation-Free Open-Vocabulary Segmentation for Remote-Sensing Images**
   - Source: arXiv, 2025-08-25
   - Authors: Kaiyu Li, Xiangyong Cao, Ruixun Liu, Shihong Wang, Zixuan Jiang et al.
   - Tags: open-vocabulary, boundary/frequency, remote sensing
   - Links: [paper](http://arxiv.org/abs/2508.18067v1) / [pdf](http://arxiv.org/pdf/2508.18067v1)
   - 论文：Annotation-Free Open-Vocabulary Segmentation for Remote-Sensing Images
   - 一句话总结：Semantic segmentation of remote sensing (RS) images is pivotal for comprehensive Earth observation, but the demand for interpreting new object categories, coupled with the high expense of manual annotation, po...
   - 任务设定：开放词汇视觉识别/分割，目标类别或文本提示在训练时未必出现。
   - 方法核心：借助 SAM/基础分割模型产生候选 mask，再做筛选或适配。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：适合拓展到开放词汇、零样本或少标注 COD。
   - 可借鉴点：prompt 设计、类别文本构造、免训练迁移流程；边界/频域增强模块。
   - 可改进点：可改进 prompt 自动生成、负样本约束和 mask 置信度校准。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

43. **Diffusion Model as a Generalist Segmentation Learner**
   - Source: arXiv, 2026-04-27
   - Authors: Haoxiao Wang, Antao Xiang, Haiyang Sun, Peilin Sun, Changhao Pan et al.
   - Tags: open-vocabulary, diffusion, remote sensing, low-level
   - Links: [paper](http://arxiv.org/abs/2604.24575v1) / [pdf](http://arxiv.org/pdf/2604.24575v1)
   - 论文：Diffusion Model as a Generalist Segmentation Learner
   - 一句话总结：Diffusion models are primarily trained for image synthesis, yet their denoising trajectories encode rich, spatially aligned visual priors. In this paper, we demonstrate that these priors can be utilized for te...
   - 任务设定：开放词汇视觉识别/分割，目标类别或文本提示在训练时未必出现。
   - 方法核心：扩散/生成式建模，可能用于数据合成、先验建模或掩码优化。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：适合拓展到开放词汇、零样本或少标注 COD。
   - 可借鉴点：prompt 设计、类别文本构造、免训练迁移流程。
   - 可改进点：可改进 prompt 自动生成、负样本约束和 mask 置信度校准。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

44. **OV-Stitcher: A Global Context-Aware Framework for Training-Free Open-Vocabulary Semantic Segmentation**
   - Source: arXiv, 2026-04-09
   - Authors: Seungjae Moon, Seunghyun Oh, Youngmin Ro
   - Tags: open-vocabulary, training-free, VLM/MLLM, reasoning, diffusion, boundary/frequency
   - Links: [paper](http://arxiv.org/abs/2604.08110v2) / [pdf](http://arxiv.org/pdf/2604.08110v2)
   - 论文：OV-Stitcher: A Global Context-Aware Framework for Training-Free Open-Vocabulary Semantic Segmentation
   - 一句话总结：Training-free open-vocabulary semantic segmentation(TF-OVSS) has recently attracted attention for its ability to perform dense prediction by leveraging the pretrained knowledge of large vision and vision-langu...
   - 任务设定：开放词汇视觉识别/分割，目标类别或文本提示在训练时未必出现。
   - 方法核心：视觉-语言对齐，把语义文本信息引入检测或分割。
   - 实验结论：可能包含新数据集/基准；适合看评测协议、失败案例和是否能服务 COD。
   - 和我课题的关系：适合拓展到开放词汇、零样本或少标注 COD。
   - 可借鉴点：prompt 设计、类别文本构造、免训练迁移流程；候选 mask 生成、视觉-语言筛选、推理式定位；边界/频域增强模块。
   - 可改进点：可改进 prompt 自动生成、负样本约束和 mask 置信度校准。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

45. **DeepTumorVQA: A Hierarchical 3D CT Benchmark for Stage-Wise Evaluation of Medical VLMs and Tool-Augmented Agents**
   - Source: arXiv, 2026-05-10
   - Authors: Yixiong Chen, Wenjie Xiao, Pedro R. A. S. Bassi, Boyan Wang, Liang He et al.
   - Tags: VLM/MLLM, reasoning, diffusion, boundary/frequency, depth/geometry, medical imaging
   - Links: [paper](http://arxiv.org/abs/2605.09679v1) / [pdf](http://arxiv.org/pdf/2605.09679v1)
   - 论文：DeepTumorVQA: A Hierarchical 3D CT Benchmark for Stage-Wise Evaluation of Medical VLMs and Tool-Augmented Agents
   - 一句话总结：Medical vision-language models (VLMs) and AI agents have made significant progress in learning to analyze and reason about clinical images. However, existing medical visual question answering (VQA) benchmarks...
   - 任务设定：基础模型驱动的视觉定位/分割/推理，可用于自动提示生成或 mask 筛选。
   - 方法核心：视觉-语言对齐，把语义文本信息引入检测或分割。
   - 实验结论：可能包含新数据集/基准；适合看评测协议、失败案例和是否能服务 COD。
   - 和我课题的关系：可补充 COD 中纹理、边界、几何先验不足的问题。
   - 可借鉴点：候选 mask 生成、视觉-语言筛选、推理式定位；边界/频域增强模块；深度或几何先验融合。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

46. **Cross-Modal-Domain Generalization Through Semantically Aligned Discrete Representations**
   - Source: arXiv, 2026-05-12
   - Authors: Souptik Sen, Raneen Younis, Zahra Ahmadi
   - Tags: retrieval/prototype, video, domain adaptation
   - Links: [paper](http://arxiv.org/abs/2605.12145v2) / [pdf](http://arxiv.org/pdf/2605.12145v2)
   - 论文：Cross-Modal-Domain Generalization Through Semantically Aligned Discrete Representations
   - 一句话总结：Multimodal learning seeks to integrate information across diverse sensory sources, yet current approaches struggle to balance cross-modal generalizability with modality-specific structure. Continuous (implicit...
   - 任务设定：视频/时序视觉任务，关注跨帧一致性、运动线索和长期上下文。
   - 方法核心：视觉-语言对齐，把语义文本信息引入检测或分割。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：不是 COD 直系论文，但可能提供可迁移的视觉表征、训练策略或评测思路。
   - 可借鉴点：跨域鲁棒性、不确定性或异常分数。
   - 可改进点：可验证在 COD 跨数据集上的泛化，加入目标缺失场景。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

47. **EDGER: EDge-Guided with HEatmap Refinement for Generalizable Image Forgery Localization**
   - Source: arXiv, 2026-05-12
   - Authors: Minh-Khoa Le-Phan, Minh-Hoang Le, Minh-Triet Tran, Trong-Le Do
   - Tags: boundary/frequency, domain adaptation
   - Links: [paper](http://arxiv.org/abs/2605.12002v1) / [pdf](http://arxiv.org/pdf/2605.12002v1)
   - 论文：EDGER: EDge-Guided with HEatmap Refinement for Generalizable Image Forgery Localization
   - 一句话总结：Text-guided inpainting has made image forgery increasingly realistic, challenging both SID and IFL. However, existing methods often struggle to point out suspicious signals across domains.
   - 任务设定：通用计算机视觉任务，先判断是否能迁移到 COD 的感知、定位或分割环节。
   - 方法核心：视觉-语言对齐，把语义文本信息引入检测或分割。
   - 实验结论：摘要强调消融、鲁棒性或泛化；适合优先看实验设计和跨域表现。
   - 和我课题的关系：可补充 COD 中纹理、边界、几何先验不足的问题。
   - 可借鉴点：边界/频域增强模块；跨域鲁棒性、不确定性或异常分数。
   - 可改进点：可结合多尺度语义上下文，避免只强化纹理导致误检。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

48. **CrossPan: A Comprehensive Benchmark for Cross-Sequence Pancreas MRI Segmentation and Generalization**
   - Source: arXiv, 2026-04-20
   - Authors: Linkai Peng, Cuiling Sun, Zheyuan Zhang, Wanying Dou, Halil Ertugrul Aktas et al.
   - Tags: unsupervised, depth/geometry, domain adaptation, medical imaging
   - Links: [paper](http://arxiv.org/abs/2604.18797v1) / [pdf](http://arxiv.org/pdf/2604.18797v1)
   - 论文：CrossPan: A Comprehensive Benchmark for Cross-Sequence Pancreas MRI Segmentation and Generalization
   - 一句话总结：Automatic pancreas segmentation is fundamental to abdominal MRI analysis, yet deep learning models trained on one MRI sequence often fail catastrophically when applied to another-a challenge that has received...
   - 任务设定：医学影像分割/检测，常见弱边界、低对比和标注稀缺问题。
   - 方法核心：借助 SAM/基础分割模型产生候选 mask，再做筛选或适配。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：可补充 COD 中纹理、边界、几何先验不足的问题。
   - 可借鉴点：深度或几何先验融合；跨域鲁棒性、不确定性或异常分数。
   - 可改进点：可验证在 COD 跨数据集上的泛化，加入目标缺失场景。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

49. **SemiSAM-O1: How far can we push the boundary of annotation-efficient medical image segmentation?**
   - Source: arXiv, 2026-04-27
   - Authors: Yichi Zhang, Le Xue, Bichun Xu, Judong Luo, Zhigang Wu et al.
   - Tags: unsupervised, retrieval/prototype, boundary/frequency, medical imaging
   - Links: [paper](http://arxiv.org/abs/2604.24109v1) / [pdf](http://arxiv.org/pdf/2604.24109v1)
   - 论文：SemiSAM-O1: How far can we push the boundary of annotation-efficient medical image segmentation?
   - 一句话总结：Semi-supervised learning (SSL) has become a promising solution to alleviate the annotation burden of deep learning-based medical image segmentation models. While recent advances in foundation model-driven SSL...
   - 任务设定：医学影像分割/检测，常见弱边界、低对比和标注稀缺问题。
   - 方法核心：提示学习或提示生成，重点看文本/视觉 prompt 如何约束定位。
   - 实验结论：摘要强调消融、鲁棒性或泛化；适合优先看实验设计和跨域表现。
   - 和我课题的关系：可补充 COD 中纹理、边界、几何先验不足的问题。
   - 可借鉴点：边界/频域增强模块。
   - 可改进点：可结合多尺度语义上下文，避免只强化纹理导致误检。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

50. **Adapting Foundation Models for Annotation-Efficient Adnexal Mass Segmentation in Cine Images**
   - Source: arXiv, 2026-04-09
   - Authors: Francesca Fati, Alberto Rota, Adriana V. Gregory, Anna Catozzo, Maria C. Giuliano et al.
   - Tags: diffusion, boundary/frequency, medical imaging
   - Links: [paper](http://arxiv.org/abs/2604.08045v1) / [pdf](http://arxiv.org/pdf/2604.08045v1)
   - 论文：Adapting Foundation Models for Annotation-Efficient Adnexal Mass Segmentation in Cine Images
   - 一句话总结：Adnexal mass evaluation via ultrasound is a challenging clinical task, often hindered by subjective interpretation and significant inter-observer variability. While automated segmentation is a foundational ste...
   - 任务设定：医学影像分割/检测，常见弱边界、低对比和标注稀缺问题。
   - 方法核心：边界感知建模，适合改善伪装目标轮廓不清的问题。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：可补充 COD 中纹理、边界、几何先验不足的问题。
   - 可借鉴点：边界/频域增强模块。
   - 可改进点：可结合多尺度语义上下文，避免只强化纹理导致误检。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

51. **HyPiDecoder: Hybrid Pixel Decoder for Efficient Segmentation and Detection**
   - Source: ICCV 2025, 2025
   - Authors: Fengzhe Zhou, Humphrey Shi
   - Tags: computer vision
   - Links: [paper](https://openaccess.thecvf.com/content/ICCV2025/html/Zhou_HyPiDecoder_Hybrid_Pixel_Decoder_for_Efficient_Segmentation_and_Detection_ICCV_2025_paper.html) / [pdf](https://openaccess.thecvf.com/content/ICCV2025/papers/Zhou_HyPiDecoder_Hybrid_Pixel_Decoder_for_Efficient_Segmentation_and_Detection_ICCV_2025_paper.pdf)
   - 论文：HyPiDecoder: Hybrid Pixel Decoder for Efficient Segmentation and Detection
   - 一句话总结：CVF OpenAccess paper. Open the paper page for full abstract and method details.
   - 任务设定：通用计算机视觉任务，先判断是否能迁移到 COD 的感知、定位或分割环节。
   - 方法核心：摘要层面未显示明确模块，建议先看方法图确认 backbone、监督信号和损失设计。
   - 实验结论：当前来源只提供标题级信息；需要打开论文页确认数据集、指标和消融。
   - 和我课题的关系：不是 COD 直系论文，但可能提供可迁移的视觉表征、训练策略或评测思路。
   - 可借鉴点：任务建模、损失函数、消融组织方式。
   - 可改进点：可思考是否缺少 COD 场景验证、复杂背景失败分析或轻量化部署。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

52. **SVHighlights: Towards Extremely Long Sport Video Highlight Detection**
   - Source: arXiv, 2026-06-05
   - Authors: Donggyu Lee, Youngbin Ki, Jeonghun Kang, Taehwan Kim
   - Tags: training-free, reasoning, boundary/frequency, video, saliency/transparent
   - Links: [paper](http://arxiv.org/abs/2606.06926v2) / [pdf](http://arxiv.org/pdf/2606.06926v2)
   - 论文：SVHighlights: Towards Extremely Long Sport Video Highlight Detection
   - 一句话总结：While highlight detection for long-form videos is of great practical importance, most existing methods remain limited to short-form content, largely due to the absence of a suitable benchmark. To bridge this g...
   - 任务设定：免训练或少训练迁移设定，重点看 prompt、特征选择和后处理。
   - 方法核心：借助 SAM/基础分割模型产生候选 mask，再做筛选或适配。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：和 COD 同属低显著/弱边界目标发现，可迁移目标-背景分离思想。
   - 可借鉴点：prompt 设计、类别文本构造、免训练迁移流程；边界/频域增强模块。
   - 可改进点：可改进 prompt 自动生成、负样本约束和 mask 置信度校准。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

53. **Binary Tracking for Spatial QA and Navigation with Open Vision-Language Models**
   - Source: arXiv, 2026-06-15
   - Authors: Dongbin Na, Chanwoo Kim, Soonbin Rho, Giyun Choi, Gangbok Lee et al.
   - Tags: VLM/MLLM, reasoning, diffusion, retrieval/prototype, video
   - Links: [paper](http://arxiv.org/abs/2606.16902v1) / [pdf](http://arxiv.org/pdf/2606.16902v1)
   - 论文：Binary Tracking for Spatial QA and Navigation with Open Vision-Language Models
   - 一句话总结：This work addresses spatial question answering for service robots traversing long egocentric routes. Given a query such as "where can I find a dry cleaner on the way back home?", the system returns a metric co...
   - 任务设定：基础模型驱动的视觉定位/分割/推理，可用于自动提示生成或 mask 筛选。
   - 方法核心：借助 SAM/基础分割模型产生候选 mask，再做筛选或适配。
   - 实验结论：可能包含新数据集/基准；适合看评测协议、失败案例和是否能服务 COD。
   - 和我课题的关系：可用于伪装目标的语义描述、环境理解和候选区域判断。
   - 可借鉴点：候选 mask 生成、视觉-语言筛选、推理式定位。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

54. **ReasonCLIP-58M: Visually Grounded Commonsense Reasoning Supervision for CLIP**
   - Source: arXiv, 2026-06-25
   - Authors: Sicheng Zhang, Muzammal Naseer, Binzhu Xie, Naufal Suryanto, Shi Qiu et al.
   - Tags: VLM/MLLM, reasoning, diffusion, retrieval/prototype
   - Links: [paper](http://arxiv.org/abs/2606.26794v1) / [pdf](http://arxiv.org/pdf/2606.26794v1)
   - 论文：ReasonCLIP-58M: Visually Grounded Commonsense Reasoning Supervision for CLIP
   - 一句话总结：CLIP and its variants are widely adopted visual backbones in multimodal systems, but their pretraining remains dominated by descriptive image-text alignment. As downstream applications increasingly demand visu...
   - 任务设定：基础模型驱动的视觉定位/分割/推理，可用于自动提示生成或 mask 筛选。
   - 方法核心：视觉-语言对齐，把语义文本信息引入检测或分割。
   - 实验结论：可能包含新数据集/基准；适合看评测协议、失败案例和是否能服务 COD。
   - 和我课题的关系：可用于伪装目标的语义描述、环境理解和候选区域判断。
   - 可借鉴点：候选 mask 生成、视觉-语言筛选、推理式定位。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

55. **IMAGIN-4D: Image-Guided Controllable Interaction Generation**
   - Source: arXiv, 2026-06-22
   - Authors: Sai Kumar Dwivedi, Federica Bogo, Buğra Tekin, Chenhongyi Yang, Nadine Bertsch et al.
   - Tags: diffusion, depth/geometry, video
   - Links: [paper](http://arxiv.org/abs/2606.23675v1) / [pdf](http://arxiv.org/pdf/2606.23675v1)
   - 论文：IMAGIN-4D: Image-Guided Controllable Interaction Generation
   - 一句话总结：Generating human-object interactions (HOI) is central to character animation, robotics, AR/VR, and embodied AI. Recent HOI generation methods synthesize motion from text, object geometry, and sparse waypoints,...
   - 任务设定：视频/时序视觉任务，关注跨帧一致性、运动线索和长期上下文。
   - 方法核心：扩散/生成式建模，可能用于数据合成、先验建模或掩码优化。
   - 实验结论：可能包含新数据集/基准；适合看评测协议、失败案例和是否能服务 COD。
   - 和我课题的关系：可补充 COD 中纹理、边界、几何先验不足的问题。
   - 可借鉴点：深度或几何先验融合。
   - 可改进点：可思考是否缺少 COD 场景验证、复杂背景失败分析或轻量化部署。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

56. **Prompting Diffusion Models for Zero-Shot Instance Segmentation**
   - Source: arXiv, 2026-06-21
   - Authors: Irem Zeynep Alagöz, Nils Morbitzer, Andrea Ramazzina, Nassir Navab, Federico Tombari et al.
   - Tags: diffusion
   - Links: [paper](http://arxiv.org/abs/2606.22660v1) / [pdf](http://arxiv.org/pdf/2606.22660v1)
   - 论文：Prompting Diffusion Models for Zero-Shot Instance Segmentation
   - 一句话总结：Several disruptive research directions have recently emerged in computer vision, including foundation models achieving previously unseen zero-shot performance in scene understanding, even interactively, and ge...
   - 任务设定：通用计算机视觉任务，先判断是否能迁移到 COD 的感知、定位或分割环节。
   - 方法核心：扩散/生成式建模，可能用于数据合成、先验建模或掩码优化。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：不是 COD 直系论文，但可能提供可迁移的视觉表征、训练策略或评测思路。
   - 可借鉴点：任务建模、损失函数、消融组织方式。
   - 可改进点：可思考是否缺少 COD 场景验证、复杂背景失败分析或轻量化部署。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

57. **ELDiff: When Evidential Learning Meets Text-to-Image Diffusion**
   - Source: arXiv, 2026-06-18
   - Authors: Qingtao Pan, Kai Ye, Zhihao Dou, Bing Ji, Shuo Li
   - Tags: diffusion, low-level
   - Links: [paper](http://arxiv.org/abs/2606.20924v1) / [pdf](http://arxiv.org/pdf/2606.20924v1)
   - 论文：ELDiff: When Evidential Learning Meets Text-to-Image Diffusion
   - 一句话总结：In multi-object text-to-image (T2I) diffusion, ensuring semantic consistency between textual prompts and generated visual content is crucial for image synthesis. However, such consistency constraint is often u...
   - 任务设定：通用计算机视觉任务，先判断是否能迁移到 COD 的感知、定位或分割环节。
   - 方法核心：扩散/生成式建模，可能用于数据合成、先验建模或掩码优化。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：不是 COD 直系论文，但可能提供可迁移的视觉表征、训练策略或评测思路。
   - 可借鉴点：任务建模、损失函数、消融组织方式。
   - 可改进点：可思考是否缺少 COD 场景验证、复杂背景失败分析或轻量化部署。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

58. **SL-S4Wave: Self-Supervised Learning of Physiological Waveforms with Structured State Space Models**
   - Source: arXiv, 2026-06-18
   - Authors: Feng Wu, Harsh Deep, Eric Lehman, Sanyam Kapoor, Guoshuai Zhao et al.
   - Tags: diffusion, video, domain adaptation
   - Links: [paper](http://arxiv.org/abs/2606.19888v1) / [pdf](http://arxiv.org/pdf/2606.19888v1)
   - 论文：SL-S4Wave: Self-Supervised Learning of Physiological Waveforms with Structured State Space Models
   - 一句话总结：Modeling long-sequence medical time series data, such as electrocardiograms (ECG), poses significant challenges due to high sampling rates, multichannel signal complexity, inherent noise, and limited labeled d...
   - 任务设定：视频/时序视觉任务，关注跨帧一致性、运动线索和长期上下文。
   - 方法核心：借助 SAM/基础分割模型产生候选 mask，再做筛选或适配。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：不是 COD 直系论文，但可能提供可迁移的视觉表征、训练策略或评测思路。
   - 可借鉴点：跨域鲁棒性、不确定性或异常分数。
   - 可改进点：可验证在 COD 跨数据集上的泛化，加入目标缺失场景。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

59. **VTOS: Learning to Orchestrate Vision Tools by Co-Searching Solutions and Observers**
   - Source: arXiv, 2026-06-17
   - Authors: Jinchao Ge, Lingqiao Liu, Shuwen Zhao, Lei Wang
   - Tags: open-vocabulary, SAM, reasoning, diffusion, boundary/frequency, anomaly/OOD, domain adaptation
   - Links: [paper](http://arxiv.org/abs/2606.20728v1) / [pdf](http://arxiv.org/pdf/2606.20728v1)
   - 论文：VTOS: Learning to Orchestrate Vision Tools by Co-Searching Solutions and Observers
   - 一句话总结：Vision foundation tools such as open-vocabulary detectors, segmentation models, and post-processing operators are powerful building blocks for computer vision, but their effectiveness depends heavily on how th...
   - 任务设定：开放词汇视觉识别/分割，目标类别或文本提示在训练时未必出现。
   - 方法核心：借助 SAM/基础分割模型产生候选 mask，再做筛选或适配。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：适合拓展到开放词汇、零样本或少标注 COD。
   - 可借鉴点：prompt 设计、类别文本构造、免训练迁移流程；候选 mask 生成、视觉-语言筛选、推理式定位；边界/频域增强模块；跨域鲁棒性、不确定性或异常分数。
   - 可改进点：可改进 prompt 自动生成、负样本约束和 mask 置信度校准。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

60. **Efficient Encoder-Free Fourier-based 3D Large Multimodal Model**
   - Source: CVPR 2026, 2026
   - Authors: Guofeng Mei, Wei Lin, Luigi Riz, Yujiao Wu, Yiming Wang et al.
   - Tags: depth/geometry
   - Links: [paper](https://openaccess.thecvf.com/content/CVPR2026/html/Mei_Efficient_Encoder-Free_Fourier-based_3D_Large_Multimodal_Model_CVPR_2026_paper.html) / [pdf](https://openaccess.thecvf.com/content/CVPR2026/papers/Mei_Efficient_Encoder-Free_Fourier-based_3D_Large_Multimodal_Model_CVPR_2026_paper.pdf)
   - 论文：Efficient Encoder-Free Fourier-based 3D Large Multimodal Model
   - 一句话总结：CVF OpenAccess paper. Open the paper page for full abstract and method details.
   - 任务设定：通用计算机视觉任务，先判断是否能迁移到 COD 的感知、定位或分割环节。
   - 方法核心：视觉-语言对齐，把语义文本信息引入检测或分割。
   - 实验结论：当前来源只提供标题级信息；需要打开论文页确认数据集、指标和消融。
   - 和我课题的关系：可补充 COD 中纹理、边界、几何先验不足的问题。
   - 可借鉴点：深度或几何先验融合。
   - 可改进点：可思考是否缺少 COD 场景验证、复杂背景失败分析或轻量化部署。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

## 2026-06-26 20:40 更新

Selected papers: 3394

### 当日优先读

1. **CFCamo: A Counterfactual Detect-or-Abstain Framework for Camouflaged Object Detection**
   - Source: arXiv, 2026-05-28
   - Authors: Suhang Li, Osamu Yoshie, Yuya Ieiri
   - Tags: COD, SAM, VLM/MLLM
   - Links: [paper](http://arxiv.org/abs/2606.11231v1) / [pdf](http://arxiv.org/pdf/2606.11231v1)
   - 论文：CFCamo: A Counterfactual Detect-or-Abstain Framework for Camouflaged Object Detection
   - 一句话总结：Vision-language reinforcement learning has recently shown strong target-present localization for camouflaged object detection (COD). Yet localization is only one side of the decision: when the agent faces an o...
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：反事实建模/拒识机制，用来降低误检或判断目标是否存在。
   - 实验结论：可能包含新数据集/基准；适合看评测协议、失败案例和是否能服务 COD。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；候选 mask 生成、视觉-语言筛选、推理式定位。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

2. **A Retinomorphic Optical Spiking Neuron for Camouflaged Object Detection**
   - Source: arXiv, 2026-05-30
   - Authors: Srilagna Sahoo, Adwaaiit Pande, Kartikey Thakar, Shubham Sahay, Saurabh Lodha
   - Tags: COD, boundary/frequency
   - Links: [paper](http://arxiv.org/abs/2606.00818v1) / [pdf](http://arxiv.org/pdf/2606.00818v1)
   - 论文：A Retinomorphic Optical Spiking Neuron for Camouflaged Object Detection
   - 一句话总结：Advanced vision systems require retinomorphic, energy-efficient spike-based preprocessing of dynamic visual scenes. Here, we demonstrate multiple retinal preprocessing functionalities by leveraging a Hodgkin-H...
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：边界感知建模，适合改善伪装目标轮廓不清的问题。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；边界/频域增强模块。
   - 可改进点：可尝试引入基础模型、文本先验或更强的环境上下文建模。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

3. **Anatomy-Guided Residual Motion Diffusion for Controllable 4D Cardiac MRI Synthesis**
   - Source: arXiv, 2026-06-25
   - Authors: Yiheng Cao, Gustavo Andrade-Miranda, Jiatian Zhang, Lingxiao Zhao, Xin Gao
   - Tags: unsupervised, diffusion, boundary/frequency, depth/geometry, video
   - Links: [paper](http://arxiv.org/abs/2606.26764v1) / [pdf](http://arxiv.org/pdf/2606.26764v1)
   - 论文：Anatomy-Guided Residual Motion Diffusion for Controllable 4D Cardiac MRI Synthesis
   - 一句话总结：Developing robust artificial intelligence models for 4D (3D + time) medical imaging is constrained by limited annotated data, inter-device domain shifts, and privacy restrictions. To address this, we propose a...
   - 任务设定：视频/时序视觉任务，关注跨帧一致性、运动线索和长期上下文。
   - 方法核心：扩散/生成式建模，可能用于数据合成、先验建模或掩码优化。
   - 实验结论：可能包含新数据集/基准；适合看评测协议、失败案例和是否能服务 COD。
   - 和我课题的关系：可补充 COD 中纹理、边界、几何先验不足的问题。
   - 可借鉴点：边界/频域增强模块；深度或几何先验融合。
   - 可改进点：可结合多尺度语义上下文，避免只强化纹理导致误检。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

4. **Vision-Language Model Reasoning for Contextual Semantic Mapping in Intralogistics**
   - Source: arXiv, 2026-06-23
   - Authors: Marvin Rüdt, Hao Pang, Constantin Enke, Zäzilia Seibold, Kai Furmans
   - Tags: open-vocabulary, SAM, VLM/MLLM, reasoning, depth/geometry
   - Links: [paper](http://arxiv.org/abs/2606.24814v1) / [pdf](http://arxiv.org/pdf/2606.24814v1)
   - 论文：Vision-Language Model Reasoning for Contextual Semantic Mapping in Intralogistics
   - 一句话总结：Autonomous mobile robots operating in intralogistics environments rely on geometric maps for localization and navigation, but lack semantic understanding of objects and their contextual properties. We present...
   - 任务设定：开放词汇视觉识别/分割，目标类别或文本提示在训练时未必出现。
   - 方法核心：提示学习或提示生成，重点看文本/视觉 prompt 如何约束定位。
   - 实验结论：摘要强调消融、鲁棒性或泛化；适合优先看实验设计和跨域表现。
   - 和我课题的关系：适合拓展到开放词汇、零样本或少标注 COD。
   - 可借鉴点：prompt 设计、类别文本构造、免训练迁移流程；候选 mask 生成、视觉-语言筛选、推理式定位；深度或几何先验融合。
   - 可改进点：可改进 prompt 自动生成、负样本约束和 mask 置信度校准。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

5. **ARTEMIS: Agent-guided Reliability-aware Temporal Mask Evolution for Imperfectly Supervised Video Polyp Segmentation**
   - Source: arXiv, 2026-06-18
   - Authors: Tong Wang, Siwen Wang, Yaolei Qi, Jinxing Zhou, Yuting He et al.
   - Tags: SAM, VLM/MLLM, retrieval/prototype, boundary/frequency, depth/geometry, video
   - Links: [paper](http://arxiv.org/abs/2606.20161v1) / [pdf](http://arxiv.org/pdf/2606.20161v1)
   - 论文：ARTEMIS: Agent-guided Reliability-aware Temporal Mask Evolution for Imperfectly Supervised Video Polyp Segmentation
   - 一句话总结：Imperfectly supervised video polyp segmentation (VPS) aims to learn dense, temporally consistent masks from inexpensive supervision, including weak annotations (points, scribbles) and semi-supervision with few...
   - 任务设定：基础模型驱动的视觉定位/分割/推理，可用于自动提示生成或 mask 筛选。
   - 方法核心：借助 SAM/基础分割模型产生候选 mask，再做筛选或适配。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：可补充 COD 中纹理、边界、几何先验不足的问题。
   - 可借鉴点：候选 mask 生成、视觉-语言筛选、推理式定位；边界/频域增强模块；深度或几何先验融合。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

6. **ActiveSAM: Image-Conditional Class Pruning for Fast and Accurate Open-Vocabulary Segmentation**
   - Source: arXiv, 2026-06-15
   - Authors: Tran Dinh Tien, Zhiqiang Shen
   - Tags: open-vocabulary, training-free, SAM, diffusion, remote sensing
   - Links: [paper](http://arxiv.org/abs/2606.16996v1) / [pdf](http://arxiv.org/pdf/2606.16996v1)
   - 论文：ActiveSAM: Image-Conditional Class Pruning for Fast and Accurate Open-Vocabulary Segmentation
   - 一句话总结：Segment Anything Model 3 (SAM 3) provides a strong frozen backbone for concept-prompted segmentation, but applying it directly to open-vocabulary semantic segmentation (OVSS) is inefficient: full-resolution de...
   - 任务设定：开放词汇视觉识别/分割，目标类别或文本提示在训练时未必出现。
   - 方法核心：提示学习或提示生成，重点看文本/视觉 prompt 如何约束定位。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：适合拓展到开放词汇、零样本或少标注 COD。
   - 可借鉴点：prompt 设计、类别文本构造、免训练迁移流程；候选 mask 生成、视觉-语言筛选、推理式定位。
   - 可改进点：可改进 prompt 自动生成、负样本约束和 mask 置信度校准。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

7. **Jolia: Concept-Level Vision-Language Alignment for 3D CT Contrastive Learning**
   - Source: arXiv, 2026-06-23
   - Authors: Julien Khlaut, Charles Corbière, Baptiste Callard, Amaury Prat, Leo Butsanets et al.
   - Tags: VLM/MLLM, depth/geometry
   - Links: [paper](http://arxiv.org/abs/2606.24570v2) / [pdf](http://arxiv.org/pdf/2606.24570v2)
   - 论文：Jolia: Concept-Level Vision-Language Alignment for 3D CT Contrastive Learning
   - 一句话总结：Vision-language contrastive pretraining has become the dominant recipe for 3D medical foundation models, leveraging the large volumes of paired scans and reports produced in clinical practice. However, medical...
   - 任务设定：基础模型驱动的视觉定位/分割/推理，可用于自动提示生成或 mask 筛选。
   - 方法核心：视觉-语言对齐，把语义文本信息引入检测或分割。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：可补充 COD 中纹理、边界、几何先验不足的问题。
   - 可借鉴点：候选 mask 生成、视觉-语言筛选、推理式定位；深度或几何先验融合。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

8. **UniDrive: A Unified Vision-Language and Grounding Framework for Interpretable Risk Understanding in Autonomous Driving**
   - Source: arXiv, 2026-06-23
   - Authors: Xiaowei Gao, Pengxiang Li, Yitai Cheng, Ruihan Xu, James Haworth et al.
   - Tags: VLM/MLLM, reasoning, video
   - Links: [paper](http://arxiv.org/abs/2606.24759v1) / [pdf](http://arxiv.org/pdf/2606.24759v1)
   - 论文：UniDrive: A Unified Vision-Language and Grounding Framework for Interpretable Risk Understanding in Autonomous Driving
   - 一句话总结：Recent multimodal large language models (MLLMs) have shown strong potential for autonomous driving scene understanding, yet existing methods still face a fundamental trade-off between temporal reasoning and sp...
   - 任务设定：基础模型驱动的视觉定位/分割/推理，可用于自动提示生成或 mask 筛选。
   - 方法核心：视觉-语言对齐，把语义文本信息引入检测或分割。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：可用于伪装目标的语义描述、环境理解和候选区域判断。
   - 可借鉴点：候选 mask 生成、视觉-语言筛选、推理式定位。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

9. **HPP: Hierarchical Programmatic Probing for Long Video Understanding by Decoupling Perception and Reasoning**
   - Source: arXiv, 2026-06-19
   - Authors: Awais Rauf, Ahmed Hasssan, Greg Slabaugh
   - Tags: VLM/MLLM, reasoning, retrieval/prototype, video
   - Links: [paper](http://arxiv.org/abs/2606.21734v1) / [pdf](http://arxiv.org/pdf/2606.21734v1)
   - 论文：HPP: Hierarchical Programmatic Probing for Long Video Understanding by Decoupling Perception and Reasoning
   - 一句话总结：Understanding long videos requires fine-grained perception and multi-step, higher-order reasoning over complex, long-range spatio-temporal dynamics. Vision-language models (VLMs) encode video frames into visua...
   - 任务设定：基础模型驱动的视觉定位/分割/推理，可用于自动提示生成或 mask 筛选。
   - 方法核心：视觉-语言对齐，把语义文本信息引入检测或分割。
   - 实验结论：可能包含新数据集/基准；适合看评测协议、失败案例和是否能服务 COD。
   - 和我课题的关系：可用于伪装目标的语义描述、环境理解和候选区域判断。
   - 可借鉴点：候选 mask 生成、视觉-语言筛选、推理式定位。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

10. **EnTrust: Modeling Inter-Modal Conflict for Trustworthy Multimodal Medical Image Analysis**
   - Source: arXiv, 2026-06-19
   - Authors: Dwarikanath Mahapatra, Abhijit Das, Behzad Bozorgtabar, Zongyuan Ge, Sudipta Roy et al.
   - Tags: SAM, diffusion
   - Links: [paper](http://arxiv.org/abs/2606.21384v1) / [pdf](http://arxiv.org/pdf/2606.21384v1)
   - 论文：EnTrust: Modeling Inter-Modal Conflict for Trustworthy Multimodal Medical Image Analysis
   - 一句话总结：Multimodal medical imaging fuses complementary anatomical and functional information, yet modalities frequently disagree in pathologically heterogeneous regions. Current segmentation models handle this in one...
   - 任务设定：基础模型驱动的视觉定位/分割/推理，可用于自动提示生成或 mask 筛选。
   - 方法核心：扩散/生成式建模，可能用于数据合成、先验建模或掩码优化。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：不是 COD 直系论文，但可能提供可迁移的视觉表征、训练策略或评测思路。
   - 可借鉴点：候选 mask 生成、视觉-语言筛选、推理式定位。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

11. **Object Tokens as a Bridge Between Segmentation and Visual Question Answering in Robotic Surgery**
   - Source: arXiv, 2026-06-14
   - Authors: Yiping Li, Ronald de Jong, Romy van Jaarsveld, Franco Badaloni, Gino Kuiper et al.
   - Tags: SAM, VLM/MLLM, reasoning
   - Links: [paper](http://arxiv.org/abs/2606.15861v1) / [pdf](http://arxiv.org/pdf/2606.15861v1)
   - 论文：Object Tokens as a Bridge Between Segmentation and Visual Question Answering in Robotic Surgery
   - 一句话总结：Visual Question Answering (VQA) in robotic surgery, referred to as surgical VQA, requires high-level understanding of complex surgical scenes and the integration of visual perception with language reasoning, w...
   - 任务设定：基础模型驱动的视觉定位/分割/推理，可用于自动提示生成或 mask 筛选。
   - 方法核心：借助 SAM/基础分割模型产生候选 mask，再做筛选或适配。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：可用于伪装目标的语义描述、环境理解和候选区域判断。
   - 可借鉴点：候选 mask 生成、视觉-语言筛选、推理式定位。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

12. **ReasonCLIP-58M: Visually Grounded Commonsense Reasoning Supervision for CLIP**
   - Source: arXiv, 2026-06-25
   - Authors: Sicheng Zhang, Muzammal Naseer, Binzhu Xie, Naufal Suryanto, Shi Qiu et al.
   - Tags: VLM/MLLM, reasoning, diffusion, retrieval/prototype
   - Links: [paper](http://arxiv.org/abs/2606.26794v1) / [pdf](http://arxiv.org/pdf/2606.26794v1)
   - 论文：ReasonCLIP-58M: Visually Grounded Commonsense Reasoning Supervision for CLIP
   - 一句话总结：CLIP and its variants are widely adopted visual backbones in multimodal systems, but their pretraining remains dominated by descriptive image-text alignment. As downstream applications increasingly demand visu...
   - 任务设定：基础模型驱动的视觉定位/分割/推理，可用于自动提示生成或 mask 筛选。
   - 方法核心：视觉-语言对齐，把语义文本信息引入检测或分割。
   - 实验结论：可能包含新数据集/基准；适合看评测协议、失败案例和是否能服务 COD。
   - 和我课题的关系：可用于伪装目标的语义描述、环境理解和候选区域判断。
   - 可借鉴点：候选 mask 生成、视觉-语言筛选、推理式定位。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

### 当日高质量来源优先读

### 当日 COD / 伪装目标检测相关

1. **Open-Vocabulary Camouflaged Object Segmentation**
   - Source: arXiv, 2023-11-19
   - Authors: Youwei Pang, Xiaoqi Zhao, Jiaming Zuo, Lihe Zhang, Huchuan Lu
   - Tags: COD, open-vocabulary, VLM/MLLM, boundary/frequency, depth/geometry, low-level
   - Links: [paper](http://arxiv.org/abs/2311.11241v3) / [pdf](http://arxiv.org/pdf/2311.11241v3)
   - 论文：Open-Vocabulary Camouflaged Object Segmentation
   - 一句话总结：Recently, the emergence of the large-scale vision-language model (VLM), such as CLIP, has opened the way towards open-world object perception. Many works have explored the utilization of pre-trained VLM for th...
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：视觉-语言对齐，把语义文本信息引入检测或分割。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；prompt 设计、类别文本构造、免训练迁移流程；候选 mask 生成、视觉-语言筛选、推理式定位；边界/频域增强模块；深度或几何先验融合。
   - 可改进点：可改进 prompt 自动生成、负样本约束和 mask 置信度校准。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

2. **Debate-Enhanced Pseudo Labeling and Frequency-Aware Progressive Debiasing for Weakly-Supervised Camouflaged Object Detection with Scribble Annotations**
   - Source: arXiv, 2025-12-23
   - Authors: Jiawei Ge, Jiuxin Cao, Xinyi Li, Xuelin Zhu, Chang Liu et al.
   - Tags: COD, unsupervised, SAM, boundary/frequency
   - Links: [paper](http://arxiv.org/abs/2512.20260v5) / [pdf](http://arxiv.org/pdf/2512.20260v5)
   - 论文：Debate-Enhanced Pseudo Labeling and Frequency-Aware Progressive Debiasing for Weakly-Supervised Camouflaged Object Detection with Scribble Annotations
   - 一句话总结：Weakly-Supervised Camouflaged Object Detection (WSCOD) aims to locate and segment objects that are visually concealed within their surrounding scenes, relying solely on sparse supervision such as scribble anno...
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：借助 SAM/基础分割模型产生候选 mask，再做筛选或适配。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；候选 mask 生成、视觉-语言筛选、推理式定位；边界/频域增强模块。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

3. **UCOD-DPL: Unsupervised Camouflaged Object Detection via Dynamic Pseudo-label Learning**
   - Source: arXiv, 2025-06-08
   - Authors: Weiqi Yan, Lvhai Chen, Huaijia Kou, Shengchuan Zhang, Yan Zhang et al.
   - Tags: COD, unsupervised, boundary/frequency, remote sensing
   - Links: [paper](http://arxiv.org/abs/2506.07087v1) / [pdf](http://arxiv.org/pdf/2506.07087v1)
   - 论文：UCOD-DPL: Unsupervised Camouflaged Object Detection via Dynamic Pseudo-label Learning
   - 一句话总结：Unsupervised Camoflaged Object Detection (UCOD) has gained attention since it doesn't need to rely on extensive pixel-level labels. Existing UCOD methods typically generate pseudo-labels using fixed strategies...
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：边界感知建模，适合改善伪装目标轮廓不清的问题。
   - 实验结论：摘要未给出强实验信号；先看实验表格和图 1，再决定是否精读。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；边界/频域增强模块。
   - 可改进点：可尝试引入基础模型、文本先验或更强的环境上下文建模。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

4. **EReCu: Pseudo-label Evolution Fusion and Refinement with Multi-Cue Learning for Unsupervised Camouflage Detection**
   - Source: arXiv, 2026-03-12
   - Authors: Shuo Jiang, Gaojia Zhang, Min Tan, Yufei Yin, Gang Pan
   - Tags: COD, unsupervised, diffusion, boundary/frequency, depth/geometry, low-level
   - Links: [paper](http://arxiv.org/abs/2603.11521v1) / [pdf](http://arxiv.org/pdf/2603.11521v1)
   - 论文：EReCu: Pseudo-label Evolution Fusion and Refinement with Multi-Cue Learning for Unsupervised Camouflage Detection
   - 一句话总结：Unsupervised Camouflaged Object Detection (UCOD) remains a challenging task due to the high intrinsic similarity between target objects and their surroundings, as well as the reliance on noisy pseudo-labels th...
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：边界感知建模，适合改善伪装目标轮廓不清的问题。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；边界/频域增强模块；深度或几何先验融合。
   - 可改进点：可尝试引入基础模型、文本先验或更强的环境上下文建模。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

5. **SAM3-Adapter: Efficient Adaptation of Segment Anything 3 for Camouflage Object Segmentation, Shadow Detection, and Medical Image Segmentation**
   - Source: arXiv, 2025-11-24
   - Authors: Tianrun Chen, Runlong Cao, Xinda Yu, Lanyun Zhu, Chaotao Ding et al.
   - Tags: COD, SAM
   - Links: [paper](http://arxiv.org/abs/2511.19425v1) / [pdf](http://arxiv.org/pdf/2511.19425v1)
   - 论文：SAM3-Adapter: Efficient Adaptation of Segment Anything 3 for Camouflage Object Segmentation, Shadow Detection, and Medical Image Segmentation
   - 一句话总结：The rapid rise of large-scale foundation models has reshaped the landscape of image segmentation, with models such as Segment Anything achieving unprecedented versatility across diverse vision tasks. However,...
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：借助 SAM/基础分割模型产生候选 mask，再做筛选或适配。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；候选 mask 生成、视觉-语言筛选、推理式定位。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

6. **High-Resolution Underwater Camouflaged Object Detection: GBU-UCOD Dataset and Topology-Aware and Frequency-Decoupled Networks**
   - Source: arXiv, 2026-02-03
   - Authors: Wenji Wu, Shuo Ye, Yiyu Liu, Jiguang He, Zhuo Wang et al.
   - Tags: COD, SAM, diffusion, boundary/frequency, depth/geometry
   - Links: [paper](http://arxiv.org/abs/2602.03591v1) / [pdf](http://arxiv.org/pdf/2602.03591v1)
   - 论文：High-Resolution Underwater Camouflaged Object Detection: GBU-UCOD Dataset and Topology-Aware and Frequency-Decoupled Networks
   - 一句话总结：Underwater Camouflaged Object Detection (UCOD) is a challenging task due to the extreme visual similarity between targets and backgrounds across varying marine depths. Existing methods often struggle with topo...
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：借助 SAM/基础分割模型产生候选 mask，再做筛选或适配。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；候选 mask 生成、视觉-语言筛选、推理式定位；边界/频域增强模块；深度或几何先验融合。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

7. **ZS-VCOS: Zero-Shot Video Camouflaged Object Segmentation By Optical Flow and Open Vocabulary Object Detection**
   - Source: arXiv, 2025-04-10
   - Authors: Wenqi Guo, Mohamed Shehata, Shan Du
   - Tags: COD, open-vocabulary, unsupervised, SAM, VLM/MLLM, diffusion, video
   - Links: [paper](http://arxiv.org/abs/2505.01431v2) / [pdf](http://arxiv.org/pdf/2505.01431v2)
   - 论文：ZS-VCOS: Zero-Shot Video Camouflaged Object Segmentation By Optical Flow and Open Vocabulary Object Detection
   - 一句话总结：Camouflaged object segmentation presents unique challenges compared to traditional segmentation tasks, primarily due to the high similarity in patterns and colors between camouflaged objects and their backgrou...
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：借助 SAM/基础分割模型产生候选 mask，再做筛选或适配。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；prompt 设计、类别文本构造、免训练迁移流程；候选 mask 生成、视觉-语言筛选、推理式定位。
   - 可改进点：可改进 prompt 自动生成、负样本约束和 mask 置信度校准。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

8. **First RAG, Second SEG: A Training-Free Paradigm for Camouflaged Object Detection**
   - Source: arXiv, 2025-08-21
   - Authors: Wutao Liu, YiDan Wang, Pan Gao
   - Tags: COD, training-free, unsupervised, SAM, retrieval/prototype, anomaly/OOD
   - Links: [paper](http://arxiv.org/abs/2508.15313v2) / [pdf](http://arxiv.org/pdf/2508.15313v2)
   - 论文：First RAG, Second SEG: A Training-Free Paradigm for Camouflaged Object Detection
   - 一句话总结：Camouflaged object detection (COD) poses a significant challenge in computer vision due to the high similarity between objects and their backgrounds. Existing approaches often rely on heavy training and large...
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：提示学习或提示生成，重点看文本/视觉 prompt 如何约束定位。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；prompt 设计、类别文本构造、免训练迁移流程；候选 mask 生成、视觉-语言筛选、推理式定位；跨域鲁棒性、不确定性或异常分数。
   - 可改进点：可改进 prompt 自动生成、负样本约束和 mask 置信度校准。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

9. **When SAM2 Meets Video Camouflaged Object Segmentation: A Comprehensive Evaluation and Adaptation**
   - Source: arXiv, 2024-09-27
   - Authors: Yuli Zhou, Guolei Sun, Yawei Li, Guo-Sen Xie, Luca Benini et al.
   - Tags: COD, SAM, VLM/MLLM, diffusion, video
   - Links: [paper](http://arxiv.org/abs/2409.18653v2) / [pdf](http://arxiv.org/pdf/2409.18653v2)
   - 论文：When SAM2 Meets Video Camouflaged Object Segmentation: A Comprehensive Evaluation and Adaptation
   - 一句话总结：This study investigates the application and performance of the Segment Anything Model 2 (SAM2) in the challenging task of video camouflaged object segmentation (VCOS). VCOS involves detecting objects that blen...
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：提示学习或提示生成，重点看文本/视觉 prompt 如何约束定位。
   - 实验结论：可能包含新数据集/基准；适合看评测协议、失败案例和是否能服务 COD。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；候选 mask 生成、视觉-语言筛选、推理式定位。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

10. **COMPrompter: reconceptualized segment anything model with multiprompt network for camouflaged object detection**
   - Source: arXiv, 2024-11-28
   - Authors: Xiaoqin Zhang, Zhenni Yu, Li Zhao, Deng-Ping Fan, Guobao Xiao
   - Tags: COD, SAM, boundary/frequency
   - Links: [paper](http://arxiv.org/abs/2411.18858v1) / [pdf](http://arxiv.org/pdf/2411.18858v1)
   - 论文：COMPrompter: reconceptualized segment anything model with multiprompt network for camouflaged object detection
   - 一句话总结：We rethink the segment anything model (SAM) and propose a novel multiprompt network called COMPrompter for camouflaged object detection (COD). SAM has zero-shot generalization ability beyond other models and c...
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：提示学习或提示生成，重点看文本/视觉 prompt 如何约束定位。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；候选 mask 生成、视觉-语言筛选、推理式定位；边界/频域增强模块。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

11. **Exploring Deeper! Segment Anything Model with Depth Perception for Camouflaged Object Detection**
   - Source: arXiv, 2024-07-17
   - Authors: Zhenni Yu, Xiaoqin Zhang, Li Zhao, Yi Bin, Guobao Xiao
   - Tags: COD, SAM, boundary/frequency, depth/geometry
   - Links: [paper](http://arxiv.org/abs/2407.12339v1) / [pdf](http://arxiv.org/pdf/2407.12339v1)
   - 论文：Exploring Deeper! Segment Anything Model with Depth Perception for Camouflaged Object Detection
   - 一句话总结：This paper introduces a new Segment Anything Model with Depth Perception (DSAM) for Camouflaged Object Detection (COD). DSAM exploits the zero-shot capability of SAM to realize precise segmentation in the RGB-...
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：提示学习或提示生成，重点看文本/视觉 prompt 如何约束定位。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；候选 mask 生成、视觉-语言筛选、推理式定位；边界/频域增强模块；深度或几何先验融合。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

12. **BED-SAM2: Boundary-Enhanced-Depth SAM2 via Monocular Geometric Priors**
   - Source: arXiv, 2026-05-24
   - Authors: Tyler Rust, Dara McNally, Kyle O'Donnell, Colin Kelly, Chandra Kambhamettu
   - Tags: COD, SAM, boundary/frequency, depth/geometry
   - Links: [paper](http://arxiv.org/abs/2605.24893v1) / [pdf](http://arxiv.org/pdf/2605.24893v1)
   - 论文：BED-SAM2: Boundary-Enhanced-Depth SAM2 via Monocular Geometric Priors
   - 一句话总结：Building upon the SAM2 vision foundation model for downstream segmentation, this study introduces Boundary Enhanced Depth (BED)-SAM2. The SAM2 Hiera encoder architecture is modified to directly encode monocula...
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：借助 SAM/基础分割模型产生候选 mask，再做筛选或适配。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；候选 mask 生成、视觉-语言筛选、推理式定位；边界/频域增强模块；深度或几何先验融合。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

13. **FCL-COD: Weakly Supervised Camouflaged Object Detection with Frequency-aware and Contrastive Learning**
   - Source: arXiv, 2026-03-24
   - Authors: Jingchen Ni, Quan Zhang, Dan Jiang, Keyu Lv, Ke Zhang et al.
   - Tags: COD, unsupervised, SAM, diffusion, boundary/frequency
   - Links: [paper](http://arxiv.org/abs/2603.22969v1) / [pdf](http://arxiv.org/pdf/2603.22969v1)
   - 论文：FCL-COD: Weakly Supervised Camouflaged Object Detection with Frequency-aware and Contrastive Learning
   - 一句话总结：Existing camouflage object detection (COD) methods typically rely on fully-supervised learning guided by mask annotations. However, obtaining mask annotations is time-consuming and labor-intensive.
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：借助 SAM/基础分割模型产生候选 mask，再做筛选或适配。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；候选 mask 生成、视觉-语言筛选、推理式定位；边界/频域增强模块。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

14. **Stepwise Decomposition and Dual-stream Focus: A Novel Approach for Training-free Camouflaged Object Segmentation**
   - Source: arXiv, 2025-06-07
   - Authors: Chao Yin, Hao Li, Kequan Yang, Jide Li, Pinpin Zhu et al.
   - Tags: COD, training-free, SAM, reasoning
   - Links: [paper](http://arxiv.org/abs/2506.06818v3) / [pdf](http://arxiv.org/pdf/2506.06818v3)
   - 论文：Stepwise Decomposition and Dual-stream Focus: A Novel Approach for Training-free Camouflaged Object Segmentation
   - 一句话总结：While promptable segmentation (\textit{e.g.}, SAM) has shown promise for various segmentation tasks, it still requires manual visual prompts for each object to be segmented. In contrast, task-generic promptabl...
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：提示学习或提示生成，重点看文本/视觉 prompt 如何约束定位。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；prompt 设计、类别文本构造、免训练迁移流程；候选 mask 生成、视觉-语言筛选、推理式定位。
   - 可改进点：可改进 prompt 自动生成、负样本约束和 mask 置信度校准。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

15. **CamSAM2: Segment Anything Accurately in Camouflaged Videos**
   - Source: arXiv, 2025-03-25
   - Authors: Yuli Zhou, Yawei Li, Yuqian Fu, Luca Benini, Ender Konukoglu et al.
   - Tags: COD, SAM, retrieval/prototype, video
   - Links: [paper](http://arxiv.org/abs/2503.19730v3) / [pdf](http://arxiv.org/pdf/2503.19730v3)
   - 论文：CamSAM2: Segment Anything Accurately in Camouflaged Videos
   - 一句话总结：Video camouflaged object segmentation (VCOS), aiming at segmenting camouflaged objects that seamlessly blend into their environment, is a fundamental vision task with various real-world applications. With the...
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：提示学习或提示生成，重点看文本/视觉 prompt 如何约束定位。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；候选 mask 生成、视觉-语言筛选、推理式定位。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

16. **SAM2-UNeXT: An Improved High-Resolution Baseline for Adapting Foundation Models to Downstream Segmentation Tasks**
   - Source: arXiv, 2025-08-05
   - Authors: Xinyu Xiong, Zihuang Wu, Lei Zhang, Lei Lu, Ming Li et al.
   - Tags: COD, SAM, remote sensing
   - Links: [paper](http://arxiv.org/abs/2508.03566v1) / [pdf](http://arxiv.org/pdf/2508.03566v1)
   - 论文：SAM2-UNeXT: An Improved High-Resolution Baseline for Adapting Foundation Models to Downstream Segmentation Tasks
   - 一句话总结：Recent studies have highlighted the potential of adapting the Segment Anything Model (SAM) for various downstream tasks. However, constructing a more powerful and generalizable encoder to further enhance perfo...
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：借助 SAM/基础分割模型产生候选 mask，再做筛选或适配。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；候选 mask 生成、视觉-语言筛选、推理式定位。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

17. **Depth-guided Texture Diffusion for Image Semantic Segmentation**
   - Source: arXiv, 2024-08-17
   - Authors: Wei Sun, Yuan Li, Qixiang Ye, Jianbin Jiao, Yanzhao Zhou
   - Tags: COD, diffusion, boundary/frequency, depth/geometry
   - Links: [paper](http://arxiv.org/abs/2408.09097v1) / [pdf](http://arxiv.org/pdf/2408.09097v1)
   - 论文：Depth-guided Texture Diffusion for Image Semantic Segmentation
   - 一句话总结：Depth information provides valuable insights into the 3D structure especially the outline of objects, which can be utilized to improve the semantic segmentation tasks. However, a naive fusion of depth informat...
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：扩散/生成式建模，可能用于数据合成、先验建模或掩码优化。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；边界/频域增强模块；深度或几何先验融合。
   - 可改进点：可尝试引入基础模型、文本先验或更强的环境上下文建模。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

18. **Weakly Supervised Camouflaged Object Detection Based on the SAM Model and Mask Guidance**
   - Source: arXiv, 2026-05-25
   - Authors: Xia Li, Xinran Liu, Lin Qi, Junyu Dong
   - Tags: COD, unsupervised, SAM, boundary/frequency, low-level
   - Links: [paper](http://arxiv.org/abs/2605.25385v1) / [pdf](http://arxiv.org/pdf/2605.25385v1)
   - 论文：Weakly Supervised Camouflaged Object Detection Based on the SAM Model and Mask Guidance
   - 一句话总结：Camouflaged object detection (COD) from a single image is a challenging task due to the high similarity between objects and their surroundings. Existing fully supervised methods require labor-intensive pixel-l...
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：提示学习或提示生成，重点看文本/视觉 prompt 如何约束定位。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；候选 mask 生成、视觉-语言筛选、推理式定位；边界/频域增强模块。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

19. **RIDE: Retinex-Informed Decoupling for Exposing Concealed Objects**
   - Source: arXiv, 2026-05-14
   - Authors: Chunming He, Rihan Zhang, Dingming Zhang, Chengyu Fang, Longxiang Tang et al.
   - Tags: COD, SAM, boundary/frequency
   - Links: [paper](http://arxiv.org/abs/2605.15450v1) / [pdf](http://arxiv.org/pdf/2605.15450v1)
   - 论文：RIDE: Retinex-Informed Decoupling for Exposing Concealed Objects
   - 一句话总结：Concealed Object Segmentation (COS) encompasses a family of dense-prediction tasks, including camouflaged object detection, polyp segmentation, transparent object detection, and industrial defect inspection, w...
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：借助 SAM/基础分割模型产生候选 mask，再做筛选或适配。
   - 实验结论：摘要未给出强实验信号；先看实验表格和图 1，再决定是否精读。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；候选 mask 生成、视觉-语言筛选、推理式定位；边界/频域增强模块。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

20. **Exploring Boundary-Aware Spatial-Frequency Fusion for Camouflaged Object Detection**
   - Source: arXiv, 2026-04-20
   - Authors: Song Yu, Yang Hu, Haokang Ding, Zhifang Liao, Yucheng Song
   - Tags: COD, diffusion, boundary/frequency
   - Links: [paper](http://arxiv.org/abs/2604.17879v1) / [pdf](http://arxiv.org/pdf/2604.17879v1)
   - 论文：Exploring Boundary-Aware Spatial-Frequency Fusion for Camouflaged Object Detection
   - 一句话总结：Camouflaged Object Detection is challenging due to the high degree of similarity between camouflaged objects and their surrounding backgrounds. Current COD methods mainly rely on edge extraction in the spatial...
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：频域/纹理特征增强，适合处理伪装背景与目标细粒度差异。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；边界/频域增强模块。
   - 可改进点：可尝试引入基础模型、文本先验或更强的环境上下文建模。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

21. **IP-SAM: Prompt-Space Conditioning for Prompt-Absent Camouflaged Object Detection**
   - Source: arXiv, 2026-03-28
   - Authors: Huiyao Zhang, Jin Bai, Rui Guo, JianWen Tan, HongFei Wang et al.
   - Tags: COD, SAM, diffusion
   - Links: [paper](http://arxiv.org/abs/2603.27250v1) / [pdf](http://arxiv.org/pdf/2603.27250v1)
   - 论文：IP-SAM: Prompt-Space Conditioning for Prompt-Absent Camouflaged Object Detection
   - 一句话总结：Prompt-conditioned foundation segmenters have emerged as a dominant paradigm for image segmentation, where explicit spatial prompts (e.g., points, boxes, masks) guide mask decoding. However, many real-world de...
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：提示学习或提示生成，重点看文本/视觉 prompt 如何约束定位。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；候选 mask 生成、视觉-语言筛选、推理式定位。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

22. **Language-Guided Structure-Aware Network for Camouflaged Object Detection**
   - Source: arXiv, 2026-03-25
   - Authors: Min Zhang
   - Tags: COD, boundary/frequency, low-level
   - Links: [paper](http://arxiv.org/abs/2603.24355v1) / [pdf](http://arxiv.org/pdf/2603.24355v1)
   - 论文：Language-Guided Structure-Aware Network for Camouflaged Object Detection
   - 一句话总结：Camouflaged Object Detection (COD) aims to segment objects that are highly integrated with the background in terms of color, texture, and structure, making it a highly challenging task in computer vision. Alth...
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：提示学习或提示生成，重点看文本/视觉 prompt 如何约束定位。
   - 实验结论：可能包含新数据集/基准；适合看评测协议、失败案例和是否能服务 COD。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；边界/频域增强模块。
   - 可改进点：可尝试引入基础模型、文本先验或更强的环境上下文建模。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

23. **An Instance-Aware Prompting Framework for Training-free Camouflaged Object Segmentation**
   - Source: arXiv, 2025-08-09
   - Authors: Chao Yin, Jide Li, Hang Yao, Xiaoqiang Li
   - Tags: COD, training-free, SAM
   - Links: [paper](http://arxiv.org/abs/2508.06904v3) / [pdf](http://arxiv.org/pdf/2508.06904v3)
   - 论文：An Instance-Aware Prompting Framework for Training-free Camouflaged Object Segmentation
   - 一句话总结：Training-free Camouflaged Object Segmentation (COS) seeks to segment camouflaged objects without task-specific training, by automatically generating visual prompts to guide the Segment Anything Model (SAM). Ho...
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：提示学习或提示生成，重点看文本/视觉 prompt 如何约束定位。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；prompt 设计、类别文本构造、免训练迁移流程；候选 mask 生成、视觉-语言筛选、推理式定位。
   - 可改进点：可改进 prompt 自动生成、负样本约束和 mask 置信度校准。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

24. **Open-Vocabulary Camouflaged Object Segmentation with Cascaded Vision Language Models**
   - Source: arXiv, 2025-06-24
   - Authors: Kai Zhao, Wubang Yuan, Zheng Wang, Guanyi Li, Xiaoqiang Zhu et al.
   - Tags: COD, open-vocabulary, SAM
   - Links: [paper](http://arxiv.org/abs/2506.19300v2) / [pdf](http://arxiv.org/pdf/2506.19300v2)
   - 论文：Open-Vocabulary Camouflaged Object Segmentation with Cascaded Vision Language Models
   - 一句话总结：Open-Vocabulary Camouflaged Object Segmentation (OVCOS) seeks to segment and classify camouflaged objects from arbitrary categories, presenting unique challenges due to visual ambiguity and unseen categories.R...
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：提示学习或提示生成，重点看文本/视觉 prompt 如何约束定位。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；prompt 设计、类别文本构造、免训练迁移流程；候选 mask 生成、视觉-语言筛选、推理式定位。
   - 可改进点：可改进 prompt 自动生成、负样本约束和 mask 置信度校准。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

25. **Towards Real Zero-Shot Camouflaged Object Segmentation without Camouflaged Annotations**
   - Source: arXiv, 2024-10-22
   - Authors: Cheng Lei, Jie Fan, Xinran Li, Tianzhu Xiang, Ao Li et al.
   - Tags: COD, VLM/MLLM, diffusion
   - Links: [paper](http://arxiv.org/abs/2410.16953v2) / [pdf](http://arxiv.org/pdf/2410.16953v2)
   - 论文：Towards Real Zero-Shot Camouflaged Object Segmentation without Camouflaged Annotations
   - 一句话总结：Camouflaged Object Segmentation (COS) faces significant challenges due to the scarcity of annotated data, where meticulous pixel-level annotation is both labor-intensive and costly, primarily due to the intric...
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：视觉-语言对齐，把语义文本信息引入检测或分割。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；候选 mask 生成、视觉-语言筛选、推理式定位。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

26. **Beyond Single Images: Retrieval Self-Augmented Unsupervised Camouflaged Object Detection**
   - Source: arXiv, 2025-10-21
   - Authors: Ji Du, Xin Wang, Fangwei Hao, Mingyang Yu, Chunyuan Chen et al.
   - Tags: COD, unsupervised, retrieval/prototype
   - Links: [paper](http://arxiv.org/abs/2510.18437v1) / [pdf](http://arxiv.org/pdf/2510.18437v1)
   - 论文：Beyond Single Images: Retrieval Self-Augmented Unsupervised Camouflaged Object Detection
   - 一句话总结：At the core of Camouflaged Object Detection (COD) lies segmenting objects from their highly similar surroundings. Previous efforts navigate this challenge primarily through image-level modeling or annotation-b...
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：提示学习或提示生成，重点看文本/视觉 prompt 如何约束定位。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析。
   - 可改进点：可尝试引入基础模型、文本先验或更强的环境上下文建模。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

27. **DGA-Net: Enhancing SAM with Depth Prompting and Graph-Anchor Guidance for Camouflaged Object Detection**
   - Source: arXiv, 2026-01-06
   - Authors: Yuetong Li, Qing Zhang, Yilin Zhao, Gongyang Li, Zeming Liu
   - Tags: COD, SAM, depth/geometry, low-level
   - Links: [paper](http://arxiv.org/abs/2601.02831v1) / [pdf](http://arxiv.org/pdf/2601.02831v1)
   - 论文：DGA-Net: Enhancing SAM with Depth Prompting and Graph-Anchor Guidance for Camouflaged Object Detection
   - 一句话总结：To fully exploit depth cues in Camouflaged Object Detection (COD), we present DGA-Net, a specialized framework that adapts the Segment Anything Model (SAM) via a novel ``depth prompting" paradigm. Distinguishe...
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：提示学习或提示生成，重点看文本/视觉 prompt 如何约束定位。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；候选 mask 生成、视觉-语言筛选、推理式定位；深度或几何先验融合。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

28. **Phantom-Insight: Adaptive Multi-cue Fusion for Video Camouflaged Object Detection with Multimodal LLM**
   - Source: arXiv, 2025-09-08
   - Authors: Hua Zhang, Changjiang Luo, Ruoyu Chen
   - Tags: COD, SAM, VLM/MLLM, diffusion, boundary/frequency, video
   - Links: [paper](http://arxiv.org/abs/2509.06422v1) / [pdf](http://arxiv.org/pdf/2509.06422v1)
   - 论文：Phantom-Insight: Adaptive Multi-cue Fusion for Video Camouflaged Object Detection with Multimodal LLM
   - 一句话总结：Video camouflaged object detection (VCOD) is challenging due to dynamic environments. Existing methods face two main issues: (1) SAM-based methods struggle to separate camouflaged object edges due to model fre...
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：提示学习或提示生成，重点看文本/视觉 prompt 如何约束定位。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；候选 mask 生成、视觉-语言筛选、推理式定位；边界/频域增强模块。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

29. **Improving SAM for Camouflaged Object Detection via Dual Stream Adapters**
   - Source: arXiv, 2025-03-08
   - Authors: Jiaming Liu, Linghe Kong, Guihai Chen
   - Tags: COD, SAM, diffusion, boundary/frequency, depth/geometry
   - Links: [paper](http://arxiv.org/abs/2503.06042v2) / [pdf](http://arxiv.org/pdf/2503.06042v2)
   - 论文：Improving SAM for Camouflaged Object Detection via Dual Stream Adapters
   - 一句话总结：Segment anything model (SAM) has shown impressive general-purpose segmentation performance on natural images, but its performance on camouflaged object detection (COD) is unsatisfactory. In this paper, we prop...
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：提示学习或提示生成，重点看文本/视觉 prompt 如何约束定位。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；候选 mask 生成、视觉-语言筛选、推理式定位；边界/频域增强模块；深度或几何先验融合。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

30. **Refining Context-Entangled Content Segmentation via Curriculum Selection and Anti-Curriculum Promotion**
   - Source: arXiv, 2026-02-01
   - Authors: Chunming He, Rihan Zhang, Fengyang Xiao, Dingming Zhang, Zhiwen Cao et al.
   - Tags: COD, SAM, boundary/frequency, video, low-level
   - Links: [paper](http://arxiv.org/abs/2602.01183v2) / [pdf](http://arxiv.org/pdf/2602.01183v2)
   - 论文：Refining Context-Entangled Content Segmentation via Curriculum Selection and Anti-Curriculum Promotion
   - 一句话总结：Biological learning proceeds from easy to difficult tasks, gradually reinforcing perception and robustness. Inspired by this principle, we address Context-Entangled Content Segmentation (CECS), a challenging s...
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：借助 SAM/基础分割模型产生候选 mask，再做筛选或适配。
   - 实验结论：可能包含新数据集/基准；适合看评测协议、失败案例和是否能服务 COD。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；候选 mask 生成、视觉-语言筛选、推理式定位；边界/频域增强模块。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

31. **Assisted Refinement Network Based on Channel Information Interaction for Camouflaged and Salient Object Detection**
   - Source: arXiv, 2025-12-12
   - Authors: Kuan Wang, Yanjun Qin, Mengge Lu, Liejun Wang, Xiaoming Tao
   - Tags: COD, SAM, diffusion, boundary/frequency, low-level
   - Links: [paper](http://arxiv.org/abs/2512.11369v1) / [pdf](http://arxiv.org/pdf/2512.11369v1)
   - 论文：Assisted Refinement Network Based on Channel Information Interaction for Camouflaged and Salient Object Detection
   - 一句话总结：Camouflaged Object Detection (COD) stands as a significant challenge in computer vision, dedicated to identifying and segmenting objects visually highly integrated with their backgrounds. Current mainstream me...
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：借助 SAM/基础分割模型产生候选 mask，再做筛选或适配。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；候选 mask 生成、视觉-语言筛选、推理式定位；边界/频域增强模块。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

32. **Exploring Depth Contribution for Camouflaged Object Detection**
   - Source: arXiv, 2021-06-24
   - Authors: Mochu Xiang, Jing Zhang, Yunqiu Lv, Aixuan Li, Yiran Zhong et al.
   - Tags: COD, diffusion, depth/geometry, remote sensing
   - Links: [paper](http://arxiv.org/abs/2106.13217v3) / [pdf](http://arxiv.org/pdf/2106.13217v3)
   - 论文：Exploring Depth Contribution for Camouflaged Object Detection
   - 一句话总结：Camouflaged object detection (COD) aims to segment camouflaged objects hiding in the environment, which is challenging due to the similar appearance of camouflaged objects and their surroundings. Research in b...
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：扩散/生成式建模，可能用于数据合成、先验建模或掩码优化。
   - 实验结论：可能包含新数据集/基准；适合看评测协议、失败案例和是否能服务 COD。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；深度或几何先验融合。
   - 可改进点：可尝试引入基础模型、文本先验或更强的环境上下文建模。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

33. **Hierarchical Consistency Learning for Test-time Adaptation in Camouflage Perception**
   - Source: arXiv, 2026-05-25
   - Authors: Mingfeng Zha, Tianyu Li, Guoqing Wang, Yunqiang Pei, Chaofan Qiao et al.
   - Tags: COD, diffusion, retrieval/prototype, boundary/frequency
   - Links: [paper](http://arxiv.org/abs/2605.25651v2) / [pdf](http://arxiv.org/pdf/2605.25651v2)
   - 论文：Hierarchical Consistency Learning for Test-time Adaptation in Camouflage Perception
   - 一句话总结：Camouflaged object detection (COD) aims to localize targets that exhibit minimal perceptual differences from backgrounds through physical attributes. Existing methods, constrained by the static train-then-free...
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：频域/纹理特征增强，适合处理伪装背景与目标细粒度差异。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；边界/频域增强模块。
   - 可改进点：可尝试引入基础模型、文本先验或更强的环境上下文建模。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

34. **When W4A4 Breaks Camouflaged Object Detection: Token-Group Dual-Constraint Activation Quantization**
   - Source: arXiv, 2026-04-18
   - Authors: Tianqi Li, Wenyu Fang, Xin He, Xue Geng, Xu Cheng et al.
   - Tags: COD, boundary/frequency
   - Links: [paper](http://arxiv.org/abs/2604.16855v1) / [pdf](http://arxiv.org/pdf/2604.16855v1)
   - 论文：When W4A4 Breaks Camouflaged Object Detection: Token-Group Dual-Constraint Activation Quantization
   - 一句话总结：Camouflaged object detection (COD) segments objects that intentionally blend with the background, so predictions depend on subtle texture and boundary cues. COD is often needed under tight on-device memory and...
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：视觉-语言对齐，把语义文本信息引入检测或分割。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；边界/频域增强模块。
   - 可改进点：可尝试引入基础模型、文本先验或更强的环境上下文建模。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

35. **Modality-Agnostic Prompt Learning for Multi-Modal Camouflaged Object Detection**
   - Source: arXiv, 2026-04-14
   - Authors: Hao Wang, Jiqing Zhang, Xin Yang, Baocai Yin, Lu Jiang et al.
   - Tags: COD, SAM, diffusion, boundary/frequency, depth/geometry
   - Links: [paper](http://arxiv.org/abs/2604.12380v1) / [pdf](http://arxiv.org/pdf/2604.12380v1)
   - 论文：Modality-Agnostic Prompt Learning for Multi-Modal Camouflaged Object Detection
   - 一句话总结：Camouflaged Object Detection (COD) aims to segment objects that blend seamlessly into complex backgrounds, with growing interest in exploiting additional visual modalities to enhance robustness through complem...
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：提示学习或提示生成，重点看文本/视觉 prompt 如何约束定位。
   - 实验结论：可能包含新数据集/基准；适合看评测协议、失败案例和是否能服务 COD。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；候选 mask 生成、视觉-语言筛选、推理式定位；边界/频域增强模块；深度或几何先验融合。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

### 当日泛计算机视觉方法池

1. **SegRAG: Training-Free Retrieval-Augmented Semantic Segmentation**
   - Source: arXiv, 2026-05-17
   - Authors: Abderrahmene Boudiaf, Irfan Hussain, Sajid Javed
   - Tags: open-vocabulary, training-free, SAM, reasoning, retrieval/prototype
   - Links: [paper](http://arxiv.org/abs/2605.17630v2) / [pdf](http://arxiv.org/pdf/2605.17630v2)
   - 论文：SegRAG: Training-Free Retrieval-Augmented Semantic Segmentation
   - 一句话总结：Open-vocabulary segmentation models such as SAM3 perform well across broad categories via text prompting, yet degrade when target classes are visually underrepresented in pretraining or depart from canonical d...
   - 任务设定：开放词汇视觉识别/分割，目标类别或文本提示在训练时未必出现。
   - 方法核心：提示学习或提示生成，重点看文本/视觉 prompt 如何约束定位。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：适合拓展到开放词汇、零样本或少标注 COD。
   - 可借鉴点：prompt 设计、类别文本构造、免训练迁移流程；候选 mask 生成、视觉-语言筛选、推理式定位。
   - 可改进点：可改进 prompt 自动生成、负样本约束和 mask 置信度校准。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

2. **OVS-DINO: Open-Vocabulary Segmentation via Structure-Aligned SAM-DINO with Language Guidance**
   - Source: arXiv, 2026-04-09
   - Authors: Haoxi Zeng, Qiankun Liu, Yi Bin, Haiyue Zhang, Yujuan Ding et al.
   - Tags: open-vocabulary, unsupervised, SAM, boundary/frequency, remote sensing
   - Links: [paper](http://arxiv.org/abs/2604.08461v1) / [pdf](http://arxiv.org/pdf/2604.08461v1)
   - 论文：OVS-DINO: Open-Vocabulary Segmentation via Structure-Aligned SAM-DINO with Language Guidance
   - 一句话总结：Open-Vocabulary Segmentation (OVS) aims to segment image regions beyond predefined category sets by leveraging semantic descriptions. While CLIP based approaches excel in semantic generalization, they frequent...
   - 任务设定：开放词汇视觉识别/分割，目标类别或文本提示在训练时未必出现。
   - 方法核心：借助 SAM/基础分割模型产生候选 mask，再做筛选或适配。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：适合拓展到开放词汇、零样本或少标注 COD。
   - 可借鉴点：prompt 设计、类别文本构造、免训练迁移流程；候选 mask 生成、视觉-语言筛选、推理式定位；边界/频域增强模块。
   - 可改进点：可改进 prompt 自动生成、负样本约束和 mask 置信度校准。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

3. **ActiveSAM: Image-Conditional Class Pruning for Fast and Accurate Open-Vocabulary Segmentation**
   - Source: arXiv, 2026-06-15
   - Authors: Tran Dinh Tien, Zhiqiang Shen
   - Tags: open-vocabulary, training-free, SAM, diffusion, remote sensing
   - Links: [paper](http://arxiv.org/abs/2606.16996v1) / [pdf](http://arxiv.org/pdf/2606.16996v1)
   - 论文：ActiveSAM: Image-Conditional Class Pruning for Fast and Accurate Open-Vocabulary Segmentation
   - 一句话总结：Segment Anything Model 3 (SAM 3) provides a strong frozen backbone for concept-prompted segmentation, but applying it directly to open-vocabulary semantic segmentation (OVSS) is inefficient: full-resolution de...
   - 任务设定：开放词汇视觉识别/分割，目标类别或文本提示在训练时未必出现。
   - 方法核心：提示学习或提示生成，重点看文本/视觉 prompt 如何约束定位。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：适合拓展到开放词汇、零样本或少标注 COD。
   - 可借鉴点：prompt 设计、类别文本构造、免训练迁移流程；候选 mask 生成、视觉-语言筛选、推理式定位。
   - 可改进点：可改进 prompt 自动生成、负样本约束和 mask 置信度校准。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

4. **Vision-Language Model Reasoning for Contextual Semantic Mapping in Intralogistics**
   - Source: arXiv, 2026-06-23
   - Authors: Marvin Rüdt, Hao Pang, Constantin Enke, Zäzilia Seibold, Kai Furmans
   - Tags: open-vocabulary, SAM, VLM/MLLM, reasoning, depth/geometry
   - Links: [paper](http://arxiv.org/abs/2606.24814v1) / [pdf](http://arxiv.org/pdf/2606.24814v1)
   - 论文：Vision-Language Model Reasoning for Contextual Semantic Mapping in Intralogistics
   - 一句话总结：Autonomous mobile robots operating in intralogistics environments rely on geometric maps for localization and navigation, but lack semantic understanding of objects and their contextual properties. We present...
   - 任务设定：开放词汇视觉识别/分割，目标类别或文本提示在训练时未必出现。
   - 方法核心：提示学习或提示生成，重点看文本/视觉 prompt 如何约束定位。
   - 实验结论：摘要强调消融、鲁棒性或泛化；适合优先看实验设计和跨域表现。
   - 和我课题的关系：适合拓展到开放词汇、零样本或少标注 COD。
   - 可借鉴点：prompt 设计、类别文本构造、免训练迁移流程；候选 mask 生成、视觉-语言筛选、推理式定位；深度或几何先验融合。
   - 可改进点：可改进 prompt 自动生成、负样本约束和 mask 置信度校准。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

5. **ARTEMIS: Agent-guided Reliability-aware Temporal Mask Evolution for Imperfectly Supervised Video Polyp Segmentation**
   - Source: arXiv, 2026-06-18
   - Authors: Tong Wang, Siwen Wang, Yaolei Qi, Jinxing Zhou, Yuting He et al.
   - Tags: SAM, VLM/MLLM, retrieval/prototype, boundary/frequency, depth/geometry, video
   - Links: [paper](http://arxiv.org/abs/2606.20161v1) / [pdf](http://arxiv.org/pdf/2606.20161v1)
   - 论文：ARTEMIS: Agent-guided Reliability-aware Temporal Mask Evolution for Imperfectly Supervised Video Polyp Segmentation
   - 一句话总结：Imperfectly supervised video polyp segmentation (VPS) aims to learn dense, temporally consistent masks from inexpensive supervision, including weak annotations (points, scribbles) and semi-supervision with few...
   - 任务设定：基础模型驱动的视觉定位/分割/推理，可用于自动提示生成或 mask 筛选。
   - 方法核心：借助 SAM/基础分割模型产生候选 mask，再做筛选或适配。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：可补充 COD 中纹理、边界、几何先验不足的问题。
   - 可借鉴点：候选 mask 生成、视觉-语言筛选、推理式定位；边界/频域增强模块；深度或几何先验融合。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

6. **Anatomy-Guided Residual Motion Diffusion for Controllable 4D Cardiac MRI Synthesis**
   - Source: arXiv, 2026-06-25
   - Authors: Yiheng Cao, Gustavo Andrade-Miranda, Jiatian Zhang, Lingxiao Zhao, Xin Gao
   - Tags: unsupervised, diffusion, boundary/frequency, depth/geometry, video
   - Links: [paper](http://arxiv.org/abs/2606.26764v1) / [pdf](http://arxiv.org/pdf/2606.26764v1)
   - 论文：Anatomy-Guided Residual Motion Diffusion for Controllable 4D Cardiac MRI Synthesis
   - 一句话总结：Developing robust artificial intelligence models for 4D (3D + time) medical imaging is constrained by limited annotated data, inter-device domain shifts, and privacy restrictions. To address this, we propose a...
   - 任务设定：视频/时序视觉任务，关注跨帧一致性、运动线索和长期上下文。
   - 方法核心：扩散/生成式建模，可能用于数据合成、先验建模或掩码优化。
   - 实验结论：可能包含新数据集/基准；适合看评测协议、失败案例和是否能服务 COD。
   - 和我课题的关系：可补充 COD 中纹理、边界、几何先验不足的问题。
   - 可借鉴点：边界/频域增强模块；深度或几何先验融合。
   - 可改进点：可结合多尺度语义上下文，避免只强化纹理导致误检。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

7. **SegEarth-OV: Towards Training-Free Open-Vocabulary Segmentation for Remote Sensing Images**
   - Source: arXiv, 2024-10-02
   - Authors: Kaiyu Li, Ruixun Liu, Xiangyong Cao, Xueru Bai, Feng Zhou et al.
   - Tags: open-vocabulary, training-free, SAM, remote sensing, anomaly/OOD
   - Links: [paper](http://arxiv.org/abs/2410.01768v2) / [pdf](http://arxiv.org/pdf/2410.01768v2)
   - 论文：SegEarth-OV: Towards Training-Free Open-Vocabulary Segmentation for Remote Sensing Images
   - 一句话总结：Remote sensing image plays an irreplaceable role in fields such as agriculture, water resources, military, and disaster relief. Pixel-level interpretation is a critical aspect of remote sensing image applicati...
   - 任务设定：开放词汇视觉识别/分割，目标类别或文本提示在训练时未必出现。
   - 方法核心：借助 SAM/基础分割模型产生候选 mask，再做筛选或适配。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：适合拓展到开放词汇、零样本或少标注 COD。
   - 可借鉴点：prompt 设计、类别文本构造、免训练迁移流程；候选 mask 生成、视觉-语言筛选、推理式定位；跨域鲁棒性、不确定性或异常分数。
   - 可改进点：可改进 prompt 自动生成、负样本约束和 mask 置信度校准。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

8. **T-REN: Learning Text-Aligned Region Tokens Improves Dense Vision-Language Alignment and Scalability**
   - Source: arXiv, 2026-04-20
   - Authors: Savya Khosla, Sethuraman T, Aryan Chadha, Alex Schwing, Derek Hoiem
   - Tags: open-vocabulary, VLM/MLLM, diffusion, retrieval/prototype, depth/geometry, video
   - Links: [paper](http://arxiv.org/abs/2604.18573v1) / [pdf](http://arxiv.org/pdf/2604.18573v1)
   - 论文：T-REN: Learning Text-Aligned Region Tokens Improves Dense Vision-Language Alignment and Scalability
   - 一句话总结：Despite recent progress, vision-language encoders struggle with two core limitations: (1) weak alignment between language and dense vision features, which hurts tasks like open-vocabulary semantic segmentation...
   - 任务设定：开放词汇视觉识别/分割，目标类别或文本提示在训练时未必出现。
   - 方法核心：视觉-语言对齐，把语义文本信息引入检测或分割。
   - 实验结论：摘要未给出强实验信号；先看实验表格和图 1，再决定是否精读。
   - 和我课题的关系：适合拓展到开放词汇、零样本或少标注 COD。
   - 可借鉴点：prompt 设计、类别文本构造、免训练迁移流程；候选 mask 生成、视觉-语言筛选、推理式定位；深度或几何先验融合。
   - 可改进点：可改进 prompt 自动生成、负样本约束和 mask 置信度校准。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

9. **MM-OVSeg:Multimodal Optical-SAR Fusion for Open-Vocabulary Segmentation in Remote Sensing**
   - Source: arXiv, 2026-03-18
   - Authors: Yimin Wei, Aoran Xiao, Hongruixuan Chen, Junshi Xia, Naoto Yokoya
   - Tags: open-vocabulary, VLM/MLLM, diffusion, remote sensing
   - Links: [paper](http://arxiv.org/abs/2603.17528v2) / [pdf](http://arxiv.org/pdf/2603.17528v2)
   - 论文：MM-OVSeg:Multimodal Optical-SAR Fusion for Open-Vocabulary Segmentation in Remote Sensing
   - 一句话总结：Open-vocabulary segmentation enables pixel-level recognition from an open set of textual categories, allowing generalization beyond fixed classes. Despite great potential in remote sensing, progress in this ar...
   - 任务设定：开放词汇视觉识别/分割，目标类别或文本提示在训练时未必出现。
   - 方法核心：视觉-语言对齐，把语义文本信息引入检测或分割。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：适合拓展到开放词汇、零样本或少标注 COD。
   - 可借鉴点：prompt 设计、类别文本构造、免训练迁移流程；候选 mask 生成、视觉-语言筛选、推理式定位。
   - 可改进点：可改进 prompt 自动生成、负样本约束和 mask 置信度校准。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

10. **Jolia: Concept-Level Vision-Language Alignment for 3D CT Contrastive Learning**
   - Source: arXiv, 2026-06-23
   - Authors: Julien Khlaut, Charles Corbière, Baptiste Callard, Amaury Prat, Leo Butsanets et al.
   - Tags: VLM/MLLM, depth/geometry
   - Links: [paper](http://arxiv.org/abs/2606.24570v2) / [pdf](http://arxiv.org/pdf/2606.24570v2)
   - 论文：Jolia: Concept-Level Vision-Language Alignment for 3D CT Contrastive Learning
   - 一句话总结：Vision-language contrastive pretraining has become the dominant recipe for 3D medical foundation models, leveraging the large volumes of paired scans and reports produced in clinical practice. However, medical...
   - 任务设定：基础模型驱动的视觉定位/分割/推理，可用于自动提示生成或 mask 筛选。
   - 方法核心：视觉-语言对齐，把语义文本信息引入检测或分割。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：可补充 COD 中纹理、边界、几何先验不足的问题。
   - 可借鉴点：候选 mask 生成、视觉-语言筛选、推理式定位；深度或几何先验融合。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

11. **HPP: Hierarchical Programmatic Probing for Long Video Understanding by Decoupling Perception and Reasoning**
   - Source: arXiv, 2026-06-19
   - Authors: Awais Rauf, Ahmed Hasssan, Greg Slabaugh
   - Tags: VLM/MLLM, reasoning, retrieval/prototype, video
   - Links: [paper](http://arxiv.org/abs/2606.21734v1) / [pdf](http://arxiv.org/pdf/2606.21734v1)
   - 论文：HPP: Hierarchical Programmatic Probing for Long Video Understanding by Decoupling Perception and Reasoning
   - 一句话总结：Understanding long videos requires fine-grained perception and multi-step, higher-order reasoning over complex, long-range spatio-temporal dynamics. Vision-language models (VLMs) encode video frames into visua...
   - 任务设定：基础模型驱动的视觉定位/分割/推理，可用于自动提示生成或 mask 筛选。
   - 方法核心：视觉-语言对齐，把语义文本信息引入检测或分割。
   - 实验结论：可能包含新数据集/基准；适合看评测协议、失败案例和是否能服务 COD。
   - 和我课题的关系：可用于伪装目标的语义描述、环境理解和候选区域判断。
   - 可借鉴点：候选 mask 生成、视觉-语言筛选、推理式定位。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

12. **UniDrive: A Unified Vision-Language and Grounding Framework for Interpretable Risk Understanding in Autonomous Driving**
   - Source: arXiv, 2026-06-23
   - Authors: Xiaowei Gao, Pengxiang Li, Yitai Cheng, Ruihan Xu, James Haworth et al.
   - Tags: VLM/MLLM, reasoning, video
   - Links: [paper](http://arxiv.org/abs/2606.24759v1) / [pdf](http://arxiv.org/pdf/2606.24759v1)
   - 论文：UniDrive: A Unified Vision-Language and Grounding Framework for Interpretable Risk Understanding in Autonomous Driving
   - 一句话总结：Recent multimodal large language models (MLLMs) have shown strong potential for autonomous driving scene understanding, yet existing methods still face a fundamental trade-off between temporal reasoning and sp...
   - 任务设定：基础模型驱动的视觉定位/分割/推理，可用于自动提示生成或 mask 筛选。
   - 方法核心：视觉-语言对齐，把语义文本信息引入检测或分割。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：可用于伪装目标的语义描述、环境理解和候选区域判断。
   - 可借鉴点：候选 mask 生成、视觉-语言筛选、推理式定位。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

13. **Object Tokens as a Bridge Between Segmentation and Visual Question Answering in Robotic Surgery**
   - Source: arXiv, 2026-06-14
   - Authors: Yiping Li, Ronald de Jong, Romy van Jaarsveld, Franco Badaloni, Gino Kuiper et al.
   - Tags: SAM, VLM/MLLM, reasoning
   - Links: [paper](http://arxiv.org/abs/2606.15861v1) / [pdf](http://arxiv.org/pdf/2606.15861v1)
   - 论文：Object Tokens as a Bridge Between Segmentation and Visual Question Answering in Robotic Surgery
   - 一句话总结：Visual Question Answering (VQA) in robotic surgery, referred to as surgical VQA, requires high-level understanding of complex surgical scenes and the integration of visual perception with language reasoning, w...
   - 任务设定：基础模型驱动的视觉定位/分割/推理，可用于自动提示生成或 mask 筛选。
   - 方法核心：借助 SAM/基础分割模型产生候选 mask，再做筛选或适配。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：可用于伪装目标的语义描述、环境理解和候选区域判断。
   - 可借鉴点：候选 mask 生成、视觉-语言筛选、推理式定位。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

14. **EnTrust: Modeling Inter-Modal Conflict for Trustworthy Multimodal Medical Image Analysis**
   - Source: arXiv, 2026-06-19
   - Authors: Dwarikanath Mahapatra, Abhijit Das, Behzad Bozorgtabar, Zongyuan Ge, Sudipta Roy et al.
   - Tags: SAM, diffusion
   - Links: [paper](http://arxiv.org/abs/2606.21384v1) / [pdf](http://arxiv.org/pdf/2606.21384v1)
   - 论文：EnTrust: Modeling Inter-Modal Conflict for Trustworthy Multimodal Medical Image Analysis
   - 一句话总结：Multimodal medical imaging fuses complementary anatomical and functional information, yet modalities frequently disagree in pathologically heterogeneous regions. Current segmentation models handle this in one...
   - 任务设定：基础模型驱动的视觉定位/分割/推理，可用于自动提示生成或 mask 筛选。
   - 方法核心：扩散/生成式建模，可能用于数据合成、先验建模或掩码优化。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：不是 COD 直系论文，但可能提供可迁移的视觉表征、训练策略或评测思路。
   - 可借鉴点：候选 mask 生成、视觉-语言筛选、推理式定位。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

15. **Annotation-Free Open-Vocabulary Segmentation for Remote-Sensing Images**
   - Source: arXiv, 2025-08-25
   - Authors: Kaiyu Li, Xiangyong Cao, Ruixun Liu, Shihong Wang, Zixuan Jiang et al.
   - Tags: open-vocabulary, SAM, boundary/frequency, remote sensing
   - Links: [paper](http://arxiv.org/abs/2508.18067v1) / [pdf](http://arxiv.org/pdf/2508.18067v1)
   - 论文：Annotation-Free Open-Vocabulary Segmentation for Remote-Sensing Images
   - 一句话总结：Semantic segmentation of remote sensing (RS) images is pivotal for comprehensive Earth observation, but the demand for interpreting new object categories, coupled with the high expense of manual annotation, po...
   - 任务设定：开放词汇视觉识别/分割，目标类别或文本提示在训练时未必出现。
   - 方法核心：借助 SAM/基础分割模型产生候选 mask，再做筛选或适配。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：适合拓展到开放词汇、零样本或少标注 COD。
   - 可借鉴点：prompt 设计、类别文本构造、免训练迁移流程；候选 mask 生成、视觉-语言筛选、推理式定位；边界/频域增强模块。
   - 可改进点：可改进 prompt 自动生成、负样本约束和 mask 置信度校准。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

16. **Diffusion Model as a Generalist Segmentation Learner**
   - Source: arXiv, 2026-04-27
   - Authors: Haoxiao Wang, Antao Xiang, Haiyang Sun, Peilin Sun, Changhao Pan et al.
   - Tags: open-vocabulary, diffusion, remote sensing, low-level
   - Links: [paper](http://arxiv.org/abs/2604.24575v1) / [pdf](http://arxiv.org/pdf/2604.24575v1)
   - 论文：Diffusion Model as a Generalist Segmentation Learner
   - 一句话总结：Diffusion models are primarily trained for image synthesis, yet their denoising trajectories encode rich, spatially aligned visual priors. In this paper, we demonstrate that these priors can be utilized for te...
   - 任务设定：开放词汇视觉识别/分割，目标类别或文本提示在训练时未必出现。
   - 方法核心：扩散/生成式建模，可能用于数据合成、先验建模或掩码优化。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：适合拓展到开放词汇、零样本或少标注 COD。
   - 可借鉴点：prompt 设计、类别文本构造、免训练迁移流程。
   - 可改进点：可改进 prompt 自动生成、负样本约束和 mask 置信度校准。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

17. **VesselSim: learning 3D blood vessel segmentation without expert annotations**
   - Source: arXiv, 2026-05-25
   - Authors: Erin Rainville, Melissa Ananian, Tristan Mirolla, Hassan Rivaz, Yiming Xiao
   - Tags: boundary/frequency, depth/geometry, anomaly/OOD
   - Links: [paper](http://arxiv.org/abs/2605.26277v2) / [pdf](http://arxiv.org/pdf/2605.26277v2)
   - 论文：VesselSim: learning 3D blood vessel segmentation without expert annotations
   - 一句话总结：Blood vessel segmentation is a core task in medical image analysis for the care of vascular diseases and surgical planning, yet the challenges of providing expert vascular annotations pose a major obstacle for...
   - 任务设定：异常检测或分布外识别，可类比伪装目标的弱异常发现。
   - 方法核心：边界感知建模，适合改善伪装目标轮廓不清的问题。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：可补充 COD 中纹理、边界、几何先验不足的问题。
   - 可借鉴点：边界/频域增强模块；深度或几何先验融合；跨域鲁棒性、不确定性或异常分数。
   - 可改进点：可结合多尺度语义上下文，避免只强化纹理导致误检。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

18. **Binary Tracking for Spatial QA and Navigation with Open Vision-Language Models**
   - Source: arXiv, 2026-06-15
   - Authors: Dongbin Na, Chanwoo Kim, Soonbin Rho, Giyun Choi, Gangbok Lee et al.
   - Tags: SAM, VLM/MLLM, reasoning, diffusion, retrieval/prototype, video
   - Links: [paper](http://arxiv.org/abs/2606.16902v1) / [pdf](http://arxiv.org/pdf/2606.16902v1)
   - 论文：Binary Tracking for Spatial QA and Navigation with Open Vision-Language Models
   - 一句话总结：This work addresses spatial question answering for service robots traversing long egocentric routes. Given a query such as "where can I find a dry cleaner on the way back home?", the system returns a metric co...
   - 任务设定：基础模型驱动的视觉定位/分割/推理，可用于自动提示生成或 mask 筛选。
   - 方法核心：借助 SAM/基础分割模型产生候选 mask，再做筛选或适配。
   - 实验结论：可能包含新数据集/基准；适合看评测协议、失败案例和是否能服务 COD。
   - 和我课题的关系：可用于伪装目标的语义描述、环境理解和候选区域判断。
   - 可借鉴点：候选 mask 生成、视觉-语言筛选、推理式定位。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

19. **ReasonCLIP-58M: Visually Grounded Commonsense Reasoning Supervision for CLIP**
   - Source: arXiv, 2026-06-25
   - Authors: Sicheng Zhang, Muzammal Naseer, Binzhu Xie, Naufal Suryanto, Shi Qiu et al.
   - Tags: VLM/MLLM, reasoning, diffusion, retrieval/prototype
   - Links: [paper](http://arxiv.org/abs/2606.26794v1) / [pdf](http://arxiv.org/pdf/2606.26794v1)
   - 论文：ReasonCLIP-58M: Visually Grounded Commonsense Reasoning Supervision for CLIP
   - 一句话总结：CLIP and its variants are widely adopted visual backbones in multimodal systems, but their pretraining remains dominated by descriptive image-text alignment. As downstream applications increasingly demand visu...
   - 任务设定：基础模型驱动的视觉定位/分割/推理，可用于自动提示生成或 mask 筛选。
   - 方法核心：视觉-语言对齐，把语义文本信息引入检测或分割。
   - 实验结论：可能包含新数据集/基准；适合看评测协议、失败案例和是否能服务 COD。
   - 和我课题的关系：可用于伪装目标的语义描述、环境理解和候选区域判断。
   - 可借鉴点：候选 mask 生成、视觉-语言筛选、推理式定位。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

20. **MLFFM-SegDiff: A Multi-Level Feature Fusion Diffusion Model for Skin Lesion Segmentation**
   - Source: arXiv, 2026-06-25
   - Authors: Jingjun Gu, Chaojie Shen, Yifeng Cao, Wei Zhang, Yiliu Li et al.
   - Tags: diffusion, boundary/frequency, low-level
   - Links: [paper](http://arxiv.org/abs/2606.26712v1) / [pdf](http://arxiv.org/pdf/2606.26712v1)
   - 论文：MLFFM-SegDiff: A Multi-Level Feature Fusion Diffusion Model for Skin Lesion Segmentation
   - 一句话总结：Skin lesion segmentation is a key task in computer-aided dermatological diagnosis, where accuracy directly impacts downstream analysis and disease classification. However, dermoscopic images are challenging du...
   - 任务设定：通用计算机视觉任务，先判断是否能迁移到 COD 的感知、定位或分割环节。
   - 方法核心：扩散/生成式建模，可能用于数据合成、先验建模或掩码优化。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：可补充 COD 中纹理、边界、几何先验不足的问题。
   - 可借鉴点：边界/频域增强模块。
   - 可改进点：可结合多尺度语义上下文，避免只强化纹理导致误检。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

21. **High-Fidelity Synthetic Transmission Electron Microscopy Image Generation Using Diffusion Probabilistic Models for Data-Limited Semiconductor Metrology**
   - Source: arXiv, 2026-06-23
   - Authors: Johannes Boehm, Bappaditya Dey
   - Tags: SAM, diffusion, low-level
   - Links: [paper](http://arxiv.org/abs/2606.24817v1) / [pdf](http://arxiv.org/pdf/2606.24817v1)
   - 论文：High-Fidelity Synthetic Transmission Electron Microscopy Image Generation Using Diffusion Probabilistic Models for Data-Limited Semiconductor Metrology
   - 一句话总结：Advanced semiconductor nodes drastically increased demand for Transmission Electron Microscopy (TEM), yet destructive sample preparation, slow imaging and high costs severely limit the availability of diverse...
   - 任务设定：基础模型驱动的视觉定位/分割/推理，可用于自动提示生成或 mask 筛选。
   - 方法核心：扩散/生成式建模，可能用于数据合成、先验建模或掩码优化。
   - 实验结论：可能包含新数据集/基准；适合看评测协议、失败案例和是否能服务 COD。
   - 和我课题的关系：不是 COD 直系论文，但可能提供可迁移的视觉表征、训练策略或评测思路。
   - 可借鉴点：候选 mask 生成、视觉-语言筛选、推理式定位。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

22. **Prob-BBDM: a Probabilistic Brownian Bridge Diffusion Model for MRI sequence image-to-image translation**
   - Source: arXiv, 2026-06-23
   - Authors: Martin Valls, Pascal Bourdon, Christine Fernandez-Maloigne, Guillaume Herpe, David Helbert
   - Tags: diffusion, depth/geometry
   - Links: [paper](http://arxiv.org/abs/2606.24313v1) / [pdf](http://arxiv.org/pdf/2606.24313v1)
   - 论文：Prob-BBDM: a Probabilistic Brownian Bridge Diffusion Model for MRI sequence image-to-image translation
   - 一句话总结：AI-driven image-to-image synthesis is rapidly advancing, with growing applications in medical imaging. Multi-modal image analysis plays a crucial role in optimizing examination quality, yet acquiring multiple...
   - 任务设定：通用计算机视觉任务，先判断是否能迁移到 COD 的感知、定位或分割环节。
   - 方法核心：扩散/生成式建模，可能用于数据合成、先验建模或掩码优化。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：可补充 COD 中纹理、边界、几何先验不足的问题。
   - 可借鉴点：深度或几何先验融合。
   - 可改进点：可思考是否缺少 COD 场景验证、复杂背景失败分析或轻量化部署。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

23. **IMAGIN-4D: Image-Guided Controllable Interaction Generation**
   - Source: arXiv, 2026-06-22
   - Authors: Sai Kumar Dwivedi, Federica Bogo, Buğra Tekin, Chenhongyi Yang, Nadine Bertsch et al.
   - Tags: SAM, diffusion, depth/geometry, video
   - Links: [paper](http://arxiv.org/abs/2606.23675v1) / [pdf](http://arxiv.org/pdf/2606.23675v1)
   - 论文：IMAGIN-4D: Image-Guided Controllable Interaction Generation
   - 一句话总结：Generating human-object interactions (HOI) is central to character animation, robotics, AR/VR, and embodied AI. Recent HOI generation methods synthesize motion from text, object geometry, and sparse waypoints,...
   - 任务设定：基础模型驱动的视觉定位/分割/推理，可用于自动提示生成或 mask 筛选。
   - 方法核心：扩散/生成式建模，可能用于数据合成、先验建模或掩码优化。
   - 实验结论：可能包含新数据集/基准；适合看评测协议、失败案例和是否能服务 COD。
   - 和我课题的关系：可补充 COD 中纹理、边界、几何先验不足的问题。
   - 可借鉴点：候选 mask 生成、视觉-语言筛选、推理式定位；深度或几何先验融合。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

24. **Prompting Diffusion Models for Zero-Shot Instance Segmentation**
   - Source: arXiv, 2026-06-21
   - Authors: Irem Zeynep Alagöz, Nils Morbitzer, Andrea Ramazzina, Nassir Navab, Federico Tombari et al.
   - Tags: diffusion
   - Links: [paper](http://arxiv.org/abs/2606.22660v1) / [pdf](http://arxiv.org/pdf/2606.22660v1)
   - 论文：Prompting Diffusion Models for Zero-Shot Instance Segmentation
   - 一句话总结：Several disruptive research directions have recently emerged in computer vision, including foundation models achieving previously unseen zero-shot performance in scene understanding, even interactively, and ge...
   - 任务设定：通用计算机视觉任务，先判断是否能迁移到 COD 的感知、定位或分割环节。
   - 方法核心：扩散/生成式建模，可能用于数据合成、先验建模或掩码优化。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：不是 COD 直系论文，但可能提供可迁移的视觉表征、训练策略或评测思路。
   - 可借鉴点：任务建模、损失函数、消融组织方式。
   - 可改进点：可思考是否缺少 COD 场景验证、复杂背景失败分析或轻量化部署。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

25. **AD-DINOv3: Enhancing DINOv3 for Zero-Shot Anomaly Detection with Anomaly-Aware Calibration**
   - Source: arXiv, 2025-09-17
   - Authors: Jingyi Yuan, Jianxiong Ye, Wenkang Chen, Chenqiang Gao
   - Tags: VLM/MLLM, diffusion, anomaly/OOD
   - Links: [paper](http://arxiv.org/abs/2509.14084v2) / [pdf](http://arxiv.org/pdf/2509.14084v2)
   - 论文：AD-DINOv3: Enhancing DINOv3 for Zero-Shot Anomaly Detection with Anomaly-Aware Calibration
   - 一句话总结：Zero-Shot Anomaly Detection (ZSAD) seeks to identify anomalies from arbitrary novel categories, offering a scalable and annotation-efficient solution. Traditionally, most ZSAD works have been based on the CLIP...
   - 任务设定：基础模型驱动的视觉定位/分割/推理，可用于自动提示生成或 mask 筛选。
   - 方法核心：提示学习或提示生成，重点看文本/视觉 prompt 如何约束定位。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：可用于伪装目标的语义描述、环境理解和候选区域判断。
   - 可借鉴点：候选 mask 生成、视觉-语言筛选、推理式定位；跨域鲁棒性、不确定性或异常分数。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

26. **FiLo++: Zero-/Few-Shot Anomaly Detection by Fused Fine-Grained Descriptions and Deformable Localization**
   - Source: arXiv, 2025-01-17
   - Authors: Zhaopeng Gu, Bingke Zhu, Guibo Zhu, Yingying Chen, Ming Tang et al.
   - Tags: SAM, reasoning, diffusion, anomaly/OOD
   - Links: [paper](http://arxiv.org/abs/2501.10067v2) / [pdf](http://arxiv.org/pdf/2501.10067v2)
   - 论文：FiLo++: Zero-/Few-Shot Anomaly Detection by Fused Fine-Grained Descriptions and Deformable Localization
   - 一句话总结：Anomaly detection methods typically require extensive normal samples from the target class for training, limiting their applicability in scenarios that require rapid adaptation, such as cold start. Zero-shot a...
   - 任务设定：基础模型驱动的视觉定位/分割/推理，可用于自动提示生成或 mask 筛选。
   - 方法核心：提示学习或提示生成，重点看文本/视觉 prompt 如何约束定位。
   - 实验结论：可能包含新数据集/基准；适合看评测协议、失败案例和是否能服务 COD。
   - 和我课题的关系：可用于伪装目标的语义描述、环境理解和候选区域判断。
   - 可借鉴点：候选 mask 生成、视觉-语言筛选、推理式定位；跨域鲁棒性、不确定性或异常分数。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

27. **Exploring Efficient Open-Vocabulary Segmentation in the Remote Sensing**
   - Source: arXiv, 2025-09-15
   - Authors: Bingyu Li, Haocheng Dong, Da Zhang, Zhiyuan Zhao, Junyu Gao et al.
   - Tags: open-vocabulary, SAM, VLM/MLLM, boundary/frequency, remote sensing
   - Links: [paper](http://arxiv.org/abs/2509.12040v2) / [pdf](http://arxiv.org/pdf/2509.12040v2)
   - 论文：Exploring Efficient Open-Vocabulary Segmentation in the Remote Sensing
   - 一句话总结：Open-Vocabulary Remote Sensing Image Segmentation (OVRSIS), an emerging task that adapts Open-Vocabulary Segmentation (OVS) to the remote sensing (RS) domain, remains underexplored due to the absence of a unif...
   - 任务设定：开放词汇视觉识别/分割，目标类别或文本提示在训练时未必出现。
   - 方法核心：借助 SAM/基础分割模型产生候选 mask，再做筛选或适配。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：适合拓展到开放词汇、零样本或少标注 COD。
   - 可借鉴点：prompt 设计、类别文本构造、免训练迁移流程；候选 mask 生成、视觉-语言筛选、推理式定位；边界/频域增强模块。
   - 可改进点：可改进 prompt 自动生成、负样本约束和 mask 置信度校准。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

28. **TravExplorer: Cross-Floor Embodied Exploration via Traversability-Aware 3-D Planning**
   - Source: arXiv, 2026-05-19
   - Authors: Han Zheng, Zhe Chen, Yudong Huang, Haoran Liu, Jinghao Wang et al.
   - Tags: open-vocabulary, reasoning, depth/geometry, video
   - Links: [paper](http://arxiv.org/abs/2605.19958v1) / [pdf](http://arxiv.org/pdf/2605.19958v1)
   - 论文：TravExplorer: Cross-Floor Embodied Exploration via Traversability-Aware 3-D Planning
   - 一句话总结：Zero-shot Object Navigation (ZSON) has shown promise for open-vocabulary target search in unseen environments, yet most existing systems remain tied to planar representations and single-floor assumptions. Thes...
   - 任务设定：开放词汇视觉识别/分割，目标类别或文本提示在训练时未必出现。
   - 方法核心：多模态大模型推理，可能用于目标描述、区域判断或链式推理。
   - 实验结论：摘要未给出强实验信号；先看实验表格和图 1，再决定是否精读。
   - 和我课题的关系：适合拓展到开放词汇、零样本或少标注 COD。
   - 可借鉴点：prompt 设计、类别文本构造、免训练迁移流程；深度或几何先验融合。
   - 可改进点：可改进 prompt 自动生成、负样本约束和 mask 置信度校准。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

29. **SparseSAM: Structured Sparsification of Activations in Segment Anything Models**
   - Source: arXiv, 2026-05-17
   - Authors: Hoai-Chau Tran, Chi H. Nguyen, Duy M. H. Nguyen, Mathias Niepert, Fan Lai et al.
   - Tags: open-vocabulary, training-free, SAM
   - Links: [paper](http://arxiv.org/abs/2605.17633v1) / [pdf](http://arxiv.org/pdf/2605.17633v1)
   - 论文：SparseSAM: Structured Sparsification of Activations in Segment Anything Models
   - 一句话总结：The Segment Anything Model (SAM) achieves strong open-vocabulary segmentation, but its ViT-based image encoders dominate inference latency and memory. Existing activation compression methods, such as token mer...
   - 任务设定：开放词汇视觉识别/分割，目标类别或文本提示在训练时未必出现。
   - 方法核心：借助 SAM/基础分割模型产生候选 mask，再做筛选或适配。
   - 实验结论：可能包含新数据集/基准；适合看评测协议、失败案例和是否能服务 COD。
   - 和我课题的关系：适合拓展到开放词汇、零样本或少标注 COD。
   - 可借鉴点：prompt 设计、类别文本构造、免训练迁移流程；候选 mask 生成、视觉-语言筛选、推理式定位。
   - 可改进点：可改进 prompt 自动生成、负样本约束和 mask 置信度校准。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

30. **Towards Realistic Open-Vocabulary Remote Sensing Segmentation: Benchmark and Baseline**
   - Source: arXiv, 2026-04-17
   - Authors: Bingyu Li, Tao Huo, Haocheng Dong, Da Zhang, Zhiyuan Zhao et al.
   - Tags: open-vocabulary, remote sensing, anomaly/OOD
   - Links: [paper](http://arxiv.org/abs/2604.15652v1) / [pdf](http://arxiv.org/pdf/2604.15652v1)
   - 论文：Towards Realistic Open-Vocabulary Remote Sensing Segmentation: Benchmark and Baseline
   - 一句话总结：Open-vocabulary remote sensing image segmentation (OVRSIS) remains underexplored due to fragmented datasets, limited training diversity, and the lack of evaluation benchmarks that reflect realistic geospatial...
   - 任务设定：开放词汇视觉识别/分割，目标类别或文本提示在训练时未必出现。
   - 方法核心：异常/OOD 建模，把目标从复杂背景中作为低概率区域凸显出来。
   - 实验结论：可能包含新数据集/基准；适合看评测协议、失败案例和是否能服务 COD。
   - 和我课题的关系：适合拓展到开放词汇、零样本或少标注 COD。
   - 可借鉴点：prompt 设计、类别文本构造、免训练迁移流程；跨域鲁棒性、不确定性或异常分数。
   - 可改进点：可改进 prompt 自动生成、负样本约束和 mask 置信度校准。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

31. **OV-Stitcher: A Global Context-Aware Framework for Training-Free Open-Vocabulary Semantic Segmentation**
   - Source: arXiv, 2026-04-09
   - Authors: Seungjae Moon, Seunghyun Oh, Youngmin Ro
   - Tags: open-vocabulary, training-free, VLM/MLLM, reasoning, diffusion, boundary/frequency
   - Links: [paper](http://arxiv.org/abs/2604.08110v2) / [pdf](http://arxiv.org/pdf/2604.08110v2)
   - 论文：OV-Stitcher: A Global Context-Aware Framework for Training-Free Open-Vocabulary Semantic Segmentation
   - 一句话总结：Training-free open-vocabulary semantic segmentation(TF-OVSS) has recently attracted attention for its ability to perform dense prediction by leveraging the pretrained knowledge of large vision and vision-langu...
   - 任务设定：开放词汇视觉识别/分割，目标类别或文本提示在训练时未必出现。
   - 方法核心：视觉-语言对齐，把语义文本信息引入检测或分割。
   - 实验结论：可能包含新数据集/基准；适合看评测协议、失败案例和是否能服务 COD。
   - 和我课题的关系：适合拓展到开放词汇、零样本或少标注 COD。
   - 可借鉴点：prompt 设计、类别文本构造、免训练迁移流程；候选 mask 生成、视觉-语言筛选、推理式定位；边界/频域增强模块。
   - 可改进点：可改进 prompt 自动生成、负样本约束和 mask 置信度校准。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

32. **TRACE: Evidence Grounding-Guided Multi-Video Event Understanding and Claim Generation**
   - Source: arXiv, 2026-05-16
   - Authors: Pengyu Yan, Akhil Gorugantu, Mahesh Bhosale, Abdul Wasi, Vishvesh Trivedi et al.
   - Tags: VLM/MLLM, reasoning, video
   - Links: [paper](http://arxiv.org/abs/2605.16740v2) / [pdf](http://arxiv.org/pdf/2605.16740v2)
   - 论文：TRACE: Evidence Grounding-Guided Multi-Video Event Understanding and Claim Generation
   - 一句话总结：Multi-video event understanding demands models that can locate and attribute query-relevant evidence scattered across long, heterogeneous video corpora. Existing large vision-language models (LVLMs) often unde...
   - 任务设定：基础模型驱动的视觉定位/分割/推理，可用于自动提示生成或 mask 筛选。
   - 方法核心：视觉-语言对齐，把语义文本信息引入检测或分割。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：可用于伪装目标的语义描述、环境理解和候选区域判断。
   - 可借鉴点：候选 mask 生成、视觉-语言筛选、推理式定位。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

33. **Segmentation, Detection and Explanation: A Unified Framework for CT Appearance Reasoning**
   - Source: arXiv, 2026-05-15
   - Authors: Yuyuan Liu, Can Peng, Yingyu Yang, Qianye Yang, Cheng Ouyang et al.
   - Tags: VLM/MLLM, reasoning, diffusion
   - Links: [paper](http://arxiv.org/abs/2605.15997v1) / [pdf](http://arxiv.org/pdf/2605.15997v1)
   - 论文：Segmentation, Detection and Explanation: A Unified Framework for CT Appearance Reasoning
   - 一句话总结：Recent progress in deep learning has significantly advanced CT image analysis, particularly for segmentation tasks. However, these advances are largely confined to image-level pattern recognition, with most me...
   - 任务设定：基础模型驱动的视觉定位/分割/推理，可用于自动提示生成或 mask 筛选。
   - 方法核心：提示学习或提示生成，重点看文本/视觉 prompt 如何约束定位。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：可用于伪装目标的语义描述、环境理解和候选区域判断。
   - 可借鉴点：候选 mask 生成、视觉-语言筛选、推理式定位。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

34. **DeepTumorVQA: A Hierarchical 3D CT Benchmark for Stage-Wise Evaluation of Medical VLMs and Tool-Augmented Agents**
   - Source: arXiv, 2026-05-10
   - Authors: Yixiong Chen, Wenjie Xiao, Pedro R. A. S. Bassi, Boyan Wang, Liang He et al.
   - Tags: VLM/MLLM, reasoning, diffusion, boundary/frequency, depth/geometry
   - Links: [paper](http://arxiv.org/abs/2605.09679v1) / [pdf](http://arxiv.org/pdf/2605.09679v1)
   - 论文：DeepTumorVQA: A Hierarchical 3D CT Benchmark for Stage-Wise Evaluation of Medical VLMs and Tool-Augmented Agents
   - 一句话总结：Medical vision-language models (VLMs) and AI agents have made significant progress in learning to analyze and reason about clinical images. However, existing medical visual question answering (VQA) benchmarks...
   - 任务设定：基础模型驱动的视觉定位/分割/推理，可用于自动提示生成或 mask 筛选。
   - 方法核心：视觉-语言对齐，把语义文本信息引入检测或分割。
   - 实验结论：可能包含新数据集/基准；适合看评测协议、失败案例和是否能服务 COD。
   - 和我课题的关系：可补充 COD 中纹理、边界、几何先验不足的问题。
   - 可借鉴点：候选 mask 生成、视觉-语言筛选、推理式定位；边界/频域增强模块；深度或几何先验融合。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

35. **SubspaceAD: Training-Free Few-Shot Anomaly Detection via Subspace Modeling**
   - Source: arXiv, 2026-02-26
   - Authors: Camile Lendering, Erkut Akdag, Egor Bondarev
   - Tags: training-free, VLM/MLLM, retrieval/prototype, remote sensing, anomaly/OOD
   - Links: [paper](http://arxiv.org/abs/2602.23013v3) / [pdf](http://arxiv.org/pdf/2602.23013v3)
   - 论文：SubspaceAD: Training-Free Few-Shot Anomaly Detection via Subspace Modeling
   - 一句话总结：Detecting visual anomalies in industrial inspection often requires training with only a few normal images per category. Recent few-shot methods achieve strong results employing foundation-model features, but t...
   - 任务设定：免训练或少训练迁移设定，重点看 prompt、特征选择和后处理。
   - 方法核心：提示学习或提示生成，重点看文本/视觉 prompt 如何约束定位。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：适合拓展到开放词汇、零样本或少标注 COD。
   - 可借鉴点：prompt 设计、类别文本构造、免训练迁移流程；候选 mask 生成、视觉-语言筛选、推理式定位；跨域鲁棒性、不确定性或异常分数。
   - 可改进点：可改进 prompt 自动生成、负样本约束和 mask 置信度校准。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

36. **V-Zero: Answer-Label-Free On-Policy Distillation with Contrastive Evidence Gating for Fine-Grained Visual Reasoning**
   - Source: arXiv, 2026-06-24
   - Authors: Haoxiang Sun, Zhihang Yi, Langxuan Deng, Yuhao Zhou, Peiqi Jia et al.
   - Tags: SAM, VLM/MLLM, reasoning
   - Links: [paper](http://arxiv.org/abs/2606.25319v1) / [pdf](http://arxiv.org/pdf/2606.25319v1)
   - 论文：V-Zero: Answer-Label-Free On-Policy Distillation with Contrastive Evidence Gating for Fine-Grained Visual Reasoning
   - 一句话总结：Fine-grained visual reasoning requires multimodal large language models (MLLMs) to identify task-relevant visual evidence and ground their reasoning in local image regions. Existing agentic methods typically r...
   - 任务设定：基础模型驱动的视觉定位/分割/推理，可用于自动提示生成或 mask 筛选。
   - 方法核心：借助 SAM/基础分割模型产生候选 mask，再做筛选或适配。
   - 实验结论：可能包含新数据集/基准；适合看评测协议、失败案例和是否能服务 COD。
   - 和我课题的关系：可用于伪装目标的语义描述、环境理解和候选区域判断。
   - 可借鉴点：候选 mask 生成、视觉-语言筛选、推理式定位。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

37. **Are We There Yet? Exploring the Capabilities of MLLMs in Assistive AI Applications**
   - Source: arXiv, 2026-06-23
   - Authors: Shayon Dasgupta, Avijit Dasgupta, C. V. Jawahar
   - Tags: VLM/MLLM, reasoning, anomaly/OOD
   - Links: [paper](http://arxiv.org/abs/2606.25084v1) / [pdf](http://arxiv.org/pdf/2606.25084v1)
   - 论文：Are We There Yet? Exploring the Capabilities of MLLMs in Assistive AI Applications
   - 一句话总结：Multimodal Large Language Models (MLLMs) have redefined visual understanding by combining vision encoders with large-scale language models. This unified architecture enables strong performance on tasks like im...
   - 任务设定：基础模型驱动的视觉定位/分割/推理，可用于自动提示生成或 mask 筛选。
   - 方法核心：视觉-语言对齐，把语义文本信息引入检测或分割。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：可用于伪装目标的语义描述、环境理解和候选区域判断。
   - 可借鉴点：候选 mask 生成、视觉-语言筛选、推理式定位；跨域鲁棒性、不确定性或异常分数。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

38. **CineCap: Structured Reasoning with Spatio-Temporal Anchors for Cinematographic Video Captioning**
   - Source: arXiv, 2026-06-23
   - Authors: Xinyu Mao, Yuhui Zeng, Xiaokun Liu, Wenyu Qin, Meng Wang et al.
   - Tags: VLM/MLLM, reasoning, diffusion, depth/geometry, video
   - Links: [paper](http://arxiv.org/abs/2606.24636v1) / [pdf](http://arxiv.org/pdf/2606.24636v1)
   - 论文：CineCap: Structured Reasoning with Spatio-Temporal Anchors for Cinematographic Video Captioning
   - 一句话总结：Cinematographic captioning aims to describe how a video is filmed using professional film-language concepts such as camera movement, shot size, depth of field, composition, and shooting angle. This capability...
   - 任务设定：基础模型驱动的视觉定位/分割/推理，可用于自动提示生成或 mask 筛选。
   - 方法核心：视觉-语言对齐，把语义文本信息引入检测或分割。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：可补充 COD 中纹理、边界、几何先验不足的问题。
   - 可借鉴点：候选 mask 生成、视觉-语言筛选、推理式定位；深度或几何先验融合。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

39. **3D-PLOT-LLM: Part-Level Object Tokens for 3D Large Language Models**
   - Source: arXiv, 2026-06-18
   - Authors: Jintang Xue, Xinyu Wang, Yixing Wu, Jingwen Chen, C. -C. Jay Kuo
   - Tags: VLM/MLLM, diffusion, depth/geometry
   - Links: [paper](http://arxiv.org/abs/2606.19828v1) / [pdf](http://arxiv.org/pdf/2606.19828v1)
   - 论文：3D-PLOT-LLM: Part-Level Object Tokens for 3D Large Language Models
   - 一句话总结：3D multimodal large language models (3D MLLMs) describe a 3D object as a whole but cannot address, name, or reason about its parts. Prior part-aware attempts add segmentation decoders, heavier 3D encoders, or...
   - 任务设定：基础模型驱动的视觉定位/分割/推理，可用于自动提示生成或 mask 筛选。
   - 方法核心：提示学习或提示生成，重点看文本/视觉 prompt 如何约束定位。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：可补充 COD 中纹理、边界、几何先验不足的问题。
   - 可借鉴点：候选 mask 生成、视觉-语言筛选、推理式定位；深度或几何先验融合。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

40. **Cross-Modality Structural Guidance in 3D Latent Diffusion for Robust FLAIR Super-Resolution**
   - Source: arXiv, 2026-06-24
   - Authors: Haoyu Lan, Jiazhen Zhang, John Onofrey, Bino Varghese, Nasim Sheikh-Bahaei et al.
   - Tags: SAM, diffusion, boundary/frequency, depth/geometry, low-level
   - Links: [paper](http://arxiv.org/abs/2606.25255v1) / [pdf](http://arxiv.org/pdf/2606.25255v1)
   - 论文：Cross-Modality Structural Guidance in 3D Latent Diffusion for Robust FLAIR Super-Resolution
   - 一句话总结：High-resolution (HR) MRI acquisition is often hampered by scan time constraints, resulting in anisotropic or low-resolution scans (e.g., thick-slice FLAIR) that limit diagnostic accuracy. While deep learning-b...
   - 任务设定：基础模型驱动的视觉定位/分割/推理，可用于自动提示生成或 mask 筛选。
   - 方法核心：扩散/生成式建模，可能用于数据合成、先验建模或掩码优化。
   - 实验结论：可能包含新数据集/基准；适合看评测协议、失败案例和是否能服务 COD。
   - 和我课题的关系：可补充 COD 中纹理、边界、几何先验不足的问题。
   - 可借鉴点：候选 mask 生成、视觉-语言筛选、推理式定位；边界/频域增强模块；深度或几何先验融合。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

41. **NeuroSonic: Conditional Flow Matching for EEG-to-Speech Reconstruction**
   - Source: arXiv, 2026-06-23
   - Authors: Wenhao Gao, Yifan Wang, Yijia Ma, Carl Yang, Wen Li et al.
   - Tags: SAM, diffusion, video, low-level
   - Links: [paper](http://arxiv.org/abs/2606.24087v1) / [pdf](http://arxiv.org/pdf/2606.24087v1)
   - 论文：NeuroSonic: Conditional Flow Matching for EEG-to-Speech Reconstruction
   - 一句话总结：Reconstructing continuous speech from scalp electroencephalography (EEG) remains fundamentally challenging. EEG provides a weak, spatially diffuse, and highly variable measurement of distributed cortical activ...
   - 任务设定：基础模型驱动的视觉定位/分割/推理，可用于自动提示生成或 mask 筛选。
   - 方法核心：扩散/生成式建模，可能用于数据合成、先验建模或掩码优化。
   - 实验结论：可能包含新数据集/基准；适合看评测协议、失败案例和是否能服务 COD。
   - 和我课题的关系：不是 COD 直系论文，但可能提供可迁移的视觉表征、训练策略或评测思路。
   - 可借鉴点：候选 mask 生成、视觉-语言筛选、推理式定位。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

42. **C^2GR: Coupled Comprehensive Generative Replay for a Continually Learnable Universal Segmentation Model**
   - Source: arXiv, 2026-06-22
   - Authors: Wei Li, Jingyang Zhang, Guoan Wang, Junzhi Ning, Yang Chen et al.
   - Tags: diffusion, low-level
   - Links: [paper](http://arxiv.org/abs/2606.23473v1) / [pdf](http://arxiv.org/pdf/2606.23473v1)
   - 论文：C^2GR: Coupled Comprehensive Generative Replay for a Continually Learnable Universal Segmentation Model
   - 一句话总结：Universal segmentation models exhibit significant potential for diverse tasks involving different imaging modalities and segmentation objectives. Task-Incremental Learning provides a privacy-preserving approac...
   - 任务设定：通用计算机视觉任务，先判断是否能迁移到 COD 的感知、定位或分割环节。
   - 方法核心：扩散/生成式建模，可能用于数据合成、先验建模或掩码优化。
   - 实验结论：摘要未给出强实验信号；先看实验表格和图 1，再决定是否精读。
   - 和我课题的关系：不是 COD 直系论文，但可能提供可迁移的视觉表征、训练策略或评测思路。
   - 可借鉴点：任务建模、损失函数、消融组织方式。
   - 可改进点：可思考是否缺少 COD 场景验证、复杂背景失败分析或轻量化部署。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

43. **BEV-Denoise: Learning Intrinsic Noise for Accurate Bird's-Eye-View Semantic Segmentation**
   - Source: arXiv, 2026-06-22
   - Authors: Dooseop Choi, Kyounghwan An, Kyoung-Wook Min
   - Tags: diffusion, low-level
   - Links: [paper](http://arxiv.org/abs/2606.22931v1) / [pdf](http://arxiv.org/pdf/2606.22931v1)
   - 论文：BEV-Denoise: Learning Intrinsic Noise for Accurate Bird's-Eye-View Semantic Segmentation
   - 一句话总结：In this paper, we present a framework dubbed \textbf{BEV-Denoise} that estimates and removes intrinsic noise from learned Bird's-Eye-View (BEV) features to achieve accurate BEV semantic segmentation. Inspired...
   - 任务设定：通用计算机视觉任务，先判断是否能迁移到 COD 的感知、定位或分割环节。
   - 方法核心：扩散/生成式建模，可能用于数据合成、先验建模或掩码优化。
   - 实验结论：可能包含新数据集/基准；适合看评测协议、失败案例和是否能服务 COD。
   - 和我课题的关系：不是 COD 直系论文，但可能提供可迁移的视觉表征、训练策略或评测思路。
   - 可借鉴点：任务建模、损失函数、消融组织方式。
   - 可改进点：可思考是否缺少 COD 场景验证、复杂背景失败分析或轻量化部署。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

44. **Crane: Context-Guided Prompt Learning and Attention Refinement for Zero-Shot Anomaly Detection**
   - Source: arXiv, 2025-04-15
   - Authors: Alireza Salehi, Mohammadreza Salehi, Reshad Hosseini, Cees G. M. Snoek, Makoto Yamada et al.
   - Tags: SAM, diffusion, boundary/frequency, anomaly/OOD
   - Links: [paper](http://arxiv.org/abs/2504.11055v2) / [pdf](http://arxiv.org/pdf/2504.11055v2)
   - 论文：Crane: Context-Guided Prompt Learning and Attention Refinement for Zero-Shot Anomaly Detection
   - 一句话总结：Anomaly Detection involves identifying deviations from normal data distributions and is critical in fields such as medical diagnostics and industrial defect detection. Traditional AD methods typically require...
   - 任务设定：基础模型驱动的视觉定位/分割/推理，可用于自动提示生成或 mask 筛选。
   - 方法核心：提示学习或提示生成，重点看文本/视觉 prompt 如何约束定位。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：可补充 COD 中纹理、边界、几何先验不足的问题。
   - 可借鉴点：候选 mask 生成、视觉-语言筛选、推理式定位；边界/频域增强模块；跨域鲁棒性、不确定性或异常分数。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

45. **Taming SAM3 in the Wild: A Concept Bank for Open-Vocabulary Segmentation**
   - Source: arXiv, 2026-02-06
   - Authors: Gensheng Pei, Xiruo Jiang, Yazhou Yao, Xiangbo Shu, Fumin Shen et al.
   - Tags: open-vocabulary, SAM, diffusion, retrieval/prototype
   - Links: [paper](http://arxiv.org/abs/2602.06333v1) / [pdf](http://arxiv.org/pdf/2602.06333v1)
   - 论文：Taming SAM3 in the Wild: A Concept Bank for Open-Vocabulary Segmentation
   - 一句话总结：The recent introduction of \texttt{SAM3} has revolutionized Open-Vocabulary Segmentation (OVS) through \textit{promptable concept segmentation}, which grounds pixel predictions in flexible concept prompts. How...
   - 任务设定：开放词汇视觉识别/分割，目标类别或文本提示在训练时未必出现。
   - 方法核心：提示学习或提示生成，重点看文本/视觉 prompt 如何约束定位。
   - 实验结论：可能包含新数据集/基准；适合看评测协议、失败案例和是否能服务 COD。
   - 和我课题的关系：适合拓展到开放词汇、零样本或少标注 COD。
   - 可借鉴点：prompt 设计、类别文本构造、免训练迁移流程；候选 mask 生成、视觉-语言筛选、推理式定位。
   - 可改进点：可改进 prompt 自动生成、负样本约束和 mask 置信度校准。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

46. **AerOSeg: Harnessing SAM for Open-Vocabulary Segmentation in Remote Sensing Images**
   - Source: arXiv, 2025-04-12
   - Authors: Saikat Dutta, Akhil Vasim, Siddhant Gole, Hamid Rezatofighi, Biplab Banerjee
   - Tags: open-vocabulary, SAM, diffusion, remote sensing
   - Links: [paper](http://arxiv.org/abs/2504.09203v1) / [pdf](http://arxiv.org/pdf/2504.09203v1)
   - 论文：AerOSeg: Harnessing SAM for Open-Vocabulary Segmentation in Remote Sensing Images
   - 一句话总结：Image segmentation beyond predefined categories is a key challenge in remote sensing, where novel and unseen classes often emerge during inference. Open-vocabulary image Segmentation addresses these generaliza...
   - 任务设定：开放词汇视觉识别/分割，目标类别或文本提示在训练时未必出现。
   - 方法核心：提示学习或提示生成，重点看文本/视觉 prompt 如何约束定位。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：适合拓展到开放词汇、零样本或少标注 COD。
   - 可借鉴点：prompt 设计、类别文本构造、免训练迁移流程；候选 mask 生成、视觉-语言筛选、推理式定位。
   - 可改进点：可改进 prompt 自动生成、负样本约束和 mask 置信度校准。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

47. **Decomposed Vision-Language Alignment for Fine-Grained Open-Vocabulary Segmentation**
   - Source: arXiv, 2026-05-15
   - Authors: Chenhao Wang, Yingrui Ji, Yu Meng, Yao Zhu
   - Tags: open-vocabulary, VLM/MLLM
   - Links: [paper](http://arxiv.org/abs/2605.15942v1) / [pdf](http://arxiv.org/pdf/2605.15942v1)
   - 论文：Decomposed Vision-Language Alignment for Fine-Grained Open-Vocabulary Segmentation
   - 一句话总结：Open-vocabulary segmentation models often struggle to generalize to unseen combinations of object categories and attributes, because fine-grained descriptions are typically encoded as holistic sentences that e...
   - 任务设定：开放词汇视觉识别/分割，目标类别或文本提示在训练时未必出现。
   - 方法核心：提示学习或提示生成，重点看文本/视觉 prompt 如何约束定位。
   - 实验结论：可能包含新数据集/基准；适合看评测协议、失败案例和是否能服务 COD。
   - 和我课题的关系：适合拓展到开放词汇、零样本或少标注 COD。
   - 可借鉴点：prompt 设计、类别文本构造、免训练迁移流程；候选 mask 生成、视觉-语言筛选、推理式定位。
   - 可改进点：可改进 prompt 自动生成、负样本约束和 mask 置信度校准。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

48. **Making Training-Free Diffusion Segmentors Scale with the Generative Power**
   - Source: arXiv, 2026-03-06
   - Authors: Benyuan Meng, Qianqian Xu, Zitai Wang, Xiaochun Cao, Longtao Huang et al.
   - Tags: training-free, diffusion
   - Links: [paper](http://arxiv.org/abs/2603.06178v3) / [pdf](http://arxiv.org/pdf/2603.06178v3)
   - 论文：Making Training-Free Diffusion Segmentors Scale with the Generative Power
   - 一句话总结：As powerful generative models, text-to-image diffusion models have recently been explored for discriminative tasks. A line of research focuses on adapting a pre-trained diffusion model to semantic segmentation...
   - 任务设定：免训练或少训练迁移设定，重点看 prompt、特征选择和后处理。
   - 方法核心：扩散/生成式建模，可能用于数据合成、先验建模或掩码优化。
   - 实验结论：可能包含新数据集/基准；适合看评测协议、失败案例和是否能服务 COD。
   - 和我课题的关系：适合拓展到开放词汇、零样本或少标注 COD。
   - 可借鉴点：prompt 设计、类别文本构造、免训练迁移流程。
   - 可改进点：可改进 prompt 自动生成、负样本约束和 mask 置信度校准。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

49. **R2AoP: Reliable and Robust Angle of Progression Estimation from Intrapartum Ultrasound**
   - Source: arXiv, 2026-05-20
   - Authors: Yuanhan Wang, Yifei Chen, Beining Wu, Mingxuan Liu, Xiaotian Hu et al.
   - Tags: diffusion, boundary/frequency, depth/geometry
   - Links: [paper](http://arxiv.org/abs/2605.21099v1) / [pdf](http://arxiv.org/pdf/2605.21099v1)
   - 论文：R2AoP: Reliable and Robust Angle of Progression Estimation from Intrapartum Ultrasound
   - 一句话总结：Accurate estimation of the Angle of Progression (AoP) from intrapartum transperineal ultrasound is critical for objective assessment of labor progression, yet remains highly sensitive to imaging noise, boundar...
   - 任务设定：通用计算机视觉任务，先判断是否能迁移到 COD 的感知、定位或分割环节。
   - 方法核心：边界感知建模，适合改善伪装目标轮廓不清的问题。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：可补充 COD 中纹理、边界、几何先验不足的问题。
   - 可借鉴点：边界/频域增强模块；深度或几何先验融合。
   - 可改进点：可结合多尺度语义上下文，避免只强化纹理导致误检。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

50. **VISTA: Variance-Gated Inter-Sequence Test-Time Adaptation for Multi-Sequence MRI Segmentation**
   - Source: arXiv, 2026-05-17
   - Authors: Zhipeng Deng, Jiale Zhou, Wenhan Jiang, Haolin Wang, Xun Lin et al.
   - Tags: boundary/frequency
   - Links: [paper](http://arxiv.org/abs/2605.17433v2) / [pdf](http://arxiv.org/pdf/2605.17433v2)
   - 论文：VISTA: Variance-Gated Inter-Sequence Test-Time Adaptation for Multi-Sequence MRI Segmentation
   - 一句话总结：Deploying multi-sequence magnetic resonance imaging (MRI) segmentation models to new clinical environments is challenging due to variations in scanners and acquisition protocols. Although existing TTA methods...
   - 任务设定：通用计算机视觉任务，先判断是否能迁移到 COD 的感知、定位或分割环节。
   - 方法核心：频域/纹理特征增强，适合处理伪装背景与目标细粒度差异。
   - 实验结论：摘要强调消融、鲁棒性或泛化；适合优先看实验设计和跨域表现。
   - 和我课题的关系：可补充 COD 中纹理、边界、几何先验不足的问题。
   - 可借鉴点：边界/频域增强模块。
   - 可改进点：可结合多尺度语义上下文，避免只强化纹理导致误检。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

51. **The Golden Subspace: Where Efficiency Meets Generalization in Continual Test-Time Adaptation**
   - Source: arXiv, 2026-03-23
   - Authors: Guannan Lai, Da-Wei Zhou, Zhenguo Li, Han-Jia Ye
   - Tags: SAM
   - Links: [paper](http://arxiv.org/abs/2603.21928v1) / [pdf](http://arxiv.org/pdf/2603.21928v1)
   - 论文：The Golden Subspace: Where Efficiency Meets Generalization in Continual Test-Time Adaptation
   - 一句话总结：Continual Test-Time Adaptation (CTTA) aims to enable models to adapt online to unlabeled data streams under distribution shift without accessing source data. Existing CTTA methods face an efficiency-generaliza...
   - 任务设定：基础模型驱动的视觉定位/分割/推理，可用于自动提示生成或 mask 筛选。
   - 方法核心：借助 SAM/基础分割模型产生候选 mask，再做筛选或适配。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：不是 COD 直系论文，但可能提供可迁移的视觉表征、训练策略或评测思路。
   - 可借鉴点：候选 mask 生成、视觉-语言筛选、推理式定位。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

52. **Staying VIGILant: Mitigating Visual Laziness via Counterfactual Visual Alignment in MLLMs**
   - Source: arXiv, 2026-06-24
   - Authors: Xi Xiao, Chen Liu, Chih-Ting Liao, Yunbei Zhang, Qizhen Lan et al.
   - Tags: VLM/MLLM, reasoning, depth/geometry
   - Links: [paper](http://arxiv.org/abs/2606.26387v1) / [pdf](http://arxiv.org/pdf/2606.26387v1)
   - 论文：Staying VIGILant: Mitigating Visual Laziness via Counterfactual Visual Alignment in MLLMs
   - 一句话总结：Multimodal large language models (MLLMs) extend large language models (LLMs) with visual perception, enabling joint reasoning over images and text. Despite inheriting strong reasoning capabilities from LLMs, t...
   - 任务设定：基础模型驱动的视觉定位/分割/推理，可用于自动提示生成或 mask 筛选。
   - 方法核心：反事实建模/拒识机制，用来降低误检或判断目标是否存在。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：可补充 COD 中纹理、边界、几何先验不足的问题。
   - 可借鉴点：候选 mask 生成、视觉-语言筛选、推理式定位；深度或几何先验融合。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

53. **Mind the Heads: Topological Representation Alignment for Multimodal LLMs**
   - Source: arXiv, 2026-06-22
   - Authors: Davide Caffagni, Alberto Compagnoni, Federico Melis, Sara Sarto, Pier Luigi Dovesi et al.
   - Tags: VLM/MLLM, anomaly/OOD
   - Links: [paper](http://arxiv.org/abs/2606.23885v1) / [pdf](http://arxiv.org/pdf/2606.23885v1)
   - 论文：Mind the Heads: Topological Representation Alignment for Multimodal LLMs
   - 一句话总结：Representation alignment has emerged as an effective approach to improve Multimodal Large Language Models (MLLMs) by regularizing their internal representations toward those of an external vision encoder. Howe...
   - 任务设定：基础模型驱动的视觉定位/分割/推理，可用于自动提示生成或 mask 筛选。
   - 方法核心：视觉-语言对齐，把语义文本信息引入检测或分割。
   - 实验结论：可能包含新数据集/基准；适合看评测协议、失败案例和是否能服务 COD。
   - 和我课题的关系：可用于伪装目标的语义描述、环境理解和候选区域判断。
   - 可借鉴点：候选 mask 生成、视觉-语言筛选、推理式定位；跨域鲁棒性、不确定性或异常分数。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

54. **Gen-VCoT: Generative Visual Chain-of-Thought Reasoning via Diffusion-Based RGB Intermediate Representations**
   - Source: arXiv, 2026-06-15
   - Authors: Zhiqiang Zhou, Junliang Dai, Xu ling
   - Tags: SAM, VLM/MLLM, reasoning, diffusion, depth/geometry
   - Links: [paper](http://arxiv.org/abs/2606.16783v1) / [pdf](http://arxiv.org/pdf/2606.16783v1)
   - 论文：Gen-VCoT: Generative Visual Chain-of-Thought Reasoning via Diffusion-Based RGB Intermediate Representations
   - 一句话总结：Multimodal large language models (MLLMs) excel at visual reasoning but rely on text-based chain-of-thought (CoT), lacking interpretable visual intermediates. Existing methods use opaque tokens or external tool...
   - 任务设定：基础模型驱动的视觉定位/分割/推理，可用于自动提示生成或 mask 筛选。
   - 方法核心：扩散/生成式建模，可能用于数据合成、先验建模或掩码优化。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：可补充 COD 中纹理、边界、几何先验不足的问题。
   - 可借鉴点：候选 mask 生成、视觉-语言筛选、推理式定位；深度或几何先验融合。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

55. **THREAD: Trajectory Planning for Hybrid Rigid-Soft Manipulators with Environment-Aware Diffusion**
   - Source: arXiv, 2026-06-19
   - Authors: Shivani Kamtikar, Pranav Asthana, Naveen Kumar Uppalapati, Girish Krishnan, Girish Chowdhary
   - Tags: diffusion, depth/geometry
   - Links: [paper](http://arxiv.org/abs/2606.21792v1) / [pdf](http://arxiv.org/pdf/2606.21792v1)
   - 论文：THREAD: Trajectory Planning for Hybrid Rigid-Soft Manipulators with Environment-Aware Diffusion
   - 一句话总结：Manipulation in confined environments, such as threading a manipulator through narrow apertures, remains a fundamental challenge, especially for conventional rigid robots. Hybrid rigid-soft manipulators offer...
   - 任务设定：通用计算机视觉任务，先判断是否能迁移到 COD 的感知、定位或分割环节。
   - 方法核心：扩散/生成式建模，可能用于数据合成、先验建模或掩码优化。
   - 实验结论：摘要未给出强实验信号；先看实验表格和图 1，再决定是否精读。
   - 和我课题的关系：可补充 COD 中纹理、边界、几何先验不足的问题。
   - 可借鉴点：深度或几何先验融合。
   - 可改进点：可思考是否缺少 COD 场景验证、复杂背景失败分析或轻量化部署。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

56. **ELDiff: When Evidential Learning Meets Text-to-Image Diffusion**
   - Source: arXiv, 2026-06-18
   - Authors: Qingtao Pan, Kai Ye, Zhihao Dou, Bing Ji, Shuo Li
   - Tags: diffusion, low-level
   - Links: [paper](http://arxiv.org/abs/2606.20924v1) / [pdf](http://arxiv.org/pdf/2606.20924v1)
   - 论文：ELDiff: When Evidential Learning Meets Text-to-Image Diffusion
   - 一句话总结：In multi-object text-to-image (T2I) diffusion, ensuring semantic consistency between textual prompts and generated visual content is crucial for image synthesis. However, such consistency constraint is often u...
   - 任务设定：通用计算机视觉任务，先判断是否能迁移到 COD 的感知、定位或分割环节。
   - 方法核心：扩散/生成式建模，可能用于数据合成、先验建模或掩码优化。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：不是 COD 直系论文，但可能提供可迁移的视觉表征、训练策略或评测思路。
   - 可借鉴点：任务建模、损失函数、消融组织方式。
   - 可改进点：可思考是否缺少 COD 场景验证、复杂背景失败分析或轻量化部署。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

57. **Search is All You Need for Few-shot Anomaly Detection**
   - Source: arXiv, 2025-04-16
   - Authors: Qishan Wang, Jia Guo, Shuyong Gao, Haofen Wang, Li Xiong et al.
   - Tags: training-free, SAM, retrieval/prototype, boundary/frequency, anomaly/OOD
   - Links: [paper](http://arxiv.org/abs/2504.11895v2) / [pdf](http://arxiv.org/pdf/2504.11895v2)
   - 论文：Search is All You Need for Few-shot Anomaly Detection
   - 一句话总结：Few-shot anomaly detection (FSAD) has emerged as a crucial yet challenging task in industrial inspection, where normal distribution modeling must be accomplished with only a few normal images. While existing a...
   - 任务设定：免训练或少训练迁移设定，重点看 prompt、特征选择和后处理。
   - 方法核心：提示学习或提示生成，重点看文本/视觉 prompt 如何约束定位。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：适合拓展到开放词汇、零样本或少标注 COD。
   - 可借鉴点：prompt 设计、类别文本构造、免训练迁移流程；候选 mask 生成、视觉-语言筛选、推理式定位；边界/频域增强模块；跨域鲁棒性、不确定性或异常分数。
   - 可改进点：可改进 prompt 自动生成、负样本约束和 mask 置信度校准。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

58. **UniVAD: A Training-free Unified Model for Few-shot Visual Anomaly Detection**
   - Source: arXiv, 2024-12-04
   - Authors: Zhaopeng Gu, Bingke Zhu, Guibo Zhu, Yingying Chen, Ming Tang et al.
   - Tags: training-free, SAM, anomaly/OOD
   - Links: [paper](http://arxiv.org/abs/2412.03342v3) / [pdf](http://arxiv.org/pdf/2412.03342v3)
   - 论文：UniVAD: A Training-free Unified Model for Few-shot Visual Anomaly Detection
   - 一句话总结：Visual Anomaly Detection (VAD) aims to identify abnormal samples in images that deviate from normal patterns, covering multiple domains, including industrial, logical, and medical fields. Due to the domain gap...
   - 任务设定：免训练或少训练迁移设定，重点看 prompt、特征选择和后处理。
   - 方法核心：借助 SAM/基础分割模型产生候选 mask，再做筛选或适配。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：适合拓展到开放词汇、零样本或少标注 COD。
   - 可借鉴点：prompt 设计、类别文本构造、免训练迁移流程；候选 mask 生成、视觉-语言筛选、推理式定位；跨域鲁棒性、不确定性或异常分数。
   - 可改进点：可改进 prompt 自动生成、负样本约束和 mask 置信度校准。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

59. **HD-TTA: Hypothesis-Driven Test-Time Adaptation for Safer Brain Tumor Segmentation**
   - Source: arXiv, 2026-02-23
   - Authors: Kartik Jhawar, Lipo Wang
   - Tags: SAM, diffusion, depth/geometry
   - Links: [paper](http://arxiv.org/abs/2602.19454v1) / [pdf](http://arxiv.org/pdf/2602.19454v1)
   - 论文：HD-TTA: Hypothesis-Driven Test-Time Adaptation for Safer Brain Tumor Segmentation
   - 一句话总结：Standard Test-Time Adaptation (TTA) methods typically treat inference as a blind optimization task, applying generic objectives to all or filtered test samples. In safety-critical medical segmentation, this la...
   - 任务设定：基础模型驱动的视觉定位/分割/推理，可用于自动提示生成或 mask 筛选。
   - 方法核心：借助 SAM/基础分割模型产生候选 mask，再做筛选或适配。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：可补充 COD 中纹理、边界、几何先验不足的问题。
   - 可借鉴点：候选 mask 生成、视觉-语言筛选、推理式定位；深度或几何先验融合。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

60. **Efficient Encoder-Free Fourier-based 3D Large Multimodal Model**
   - Source: CVPR 2026, 2026
   - Authors: Guofeng Mei, Wei Lin, Luigi Riz, Yujiao Wu, Yiming Wang et al.
   - Tags: depth/geometry
   - Links: [paper](https://openaccess.thecvf.com/content/CVPR2026/html/Mei_Efficient_Encoder-Free_Fourier-based_3D_Large_Multimodal_Model_CVPR_2026_paper.html) / [pdf](https://openaccess.thecvf.com/content/CVPR2026/papers/Mei_Efficient_Encoder-Free_Fourier-based_3D_Large_Multimodal_Model_CVPR_2026_paper.pdf)
   - 论文：Efficient Encoder-Free Fourier-based 3D Large Multimodal Model
   - 一句话总结：CVF OpenAccess paper. Open the paper page for full abstract and method details.
   - 任务设定：通用计算机视觉任务，先判断是否能迁移到 COD 的感知、定位或分割环节。
   - 方法核心：视觉-语言对齐，把语义文本信息引入检测或分割。
   - 实验结论：当前来源只提供标题级信息；需要打开论文页确认数据集、指标和消融。
   - 和我课题的关系：可补充 COD 中纹理、边界、几何先验不足的问题。
   - 可借鉴点：深度或几何先验融合。
   - 可改进点：可思考是否缺少 COD 场景验证、复杂背景失败分析或轻量化部署。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

## 2026-06-26 20:37 更新

Selected papers: 3394

### 当日优先读

1. **CFCamo: A Counterfactual Detect-or-Abstain Framework for Camouflaged Object Detection**
   - Source: arXiv, 2026-05-28
   - Authors: Suhang Li, Osamu Yoshie, Yuya Ieiri
   - Tags: COD, SAM, VLM/MLLM
   - Links: [paper](http://arxiv.org/abs/2606.11231v1) / [pdf](http://arxiv.org/pdf/2606.11231v1)
   - 论文：CFCamo: A Counterfactual Detect-or-Abstain Framework for Camouflaged Object Detection
   - 一句话总结：Vision-language reinforcement learning has recently shown strong target-present localization for camouflaged object detection (COD). Yet localization is only one side of the decision: when the agent faces an o...
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：反事实建模/拒识机制，用来降低误检或判断目标是否存在。
   - 实验结论：可能包含新数据集/基准；适合看评测协议、失败案例和是否能服务 COD。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；候选 mask 生成、视觉-语言筛选、推理式定位。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

2. **A Retinomorphic Optical Spiking Neuron for Camouflaged Object Detection**
   - Source: arXiv, 2026-05-30
   - Authors: Srilagna Sahoo, Adwaaiit Pande, Kartikey Thakar, Shubham Sahay, Saurabh Lodha
   - Tags: COD, boundary/frequency
   - Links: [paper](http://arxiv.org/abs/2606.00818v1) / [pdf](http://arxiv.org/pdf/2606.00818v1)
   - 论文：A Retinomorphic Optical Spiking Neuron for Camouflaged Object Detection
   - 一句话总结：Advanced vision systems require retinomorphic, energy-efficient spike-based preprocessing of dynamic visual scenes. Here, we demonstrate multiple retinal preprocessing functionalities by leveraging a Hodgkin-H...
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：边界感知建模，适合改善伪装目标轮廓不清的问题。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；边界/频域增强模块。
   - 可改进点：可尝试引入基础模型、文本先验或更强的环境上下文建模。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

3. **Anatomy-Guided Residual Motion Diffusion for Controllable 4D Cardiac MRI Synthesis**
   - Source: arXiv, 2026-06-25
   - Authors: Yiheng Cao, Gustavo Andrade-Miranda, Jiatian Zhang, Lingxiao Zhao, Xin Gao
   - Tags: unsupervised, diffusion, boundary/frequency, depth/geometry, video
   - Links: [paper](http://arxiv.org/abs/2606.26764v1) / [pdf](http://arxiv.org/pdf/2606.26764v1)
   - 论文：Anatomy-Guided Residual Motion Diffusion for Controllable 4D Cardiac MRI Synthesis
   - 一句话总结：Developing robust artificial intelligence models for 4D (3D + time) medical imaging is constrained by limited annotated data, inter-device domain shifts, and privacy restrictions. To address this, we propose a...
   - 任务设定：视频/时序视觉任务，关注跨帧一致性、运动线索和长期上下文。
   - 方法核心：扩散/生成式建模，可能用于数据合成、先验建模或掩码优化。
   - 实验结论：可能包含新数据集/基准；适合看评测协议、失败案例和是否能服务 COD。
   - 和我课题的关系：可补充 COD 中纹理、边界、几何先验不足的问题。
   - 可借鉴点：边界/频域增强模块；深度或几何先验融合。
   - 可改进点：可结合多尺度语义上下文，避免只强化纹理导致误检。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

4. **Vision-Language Model Reasoning for Contextual Semantic Mapping in Intralogistics**
   - Source: arXiv, 2026-06-23
   - Authors: Marvin Rüdt, Hao Pang, Constantin Enke, Zäzilia Seibold, Kai Furmans
   - Tags: open-vocabulary, SAM, VLM/MLLM, reasoning, depth/geometry
   - Links: [paper](http://arxiv.org/abs/2606.24814v1) / [pdf](http://arxiv.org/pdf/2606.24814v1)
   - 论文：Vision-Language Model Reasoning for Contextual Semantic Mapping in Intralogistics
   - 一句话总结：Autonomous mobile robots operating in intralogistics environments rely on geometric maps for localization and navigation, but lack semantic understanding of objects and their contextual properties. We present...
   - 任务设定：开放词汇视觉识别/分割，目标类别或文本提示在训练时未必出现。
   - 方法核心：提示学习或提示生成，重点看文本/视觉 prompt 如何约束定位。
   - 实验结论：摘要强调消融、鲁棒性或泛化；适合优先看实验设计和跨域表现。
   - 和我课题的关系：适合拓展到开放词汇、零样本或少标注 COD。
   - 可借鉴点：prompt 设计、类别文本构造、免训练迁移流程；候选 mask 生成、视觉-语言筛选、推理式定位；深度或几何先验融合。
   - 可改进点：可改进 prompt 自动生成、负样本约束和 mask 置信度校准。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

5. **ARTEMIS: Agent-guided Reliability-aware Temporal Mask Evolution for Imperfectly Supervised Video Polyp Segmentation**
   - Source: arXiv, 2026-06-18
   - Authors: Tong Wang, Siwen Wang, Yaolei Qi, Jinxing Zhou, Yuting He et al.
   - Tags: SAM, VLM/MLLM, retrieval/prototype, boundary/frequency, depth/geometry, video
   - Links: [paper](http://arxiv.org/abs/2606.20161v1) / [pdf](http://arxiv.org/pdf/2606.20161v1)
   - 论文：ARTEMIS: Agent-guided Reliability-aware Temporal Mask Evolution for Imperfectly Supervised Video Polyp Segmentation
   - 一句话总结：Imperfectly supervised video polyp segmentation (VPS) aims to learn dense, temporally consistent masks from inexpensive supervision, including weak annotations (points, scribbles) and semi-supervision with few...
   - 任务设定：基础模型驱动的视觉定位/分割/推理，可用于自动提示生成或 mask 筛选。
   - 方法核心：借助 SAM/基础分割模型产生候选 mask，再做筛选或适配。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：可补充 COD 中纹理、边界、几何先验不足的问题。
   - 可借鉴点：候选 mask 生成、视觉-语言筛选、推理式定位；边界/频域增强模块；深度或几何先验融合。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

6. **ActiveSAM: Image-Conditional Class Pruning for Fast and Accurate Open-Vocabulary Segmentation**
   - Source: arXiv, 2026-06-15
   - Authors: Tran Dinh Tien, Zhiqiang Shen
   - Tags: open-vocabulary, training-free, SAM, diffusion, remote sensing
   - Links: [paper](http://arxiv.org/abs/2606.16996v1) / [pdf](http://arxiv.org/pdf/2606.16996v1)
   - 论文：ActiveSAM: Image-Conditional Class Pruning for Fast and Accurate Open-Vocabulary Segmentation
   - 一句话总结：Segment Anything Model 3 (SAM 3) provides a strong frozen backbone for concept-prompted segmentation, but applying it directly to open-vocabulary semantic segmentation (OVSS) is inefficient: full-resolution de...
   - 任务设定：开放词汇视觉识别/分割，目标类别或文本提示在训练时未必出现。
   - 方法核心：提示学习或提示生成，重点看文本/视觉 prompt 如何约束定位。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：适合拓展到开放词汇、零样本或少标注 COD。
   - 可借鉴点：prompt 设计、类别文本构造、免训练迁移流程；候选 mask 生成、视觉-语言筛选、推理式定位。
   - 可改进点：可改进 prompt 自动生成、负样本约束和 mask 置信度校准。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

7. **Jolia: Concept-Level Vision-Language Alignment for 3D CT Contrastive Learning**
   - Source: arXiv, 2026-06-23
   - Authors: Julien Khlaut, Charles Corbière, Baptiste Callard, Amaury Prat, Leo Butsanets et al.
   - Tags: VLM/MLLM, depth/geometry
   - Links: [paper](http://arxiv.org/abs/2606.24570v2) / [pdf](http://arxiv.org/pdf/2606.24570v2)
   - 论文：Jolia: Concept-Level Vision-Language Alignment for 3D CT Contrastive Learning
   - 一句话总结：Vision-language contrastive pretraining has become the dominant recipe for 3D medical foundation models, leveraging the large volumes of paired scans and reports produced in clinical practice. However, medical...
   - 任务设定：基础模型驱动的视觉定位/分割/推理，可用于自动提示生成或 mask 筛选。
   - 方法核心：视觉-语言对齐，把语义文本信息引入检测或分割。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：可补充 COD 中纹理、边界、几何先验不足的问题。
   - 可借鉴点：候选 mask 生成、视觉-语言筛选、推理式定位；深度或几何先验融合。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

8. **UniDrive: A Unified Vision-Language and Grounding Framework for Interpretable Risk Understanding in Autonomous Driving**
   - Source: arXiv, 2026-06-23
   - Authors: Xiaowei Gao, Pengxiang Li, Yitai Cheng, Ruihan Xu, James Haworth et al.
   - Tags: VLM/MLLM, reasoning, video
   - Links: [paper](http://arxiv.org/abs/2606.24759v1) / [pdf](http://arxiv.org/pdf/2606.24759v1)
   - 论文：UniDrive: A Unified Vision-Language and Grounding Framework for Interpretable Risk Understanding in Autonomous Driving
   - 一句话总结：Recent multimodal large language models (MLLMs) have shown strong potential for autonomous driving scene understanding, yet existing methods still face a fundamental trade-off between temporal reasoning and sp...
   - 任务设定：基础模型驱动的视觉定位/分割/推理，可用于自动提示生成或 mask 筛选。
   - 方法核心：视觉-语言对齐，把语义文本信息引入检测或分割。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：可用于伪装目标的语义描述、环境理解和候选区域判断。
   - 可借鉴点：候选 mask 生成、视觉-语言筛选、推理式定位。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

9. **HPP: Hierarchical Programmatic Probing for Long Video Understanding by Decoupling Perception and Reasoning**
   - Source: arXiv, 2026-06-19
   - Authors: Awais Rauf, Ahmed Hasssan, Greg Slabaugh
   - Tags: VLM/MLLM, reasoning, retrieval/prototype, video
   - Links: [paper](http://arxiv.org/abs/2606.21734v1) / [pdf](http://arxiv.org/pdf/2606.21734v1)
   - 论文：HPP: Hierarchical Programmatic Probing for Long Video Understanding by Decoupling Perception and Reasoning
   - 一句话总结：Understanding long videos requires fine-grained perception and multi-step, higher-order reasoning over complex, long-range spatio-temporal dynamics. Vision-language models (VLMs) encode video frames into visua...
   - 任务设定：基础模型驱动的视觉定位/分割/推理，可用于自动提示生成或 mask 筛选。
   - 方法核心：视觉-语言对齐，把语义文本信息引入检测或分割。
   - 实验结论：可能包含新数据集/基准；适合看评测协议、失败案例和是否能服务 COD。
   - 和我课题的关系：可用于伪装目标的语义描述、环境理解和候选区域判断。
   - 可借鉴点：候选 mask 生成、视觉-语言筛选、推理式定位。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

10. **EnTrust: Modeling Inter-Modal Conflict for Trustworthy Multimodal Medical Image Analysis**
   - Source: arXiv, 2026-06-19
   - Authors: Dwarikanath Mahapatra, Abhijit Das, Behzad Bozorgtabar, Zongyuan Ge, Sudipta Roy et al.
   - Tags: SAM, diffusion
   - Links: [paper](http://arxiv.org/abs/2606.21384v1) / [pdf](http://arxiv.org/pdf/2606.21384v1)
   - 论文：EnTrust: Modeling Inter-Modal Conflict for Trustworthy Multimodal Medical Image Analysis
   - 一句话总结：Multimodal medical imaging fuses complementary anatomical and functional information, yet modalities frequently disagree in pathologically heterogeneous regions. Current segmentation models handle this in one...
   - 任务设定：基础模型驱动的视觉定位/分割/推理，可用于自动提示生成或 mask 筛选。
   - 方法核心：扩散/生成式建模，可能用于数据合成、先验建模或掩码优化。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：不是 COD 直系论文，但可能提供可迁移的视觉表征、训练策略或评测思路。
   - 可借鉴点：候选 mask 生成、视觉-语言筛选、推理式定位。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

11. **Object Tokens as a Bridge Between Segmentation and Visual Question Answering in Robotic Surgery**
   - Source: arXiv, 2026-06-14
   - Authors: Yiping Li, Ronald de Jong, Romy van Jaarsveld, Franco Badaloni, Gino Kuiper et al.
   - Tags: SAM, VLM/MLLM, reasoning
   - Links: [paper](http://arxiv.org/abs/2606.15861v1) / [pdf](http://arxiv.org/pdf/2606.15861v1)
   - 论文：Object Tokens as a Bridge Between Segmentation and Visual Question Answering in Robotic Surgery
   - 一句话总结：Visual Question Answering (VQA) in robotic surgery, referred to as surgical VQA, requires high-level understanding of complex surgical scenes and the integration of visual perception with language reasoning, w...
   - 任务设定：基础模型驱动的视觉定位/分割/推理，可用于自动提示生成或 mask 筛选。
   - 方法核心：借助 SAM/基础分割模型产生候选 mask，再做筛选或适配。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：可用于伪装目标的语义描述、环境理解和候选区域判断。
   - 可借鉴点：候选 mask 生成、视觉-语言筛选、推理式定位。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

12. **ReasonCLIP-58M: Visually Grounded Commonsense Reasoning Supervision for CLIP**
   - Source: arXiv, 2026-06-25
   - Authors: Sicheng Zhang, Muzammal Naseer, Binzhu Xie, Naufal Suryanto, Shi Qiu et al.
   - Tags: VLM/MLLM, reasoning, diffusion, retrieval/prototype
   - Links: [paper](http://arxiv.org/abs/2606.26794v1) / [pdf](http://arxiv.org/pdf/2606.26794v1)
   - 论文：ReasonCLIP-58M: Visually Grounded Commonsense Reasoning Supervision for CLIP
   - 一句话总结：CLIP and its variants are widely adopted visual backbones in multimodal systems, but their pretraining remains dominated by descriptive image-text alignment. As downstream applications increasingly demand visu...
   - 任务设定：基础模型驱动的视觉定位/分割/推理，可用于自动提示生成或 mask 筛选。
   - 方法核心：视觉-语言对齐，把语义文本信息引入检测或分割。
   - 实验结论：可能包含新数据集/基准；适合看评测协议、失败案例和是否能服务 COD。
   - 和我课题的关系：可用于伪装目标的语义描述、环境理解和候选区域判断。
   - 可借鉴点：候选 mask 生成、视觉-语言筛选、推理式定位。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

### 当日高质量来源优先读

### 当日 COD / 伪装目标检测相关

1. **Open-Vocabulary Camouflaged Object Segmentation**
   - Source: arXiv, 2023-11-19
   - Authors: Youwei Pang, Xiaoqi Zhao, Jiaming Zuo, Lihe Zhang, Huchuan Lu
   - Tags: COD, open-vocabulary, VLM/MLLM, boundary/frequency, depth/geometry, low-level
   - Links: [paper](http://arxiv.org/abs/2311.11241v3) / [pdf](http://arxiv.org/pdf/2311.11241v3)
   - 论文：Open-Vocabulary Camouflaged Object Segmentation
   - 一句话总结：Recently, the emergence of the large-scale vision-language model (VLM), such as CLIP, has opened the way towards open-world object perception. Many works have explored the utilization of pre-trained VLM for th...
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：视觉-语言对齐，把语义文本信息引入检测或分割。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；prompt 设计、类别文本构造、免训练迁移流程；候选 mask 生成、视觉-语言筛选、推理式定位；边界/频域增强模块；深度或几何先验融合。
   - 可改进点：可改进 prompt 自动生成、负样本约束和 mask 置信度校准。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

2. **Debate-Enhanced Pseudo Labeling and Frequency-Aware Progressive Debiasing for Weakly-Supervised Camouflaged Object Detection with Scribble Annotations**
   - Source: arXiv, 2025-12-23
   - Authors: Jiawei Ge, Jiuxin Cao, Xinyi Li, Xuelin Zhu, Chang Liu et al.
   - Tags: COD, unsupervised, SAM, boundary/frequency
   - Links: [paper](http://arxiv.org/abs/2512.20260v5) / [pdf](http://arxiv.org/pdf/2512.20260v5)
   - 论文：Debate-Enhanced Pseudo Labeling and Frequency-Aware Progressive Debiasing for Weakly-Supervised Camouflaged Object Detection with Scribble Annotations
   - 一句话总结：Weakly-Supervised Camouflaged Object Detection (WSCOD) aims to locate and segment objects that are visually concealed within their surrounding scenes, relying solely on sparse supervision such as scribble anno...
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：借助 SAM/基础分割模型产生候选 mask，再做筛选或适配。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；候选 mask 生成、视觉-语言筛选、推理式定位；边界/频域增强模块。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

3. **UCOD-DPL: Unsupervised Camouflaged Object Detection via Dynamic Pseudo-label Learning**
   - Source: arXiv, 2025-06-08
   - Authors: Weiqi Yan, Lvhai Chen, Huaijia Kou, Shengchuan Zhang, Yan Zhang et al.
   - Tags: COD, unsupervised, boundary/frequency, remote sensing
   - Links: [paper](http://arxiv.org/abs/2506.07087v1) / [pdf](http://arxiv.org/pdf/2506.07087v1)
   - 论文：UCOD-DPL: Unsupervised Camouflaged Object Detection via Dynamic Pseudo-label Learning
   - 一句话总结：Unsupervised Camoflaged Object Detection (UCOD) has gained attention since it doesn't need to rely on extensive pixel-level labels. Existing UCOD methods typically generate pseudo-labels using fixed strategies...
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：边界感知建模，适合改善伪装目标轮廓不清的问题。
   - 实验结论：摘要未给出强实验信号；先看实验表格和图 1，再决定是否精读。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；边界/频域增强模块。
   - 可改进点：可尝试引入基础模型、文本先验或更强的环境上下文建模。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

4. **EReCu: Pseudo-label Evolution Fusion and Refinement with Multi-Cue Learning for Unsupervised Camouflage Detection**
   - Source: arXiv, 2026-03-12
   - Authors: Shuo Jiang, Gaojia Zhang, Min Tan, Yufei Yin, Gang Pan
   - Tags: COD, unsupervised, diffusion, boundary/frequency, depth/geometry, low-level
   - Links: [paper](http://arxiv.org/abs/2603.11521v1) / [pdf](http://arxiv.org/pdf/2603.11521v1)
   - 论文：EReCu: Pseudo-label Evolution Fusion and Refinement with Multi-Cue Learning for Unsupervised Camouflage Detection
   - 一句话总结：Unsupervised Camouflaged Object Detection (UCOD) remains a challenging task due to the high intrinsic similarity between target objects and their surroundings, as well as the reliance on noisy pseudo-labels th...
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：边界感知建模，适合改善伪装目标轮廓不清的问题。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；边界/频域增强模块；深度或几何先验融合。
   - 可改进点：可尝试引入基础模型、文本先验或更强的环境上下文建模。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

5. **SAM3-Adapter: Efficient Adaptation of Segment Anything 3 for Camouflage Object Segmentation, Shadow Detection, and Medical Image Segmentation**
   - Source: arXiv, 2025-11-24
   - Authors: Tianrun Chen, Runlong Cao, Xinda Yu, Lanyun Zhu, Chaotao Ding et al.
   - Tags: COD, SAM
   - Links: [paper](http://arxiv.org/abs/2511.19425v1) / [pdf](http://arxiv.org/pdf/2511.19425v1)
   - 论文：SAM3-Adapter: Efficient Adaptation of Segment Anything 3 for Camouflage Object Segmentation, Shadow Detection, and Medical Image Segmentation
   - 一句话总结：The rapid rise of large-scale foundation models has reshaped the landscape of image segmentation, with models such as Segment Anything achieving unprecedented versatility across diverse vision tasks. However,...
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：借助 SAM/基础分割模型产生候选 mask，再做筛选或适配。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；候选 mask 生成、视觉-语言筛选、推理式定位。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

6. **High-Resolution Underwater Camouflaged Object Detection: GBU-UCOD Dataset and Topology-Aware and Frequency-Decoupled Networks**
   - Source: arXiv, 2026-02-03
   - Authors: Wenji Wu, Shuo Ye, Yiyu Liu, Jiguang He, Zhuo Wang et al.
   - Tags: COD, SAM, diffusion, boundary/frequency, depth/geometry
   - Links: [paper](http://arxiv.org/abs/2602.03591v1) / [pdf](http://arxiv.org/pdf/2602.03591v1)
   - 论文：High-Resolution Underwater Camouflaged Object Detection: GBU-UCOD Dataset and Topology-Aware and Frequency-Decoupled Networks
   - 一句话总结：Underwater Camouflaged Object Detection (UCOD) is a challenging task due to the extreme visual similarity between targets and backgrounds across varying marine depths. Existing methods often struggle with topo...
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：借助 SAM/基础分割模型产生候选 mask，再做筛选或适配。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；候选 mask 生成、视觉-语言筛选、推理式定位；边界/频域增强模块；深度或几何先验融合。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

7. **ZS-VCOS: Zero-Shot Video Camouflaged Object Segmentation By Optical Flow and Open Vocabulary Object Detection**
   - Source: arXiv, 2025-04-10
   - Authors: Wenqi Guo, Mohamed Shehata, Shan Du
   - Tags: COD, open-vocabulary, unsupervised, SAM, VLM/MLLM, diffusion, video
   - Links: [paper](http://arxiv.org/abs/2505.01431v2) / [pdf](http://arxiv.org/pdf/2505.01431v2)
   - 论文：ZS-VCOS: Zero-Shot Video Camouflaged Object Segmentation By Optical Flow and Open Vocabulary Object Detection
   - 一句话总结：Camouflaged object segmentation presents unique challenges compared to traditional segmentation tasks, primarily due to the high similarity in patterns and colors between camouflaged objects and their backgrou...
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：借助 SAM/基础分割模型产生候选 mask，再做筛选或适配。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；prompt 设计、类别文本构造、免训练迁移流程；候选 mask 生成、视觉-语言筛选、推理式定位。
   - 可改进点：可改进 prompt 自动生成、负样本约束和 mask 置信度校准。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

8. **First RAG, Second SEG: A Training-Free Paradigm for Camouflaged Object Detection**
   - Source: arXiv, 2025-08-21
   - Authors: Wutao Liu, YiDan Wang, Pan Gao
   - Tags: COD, training-free, unsupervised, SAM, retrieval/prototype, anomaly/OOD
   - Links: [paper](http://arxiv.org/abs/2508.15313v2) / [pdf](http://arxiv.org/pdf/2508.15313v2)
   - 论文：First RAG, Second SEG: A Training-Free Paradigm for Camouflaged Object Detection
   - 一句话总结：Camouflaged object detection (COD) poses a significant challenge in computer vision due to the high similarity between objects and their backgrounds. Existing approaches often rely on heavy training and large...
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：提示学习或提示生成，重点看文本/视觉 prompt 如何约束定位。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；prompt 设计、类别文本构造、免训练迁移流程；候选 mask 生成、视觉-语言筛选、推理式定位；跨域鲁棒性、不确定性或异常分数。
   - 可改进点：可改进 prompt 自动生成、负样本约束和 mask 置信度校准。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

9. **When SAM2 Meets Video Camouflaged Object Segmentation: A Comprehensive Evaluation and Adaptation**
   - Source: arXiv, 2024-09-27
   - Authors: Yuli Zhou, Guolei Sun, Yawei Li, Guo-Sen Xie, Luca Benini et al.
   - Tags: COD, SAM, VLM/MLLM, diffusion, video
   - Links: [paper](http://arxiv.org/abs/2409.18653v2) / [pdf](http://arxiv.org/pdf/2409.18653v2)
   - 论文：When SAM2 Meets Video Camouflaged Object Segmentation: A Comprehensive Evaluation and Adaptation
   - 一句话总结：This study investigates the application and performance of the Segment Anything Model 2 (SAM2) in the challenging task of video camouflaged object segmentation (VCOS). VCOS involves detecting objects that blen...
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：提示学习或提示生成，重点看文本/视觉 prompt 如何约束定位。
   - 实验结论：可能包含新数据集/基准；适合看评测协议、失败案例和是否能服务 COD。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；候选 mask 生成、视觉-语言筛选、推理式定位。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

10. **COMPrompter: reconceptualized segment anything model with multiprompt network for camouflaged object detection**
   - Source: arXiv, 2024-11-28
   - Authors: Xiaoqin Zhang, Zhenni Yu, Li Zhao, Deng-Ping Fan, Guobao Xiao
   - Tags: COD, SAM, boundary/frequency
   - Links: [paper](http://arxiv.org/abs/2411.18858v1) / [pdf](http://arxiv.org/pdf/2411.18858v1)
   - 论文：COMPrompter: reconceptualized segment anything model with multiprompt network for camouflaged object detection
   - 一句话总结：We rethink the segment anything model (SAM) and propose a novel multiprompt network called COMPrompter for camouflaged object detection (COD). SAM has zero-shot generalization ability beyond other models and c...
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：提示学习或提示生成，重点看文本/视觉 prompt 如何约束定位。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；候选 mask 生成、视觉-语言筛选、推理式定位；边界/频域增强模块。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

11. **Exploring Deeper! Segment Anything Model with Depth Perception for Camouflaged Object Detection**
   - Source: arXiv, 2024-07-17
   - Authors: Zhenni Yu, Xiaoqin Zhang, Li Zhao, Yi Bin, Guobao Xiao
   - Tags: COD, SAM, boundary/frequency, depth/geometry
   - Links: [paper](http://arxiv.org/abs/2407.12339v1) / [pdf](http://arxiv.org/pdf/2407.12339v1)
   - 论文：Exploring Deeper! Segment Anything Model with Depth Perception for Camouflaged Object Detection
   - 一句话总结：This paper introduces a new Segment Anything Model with Depth Perception (DSAM) for Camouflaged Object Detection (COD). DSAM exploits the zero-shot capability of SAM to realize precise segmentation in the RGB-...
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：提示学习或提示生成，重点看文本/视觉 prompt 如何约束定位。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；候选 mask 生成、视觉-语言筛选、推理式定位；边界/频域增强模块；深度或几何先验融合。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

12. **BED-SAM2: Boundary-Enhanced-Depth SAM2 via Monocular Geometric Priors**
   - Source: arXiv, 2026-05-24
   - Authors: Tyler Rust, Dara McNally, Kyle O'Donnell, Colin Kelly, Chandra Kambhamettu
   - Tags: COD, SAM, boundary/frequency, depth/geometry
   - Links: [paper](http://arxiv.org/abs/2605.24893v1) / [pdf](http://arxiv.org/pdf/2605.24893v1)
   - 论文：BED-SAM2: Boundary-Enhanced-Depth SAM2 via Monocular Geometric Priors
   - 一句话总结：Building upon the SAM2 vision foundation model for downstream segmentation, this study introduces Boundary Enhanced Depth (BED)-SAM2. The SAM2 Hiera encoder architecture is modified to directly encode monocula...
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：借助 SAM/基础分割模型产生候选 mask，再做筛选或适配。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；候选 mask 生成、视觉-语言筛选、推理式定位；边界/频域增强模块；深度或几何先验融合。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

13. **FCL-COD: Weakly Supervised Camouflaged Object Detection with Frequency-aware and Contrastive Learning**
   - Source: arXiv, 2026-03-24
   - Authors: Jingchen Ni, Quan Zhang, Dan Jiang, Keyu Lv, Ke Zhang et al.
   - Tags: COD, unsupervised, SAM, diffusion, boundary/frequency
   - Links: [paper](http://arxiv.org/abs/2603.22969v1) / [pdf](http://arxiv.org/pdf/2603.22969v1)
   - 论文：FCL-COD: Weakly Supervised Camouflaged Object Detection with Frequency-aware and Contrastive Learning
   - 一句话总结：Existing camouflage object detection (COD) methods typically rely on fully-supervised learning guided by mask annotations. However, obtaining mask annotations is time-consuming and labor-intensive.
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：借助 SAM/基础分割模型产生候选 mask，再做筛选或适配。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；候选 mask 生成、视觉-语言筛选、推理式定位；边界/频域增强模块。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

14. **Stepwise Decomposition and Dual-stream Focus: A Novel Approach for Training-free Camouflaged Object Segmentation**
   - Source: arXiv, 2025-06-07
   - Authors: Chao Yin, Hao Li, Kequan Yang, Jide Li, Pinpin Zhu et al.
   - Tags: COD, training-free, SAM, reasoning
   - Links: [paper](http://arxiv.org/abs/2506.06818v3) / [pdf](http://arxiv.org/pdf/2506.06818v3)
   - 论文：Stepwise Decomposition and Dual-stream Focus: A Novel Approach for Training-free Camouflaged Object Segmentation
   - 一句话总结：While promptable segmentation (\textit{e.g.}, SAM) has shown promise for various segmentation tasks, it still requires manual visual prompts for each object to be segmented. In contrast, task-generic promptabl...
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：提示学习或提示生成，重点看文本/视觉 prompt 如何约束定位。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；prompt 设计、类别文本构造、免训练迁移流程；候选 mask 生成、视觉-语言筛选、推理式定位。
   - 可改进点：可改进 prompt 自动生成、负样本约束和 mask 置信度校准。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

15. **CamSAM2: Segment Anything Accurately in Camouflaged Videos**
   - Source: arXiv, 2025-03-25
   - Authors: Yuli Zhou, Yawei Li, Yuqian Fu, Luca Benini, Ender Konukoglu et al.
   - Tags: COD, SAM, retrieval/prototype, video
   - Links: [paper](http://arxiv.org/abs/2503.19730v3) / [pdf](http://arxiv.org/pdf/2503.19730v3)
   - 论文：CamSAM2: Segment Anything Accurately in Camouflaged Videos
   - 一句话总结：Video camouflaged object segmentation (VCOS), aiming at segmenting camouflaged objects that seamlessly blend into their environment, is a fundamental vision task with various real-world applications. With the...
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：提示学习或提示生成，重点看文本/视觉 prompt 如何约束定位。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；候选 mask 生成、视觉-语言筛选、推理式定位。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

16. **SAM2-UNeXT: An Improved High-Resolution Baseline for Adapting Foundation Models to Downstream Segmentation Tasks**
   - Source: arXiv, 2025-08-05
   - Authors: Xinyu Xiong, Zihuang Wu, Lei Zhang, Lei Lu, Ming Li et al.
   - Tags: COD, SAM, remote sensing
   - Links: [paper](http://arxiv.org/abs/2508.03566v1) / [pdf](http://arxiv.org/pdf/2508.03566v1)
   - 论文：SAM2-UNeXT: An Improved High-Resolution Baseline for Adapting Foundation Models to Downstream Segmentation Tasks
   - 一句话总结：Recent studies have highlighted the potential of adapting the Segment Anything Model (SAM) for various downstream tasks. However, constructing a more powerful and generalizable encoder to further enhance perfo...
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：借助 SAM/基础分割模型产生候选 mask，再做筛选或适配。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；候选 mask 生成、视觉-语言筛选、推理式定位。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

17. **Depth-guided Texture Diffusion for Image Semantic Segmentation**
   - Source: arXiv, 2024-08-17
   - Authors: Wei Sun, Yuan Li, Qixiang Ye, Jianbin Jiao, Yanzhao Zhou
   - Tags: COD, diffusion, boundary/frequency, depth/geometry
   - Links: [paper](http://arxiv.org/abs/2408.09097v1) / [pdf](http://arxiv.org/pdf/2408.09097v1)
   - 论文：Depth-guided Texture Diffusion for Image Semantic Segmentation
   - 一句话总结：Depth information provides valuable insights into the 3D structure especially the outline of objects, which can be utilized to improve the semantic segmentation tasks. However, a naive fusion of depth informat...
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：扩散/生成式建模，可能用于数据合成、先验建模或掩码优化。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；边界/频域增强模块；深度或几何先验融合。
   - 可改进点：可尝试引入基础模型、文本先验或更强的环境上下文建模。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

18. **Weakly Supervised Camouflaged Object Detection Based on the SAM Model and Mask Guidance**
   - Source: arXiv, 2026-05-25
   - Authors: Xia Li, Xinran Liu, Lin Qi, Junyu Dong
   - Tags: COD, unsupervised, SAM, boundary/frequency, low-level
   - Links: [paper](http://arxiv.org/abs/2605.25385v1) / [pdf](http://arxiv.org/pdf/2605.25385v1)
   - 论文：Weakly Supervised Camouflaged Object Detection Based on the SAM Model and Mask Guidance
   - 一句话总结：Camouflaged object detection (COD) from a single image is a challenging task due to the high similarity between objects and their surroundings. Existing fully supervised methods require labor-intensive pixel-l...
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：提示学习或提示生成，重点看文本/视觉 prompt 如何约束定位。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；候选 mask 生成、视觉-语言筛选、推理式定位；边界/频域增强模块。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

19. **RIDE: Retinex-Informed Decoupling for Exposing Concealed Objects**
   - Source: arXiv, 2026-05-14
   - Authors: Chunming He, Rihan Zhang, Dingming Zhang, Chengyu Fang, Longxiang Tang et al.
   - Tags: COD, SAM, boundary/frequency
   - Links: [paper](http://arxiv.org/abs/2605.15450v1) / [pdf](http://arxiv.org/pdf/2605.15450v1)
   - 论文：RIDE: Retinex-Informed Decoupling for Exposing Concealed Objects
   - 一句话总结：Concealed Object Segmentation (COS) encompasses a family of dense-prediction tasks, including camouflaged object detection, polyp segmentation, transparent object detection, and industrial defect inspection, w...
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：借助 SAM/基础分割模型产生候选 mask，再做筛选或适配。
   - 实验结论：摘要未给出强实验信号；先看实验表格和图 1，再决定是否精读。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；候选 mask 生成、视觉-语言筛选、推理式定位；边界/频域增强模块。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

20. **Exploring Boundary-Aware Spatial-Frequency Fusion for Camouflaged Object Detection**
   - Source: arXiv, 2026-04-20
   - Authors: Song Yu, Yang Hu, Haokang Ding, Zhifang Liao, Yucheng Song
   - Tags: COD, diffusion, boundary/frequency
   - Links: [paper](http://arxiv.org/abs/2604.17879v1) / [pdf](http://arxiv.org/pdf/2604.17879v1)
   - 论文：Exploring Boundary-Aware Spatial-Frequency Fusion for Camouflaged Object Detection
   - 一句话总结：Camouflaged Object Detection is challenging due to the high degree of similarity between camouflaged objects and their surrounding backgrounds. Current COD methods mainly rely on edge extraction in the spatial...
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：频域/纹理特征增强，适合处理伪装背景与目标细粒度差异。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；边界/频域增强模块。
   - 可改进点：可尝试引入基础模型、文本先验或更强的环境上下文建模。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

21. **IP-SAM: Prompt-Space Conditioning for Prompt-Absent Camouflaged Object Detection**
   - Source: arXiv, 2026-03-28
   - Authors: Huiyao Zhang, Jin Bai, Rui Guo, JianWen Tan, HongFei Wang et al.
   - Tags: COD, SAM, diffusion
   - Links: [paper](http://arxiv.org/abs/2603.27250v1) / [pdf](http://arxiv.org/pdf/2603.27250v1)
   - 论文：IP-SAM: Prompt-Space Conditioning for Prompt-Absent Camouflaged Object Detection
   - 一句话总结：Prompt-conditioned foundation segmenters have emerged as a dominant paradigm for image segmentation, where explicit spatial prompts (e.g., points, boxes, masks) guide mask decoding. However, many real-world de...
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：提示学习或提示生成，重点看文本/视觉 prompt 如何约束定位。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；候选 mask 生成、视觉-语言筛选、推理式定位。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

22. **Language-Guided Structure-Aware Network for Camouflaged Object Detection**
   - Source: arXiv, 2026-03-25
   - Authors: Min Zhang
   - Tags: COD, boundary/frequency, low-level
   - Links: [paper](http://arxiv.org/abs/2603.24355v1) / [pdf](http://arxiv.org/pdf/2603.24355v1)
   - 论文：Language-Guided Structure-Aware Network for Camouflaged Object Detection
   - 一句话总结：Camouflaged Object Detection (COD) aims to segment objects that are highly integrated with the background in terms of color, texture, and structure, making it a highly challenging task in computer vision. Alth...
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：提示学习或提示生成，重点看文本/视觉 prompt 如何约束定位。
   - 实验结论：可能包含新数据集/基准；适合看评测协议、失败案例和是否能服务 COD。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；边界/频域增强模块。
   - 可改进点：可尝试引入基础模型、文本先验或更强的环境上下文建模。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

23. **An Instance-Aware Prompting Framework for Training-free Camouflaged Object Segmentation**
   - Source: arXiv, 2025-08-09
   - Authors: Chao Yin, Jide Li, Hang Yao, Xiaoqiang Li
   - Tags: COD, training-free, SAM
   - Links: [paper](http://arxiv.org/abs/2508.06904v3) / [pdf](http://arxiv.org/pdf/2508.06904v3)
   - 论文：An Instance-Aware Prompting Framework for Training-free Camouflaged Object Segmentation
   - 一句话总结：Training-free Camouflaged Object Segmentation (COS) seeks to segment camouflaged objects without task-specific training, by automatically generating visual prompts to guide the Segment Anything Model (SAM). Ho...
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：提示学习或提示生成，重点看文本/视觉 prompt 如何约束定位。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；prompt 设计、类别文本构造、免训练迁移流程；候选 mask 生成、视觉-语言筛选、推理式定位。
   - 可改进点：可改进 prompt 自动生成、负样本约束和 mask 置信度校准。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

24. **Open-Vocabulary Camouflaged Object Segmentation with Cascaded Vision Language Models**
   - Source: arXiv, 2025-06-24
   - Authors: Kai Zhao, Wubang Yuan, Zheng Wang, Guanyi Li, Xiaoqiang Zhu et al.
   - Tags: COD, open-vocabulary, SAM
   - Links: [paper](http://arxiv.org/abs/2506.19300v2) / [pdf](http://arxiv.org/pdf/2506.19300v2)
   - 论文：Open-Vocabulary Camouflaged Object Segmentation with Cascaded Vision Language Models
   - 一句话总结：Open-Vocabulary Camouflaged Object Segmentation (OVCOS) seeks to segment and classify camouflaged objects from arbitrary categories, presenting unique challenges due to visual ambiguity and unseen categories.R...
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：提示学习或提示生成，重点看文本/视觉 prompt 如何约束定位。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；prompt 设计、类别文本构造、免训练迁移流程；候选 mask 生成、视觉-语言筛选、推理式定位。
   - 可改进点：可改进 prompt 自动生成、负样本约束和 mask 置信度校准。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

25. **Towards Real Zero-Shot Camouflaged Object Segmentation without Camouflaged Annotations**
   - Source: arXiv, 2024-10-22
   - Authors: Cheng Lei, Jie Fan, Xinran Li, Tianzhu Xiang, Ao Li et al.
   - Tags: COD, VLM/MLLM, diffusion
   - Links: [paper](http://arxiv.org/abs/2410.16953v2) / [pdf](http://arxiv.org/pdf/2410.16953v2)
   - 论文：Towards Real Zero-Shot Camouflaged Object Segmentation without Camouflaged Annotations
   - 一句话总结：Camouflaged Object Segmentation (COS) faces significant challenges due to the scarcity of annotated data, where meticulous pixel-level annotation is both labor-intensive and costly, primarily due to the intric...
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：视觉-语言对齐，把语义文本信息引入检测或分割。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；候选 mask 生成、视觉-语言筛选、推理式定位。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

26. **Beyond Single Images: Retrieval Self-Augmented Unsupervised Camouflaged Object Detection**
   - Source: arXiv, 2025-10-21
   - Authors: Ji Du, Xin Wang, Fangwei Hao, Mingyang Yu, Chunyuan Chen et al.
   - Tags: COD, unsupervised, retrieval/prototype
   - Links: [paper](http://arxiv.org/abs/2510.18437v1) / [pdf](http://arxiv.org/pdf/2510.18437v1)
   - 论文：Beyond Single Images: Retrieval Self-Augmented Unsupervised Camouflaged Object Detection
   - 一句话总结：At the core of Camouflaged Object Detection (COD) lies segmenting objects from their highly similar surroundings. Previous efforts navigate this challenge primarily through image-level modeling or annotation-b...
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：提示学习或提示生成，重点看文本/视觉 prompt 如何约束定位。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析。
   - 可改进点：可尝试引入基础模型、文本先验或更强的环境上下文建模。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

27. **DGA-Net: Enhancing SAM with Depth Prompting and Graph-Anchor Guidance for Camouflaged Object Detection**
   - Source: arXiv, 2026-01-06
   - Authors: Yuetong Li, Qing Zhang, Yilin Zhao, Gongyang Li, Zeming Liu
   - Tags: COD, SAM, depth/geometry, low-level
   - Links: [paper](http://arxiv.org/abs/2601.02831v1) / [pdf](http://arxiv.org/pdf/2601.02831v1)
   - 论文：DGA-Net: Enhancing SAM with Depth Prompting and Graph-Anchor Guidance for Camouflaged Object Detection
   - 一句话总结：To fully exploit depth cues in Camouflaged Object Detection (COD), we present DGA-Net, a specialized framework that adapts the Segment Anything Model (SAM) via a novel ``depth prompting" paradigm. Distinguishe...
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：提示学习或提示生成，重点看文本/视觉 prompt 如何约束定位。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；候选 mask 生成、视觉-语言筛选、推理式定位；深度或几何先验融合。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

28. **Phantom-Insight: Adaptive Multi-cue Fusion for Video Camouflaged Object Detection with Multimodal LLM**
   - Source: arXiv, 2025-09-08
   - Authors: Hua Zhang, Changjiang Luo, Ruoyu Chen
   - Tags: COD, SAM, VLM/MLLM, diffusion, boundary/frequency, video
   - Links: [paper](http://arxiv.org/abs/2509.06422v1) / [pdf](http://arxiv.org/pdf/2509.06422v1)
   - 论文：Phantom-Insight: Adaptive Multi-cue Fusion for Video Camouflaged Object Detection with Multimodal LLM
   - 一句话总结：Video camouflaged object detection (VCOD) is challenging due to dynamic environments. Existing methods face two main issues: (1) SAM-based methods struggle to separate camouflaged object edges due to model fre...
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：提示学习或提示生成，重点看文本/视觉 prompt 如何约束定位。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；候选 mask 生成、视觉-语言筛选、推理式定位；边界/频域增强模块。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

29. **Improving SAM for Camouflaged Object Detection via Dual Stream Adapters**
   - Source: arXiv, 2025-03-08
   - Authors: Jiaming Liu, Linghe Kong, Guihai Chen
   - Tags: COD, SAM, diffusion, boundary/frequency, depth/geometry
   - Links: [paper](http://arxiv.org/abs/2503.06042v2) / [pdf](http://arxiv.org/pdf/2503.06042v2)
   - 论文：Improving SAM for Camouflaged Object Detection via Dual Stream Adapters
   - 一句话总结：Segment anything model (SAM) has shown impressive general-purpose segmentation performance on natural images, but its performance on camouflaged object detection (COD) is unsatisfactory. In this paper, we prop...
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：提示学习或提示生成，重点看文本/视觉 prompt 如何约束定位。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；候选 mask 生成、视觉-语言筛选、推理式定位；边界/频域增强模块；深度或几何先验融合。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

30. **Refining Context-Entangled Content Segmentation via Curriculum Selection and Anti-Curriculum Promotion**
   - Source: arXiv, 2026-02-01
   - Authors: Chunming He, Rihan Zhang, Fengyang Xiao, Dingming Zhang, Zhiwen Cao et al.
   - Tags: COD, SAM, boundary/frequency, video, low-level
   - Links: [paper](http://arxiv.org/abs/2602.01183v2) / [pdf](http://arxiv.org/pdf/2602.01183v2)
   - 论文：Refining Context-Entangled Content Segmentation via Curriculum Selection and Anti-Curriculum Promotion
   - 一句话总结：Biological learning proceeds from easy to difficult tasks, gradually reinforcing perception and robustness. Inspired by this principle, we address Context-Entangled Content Segmentation (CECS), a challenging s...
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：借助 SAM/基础分割模型产生候选 mask，再做筛选或适配。
   - 实验结论：可能包含新数据集/基准；适合看评测协议、失败案例和是否能服务 COD。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；候选 mask 生成、视觉-语言筛选、推理式定位；边界/频域增强模块。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

31. **Assisted Refinement Network Based on Channel Information Interaction for Camouflaged and Salient Object Detection**
   - Source: arXiv, 2025-12-12
   - Authors: Kuan Wang, Yanjun Qin, Mengge Lu, Liejun Wang, Xiaoming Tao
   - Tags: COD, SAM, diffusion, boundary/frequency, low-level
   - Links: [paper](http://arxiv.org/abs/2512.11369v1) / [pdf](http://arxiv.org/pdf/2512.11369v1)
   - 论文：Assisted Refinement Network Based on Channel Information Interaction for Camouflaged and Salient Object Detection
   - 一句话总结：Camouflaged Object Detection (COD) stands as a significant challenge in computer vision, dedicated to identifying and segmenting objects visually highly integrated with their backgrounds. Current mainstream me...
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：借助 SAM/基础分割模型产生候选 mask，再做筛选或适配。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；候选 mask 生成、视觉-语言筛选、推理式定位；边界/频域增强模块。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

32. **Exploring Depth Contribution for Camouflaged Object Detection**
   - Source: arXiv, 2021-06-24
   - Authors: Mochu Xiang, Jing Zhang, Yunqiu Lv, Aixuan Li, Yiran Zhong et al.
   - Tags: COD, diffusion, depth/geometry, remote sensing
   - Links: [paper](http://arxiv.org/abs/2106.13217v3) / [pdf](http://arxiv.org/pdf/2106.13217v3)
   - 论文：Exploring Depth Contribution for Camouflaged Object Detection
   - 一句话总结：Camouflaged object detection (COD) aims to segment camouflaged objects hiding in the environment, which is challenging due to the similar appearance of camouflaged objects and their surroundings. Research in b...
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：扩散/生成式建模，可能用于数据合成、先验建模或掩码优化。
   - 实验结论：可能包含新数据集/基准；适合看评测协议、失败案例和是否能服务 COD。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；深度或几何先验融合。
   - 可改进点：可尝试引入基础模型、文本先验或更强的环境上下文建模。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

33. **Hierarchical Consistency Learning for Test-time Adaptation in Camouflage Perception**
   - Source: arXiv, 2026-05-25
   - Authors: Mingfeng Zha, Tianyu Li, Guoqing Wang, Yunqiang Pei, Chaofan Qiao et al.
   - Tags: COD, diffusion, retrieval/prototype, boundary/frequency
   - Links: [paper](http://arxiv.org/abs/2605.25651v2) / [pdf](http://arxiv.org/pdf/2605.25651v2)
   - 论文：Hierarchical Consistency Learning for Test-time Adaptation in Camouflage Perception
   - 一句话总结：Camouflaged object detection (COD) aims to localize targets that exhibit minimal perceptual differences from backgrounds through physical attributes. Existing methods, constrained by the static train-then-free...
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：频域/纹理特征增强，适合处理伪装背景与目标细粒度差异。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；边界/频域增强模块。
   - 可改进点：可尝试引入基础模型、文本先验或更强的环境上下文建模。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

34. **When W4A4 Breaks Camouflaged Object Detection: Token-Group Dual-Constraint Activation Quantization**
   - Source: arXiv, 2026-04-18
   - Authors: Tianqi Li, Wenyu Fang, Xin He, Xue Geng, Xu Cheng et al.
   - Tags: COD, boundary/frequency
   - Links: [paper](http://arxiv.org/abs/2604.16855v1) / [pdf](http://arxiv.org/pdf/2604.16855v1)
   - 论文：When W4A4 Breaks Camouflaged Object Detection: Token-Group Dual-Constraint Activation Quantization
   - 一句话总结：Camouflaged object detection (COD) segments objects that intentionally blend with the background, so predictions depend on subtle texture and boundary cues. COD is often needed under tight on-device memory and...
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：视觉-语言对齐，把语义文本信息引入检测或分割。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；边界/频域增强模块。
   - 可改进点：可尝试引入基础模型、文本先验或更强的环境上下文建模。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

35. **Modality-Agnostic Prompt Learning for Multi-Modal Camouflaged Object Detection**
   - Source: arXiv, 2026-04-14
   - Authors: Hao Wang, Jiqing Zhang, Xin Yang, Baocai Yin, Lu Jiang et al.
   - Tags: COD, SAM, diffusion, boundary/frequency, depth/geometry
   - Links: [paper](http://arxiv.org/abs/2604.12380v1) / [pdf](http://arxiv.org/pdf/2604.12380v1)
   - 论文：Modality-Agnostic Prompt Learning for Multi-Modal Camouflaged Object Detection
   - 一句话总结：Camouflaged Object Detection (COD) aims to segment objects that blend seamlessly into complex backgrounds, with growing interest in exploiting additional visual modalities to enhance robustness through complem...
   - 任务设定：伪装/隐蔽目标检测或分割，重点是低显著、边界模糊、目标与背景相似。
   - 方法核心：提示学习或提示生成，重点看文本/视觉 prompt 如何约束定位。
   - 实验结论：可能包含新数据集/基准；适合看评测协议、失败案例和是否能服务 COD。
   - 和我课题的关系：和伪装目标检测高度相关，可直接作为方法、实验或 baseline 参考。
   - 可借鉴点：数据集设置、评价指标、失败案例分析；候选 mask 生成、视觉-语言筛选、推理式定位；边界/频域增强模块；深度或几何先验融合。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：值得精读：和课题高度相关，优先看摘要、方法图、消融和失败案例。

### 当日泛计算机视觉方法池

1. **SegRAG: Training-Free Retrieval-Augmented Semantic Segmentation**
   - Source: arXiv, 2026-05-17
   - Authors: Abderrahmene Boudiaf, Irfan Hussain, Sajid Javed
   - Tags: open-vocabulary, training-free, SAM, reasoning, retrieval/prototype
   - Links: [paper](http://arxiv.org/abs/2605.17630v2) / [pdf](http://arxiv.org/pdf/2605.17630v2)
   - 论文：SegRAG: Training-Free Retrieval-Augmented Semantic Segmentation
   - 一句话总结：Open-vocabulary segmentation models such as SAM3 perform well across broad categories via text prompting, yet degrade when target classes are visually underrepresented in pretraining or depart from canonical d...
   - 任务设定：开放词汇视觉识别/分割，目标类别或文本提示在训练时未必出现。
   - 方法核心：提示学习或提示生成，重点看文本/视觉 prompt 如何约束定位。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：适合拓展到开放词汇、零样本或少标注 COD。
   - 可借鉴点：prompt 设计、类别文本构造、免训练迁移流程；候选 mask 生成、视觉-语言筛选、推理式定位。
   - 可改进点：可改进 prompt 自动生成、负样本约束和 mask 置信度校准。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

2. **OVS-DINO: Open-Vocabulary Segmentation via Structure-Aligned SAM-DINO with Language Guidance**
   - Source: arXiv, 2026-04-09
   - Authors: Haoxi Zeng, Qiankun Liu, Yi Bin, Haiyue Zhang, Yujuan Ding et al.
   - Tags: open-vocabulary, unsupervised, SAM, boundary/frequency, remote sensing
   - Links: [paper](http://arxiv.org/abs/2604.08461v1) / [pdf](http://arxiv.org/pdf/2604.08461v1)
   - 论文：OVS-DINO: Open-Vocabulary Segmentation via Structure-Aligned SAM-DINO with Language Guidance
   - 一句话总结：Open-Vocabulary Segmentation (OVS) aims to segment image regions beyond predefined category sets by leveraging semantic descriptions. While CLIP based approaches excel in semantic generalization, they frequent...
   - 任务设定：开放词汇视觉识别/分割，目标类别或文本提示在训练时未必出现。
   - 方法核心：借助 SAM/基础分割模型产生候选 mask，再做筛选或适配。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：适合拓展到开放词汇、零样本或少标注 COD。
   - 可借鉴点：prompt 设计、类别文本构造、免训练迁移流程；候选 mask 生成、视觉-语言筛选、推理式定位；边界/频域增强模块。
   - 可改进点：可改进 prompt 自动生成、负样本约束和 mask 置信度校准。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

3. **ActiveSAM: Image-Conditional Class Pruning for Fast and Accurate Open-Vocabulary Segmentation**
   - Source: arXiv, 2026-06-15
   - Authors: Tran Dinh Tien, Zhiqiang Shen
   - Tags: open-vocabulary, training-free, SAM, diffusion, remote sensing
   - Links: [paper](http://arxiv.org/abs/2606.16996v1) / [pdf](http://arxiv.org/pdf/2606.16996v1)
   - 论文：ActiveSAM: Image-Conditional Class Pruning for Fast and Accurate Open-Vocabulary Segmentation
   - 一句话总结：Segment Anything Model 3 (SAM 3) provides a strong frozen backbone for concept-prompted segmentation, but applying it directly to open-vocabulary semantic segmentation (OVSS) is inefficient: full-resolution de...
   - 任务设定：开放词汇视觉识别/分割，目标类别或文本提示在训练时未必出现。
   - 方法核心：提示学习或提示生成，重点看文本/视觉 prompt 如何约束定位。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：适合拓展到开放词汇、零样本或少标注 COD。
   - 可借鉴点：prompt 设计、类别文本构造、免训练迁移流程；候选 mask 生成、视觉-语言筛选、推理式定位。
   - 可改进点：可改进 prompt 自动生成、负样本约束和 mask 置信度校准。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

4. **Vision-Language Model Reasoning for Contextual Semantic Mapping in Intralogistics**
   - Source: arXiv, 2026-06-23
   - Authors: Marvin Rüdt, Hao Pang, Constantin Enke, Zäzilia Seibold, Kai Furmans
   - Tags: open-vocabulary, SAM, VLM/MLLM, reasoning, depth/geometry
   - Links: [paper](http://arxiv.org/abs/2606.24814v1) / [pdf](http://arxiv.org/pdf/2606.24814v1)
   - 论文：Vision-Language Model Reasoning for Contextual Semantic Mapping in Intralogistics
   - 一句话总结：Autonomous mobile robots operating in intralogistics environments rely on geometric maps for localization and navigation, but lack semantic understanding of objects and their contextual properties. We present...
   - 任务设定：开放词汇视觉识别/分割，目标类别或文本提示在训练时未必出现。
   - 方法核心：提示学习或提示生成，重点看文本/视觉 prompt 如何约束定位。
   - 实验结论：摘要强调消融、鲁棒性或泛化；适合优先看实验设计和跨域表现。
   - 和我课题的关系：适合拓展到开放词汇、零样本或少标注 COD。
   - 可借鉴点：prompt 设计、类别文本构造、免训练迁移流程；候选 mask 生成、视觉-语言筛选、推理式定位；深度或几何先验融合。
   - 可改进点：可改进 prompt 自动生成、负样本约束和 mask 置信度校准。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

5. **ARTEMIS: Agent-guided Reliability-aware Temporal Mask Evolution for Imperfectly Supervised Video Polyp Segmentation**
   - Source: arXiv, 2026-06-18
   - Authors: Tong Wang, Siwen Wang, Yaolei Qi, Jinxing Zhou, Yuting He et al.
   - Tags: SAM, VLM/MLLM, retrieval/prototype, boundary/frequency, depth/geometry, video
   - Links: [paper](http://arxiv.org/abs/2606.20161v1) / [pdf](http://arxiv.org/pdf/2606.20161v1)
   - 论文：ARTEMIS: Agent-guided Reliability-aware Temporal Mask Evolution for Imperfectly Supervised Video Polyp Segmentation
   - 一句话总结：Imperfectly supervised video polyp segmentation (VPS) aims to learn dense, temporally consistent masks from inexpensive supervision, including weak annotations (points, scribbles) and semi-supervision with few...
   - 任务设定：基础模型驱动的视觉定位/分割/推理，可用于自动提示生成或 mask 筛选。
   - 方法核心：借助 SAM/基础分割模型产生候选 mask，再做筛选或适配。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：可补充 COD 中纹理、边界、几何先验不足的问题。
   - 可借鉴点：候选 mask 生成、视觉-语言筛选、推理式定位；边界/频域增强模块；深度或几何先验融合。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

6. **Anatomy-Guided Residual Motion Diffusion for Controllable 4D Cardiac MRI Synthesis**
   - Source: arXiv, 2026-06-25
   - Authors: Yiheng Cao, Gustavo Andrade-Miranda, Jiatian Zhang, Lingxiao Zhao, Xin Gao
   - Tags: unsupervised, diffusion, boundary/frequency, depth/geometry, video
   - Links: [paper](http://arxiv.org/abs/2606.26764v1) / [pdf](http://arxiv.org/pdf/2606.26764v1)
   - 论文：Anatomy-Guided Residual Motion Diffusion for Controllable 4D Cardiac MRI Synthesis
   - 一句话总结：Developing robust artificial intelligence models for 4D (3D + time) medical imaging is constrained by limited annotated data, inter-device domain shifts, and privacy restrictions. To address this, we propose a...
   - 任务设定：视频/时序视觉任务，关注跨帧一致性、运动线索和长期上下文。
   - 方法核心：扩散/生成式建模，可能用于数据合成、先验建模或掩码优化。
   - 实验结论：可能包含新数据集/基准；适合看评测协议、失败案例和是否能服务 COD。
   - 和我课题的关系：可补充 COD 中纹理、边界、几何先验不足的问题。
   - 可借鉴点：边界/频域增强模块；深度或几何先验融合。
   - 可改进点：可结合多尺度语义上下文，避免只强化纹理导致误检。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

7. **SegEarth-OV: Towards Training-Free Open-Vocabulary Segmentation for Remote Sensing Images**
   - Source: arXiv, 2024-10-02
   - Authors: Kaiyu Li, Ruixun Liu, Xiangyong Cao, Xueru Bai, Feng Zhou et al.
   - Tags: open-vocabulary, training-free, SAM, remote sensing, anomaly/OOD
   - Links: [paper](http://arxiv.org/abs/2410.01768v2) / [pdf](http://arxiv.org/pdf/2410.01768v2)
   - 论文：SegEarth-OV: Towards Training-Free Open-Vocabulary Segmentation for Remote Sensing Images
   - 一句话总结：Remote sensing image plays an irreplaceable role in fields such as agriculture, water resources, military, and disaster relief. Pixel-level interpretation is a critical aspect of remote sensing image applicati...
   - 任务设定：开放词汇视觉识别/分割，目标类别或文本提示在训练时未必出现。
   - 方法核心：借助 SAM/基础分割模型产生候选 mask，再做筛选或适配。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：适合拓展到开放词汇、零样本或少标注 COD。
   - 可借鉴点：prompt 设计、类别文本构造、免训练迁移流程；候选 mask 生成、视觉-语言筛选、推理式定位；跨域鲁棒性、不确定性或异常分数。
   - 可改进点：可改进 prompt 自动生成、负样本约束和 mask 置信度校准。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

8. **T-REN: Learning Text-Aligned Region Tokens Improves Dense Vision-Language Alignment and Scalability**
   - Source: arXiv, 2026-04-20
   - Authors: Savya Khosla, Sethuraman T, Aryan Chadha, Alex Schwing, Derek Hoiem
   - Tags: open-vocabulary, VLM/MLLM, diffusion, retrieval/prototype, depth/geometry, video
   - Links: [paper](http://arxiv.org/abs/2604.18573v1) / [pdf](http://arxiv.org/pdf/2604.18573v1)
   - 论文：T-REN: Learning Text-Aligned Region Tokens Improves Dense Vision-Language Alignment and Scalability
   - 一句话总结：Despite recent progress, vision-language encoders struggle with two core limitations: (1) weak alignment between language and dense vision features, which hurts tasks like open-vocabulary semantic segmentation...
   - 任务设定：开放词汇视觉识别/分割，目标类别或文本提示在训练时未必出现。
   - 方法核心：视觉-语言对齐，把语义文本信息引入检测或分割。
   - 实验结论：摘要未给出强实验信号；先看实验表格和图 1，再决定是否精读。
   - 和我课题的关系：适合拓展到开放词汇、零样本或少标注 COD。
   - 可借鉴点：prompt 设计、类别文本构造、免训练迁移流程；候选 mask 生成、视觉-语言筛选、推理式定位；深度或几何先验融合。
   - 可改进点：可改进 prompt 自动生成、负样本约束和 mask 置信度校准。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

9. **MM-OVSeg:Multimodal Optical-SAR Fusion for Open-Vocabulary Segmentation in Remote Sensing**
   - Source: arXiv, 2026-03-18
   - Authors: Yimin Wei, Aoran Xiao, Hongruixuan Chen, Junshi Xia, Naoto Yokoya
   - Tags: open-vocabulary, VLM/MLLM, diffusion, remote sensing
   - Links: [paper](http://arxiv.org/abs/2603.17528v2) / [pdf](http://arxiv.org/pdf/2603.17528v2)
   - 论文：MM-OVSeg:Multimodal Optical-SAR Fusion for Open-Vocabulary Segmentation in Remote Sensing
   - 一句话总结：Open-vocabulary segmentation enables pixel-level recognition from an open set of textual categories, allowing generalization beyond fixed classes. Despite great potential in remote sensing, progress in this ar...
   - 任务设定：开放词汇视觉识别/分割，目标类别或文本提示在训练时未必出现。
   - 方法核心：视觉-语言对齐，把语义文本信息引入检测或分割。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：适合拓展到开放词汇、零样本或少标注 COD。
   - 可借鉴点：prompt 设计、类别文本构造、免训练迁移流程；候选 mask 生成、视觉-语言筛选、推理式定位。
   - 可改进点：可改进 prompt 自动生成、负样本约束和 mask 置信度校准。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

10. **Jolia: Concept-Level Vision-Language Alignment for 3D CT Contrastive Learning**
   - Source: arXiv, 2026-06-23
   - Authors: Julien Khlaut, Charles Corbière, Baptiste Callard, Amaury Prat, Leo Butsanets et al.
   - Tags: VLM/MLLM, depth/geometry
   - Links: [paper](http://arxiv.org/abs/2606.24570v2) / [pdf](http://arxiv.org/pdf/2606.24570v2)
   - 论文：Jolia: Concept-Level Vision-Language Alignment for 3D CT Contrastive Learning
   - 一句话总结：Vision-language contrastive pretraining has become the dominant recipe for 3D medical foundation models, leveraging the large volumes of paired scans and reports produced in clinical practice. However, medical...
   - 任务设定：基础模型驱动的视觉定位/分割/推理，可用于自动提示生成或 mask 筛选。
   - 方法核心：视觉-语言对齐，把语义文本信息引入检测或分割。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：可补充 COD 中纹理、边界、几何先验不足的问题。
   - 可借鉴点：候选 mask 生成、视觉-语言筛选、推理式定位；深度或几何先验融合。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

11. **HPP: Hierarchical Programmatic Probing for Long Video Understanding by Decoupling Perception and Reasoning**
   - Source: arXiv, 2026-06-19
   - Authors: Awais Rauf, Ahmed Hasssan, Greg Slabaugh
   - Tags: VLM/MLLM, reasoning, retrieval/prototype, video
   - Links: [paper](http://arxiv.org/abs/2606.21734v1) / [pdf](http://arxiv.org/pdf/2606.21734v1)
   - 论文：HPP: Hierarchical Programmatic Probing for Long Video Understanding by Decoupling Perception and Reasoning
   - 一句话总结：Understanding long videos requires fine-grained perception and multi-step, higher-order reasoning over complex, long-range spatio-temporal dynamics. Vision-language models (VLMs) encode video frames into visua...
   - 任务设定：基础模型驱动的视觉定位/分割/推理，可用于自动提示生成或 mask 筛选。
   - 方法核心：视觉-语言对齐，把语义文本信息引入检测或分割。
   - 实验结论：可能包含新数据集/基准；适合看评测协议、失败案例和是否能服务 COD。
   - 和我课题的关系：可用于伪装目标的语义描述、环境理解和候选区域判断。
   - 可借鉴点：候选 mask 生成、视觉-语言筛选、推理式定位。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

12. **UniDrive: A Unified Vision-Language and Grounding Framework for Interpretable Risk Understanding in Autonomous Driving**
   - Source: arXiv, 2026-06-23
   - Authors: Xiaowei Gao, Pengxiang Li, Yitai Cheng, Ruihan Xu, James Haworth et al.
   - Tags: VLM/MLLM, reasoning, video
   - Links: [paper](http://arxiv.org/abs/2606.24759v1) / [pdf](http://arxiv.org/pdf/2606.24759v1)
   - 论文：UniDrive: A Unified Vision-Language and Grounding Framework for Interpretable Risk Understanding in Autonomous Driving
   - 一句话总结：Recent multimodal large language models (MLLMs) have shown strong potential for autonomous driving scene understanding, yet existing methods still face a fundamental trade-off between temporal reasoning and sp...
   - 任务设定：基础模型驱动的视觉定位/分割/推理，可用于自动提示生成或 mask 筛选。
   - 方法核心：视觉-语言对齐，把语义文本信息引入检测或分割。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：可用于伪装目标的语义描述、环境理解和候选区域判断。
   - 可借鉴点：候选 mask 生成、视觉-语言筛选、推理式定位。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

13. **Object Tokens as a Bridge Between Segmentation and Visual Question Answering in Robotic Surgery**
   - Source: arXiv, 2026-06-14
   - Authors: Yiping Li, Ronald de Jong, Romy van Jaarsveld, Franco Badaloni, Gino Kuiper et al.
   - Tags: SAM, VLM/MLLM, reasoning
   - Links: [paper](http://arxiv.org/abs/2606.15861v1) / [pdf](http://arxiv.org/pdf/2606.15861v1)
   - 论文：Object Tokens as a Bridge Between Segmentation and Visual Question Answering in Robotic Surgery
   - 一句话总结：Visual Question Answering (VQA) in robotic surgery, referred to as surgical VQA, requires high-level understanding of complex surgical scenes and the integration of visual perception with language reasoning, w...
   - 任务设定：基础模型驱动的视觉定位/分割/推理，可用于自动提示生成或 mask 筛选。
   - 方法核心：借助 SAM/基础分割模型产生候选 mask，再做筛选或适配。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：可用于伪装目标的语义描述、环境理解和候选区域判断。
   - 可借鉴点：候选 mask 生成、视觉-语言筛选、推理式定位。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

14. **EnTrust: Modeling Inter-Modal Conflict for Trustworthy Multimodal Medical Image Analysis**
   - Source: arXiv, 2026-06-19
   - Authors: Dwarikanath Mahapatra, Abhijit Das, Behzad Bozorgtabar, Zongyuan Ge, Sudipta Roy et al.
   - Tags: SAM, diffusion
   - Links: [paper](http://arxiv.org/abs/2606.21384v1) / [pdf](http://arxiv.org/pdf/2606.21384v1)
   - 论文：EnTrust: Modeling Inter-Modal Conflict for Trustworthy Multimodal Medical Image Analysis
   - 一句话总结：Multimodal medical imaging fuses complementary anatomical and functional information, yet modalities frequently disagree in pathologically heterogeneous regions. Current segmentation models handle this in one...
   - 任务设定：基础模型驱动的视觉定位/分割/推理，可用于自动提示生成或 mask 筛选。
   - 方法核心：扩散/生成式建模，可能用于数据合成、先验建模或掩码优化。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：不是 COD 直系论文，但可能提供可迁移的视觉表征、训练策略或评测思路。
   - 可借鉴点：候选 mask 生成、视觉-语言筛选、推理式定位。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

15. **Annotation-Free Open-Vocabulary Segmentation for Remote-Sensing Images**
   - Source: arXiv, 2025-08-25
   - Authors: Kaiyu Li, Xiangyong Cao, Ruixun Liu, Shihong Wang, Zixuan Jiang et al.
   - Tags: open-vocabulary, SAM, boundary/frequency, remote sensing
   - Links: [paper](http://arxiv.org/abs/2508.18067v1) / [pdf](http://arxiv.org/pdf/2508.18067v1)
   - 论文：Annotation-Free Open-Vocabulary Segmentation for Remote-Sensing Images
   - 一句话总结：Semantic segmentation of remote sensing (RS) images is pivotal for comprehensive Earth observation, but the demand for interpreting new object categories, coupled with the high expense of manual annotation, po...
   - 任务设定：开放词汇视觉识别/分割，目标类别或文本提示在训练时未必出现。
   - 方法核心：借助 SAM/基础分割模型产生候选 mask，再做筛选或适配。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：适合拓展到开放词汇、零样本或少标注 COD。
   - 可借鉴点：prompt 设计、类别文本构造、免训练迁移流程；候选 mask 生成、视觉-语言筛选、推理式定位；边界/频域增强模块。
   - 可改进点：可改进 prompt 自动生成、负样本约束和 mask 置信度校准。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

16. **Diffusion Model as a Generalist Segmentation Learner**
   - Source: arXiv, 2026-04-27
   - Authors: Haoxiao Wang, Antao Xiang, Haiyang Sun, Peilin Sun, Changhao Pan et al.
   - Tags: open-vocabulary, diffusion, remote sensing, low-level
   - Links: [paper](http://arxiv.org/abs/2604.24575v1) / [pdf](http://arxiv.org/pdf/2604.24575v1)
   - 论文：Diffusion Model as a Generalist Segmentation Learner
   - 一句话总结：Diffusion models are primarily trained for image synthesis, yet their denoising trajectories encode rich, spatially aligned visual priors. In this paper, we demonstrate that these priors can be utilized for te...
   - 任务设定：开放词汇视觉识别/分割，目标类别或文本提示在训练时未必出现。
   - 方法核心：扩散/生成式建模，可能用于数据合成、先验建模或掩码优化。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：适合拓展到开放词汇、零样本或少标注 COD。
   - 可借鉴点：prompt 设计、类别文本构造、免训练迁移流程。
   - 可改进点：可改进 prompt 自动生成、负样本约束和 mask 置信度校准。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

17. **VesselSim: learning 3D blood vessel segmentation without expert annotations**
   - Source: arXiv, 2026-05-25
   - Authors: Erin Rainville, Melissa Ananian, Tristan Mirolla, Hassan Rivaz, Yiming Xiao
   - Tags: boundary/frequency, depth/geometry, anomaly/OOD
   - Links: [paper](http://arxiv.org/abs/2605.26277v2) / [pdf](http://arxiv.org/pdf/2605.26277v2)
   - 论文：VesselSim: learning 3D blood vessel segmentation without expert annotations
   - 一句话总结：Blood vessel segmentation is a core task in medical image analysis for the care of vascular diseases and surgical planning, yet the challenges of providing expert vascular annotations pose a major obstacle for...
   - 任务设定：异常检测或分布外识别，可类比伪装目标的弱异常发现。
   - 方法核心：边界感知建模，适合改善伪装目标轮廓不清的问题。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：可补充 COD 中纹理、边界、几何先验不足的问题。
   - 可借鉴点：边界/频域增强模块；深度或几何先验融合；跨域鲁棒性、不确定性或异常分数。
   - 可改进点：可结合多尺度语义上下文，避免只强化纹理导致误检。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

18. **Binary Tracking for Spatial QA and Navigation with Open Vision-Language Models**
   - Source: arXiv, 2026-06-15
   - Authors: Dongbin Na, Chanwoo Kim, Soonbin Rho, Giyun Choi, Gangbok Lee et al.
   - Tags: SAM, VLM/MLLM, reasoning, diffusion, retrieval/prototype, video
   - Links: [paper](http://arxiv.org/abs/2606.16902v1) / [pdf](http://arxiv.org/pdf/2606.16902v1)
   - 论文：Binary Tracking for Spatial QA and Navigation with Open Vision-Language Models
   - 一句话总结：This work addresses spatial question answering for service robots traversing long egocentric routes. Given a query such as "where can I find a dry cleaner on the way back home?", the system returns a metric co...
   - 任务设定：基础模型驱动的视觉定位/分割/推理，可用于自动提示生成或 mask 筛选。
   - 方法核心：借助 SAM/基础分割模型产生候选 mask，再做筛选或适配。
   - 实验结论：可能包含新数据集/基准；适合看评测协议、失败案例和是否能服务 COD。
   - 和我课题的关系：可用于伪装目标的语义描述、环境理解和候选区域判断。
   - 可借鉴点：候选 mask 生成、视觉-语言筛选、推理式定位。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

19. **ReasonCLIP-58M: Visually Grounded Commonsense Reasoning Supervision for CLIP**
   - Source: arXiv, 2026-06-25
   - Authors: Sicheng Zhang, Muzammal Naseer, Binzhu Xie, Naufal Suryanto, Shi Qiu et al.
   - Tags: VLM/MLLM, reasoning, diffusion, retrieval/prototype
   - Links: [paper](http://arxiv.org/abs/2606.26794v1) / [pdf](http://arxiv.org/pdf/2606.26794v1)
   - 论文：ReasonCLIP-58M: Visually Grounded Commonsense Reasoning Supervision for CLIP
   - 一句话总结：CLIP and its variants are widely adopted visual backbones in multimodal systems, but their pretraining remains dominated by descriptive image-text alignment. As downstream applications increasingly demand visu...
   - 任务设定：基础模型驱动的视觉定位/分割/推理，可用于自动提示生成或 mask 筛选。
   - 方法核心：视觉-语言对齐，把语义文本信息引入检测或分割。
   - 实验结论：可能包含新数据集/基准；适合看评测协议、失败案例和是否能服务 COD。
   - 和我课题的关系：可用于伪装目标的语义描述、环境理解和候选区域判断。
   - 可借鉴点：候选 mask 生成、视觉-语言筛选、推理式定位。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

20. **MLFFM-SegDiff: A Multi-Level Feature Fusion Diffusion Model for Skin Lesion Segmentation**
   - Source: arXiv, 2026-06-25
   - Authors: Jingjun Gu, Chaojie Shen, Yifeng Cao, Wei Zhang, Yiliu Li et al.
   - Tags: diffusion, boundary/frequency, low-level
   - Links: [paper](http://arxiv.org/abs/2606.26712v1) / [pdf](http://arxiv.org/pdf/2606.26712v1)
   - 论文：MLFFM-SegDiff: A Multi-Level Feature Fusion Diffusion Model for Skin Lesion Segmentation
   - 一句话总结：Skin lesion segmentation is a key task in computer-aided dermatological diagnosis, where accuracy directly impacts downstream analysis and disease classification. However, dermoscopic images are challenging du...
   - 任务设定：通用计算机视觉任务，先判断是否能迁移到 COD 的感知、定位或分割环节。
   - 方法核心：扩散/生成式建模，可能用于数据合成、先验建模或掩码优化。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：可补充 COD 中纹理、边界、几何先验不足的问题。
   - 可借鉴点：边界/频域增强模块。
   - 可改进点：可结合多尺度语义上下文，避免只强化纹理导致误检。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

21. **High-Fidelity Synthetic Transmission Electron Microscopy Image Generation Using Diffusion Probabilistic Models for Data-Limited Semiconductor Metrology**
   - Source: arXiv, 2026-06-23
   - Authors: Johannes Boehm, Bappaditya Dey
   - Tags: SAM, diffusion, low-level
   - Links: [paper](http://arxiv.org/abs/2606.24817v1) / [pdf](http://arxiv.org/pdf/2606.24817v1)
   - 论文：High-Fidelity Synthetic Transmission Electron Microscopy Image Generation Using Diffusion Probabilistic Models for Data-Limited Semiconductor Metrology
   - 一句话总结：Advanced semiconductor nodes drastically increased demand for Transmission Electron Microscopy (TEM), yet destructive sample preparation, slow imaging and high costs severely limit the availability of diverse...
   - 任务设定：基础模型驱动的视觉定位/分割/推理，可用于自动提示生成或 mask 筛选。
   - 方法核心：扩散/生成式建模，可能用于数据合成、先验建模或掩码优化。
   - 实验结论：可能包含新数据集/基准；适合看评测协议、失败案例和是否能服务 COD。
   - 和我课题的关系：不是 COD 直系论文，但可能提供可迁移的视觉表征、训练策略或评测思路。
   - 可借鉴点：候选 mask 生成、视觉-语言筛选、推理式定位。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

22. **Prob-BBDM: a Probabilistic Brownian Bridge Diffusion Model for MRI sequence image-to-image translation**
   - Source: arXiv, 2026-06-23
   - Authors: Martin Valls, Pascal Bourdon, Christine Fernandez-Maloigne, Guillaume Herpe, David Helbert
   - Tags: diffusion, depth/geometry
   - Links: [paper](http://arxiv.org/abs/2606.24313v1) / [pdf](http://arxiv.org/pdf/2606.24313v1)
   - 论文：Prob-BBDM: a Probabilistic Brownian Bridge Diffusion Model for MRI sequence image-to-image translation
   - 一句话总结：AI-driven image-to-image synthesis is rapidly advancing, with growing applications in medical imaging. Multi-modal image analysis plays a crucial role in optimizing examination quality, yet acquiring multiple...
   - 任务设定：通用计算机视觉任务，先判断是否能迁移到 COD 的感知、定位或分割环节。
   - 方法核心：扩散/生成式建模，可能用于数据合成、先验建模或掩码优化。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：可补充 COD 中纹理、边界、几何先验不足的问题。
   - 可借鉴点：深度或几何先验融合。
   - 可改进点：可思考是否缺少 COD 场景验证、复杂背景失败分析或轻量化部署。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

23. **IMAGIN-4D: Image-Guided Controllable Interaction Generation**
   - Source: arXiv, 2026-06-22
   - Authors: Sai Kumar Dwivedi, Federica Bogo, Buğra Tekin, Chenhongyi Yang, Nadine Bertsch et al.
   - Tags: SAM, diffusion, depth/geometry, video
   - Links: [paper](http://arxiv.org/abs/2606.23675v1) / [pdf](http://arxiv.org/pdf/2606.23675v1)
   - 论文：IMAGIN-4D: Image-Guided Controllable Interaction Generation
   - 一句话总结：Generating human-object interactions (HOI) is central to character animation, robotics, AR/VR, and embodied AI. Recent HOI generation methods synthesize motion from text, object geometry, and sparse waypoints,...
   - 任务设定：基础模型驱动的视觉定位/分割/推理，可用于自动提示生成或 mask 筛选。
   - 方法核心：扩散/生成式建模，可能用于数据合成、先验建模或掩码优化。
   - 实验结论：可能包含新数据集/基准；适合看评测协议、失败案例和是否能服务 COD。
   - 和我课题的关系：可补充 COD 中纹理、边界、几何先验不足的问题。
   - 可借鉴点：候选 mask 生成、视觉-语言筛选、推理式定位；深度或几何先验融合。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

24. **Prompting Diffusion Models for Zero-Shot Instance Segmentation**
   - Source: arXiv, 2026-06-21
   - Authors: Irem Zeynep Alagöz, Nils Morbitzer, Andrea Ramazzina, Nassir Navab, Federico Tombari et al.
   - Tags: diffusion
   - Links: [paper](http://arxiv.org/abs/2606.22660v1) / [pdf](http://arxiv.org/pdf/2606.22660v1)
   - 论文：Prompting Diffusion Models for Zero-Shot Instance Segmentation
   - 一句话总结：Several disruptive research directions have recently emerged in computer vision, including foundation models achieving previously unseen zero-shot performance in scene understanding, even interactively, and ge...
   - 任务设定：通用计算机视觉任务，先判断是否能迁移到 COD 的感知、定位或分割环节。
   - 方法核心：扩散/生成式建模，可能用于数据合成、先验建模或掩码优化。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：不是 COD 直系论文，但可能提供可迁移的视觉表征、训练策略或评测思路。
   - 可借鉴点：任务建模、损失函数、消融组织方式。
   - 可改进点：可思考是否缺少 COD 场景验证、复杂背景失败分析或轻量化部署。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

25. **AD-DINOv3: Enhancing DINOv3 for Zero-Shot Anomaly Detection with Anomaly-Aware Calibration**
   - Source: arXiv, 2025-09-17
   - Authors: Jingyi Yuan, Jianxiong Ye, Wenkang Chen, Chenqiang Gao
   - Tags: VLM/MLLM, diffusion, anomaly/OOD
   - Links: [paper](http://arxiv.org/abs/2509.14084v2) / [pdf](http://arxiv.org/pdf/2509.14084v2)
   - 论文：AD-DINOv3: Enhancing DINOv3 for Zero-Shot Anomaly Detection with Anomaly-Aware Calibration
   - 一句话总结：Zero-Shot Anomaly Detection (ZSAD) seeks to identify anomalies from arbitrary novel categories, offering a scalable and annotation-efficient solution. Traditionally, most ZSAD works have been based on the CLIP...
   - 任务设定：基础模型驱动的视觉定位/分割/推理，可用于自动提示生成或 mask 筛选。
   - 方法核心：提示学习或提示生成，重点看文本/视觉 prompt 如何约束定位。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：可用于伪装目标的语义描述、环境理解和候选区域判断。
   - 可借鉴点：候选 mask 生成、视觉-语言筛选、推理式定位；跨域鲁棒性、不确定性或异常分数。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

26. **FiLo++: Zero-/Few-Shot Anomaly Detection by Fused Fine-Grained Descriptions and Deformable Localization**
   - Source: arXiv, 2025-01-17
   - Authors: Zhaopeng Gu, Bingke Zhu, Guibo Zhu, Yingying Chen, Ming Tang et al.
   - Tags: SAM, reasoning, diffusion, anomaly/OOD
   - Links: [paper](http://arxiv.org/abs/2501.10067v2) / [pdf](http://arxiv.org/pdf/2501.10067v2)
   - 论文：FiLo++: Zero-/Few-Shot Anomaly Detection by Fused Fine-Grained Descriptions and Deformable Localization
   - 一句话总结：Anomaly detection methods typically require extensive normal samples from the target class for training, limiting their applicability in scenarios that require rapid adaptation, such as cold start. Zero-shot a...
   - 任务设定：基础模型驱动的视觉定位/分割/推理，可用于自动提示生成或 mask 筛选。
   - 方法核心：提示学习或提示生成，重点看文本/视觉 prompt 如何约束定位。
   - 实验结论：可能包含新数据集/基准；适合看评测协议、失败案例和是否能服务 COD。
   - 和我课题的关系：可用于伪装目标的语义描述、环境理解和候选区域判断。
   - 可借鉴点：候选 mask 生成、视觉-语言筛选、推理式定位；跨域鲁棒性、不确定性或异常分数。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

27. **Exploring Efficient Open-Vocabulary Segmentation in the Remote Sensing**
   - Source: arXiv, 2025-09-15
   - Authors: Bingyu Li, Haocheng Dong, Da Zhang, Zhiyuan Zhao, Junyu Gao et al.
   - Tags: open-vocabulary, SAM, VLM/MLLM, boundary/frequency, remote sensing
   - Links: [paper](http://arxiv.org/abs/2509.12040v2) / [pdf](http://arxiv.org/pdf/2509.12040v2)
   - 论文：Exploring Efficient Open-Vocabulary Segmentation in the Remote Sensing
   - 一句话总结：Open-Vocabulary Remote Sensing Image Segmentation (OVRSIS), an emerging task that adapts Open-Vocabulary Segmentation (OVS) to the remote sensing (RS) domain, remains underexplored due to the absence of a unif...
   - 任务设定：开放词汇视觉识别/分割，目标类别或文本提示在训练时未必出现。
   - 方法核心：借助 SAM/基础分割模型产生候选 mask，再做筛选或适配。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：适合拓展到开放词汇、零样本或少标注 COD。
   - 可借鉴点：prompt 设计、类别文本构造、免训练迁移流程；候选 mask 生成、视觉-语言筛选、推理式定位；边界/频域增强模块。
   - 可改进点：可改进 prompt 自动生成、负样本约束和 mask 置信度校准。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

28. **TravExplorer: Cross-Floor Embodied Exploration via Traversability-Aware 3-D Planning**
   - Source: arXiv, 2026-05-19
   - Authors: Han Zheng, Zhe Chen, Yudong Huang, Haoran Liu, Jinghao Wang et al.
   - Tags: open-vocabulary, reasoning, depth/geometry, video
   - Links: [paper](http://arxiv.org/abs/2605.19958v1) / [pdf](http://arxiv.org/pdf/2605.19958v1)
   - 论文：TravExplorer: Cross-Floor Embodied Exploration via Traversability-Aware 3-D Planning
   - 一句话总结：Zero-shot Object Navigation (ZSON) has shown promise for open-vocabulary target search in unseen environments, yet most existing systems remain tied to planar representations and single-floor assumptions. Thes...
   - 任务设定：开放词汇视觉识别/分割，目标类别或文本提示在训练时未必出现。
   - 方法核心：多模态大模型推理，可能用于目标描述、区域判断或链式推理。
   - 实验结论：摘要未给出强实验信号；先看实验表格和图 1，再决定是否精读。
   - 和我课题的关系：适合拓展到开放词汇、零样本或少标注 COD。
   - 可借鉴点：prompt 设计、类别文本构造、免训练迁移流程；深度或几何先验融合。
   - 可改进点：可改进 prompt 自动生成、负样本约束和 mask 置信度校准。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

29. **SparseSAM: Structured Sparsification of Activations in Segment Anything Models**
   - Source: arXiv, 2026-05-17
   - Authors: Hoai-Chau Tran, Chi H. Nguyen, Duy M. H. Nguyen, Mathias Niepert, Fan Lai et al.
   - Tags: open-vocabulary, training-free, SAM
   - Links: [paper](http://arxiv.org/abs/2605.17633v1) / [pdf](http://arxiv.org/pdf/2605.17633v1)
   - 论文：SparseSAM: Structured Sparsification of Activations in Segment Anything Models
   - 一句话总结：The Segment Anything Model (SAM) achieves strong open-vocabulary segmentation, but its ViT-based image encoders dominate inference latency and memory. Existing activation compression methods, such as token mer...
   - 任务设定：开放词汇视觉识别/分割，目标类别或文本提示在训练时未必出现。
   - 方法核心：借助 SAM/基础分割模型产生候选 mask，再做筛选或适配。
   - 实验结论：可能包含新数据集/基准；适合看评测协议、失败案例和是否能服务 COD。
   - 和我课题的关系：适合拓展到开放词汇、零样本或少标注 COD。
   - 可借鉴点：prompt 设计、类别文本构造、免训练迁移流程；候选 mask 生成、视觉-语言筛选、推理式定位。
   - 可改进点：可改进 prompt 自动生成、负样本约束和 mask 置信度校准。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

30. **Towards Realistic Open-Vocabulary Remote Sensing Segmentation: Benchmark and Baseline**
   - Source: arXiv, 2026-04-17
   - Authors: Bingyu Li, Tao Huo, Haocheng Dong, Da Zhang, Zhiyuan Zhao et al.
   - Tags: open-vocabulary, remote sensing, anomaly/OOD
   - Links: [paper](http://arxiv.org/abs/2604.15652v1) / [pdf](http://arxiv.org/pdf/2604.15652v1)
   - 论文：Towards Realistic Open-Vocabulary Remote Sensing Segmentation: Benchmark and Baseline
   - 一句话总结：Open-vocabulary remote sensing image segmentation (OVRSIS) remains underexplored due to fragmented datasets, limited training diversity, and the lack of evaluation benchmarks that reflect realistic geospatial...
   - 任务设定：开放词汇视觉识别/分割，目标类别或文本提示在训练时未必出现。
   - 方法核心：异常/OOD 建模，把目标从复杂背景中作为低概率区域凸显出来。
   - 实验结论：可能包含新数据集/基准；适合看评测协议、失败案例和是否能服务 COD。
   - 和我课题的关系：适合拓展到开放词汇、零样本或少标注 COD。
   - 可借鉴点：prompt 设计、类别文本构造、免训练迁移流程；跨域鲁棒性、不确定性或异常分数。
   - 可改进点：可改进 prompt 自动生成、负样本约束和 mask 置信度校准。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

31. **OV-Stitcher: A Global Context-Aware Framework for Training-Free Open-Vocabulary Semantic Segmentation**
   - Source: arXiv, 2026-04-09
   - Authors: Seungjae Moon, Seunghyun Oh, Youngmin Ro
   - Tags: open-vocabulary, training-free, VLM/MLLM, reasoning, diffusion, boundary/frequency
   - Links: [paper](http://arxiv.org/abs/2604.08110v2) / [pdf](http://arxiv.org/pdf/2604.08110v2)
   - 论文：OV-Stitcher: A Global Context-Aware Framework for Training-Free Open-Vocabulary Semantic Segmentation
   - 一句话总结：Training-free open-vocabulary semantic segmentation(TF-OVSS) has recently attracted attention for its ability to perform dense prediction by leveraging the pretrained knowledge of large vision and vision-langu...
   - 任务设定：开放词汇视觉识别/分割，目标类别或文本提示在训练时未必出现。
   - 方法核心：视觉-语言对齐，把语义文本信息引入检测或分割。
   - 实验结论：可能包含新数据集/基准；适合看评测协议、失败案例和是否能服务 COD。
   - 和我课题的关系：适合拓展到开放词汇、零样本或少标注 COD。
   - 可借鉴点：prompt 设计、类别文本构造、免训练迁移流程；候选 mask 生成、视觉-语言筛选、推理式定位；边界/频域增强模块。
   - 可改进点：可改进 prompt 自动生成、负样本约束和 mask 置信度校准。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

32. **TRACE: Evidence Grounding-Guided Multi-Video Event Understanding and Claim Generation**
   - Source: arXiv, 2026-05-16
   - Authors: Pengyu Yan, Akhil Gorugantu, Mahesh Bhosale, Abdul Wasi, Vishvesh Trivedi et al.
   - Tags: VLM/MLLM, reasoning, video
   - Links: [paper](http://arxiv.org/abs/2605.16740v2) / [pdf](http://arxiv.org/pdf/2605.16740v2)
   - 论文：TRACE: Evidence Grounding-Guided Multi-Video Event Understanding and Claim Generation
   - 一句话总结：Multi-video event understanding demands models that can locate and attribute query-relevant evidence scattered across long, heterogeneous video corpora. Existing large vision-language models (LVLMs) often unde...
   - 任务设定：基础模型驱动的视觉定位/分割/推理，可用于自动提示生成或 mask 筛选。
   - 方法核心：视觉-语言对齐，把语义文本信息引入检测或分割。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：可用于伪装目标的语义描述、环境理解和候选区域判断。
   - 可借鉴点：候选 mask 生成、视觉-语言筛选、推理式定位。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

33. **Segmentation, Detection and Explanation: A Unified Framework for CT Appearance Reasoning**
   - Source: arXiv, 2026-05-15
   - Authors: Yuyuan Liu, Can Peng, Yingyu Yang, Qianye Yang, Cheng Ouyang et al.
   - Tags: VLM/MLLM, reasoning, diffusion
   - Links: [paper](http://arxiv.org/abs/2605.15997v1) / [pdf](http://arxiv.org/pdf/2605.15997v1)
   - 论文：Segmentation, Detection and Explanation: A Unified Framework for CT Appearance Reasoning
   - 一句话总结：Recent progress in deep learning has significantly advanced CT image analysis, particularly for segmentation tasks. However, these advances are largely confined to image-level pattern recognition, with most me...
   - 任务设定：基础模型驱动的视觉定位/分割/推理，可用于自动提示生成或 mask 筛选。
   - 方法核心：提示学习或提示生成，重点看文本/视觉 prompt 如何约束定位。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：可用于伪装目标的语义描述、环境理解和候选区域判断。
   - 可借鉴点：候选 mask 生成、视觉-语言筛选、推理式定位。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

34. **DeepTumorVQA: A Hierarchical 3D CT Benchmark for Stage-Wise Evaluation of Medical VLMs and Tool-Augmented Agents**
   - Source: arXiv, 2026-05-10
   - Authors: Yixiong Chen, Wenjie Xiao, Pedro R. A. S. Bassi, Boyan Wang, Liang He et al.
   - Tags: VLM/MLLM, reasoning, diffusion, boundary/frequency, depth/geometry
   - Links: [paper](http://arxiv.org/abs/2605.09679v1) / [pdf](http://arxiv.org/pdf/2605.09679v1)
   - 论文：DeepTumorVQA: A Hierarchical 3D CT Benchmark for Stage-Wise Evaluation of Medical VLMs and Tool-Augmented Agents
   - 一句话总结：Medical vision-language models (VLMs) and AI agents have made significant progress in learning to analyze and reason about clinical images. However, existing medical visual question answering (VQA) benchmarks...
   - 任务设定：基础模型驱动的视觉定位/分割/推理，可用于自动提示生成或 mask 筛选。
   - 方法核心：视觉-语言对齐，把语义文本信息引入检测或分割。
   - 实验结论：可能包含新数据集/基准；适合看评测协议、失败案例和是否能服务 COD。
   - 和我课题的关系：可补充 COD 中纹理、边界、几何先验不足的问题。
   - 可借鉴点：候选 mask 生成、视觉-语言筛选、推理式定位；边界/频域增强模块；深度或几何先验融合。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

35. **SubspaceAD: Training-Free Few-Shot Anomaly Detection via Subspace Modeling**
   - Source: arXiv, 2026-02-26
   - Authors: Camile Lendering, Erkut Akdag, Egor Bondarev
   - Tags: training-free, VLM/MLLM, retrieval/prototype, remote sensing, anomaly/OOD
   - Links: [paper](http://arxiv.org/abs/2602.23013v3) / [pdf](http://arxiv.org/pdf/2602.23013v3)
   - 论文：SubspaceAD: Training-Free Few-Shot Anomaly Detection via Subspace Modeling
   - 一句话总结：Detecting visual anomalies in industrial inspection often requires training with only a few normal images per category. Recent few-shot methods achieve strong results employing foundation-model features, but t...
   - 任务设定：免训练或少训练迁移设定，重点看 prompt、特征选择和后处理。
   - 方法核心：提示学习或提示生成，重点看文本/视觉 prompt 如何约束定位。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：适合拓展到开放词汇、零样本或少标注 COD。
   - 可借鉴点：prompt 设计、类别文本构造、免训练迁移流程；候选 mask 生成、视觉-语言筛选、推理式定位；跨域鲁棒性、不确定性或异常分数。
   - 可改进点：可改进 prompt 自动生成、负样本约束和 mask 置信度校准。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

36. **V-Zero: Answer-Label-Free On-Policy Distillation with Contrastive Evidence Gating for Fine-Grained Visual Reasoning**
   - Source: arXiv, 2026-06-24
   - Authors: Haoxiang Sun, Zhihang Yi, Langxuan Deng, Yuhao Zhou, Peiqi Jia et al.
   - Tags: SAM, VLM/MLLM, reasoning
   - Links: [paper](http://arxiv.org/abs/2606.25319v1) / [pdf](http://arxiv.org/pdf/2606.25319v1)
   - 论文：V-Zero: Answer-Label-Free On-Policy Distillation with Contrastive Evidence Gating for Fine-Grained Visual Reasoning
   - 一句话总结：Fine-grained visual reasoning requires multimodal large language models (MLLMs) to identify task-relevant visual evidence and ground their reasoning in local image regions. Existing agentic methods typically r...
   - 任务设定：基础模型驱动的视觉定位/分割/推理，可用于自动提示生成或 mask 筛选。
   - 方法核心：借助 SAM/基础分割模型产生候选 mask，再做筛选或适配。
   - 实验结论：可能包含新数据集/基准；适合看评测协议、失败案例和是否能服务 COD。
   - 和我课题的关系：可用于伪装目标的语义描述、环境理解和候选区域判断。
   - 可借鉴点：候选 mask 生成、视觉-语言筛选、推理式定位。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

37. **Are We There Yet? Exploring the Capabilities of MLLMs in Assistive AI Applications**
   - Source: arXiv, 2026-06-23
   - Authors: Shayon Dasgupta, Avijit Dasgupta, C. V. Jawahar
   - Tags: VLM/MLLM, reasoning, anomaly/OOD
   - Links: [paper](http://arxiv.org/abs/2606.25084v1) / [pdf](http://arxiv.org/pdf/2606.25084v1)
   - 论文：Are We There Yet? Exploring the Capabilities of MLLMs in Assistive AI Applications
   - 一句话总结：Multimodal Large Language Models (MLLMs) have redefined visual understanding by combining vision encoders with large-scale language models. This unified architecture enables strong performance on tasks like im...
   - 任务设定：基础模型驱动的视觉定位/分割/推理，可用于自动提示生成或 mask 筛选。
   - 方法核心：视觉-语言对齐，把语义文本信息引入检测或分割。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：可用于伪装目标的语义描述、环境理解和候选区域判断。
   - 可借鉴点：候选 mask 生成、视觉-语言筛选、推理式定位；跨域鲁棒性、不确定性或异常分数。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

38. **CineCap: Structured Reasoning with Spatio-Temporal Anchors for Cinematographic Video Captioning**
   - Source: arXiv, 2026-06-23
   - Authors: Xinyu Mao, Yuhui Zeng, Xiaokun Liu, Wenyu Qin, Meng Wang et al.
   - Tags: VLM/MLLM, reasoning, diffusion, depth/geometry, video
   - Links: [paper](http://arxiv.org/abs/2606.24636v1) / [pdf](http://arxiv.org/pdf/2606.24636v1)
   - 论文：CineCap: Structured Reasoning with Spatio-Temporal Anchors for Cinematographic Video Captioning
   - 一句话总结：Cinematographic captioning aims to describe how a video is filmed using professional film-language concepts such as camera movement, shot size, depth of field, composition, and shooting angle. This capability...
   - 任务设定：基础模型驱动的视觉定位/分割/推理，可用于自动提示生成或 mask 筛选。
   - 方法核心：视觉-语言对齐，把语义文本信息引入检测或分割。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：可补充 COD 中纹理、边界、几何先验不足的问题。
   - 可借鉴点：候选 mask 生成、视觉-语言筛选、推理式定位；深度或几何先验融合。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

39. **3D-PLOT-LLM: Part-Level Object Tokens for 3D Large Language Models**
   - Source: arXiv, 2026-06-18
   - Authors: Jintang Xue, Xinyu Wang, Yixing Wu, Jingwen Chen, C. -C. Jay Kuo
   - Tags: VLM/MLLM, diffusion, depth/geometry
   - Links: [paper](http://arxiv.org/abs/2606.19828v1) / [pdf](http://arxiv.org/pdf/2606.19828v1)
   - 论文：3D-PLOT-LLM: Part-Level Object Tokens for 3D Large Language Models
   - 一句话总结：3D multimodal large language models (3D MLLMs) describe a 3D object as a whole but cannot address, name, or reason about its parts. Prior part-aware attempts add segmentation decoders, heavier 3D encoders, or...
   - 任务设定：基础模型驱动的视觉定位/分割/推理，可用于自动提示生成或 mask 筛选。
   - 方法核心：提示学习或提示生成，重点看文本/视觉 prompt 如何约束定位。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：可补充 COD 中纹理、边界、几何先验不足的问题。
   - 可借鉴点：候选 mask 生成、视觉-语言筛选、推理式定位；深度或几何先验融合。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

40. **Cross-Modality Structural Guidance in 3D Latent Diffusion for Robust FLAIR Super-Resolution**
   - Source: arXiv, 2026-06-24
   - Authors: Haoyu Lan, Jiazhen Zhang, John Onofrey, Bino Varghese, Nasim Sheikh-Bahaei et al.
   - Tags: SAM, diffusion, boundary/frequency, depth/geometry, low-level
   - Links: [paper](http://arxiv.org/abs/2606.25255v1) / [pdf](http://arxiv.org/pdf/2606.25255v1)
   - 论文：Cross-Modality Structural Guidance in 3D Latent Diffusion for Robust FLAIR Super-Resolution
   - 一句话总结：High-resolution (HR) MRI acquisition is often hampered by scan time constraints, resulting in anisotropic or low-resolution scans (e.g., thick-slice FLAIR) that limit diagnostic accuracy. While deep learning-b...
   - 任务设定：基础模型驱动的视觉定位/分割/推理，可用于自动提示生成或 mask 筛选。
   - 方法核心：扩散/生成式建模，可能用于数据合成、先验建模或掩码优化。
   - 实验结论：可能包含新数据集/基准；适合看评测协议、失败案例和是否能服务 COD。
   - 和我课题的关系：可补充 COD 中纹理、边界、几何先验不足的问题。
   - 可借鉴点：候选 mask 生成、视觉-语言筛选、推理式定位；边界/频域增强模块；深度或几何先验融合。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

41. **NeuroSonic: Conditional Flow Matching for EEG-to-Speech Reconstruction**
   - Source: arXiv, 2026-06-23
   - Authors: Wenhao Gao, Yifan Wang, Yijia Ma, Carl Yang, Wen Li et al.
   - Tags: SAM, diffusion, video, low-level
   - Links: [paper](http://arxiv.org/abs/2606.24087v1) / [pdf](http://arxiv.org/pdf/2606.24087v1)
   - 论文：NeuroSonic: Conditional Flow Matching for EEG-to-Speech Reconstruction
   - 一句话总结：Reconstructing continuous speech from scalp electroencephalography (EEG) remains fundamentally challenging. EEG provides a weak, spatially diffuse, and highly variable measurement of distributed cortical activ...
   - 任务设定：基础模型驱动的视觉定位/分割/推理，可用于自动提示生成或 mask 筛选。
   - 方法核心：扩散/生成式建模，可能用于数据合成、先验建模或掩码优化。
   - 实验结论：可能包含新数据集/基准；适合看评测协议、失败案例和是否能服务 COD。
   - 和我课题的关系：不是 COD 直系论文，但可能提供可迁移的视觉表征、训练策略或评测思路。
   - 可借鉴点：候选 mask 生成、视觉-语言筛选、推理式定位。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

42. **C^2GR: Coupled Comprehensive Generative Replay for a Continually Learnable Universal Segmentation Model**
   - Source: arXiv, 2026-06-22
   - Authors: Wei Li, Jingyang Zhang, Guoan Wang, Junzhi Ning, Yang Chen et al.
   - Tags: diffusion, low-level
   - Links: [paper](http://arxiv.org/abs/2606.23473v1) / [pdf](http://arxiv.org/pdf/2606.23473v1)
   - 论文：C^2GR: Coupled Comprehensive Generative Replay for a Continually Learnable Universal Segmentation Model
   - 一句话总结：Universal segmentation models exhibit significant potential for diverse tasks involving different imaging modalities and segmentation objectives. Task-Incremental Learning provides a privacy-preserving approac...
   - 任务设定：通用计算机视觉任务，先判断是否能迁移到 COD 的感知、定位或分割环节。
   - 方法核心：扩散/生成式建模，可能用于数据合成、先验建模或掩码优化。
   - 实验结论：摘要未给出强实验信号；先看实验表格和图 1，再决定是否精读。
   - 和我课题的关系：不是 COD 直系论文，但可能提供可迁移的视觉表征、训练策略或评测思路。
   - 可借鉴点：任务建模、损失函数、消融组织方式。
   - 可改进点：可思考是否缺少 COD 场景验证、复杂背景失败分析或轻量化部署。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

43. **BEV-Denoise: Learning Intrinsic Noise for Accurate Bird's-Eye-View Semantic Segmentation**
   - Source: arXiv, 2026-06-22
   - Authors: Dooseop Choi, Kyounghwan An, Kyoung-Wook Min
   - Tags: diffusion, low-level
   - Links: [paper](http://arxiv.org/abs/2606.22931v1) / [pdf](http://arxiv.org/pdf/2606.22931v1)
   - 论文：BEV-Denoise: Learning Intrinsic Noise for Accurate Bird's-Eye-View Semantic Segmentation
   - 一句话总结：In this paper, we present a framework dubbed \textbf{BEV-Denoise} that estimates and removes intrinsic noise from learned Bird's-Eye-View (BEV) features to achieve accurate BEV semantic segmentation. Inspired...
   - 任务设定：通用计算机视觉任务，先判断是否能迁移到 COD 的感知、定位或分割环节。
   - 方法核心：扩散/生成式建模，可能用于数据合成、先验建模或掩码优化。
   - 实验结论：可能包含新数据集/基准；适合看评测协议、失败案例和是否能服务 COD。
   - 和我课题的关系：不是 COD 直系论文，但可能提供可迁移的视觉表征、训练策略或评测思路。
   - 可借鉴点：任务建模、损失函数、消融组织方式。
   - 可改进点：可思考是否缺少 COD 场景验证、复杂背景失败分析或轻量化部署。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

44. **Crane: Context-Guided Prompt Learning and Attention Refinement for Zero-Shot Anomaly Detection**
   - Source: arXiv, 2025-04-15
   - Authors: Alireza Salehi, Mohammadreza Salehi, Reshad Hosseini, Cees G. M. Snoek, Makoto Yamada et al.
   - Tags: SAM, diffusion, boundary/frequency, anomaly/OOD
   - Links: [paper](http://arxiv.org/abs/2504.11055v2) / [pdf](http://arxiv.org/pdf/2504.11055v2)
   - 论文：Crane: Context-Guided Prompt Learning and Attention Refinement for Zero-Shot Anomaly Detection
   - 一句话总结：Anomaly Detection involves identifying deviations from normal data distributions and is critical in fields such as medical diagnostics and industrial defect detection. Traditional AD methods typically require...
   - 任务设定：基础模型驱动的视觉定位/分割/推理，可用于自动提示生成或 mask 筛选。
   - 方法核心：提示学习或提示生成，重点看文本/视觉 prompt 如何约束定位。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：可补充 COD 中纹理、边界、几何先验不足的问题。
   - 可借鉴点：候选 mask 生成、视觉-语言筛选、推理式定位；边界/频域增强模块；跨域鲁棒性、不确定性或异常分数。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

45. **Taming SAM3 in the Wild: A Concept Bank for Open-Vocabulary Segmentation**
   - Source: arXiv, 2026-02-06
   - Authors: Gensheng Pei, Xiruo Jiang, Yazhou Yao, Xiangbo Shu, Fumin Shen et al.
   - Tags: open-vocabulary, SAM, diffusion, retrieval/prototype
   - Links: [paper](http://arxiv.org/abs/2602.06333v1) / [pdf](http://arxiv.org/pdf/2602.06333v1)
   - 论文：Taming SAM3 in the Wild: A Concept Bank for Open-Vocabulary Segmentation
   - 一句话总结：The recent introduction of \texttt{SAM3} has revolutionized Open-Vocabulary Segmentation (OVS) through \textit{promptable concept segmentation}, which grounds pixel predictions in flexible concept prompts. How...
   - 任务设定：开放词汇视觉识别/分割，目标类别或文本提示在训练时未必出现。
   - 方法核心：提示学习或提示生成，重点看文本/视觉 prompt 如何约束定位。
   - 实验结论：可能包含新数据集/基准；适合看评测协议、失败案例和是否能服务 COD。
   - 和我课题的关系：适合拓展到开放词汇、零样本或少标注 COD。
   - 可借鉴点：prompt 设计、类别文本构造、免训练迁移流程；候选 mask 生成、视觉-语言筛选、推理式定位。
   - 可改进点：可改进 prompt 自动生成、负样本约束和 mask 置信度校准。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

46. **AerOSeg: Harnessing SAM for Open-Vocabulary Segmentation in Remote Sensing Images**
   - Source: arXiv, 2025-04-12
   - Authors: Saikat Dutta, Akhil Vasim, Siddhant Gole, Hamid Rezatofighi, Biplab Banerjee
   - Tags: open-vocabulary, SAM, diffusion, remote sensing
   - Links: [paper](http://arxiv.org/abs/2504.09203v1) / [pdf](http://arxiv.org/pdf/2504.09203v1)
   - 论文：AerOSeg: Harnessing SAM for Open-Vocabulary Segmentation in Remote Sensing Images
   - 一句话总结：Image segmentation beyond predefined categories is a key challenge in remote sensing, where novel and unseen classes often emerge during inference. Open-vocabulary image Segmentation addresses these generaliza...
   - 任务设定：开放词汇视觉识别/分割，目标类别或文本提示在训练时未必出现。
   - 方法核心：提示学习或提示生成，重点看文本/视觉 prompt 如何约束定位。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：适合拓展到开放词汇、零样本或少标注 COD。
   - 可借鉴点：prompt 设计、类别文本构造、免训练迁移流程；候选 mask 生成、视觉-语言筛选、推理式定位。
   - 可改进点：可改进 prompt 自动生成、负样本约束和 mask 置信度校准。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

47. **Decomposed Vision-Language Alignment for Fine-Grained Open-Vocabulary Segmentation**
   - Source: arXiv, 2026-05-15
   - Authors: Chenhao Wang, Yingrui Ji, Yu Meng, Yao Zhu
   - Tags: open-vocabulary, VLM/MLLM
   - Links: [paper](http://arxiv.org/abs/2605.15942v1) / [pdf](http://arxiv.org/pdf/2605.15942v1)
   - 论文：Decomposed Vision-Language Alignment for Fine-Grained Open-Vocabulary Segmentation
   - 一句话总结：Open-vocabulary segmentation models often struggle to generalize to unseen combinations of object categories and attributes, because fine-grained descriptions are typically encoded as holistic sentences that e...
   - 任务设定：开放词汇视觉识别/分割，目标类别或文本提示在训练时未必出现。
   - 方法核心：提示学习或提示生成，重点看文本/视觉 prompt 如何约束定位。
   - 实验结论：可能包含新数据集/基准；适合看评测协议、失败案例和是否能服务 COD。
   - 和我课题的关系：适合拓展到开放词汇、零样本或少标注 COD。
   - 可借鉴点：prompt 设计、类别文本构造、免训练迁移流程；候选 mask 生成、视觉-语言筛选、推理式定位。
   - 可改进点：可改进 prompt 自动生成、负样本约束和 mask 置信度校准。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

48. **Making Training-Free Diffusion Segmentors Scale with the Generative Power**
   - Source: arXiv, 2026-03-06
   - Authors: Benyuan Meng, Qianqian Xu, Zitai Wang, Xiaochun Cao, Longtao Huang et al.
   - Tags: training-free, diffusion
   - Links: [paper](http://arxiv.org/abs/2603.06178v3) / [pdf](http://arxiv.org/pdf/2603.06178v3)
   - 论文：Making Training-Free Diffusion Segmentors Scale with the Generative Power
   - 一句话总结：As powerful generative models, text-to-image diffusion models have recently been explored for discriminative tasks. A line of research focuses on adapting a pre-trained diffusion model to semantic segmentation...
   - 任务设定：免训练或少训练迁移设定，重点看 prompt、特征选择和后处理。
   - 方法核心：扩散/生成式建模，可能用于数据合成、先验建模或掩码优化。
   - 实验结论：可能包含新数据集/基准；适合看评测协议、失败案例和是否能服务 COD。
   - 和我课题的关系：适合拓展到开放词汇、零样本或少标注 COD。
   - 可借鉴点：prompt 设计、类别文本构造、免训练迁移流程。
   - 可改进点：可改进 prompt 自动生成、负样本约束和 mask 置信度校准。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

49. **R2AoP: Reliable and Robust Angle of Progression Estimation from Intrapartum Ultrasound**
   - Source: arXiv, 2026-05-20
   - Authors: Yuanhan Wang, Yifei Chen, Beining Wu, Mingxuan Liu, Xiaotian Hu et al.
   - Tags: diffusion, boundary/frequency, depth/geometry
   - Links: [paper](http://arxiv.org/abs/2605.21099v1) / [pdf](http://arxiv.org/pdf/2605.21099v1)
   - 论文：R2AoP: Reliable and Robust Angle of Progression Estimation from Intrapartum Ultrasound
   - 一句话总结：Accurate estimation of the Angle of Progression (AoP) from intrapartum transperineal ultrasound is critical for objective assessment of labor progression, yet remains highly sensitive to imaging noise, boundar...
   - 任务设定：通用计算机视觉任务，先判断是否能迁移到 COD 的感知、定位或分割环节。
   - 方法核心：边界感知建模，适合改善伪装目标轮廓不清的问题。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：可补充 COD 中纹理、边界、几何先验不足的问题。
   - 可借鉴点：边界/频域增强模块；深度或几何先验融合。
   - 可改进点：可结合多尺度语义上下文，避免只强化纹理导致误检。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

50. **VISTA: Variance-Gated Inter-Sequence Test-Time Adaptation for Multi-Sequence MRI Segmentation**
   - Source: arXiv, 2026-05-17
   - Authors: Zhipeng Deng, Jiale Zhou, Wenhan Jiang, Haolin Wang, Xun Lin et al.
   - Tags: boundary/frequency
   - Links: [paper](http://arxiv.org/abs/2605.17433v2) / [pdf](http://arxiv.org/pdf/2605.17433v2)
   - 论文：VISTA: Variance-Gated Inter-Sequence Test-Time Adaptation for Multi-Sequence MRI Segmentation
   - 一句话总结：Deploying multi-sequence magnetic resonance imaging (MRI) segmentation models to new clinical environments is challenging due to variations in scanners and acquisition protocols. Although existing TTA methods...
   - 任务设定：通用计算机视觉任务，先判断是否能迁移到 COD 的感知、定位或分割环节。
   - 方法核心：频域/纹理特征增强，适合处理伪装背景与目标细粒度差异。
   - 实验结论：摘要强调消融、鲁棒性或泛化；适合优先看实验设计和跨域表现。
   - 和我课题的关系：可补充 COD 中纹理、边界、几何先验不足的问题。
   - 可借鉴点：边界/频域增强模块。
   - 可改进点：可结合多尺度语义上下文，避免只强化纹理导致误检。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

51. **The Golden Subspace: Where Efficiency Meets Generalization in Continual Test-Time Adaptation**
   - Source: arXiv, 2026-03-23
   - Authors: Guannan Lai, Da-Wei Zhou, Zhenguo Li, Han-Jia Ye
   - Tags: SAM
   - Links: [paper](http://arxiv.org/abs/2603.21928v1) / [pdf](http://arxiv.org/pdf/2603.21928v1)
   - 论文：The Golden Subspace: Where Efficiency Meets Generalization in Continual Test-Time Adaptation
   - 一句话总结：Continual Test-Time Adaptation (CTTA) aims to enable models to adapt online to unlabeled data streams under distribution shift without accessing source data. Existing CTTA methods face an efficiency-generaliza...
   - 任务设定：基础模型驱动的视觉定位/分割/推理，可用于自动提示生成或 mask 筛选。
   - 方法核心：借助 SAM/基础分割模型产生候选 mask，再做筛选或适配。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：不是 COD 直系论文，但可能提供可迁移的视觉表征、训练策略或评测思路。
   - 可借鉴点：候选 mask 生成、视觉-语言筛选、推理式定位。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

52. **Staying VIGILant: Mitigating Visual Laziness via Counterfactual Visual Alignment in MLLMs**
   - Source: arXiv, 2026-06-24
   - Authors: Xi Xiao, Chen Liu, Chih-Ting Liao, Yunbei Zhang, Qizhen Lan et al.
   - Tags: VLM/MLLM, reasoning, depth/geometry
   - Links: [paper](http://arxiv.org/abs/2606.26387v1) / [pdf](http://arxiv.org/pdf/2606.26387v1)
   - 论文：Staying VIGILant: Mitigating Visual Laziness via Counterfactual Visual Alignment in MLLMs
   - 一句话总结：Multimodal large language models (MLLMs) extend large language models (LLMs) with visual perception, enabling joint reasoning over images and text. Despite inheriting strong reasoning capabilities from LLMs, t...
   - 任务设定：基础模型驱动的视觉定位/分割/推理，可用于自动提示生成或 mask 筛选。
   - 方法核心：反事实建模/拒识机制，用来降低误检或判断目标是否存在。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：可补充 COD 中纹理、边界、几何先验不足的问题。
   - 可借鉴点：候选 mask 生成、视觉-语言筛选、推理式定位；深度或几何先验融合。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

53. **Mind the Heads: Topological Representation Alignment for Multimodal LLMs**
   - Source: arXiv, 2026-06-22
   - Authors: Davide Caffagni, Alberto Compagnoni, Federico Melis, Sara Sarto, Pier Luigi Dovesi et al.
   - Tags: VLM/MLLM, anomaly/OOD
   - Links: [paper](http://arxiv.org/abs/2606.23885v1) / [pdf](http://arxiv.org/pdf/2606.23885v1)
   - 论文：Mind the Heads: Topological Representation Alignment for Multimodal LLMs
   - 一句话总结：Representation alignment has emerged as an effective approach to improve Multimodal Large Language Models (MLLMs) by regularizing their internal representations toward those of an external vision encoder. Howe...
   - 任务设定：基础模型驱动的视觉定位/分割/推理，可用于自动提示生成或 mask 筛选。
   - 方法核心：视觉-语言对齐，把语义文本信息引入检测或分割。
   - 实验结论：可能包含新数据集/基准；适合看评测协议、失败案例和是否能服务 COD。
   - 和我课题的关系：可用于伪装目标的语义描述、环境理解和候选区域判断。
   - 可借鉴点：候选 mask 生成、视觉-语言筛选、推理式定位；跨域鲁棒性、不确定性或异常分数。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

54. **Gen-VCoT: Generative Visual Chain-of-Thought Reasoning via Diffusion-Based RGB Intermediate Representations**
   - Source: arXiv, 2026-06-15
   - Authors: Zhiqiang Zhou, Junliang Dai, Xu ling
   - Tags: SAM, VLM/MLLM, reasoning, diffusion, depth/geometry
   - Links: [paper](http://arxiv.org/abs/2606.16783v1) / [pdf](http://arxiv.org/pdf/2606.16783v1)
   - 论文：Gen-VCoT: Generative Visual Chain-of-Thought Reasoning via Diffusion-Based RGB Intermediate Representations
   - 一句话总结：Multimodal large language models (MLLMs) excel at visual reasoning but rely on text-based chain-of-thought (CoT), lacking interpretable visual intermediates. Existing methods use opaque tokens or external tool...
   - 任务设定：基础模型驱动的视觉定位/分割/推理，可用于自动提示生成或 mask 筛选。
   - 方法核心：扩散/生成式建模，可能用于数据合成、先验建模或掩码优化。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：可补充 COD 中纹理、边界、几何先验不足的问题。
   - 可借鉴点：候选 mask 生成、视觉-语言筛选、推理式定位；深度或几何先验融合。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

55. **THREAD: Trajectory Planning for Hybrid Rigid-Soft Manipulators with Environment-Aware Diffusion**
   - Source: arXiv, 2026-06-19
   - Authors: Shivani Kamtikar, Pranav Asthana, Naveen Kumar Uppalapati, Girish Krishnan, Girish Chowdhary
   - Tags: diffusion, depth/geometry
   - Links: [paper](http://arxiv.org/abs/2606.21792v1) / [pdf](http://arxiv.org/pdf/2606.21792v1)
   - 论文：THREAD: Trajectory Planning for Hybrid Rigid-Soft Manipulators with Environment-Aware Diffusion
   - 一句话总结：Manipulation in confined environments, such as threading a manipulator through narrow apertures, remains a fundamental challenge, especially for conventional rigid robots. Hybrid rigid-soft manipulators offer...
   - 任务设定：通用计算机视觉任务，先判断是否能迁移到 COD 的感知、定位或分割环节。
   - 方法核心：扩散/生成式建模，可能用于数据合成、先验建模或掩码优化。
   - 实验结论：摘要未给出强实验信号；先看实验表格和图 1，再决定是否精读。
   - 和我课题的关系：可补充 COD 中纹理、边界、几何先验不足的问题。
   - 可借鉴点：深度或几何先验融合。
   - 可改进点：可思考是否缺少 COD 场景验证、复杂背景失败分析或轻量化部署。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

56. **ELDiff: When Evidential Learning Meets Text-to-Image Diffusion**
   - Source: arXiv, 2026-06-18
   - Authors: Qingtao Pan, Kai Ye, Zhihao Dou, Bing Ji, Shuo Li
   - Tags: diffusion, low-level
   - Links: [paper](http://arxiv.org/abs/2606.20924v1) / [pdf](http://arxiv.org/pdf/2606.20924v1)
   - 论文：ELDiff: When Evidential Learning Meets Text-to-Image Diffusion
   - 一句话总结：In multi-object text-to-image (T2I) diffusion, ensuring semantic consistency between textual prompts and generated visual content is crucial for image synthesis. However, such consistency constraint is often u...
   - 任务设定：通用计算机视觉任务，先判断是否能迁移到 COD 的感知、定位或分割环节。
   - 方法核心：扩散/生成式建模，可能用于数据合成、先验建模或掩码优化。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：不是 COD 直系论文，但可能提供可迁移的视觉表征、训练策略或评测思路。
   - 可借鉴点：任务建模、损失函数、消融组织方式。
   - 可改进点：可思考是否缺少 COD 场景验证、复杂背景失败分析或轻量化部署。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

57. **Search is All You Need for Few-shot Anomaly Detection**
   - Source: arXiv, 2025-04-16
   - Authors: Qishan Wang, Jia Guo, Shuyong Gao, Haofen Wang, Li Xiong et al.
   - Tags: training-free, SAM, retrieval/prototype, boundary/frequency, anomaly/OOD
   - Links: [paper](http://arxiv.org/abs/2504.11895v2) / [pdf](http://arxiv.org/pdf/2504.11895v2)
   - 论文：Search is All You Need for Few-shot Anomaly Detection
   - 一句话总结：Few-shot anomaly detection (FSAD) has emerged as a crucial yet challenging task in industrial inspection, where normal distribution modeling must be accomplished with only a few normal images. While existing a...
   - 任务设定：免训练或少训练迁移设定，重点看 prompt、特征选择和后处理。
   - 方法核心：提示学习或提示生成，重点看文本/视觉 prompt 如何约束定位。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：适合拓展到开放词汇、零样本或少标注 COD。
   - 可借鉴点：prompt 设计、类别文本构造、免训练迁移流程；候选 mask 生成、视觉-语言筛选、推理式定位；边界/频域增强模块；跨域鲁棒性、不确定性或异常分数。
   - 可改进点：可改进 prompt 自动生成、负样本约束和 mask 置信度校准。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

58. **UniVAD: A Training-free Unified Model for Few-shot Visual Anomaly Detection**
   - Source: arXiv, 2024-12-04
   - Authors: Zhaopeng Gu, Bingke Zhu, Guibo Zhu, Yingying Chen, Ming Tang et al.
   - Tags: training-free, SAM, anomaly/OOD
   - Links: [paper](http://arxiv.org/abs/2412.03342v3) / [pdf](http://arxiv.org/pdf/2412.03342v3)
   - 论文：UniVAD: A Training-free Unified Model for Few-shot Visual Anomaly Detection
   - 一句话总结：Visual Anomaly Detection (VAD) aims to identify abnormal samples in images that deviate from normal patterns, covering multiple domains, including industrial, logical, and medical fields. Due to the domain gap...
   - 任务设定：免训练或少训练迁移设定，重点看 prompt、特征选择和后处理。
   - 方法核心：借助 SAM/基础分割模型产生候选 mask，再做筛选或适配。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：适合拓展到开放词汇、零样本或少标注 COD。
   - 可借鉴点：prompt 设计、类别文本构造、免训练迁移流程；候选 mask 生成、视觉-语言筛选、推理式定位；跨域鲁棒性、不确定性或异常分数。
   - 可改进点：可改进 prompt 自动生成、负样本约束和 mask 置信度校准。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

59. **HD-TTA: Hypothesis-Driven Test-Time Adaptation for Safer Brain Tumor Segmentation**
   - Source: arXiv, 2026-02-23
   - Authors: Kartik Jhawar, Lipo Wang
   - Tags: SAM, diffusion, depth/geometry
   - Links: [paper](http://arxiv.org/abs/2602.19454v1) / [pdf](http://arxiv.org/pdf/2602.19454v1)
   - 论文：HD-TTA: Hypothesis-Driven Test-Time Adaptation for Safer Brain Tumor Segmentation
   - 一句话总结：Standard Test-Time Adaptation (TTA) methods typically treat inference as a blind optimization task, applying generic objectives to all or filtered test samples. In safety-critical medical segmentation, this la...
   - 任务设定：基础模型驱动的视觉定位/分割/推理，可用于自动提示生成或 mask 筛选。
   - 方法核心：借助 SAM/基础分割模型产生候选 mask，再做筛选或适配。
   - 实验结论：摘要声称优于已有方法；精读时重点核对对比基线、数据集覆盖和消融是否充分。
   - 和我课题的关系：可补充 COD 中纹理、边界、几何先验不足的问题。
   - 可借鉴点：候选 mask 生成、视觉-语言筛选、推理式定位；深度或几何先验融合。
   - 可改进点：可改进细粒度目标绑定、误检拒识和小目标/低对比区域筛选。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

60. **Efficient Encoder-Free Fourier-based 3D Large Multimodal Model**
   - Source: CVPR 2026, 2026
   - Authors: Guofeng Mei, Wei Lin, Luigi Riz, Yujiao Wu, Yiming Wang et al.
   - Tags: depth/geometry
   - Links: [paper](https://openaccess.thecvf.com/content/CVPR2026/html/Mei_Efficient_Encoder-Free_Fourier-based_3D_Large_Multimodal_Model_CVPR_2026_paper.html) / [pdf](https://openaccess.thecvf.com/content/CVPR2026/papers/Mei_Efficient_Encoder-Free_Fourier-based_3D_Large_Multimodal_Model_CVPR_2026_paper.pdf)
   - 论文：Efficient Encoder-Free Fourier-based 3D Large Multimodal Model
   - 一句话总结：CVF OpenAccess paper. Open the paper page for full abstract and method details.
   - 任务设定：通用计算机视觉任务，先判断是否能迁移到 COD 的感知、定位或分割环节。
   - 方法核心：视觉-语言对齐，把语义文本信息引入检测或分割。
   - 实验结论：当前来源只提供标题级信息；需要打开论文页确认数据集、指标和消融。
   - 和我课题的关系：可补充 COD 中纹理、边界、几何先验不足的问题。
   - 可借鉴点：深度或几何先验融合。
   - 可改进点：可思考是否缺少 COD 场景验证、复杂背景失败分析或轻量化部署。
   - 是否值得精读：建议精读：高质量来源或方法迁移价值较高。

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

- arXiv API: recent preprints from COD, weak/salient/transparent objects, VLM, segmentation, diffusion, adaptation, medical and remote-sensing queries.
- CVF OpenAccess: CVPR/ECCV/ICCV/WACV title-level scan.
- Semantic Scholar Graph API: broad high-quality venue and topic search when rate limits allow.
- Crossref API: TPAMI, IJCV, TIP, TMM, TCSVT, Pattern Recognition, CVIU, TGRS, ISPRS JPRS, Medical Image Analysis.

说明：自动简介是基于题名、摘要和来源的初筛笔记，不等同于阅读全文后的结论；精读时建议再核对 method、experiment 和 limitation。
