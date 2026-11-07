# University of Macau — MSc in Artificial Intelligence

**Jiang ZhengMeng** | BSc in Automation and Systems Engineering, Macau University of Science and Technology

This path centres on **perception, careful machine-learning evaluation, and the transition from model behaviour to engineering decisions**. My projects cover different domains, but each makes the limits of its evidence visible.

## Suggested reading order

| Read | Inspect | Evidence and relevance |
|---|---|---|
| **04 — Fire & Smoke Detection** | [Visual overview](../../projects/04-fire-smoke-detection/OVERVIEW.md) · [Per-class results](../../projects/04-fire-smoke-detection/results/two_class_per_class_metrics.csv) | Applied computer vision, data quality and why fire/smoke errors cannot be judged by aggregate validation mAP alone. |
| **02 — Machine Learning Evaluation** | [Visual overview](../../projects/02-ml-evaluation/OVERVIEW.md) · [Nested-CV workflow](../../projects/02-ml-evaluation/src/nested_cv_demo.py) | Train-only scaling, held-out testing, model-selection discipline and uncertainty across folds. |
| **03 — Medical Segmentation Review** | [Visual overview](../../projects/03-medical-segmentation-review/OVERVIEW.md) · [Technical review](../../projects/03-medical-segmentation-review/docs/technical_review.md) | Literature-grounded comparison of SAM, SAM-Path and MedSAM, including domain shift and evaluation conditions. |

## Why Artificial Intelligence

Studying image processing and machine learning showed me that applying a model responsibly requires more than training code. During an industrial fire/smoke detection internship, questions around label quality, small targets and validation metrics became concrete engineering constraints. A separate literature review of medical segmentation foundation models reinforced the same point: conclusions depend on the task and evaluation setting.

UM's AI programme learning outcomes stress **computational problem formulation, system implementation and evaluation, and responsible application**. I hope to deepen mathematical foundations, advanced deep learning, model robustness and the integration of AI with real systems.

## Scope and gaps

- The medical segmentation work is a **literature review**, not medical-data training, fine-tuning or a clinical benchmark.
- Industrial vision figures are **validation-stage** and include archived shared-server work with explicitly limited attribution; no deployment success is claimed.
- Regression evaluation uses **synthetic data**; different projects and datasets are **not** directly compared as a single benchmark.
- The page does not claim completed foundation-model research, an original large language model or a deployed AI product.

[UM programme list](https://www.fst.um.edu.mo/academics/programs/) · [UM postgraduate learning outcomes](https://www.fst.um.edu.mo/academics/current-students/graduate-students/pilos/) · [AI for Science / Health track](../tracks/ai-for-science-health.md) · [Portfolio homepage](../../README.md)
