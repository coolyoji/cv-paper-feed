# Supplemental Paper Search Report - 2026-07-28

Query cluster: `safety-critical perception multimodal hazard grounding missing degraded modality OOD selective prediction video anticipation UAV tiny object fire smoke RGB-T`

Year range: 2024-2026

Maximum results per source: 10

## Source Results

### Crossref (10 discovery records)

Crossref returned a mixture of UAV, fire/smoke, and cross-modal records, including an SSRN UAV-guided detector, *GLAFC-YOLO*, an ICICAT fire/smoke paper, *YOLOv7-FIRE*, *LFS-YOLO*, an RGB-T cross-modal Mamba record, and several unrelated or weak-venue UAV records. These records were retained only as discovery metadata. None was promoted from title matching because venue quality, abstract evidence, or complete full text was insufficient for today's queue.

### Semantic Scholar (0 papers)

Source error: rate limited during the supplemental query. The affected clusters remain in the cached-candidate and next-run search plan.

### OpenAlex (0 papers)

Source error: gateway timeout (`504`).

### arXiv (0 papers)

Source error: request timed out. This was treated as a degraded source, not evidence that no relevant preprints exist.

### OpenReview (0 papers)

Source error: the OpenReview client is not installed in the paper-search environment.

### DBLP (0 papers)

Source error: the upstream request returned `500`.

## Independent Primary-Source Verification

Because the aggregator run was degraded, candidate screening continued through official CVF, IEEE, Elsevier, and publisher full texts plus the project's cached pool. Every selected paper was checked beyond the abstract, including its complete method, numbered equations, implementation details, main experiments, ablations, qualitative evidence, and stated limitations. The five PDFs passed local text and visual preflight checks.

The final non-duplicate deep-reading queue is:

1. *Quantifying and Communicating Uncertainty in SAR-Based Flood Mapping via Density-Aware Neural Networks and Conformal Risk Control* (IEEE TGRS 2026).
2. *Slot-BERT: Self-supervised Object Discovery in Surgical Video* (Medical Image Analysis 2026).
3. *Multimodal Learning on Low-Quality Data with Conformal Predictive Self-Calibration* (CVPR 2026).
4. *Enhanced OoD Detection through Cross-Modal Alignment of Multi-Modal Representations* (CVPR 2025).
5. *SafeDrive: Fine-Grained Safety Reasoning for End-to-End Driving in a Sparse World* (CVPR 2026).

This queue covers conformal risk control, temporal object-centric discovery, reliability-aware multimodal learning, multimodal OOD geometry, and fine-grained safety reasoning. No direct COD paper was forced into the five; each paper instead supplies a distinct transferable hypothesis for weak-evidence perception.

## Dedicated UAV and Fire Monitoring

Two formally published candidates were independently verified and surfaced in the daily targeted sections without displacing the five deep reads:

- *Detection-Friendly Nonuniformity Correction: A Union Framework for Infrared UAV Target Detection* (CVPR 2025) anchors degraded thermal sensing and tiny-target feature preservation.
- *AusSmoke meets MultiNatSmoke: a fully-labelled diverse smoke segmentation dataset* (WACV 2026) anchors visible-smoke segmentation, hard-background false alarms, and multimodal fire monitoring.

Additional full-text-audited candidates retained for future runs include PURA (CVPR 2025), Event-based Tiny Object Detection (ICCV 2025), SET (CVPR 2025), SimMLM (ICCV 2025), Caltech Aerial RGB-Thermal (ECCV 2024), and OpenRSS (ECCV 2024). Their inclusion in a future top-five queue remains contingent on daily non-duplication and comparative method strength.
