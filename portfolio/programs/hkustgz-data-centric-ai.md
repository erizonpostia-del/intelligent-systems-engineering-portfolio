# HKUST (Guangzhou) — MSc in Data-Centric Artificial Intelligence Technology

**Jiang ZhengMeng** | Automation and Systems Engineering, Macau University of Science and Technology

This is the closest programme-facing guide to my work at the intersection of **data quality, evaluation protocols, and applied machine learning**. It prioritises inspectable evidence over claims about achieving a benchmark score.

## Suggested reading order

| Priority | Evidence | Why it matters |
|---|---|---|
| **1** | [Fire & Smoke Detection — visual overview](../../projects/04-fire-smoke-detection/OVERVIEW.md) · [Data-governance notes](../../projects/04-fire-smoke-detection/docs/data_governance.md) · [Attribution](../../projects/04-fire-smoke-detection/docs/contribution_scope.md) | Source-media registration, duplicate control, annotation review, data-split concerns, per-class failure analysis and traceable development records. |
| **2** | [Machine Learning Evaluation — visual overview](../../projects/02-ml-evaluation/OVERVIEW.md) · [Nested CV](../../projects/02-ml-evaluation/src/nested_cv_demo.py) | Leakage-aware scaling, model selection, held-out evaluation and uncertainty from repeated cross-validation. |
| **3** | [Medical Segmentation Review — visual overview](../../projects/03-medical-segmentation-review/OVERVIEW.md) · [Technical review](../../projects/03-medical-segmentation-review/docs/technical_review.md) | Domain shift and evaluation design: an example of assessing when different datasets and application conditions invalidate superficial comparisons. |

## Why data-centric AI

During an industrial forest-monitoring vision internship, model quality was inseparable from the quality of the input media, annotations, class definitions and validation design. In the public record, development checkpoint rankings depend on the chosen metrics; difficult smoke targets are not resolved simply by increasing image resolution. That experience made **data governance, error diagnosis and evaluation design** central to my understanding of applied AI.

I want to deepen data engineering, robust learning, dataset shift analysis and scalable ML-system design. My longer-term goal is to build AI systems that can be evaluated and maintained under actual data and deployment constraints.

## Results and attribution boundaries

- The public record concerns **development and validation**, not an independent deployment benchmark or verified production performance.
- The archived industrial work involved a shared server; the [contribution scope](../../projects/04-fire-smoke-detection/docs/contribution_scope.md) distinguishes confirmed records from actions not individually attributable.
- Model checkpoints and datasets from different experimental settings must not be compared as if they were interchangeable.
- The Ridge/Lasso work uses **synthetic data**; the medical segmentation project is a **literature review**, not a trained medical model.
- Commercial-scale data infrastructure and deployed data-centric AI services are **future learning goals**, not current achievements.

[AI Innovation / Deployment track](../tracks/ai-innovation-deployment.md) · [All programme guides](../README.md) · [Portfolio homepage](../../README.md)
