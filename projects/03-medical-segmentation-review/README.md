# Medical Image Segmentation with Foundation Models

> A literature-based technical review of foundation models for medical image segmentation, with a focused discussion of SAM, digital-pathology adaptation, MedSAM, prompting, domain shift, and evaluation.

**Quick visual walkthrough:** [Evidence-led project overview](OVERVIEW.md)

## Project overview

This repository is a technical review, not an experimental report. I organized it around a practical question: which parts of a promptable natural-image foundation model transfer to medical imaging, and which parts require domain-specific adaptation? It contains my synthesis, original schematics, comparison tables, and a bounded inference plan—not patient data, checkpoints, training, fine-tuning, or project-computed segmentation metrics.

Medical segmentation is not a single visual task. A model may outline an organ on CT, a lesion on MRI, a nucleus in microscopy, or tissue regions in whole-slide pathology. These settings differ in image formation, dimensionality, target scale, annotation conventions, and consequences of error. A score from one study is not a universal model ranking.

## Review questions

1. How did task-specific U-Net-style pipelines, automated configuration, and Transformer segmentation set the context for foundation models?
2. What does SAM add through promptable segmentation and zero-shot transfer?
3. Why do modality, scale, and annotation differences create a domain shift from natural images to medical data?
4. How do SAM-Path and MedSAM address different versions of this problem?
5. What makes a segmentation evaluation interpretable rather than a collection of incomparable scores?

## Model landscape

![Original model landscape](figures/segmentation_model_landscape.svg)

U-Net established the encoder--decoder and skip-connection pattern for biomedical localization [R1]. nnU-Net showed the importance of data-aware configuration [R2], while TransUNet brought global-context modeling into this family [R3]. These are context, not direct baselines for every foundation-model paper.

SAM reframes segmentation as a promptable task. An image encoder, prompt encoder, and mask decoder combine to predict masks. Point, box, and mask prompts make target specification explicit, enabling interactive use and zero-shot transfer but not removing the need to test a new domain [R5]. SA-1B contains over one billion masks from 11 million natural images [R5].

## Key technical observations

![Original SAM-to-medical adaptation map](figures/sam_to_medical_adaptation.svg)

The main transfer problem is not simply “medical images are harder.” Medical modalities can be grayscale or multi-channel; CT and MRI are commonly volumetric; pathology images are extremely large and multi-scale; and targets may be small, weakly bounded, or annotation-dependent. Scanner, staining, acquisition protocol, and institution can also alter image appearance. A useful review therefore distinguishes direct zero-shot evaluation, full fine-tuning, parameter-efficient adaptation, prompt tuning, domain adaptation, and domain generalization rather than calling all of them “adaptation.”

Deng et al. evaluated zero-shot SAM on whole-slide pathology tasks including tumour, non-tumour tissue, and nuclei segmentation [R6]. Their paper reports better behavior for large connected objects than dense instances; its “20 prompts” means 20 clicks or boxes per image. SAM-Path is a different study: Zhang et al. adapt SAM for semantic pathology segmentation using trainable class prompts and a pathology encoder, evaluated on BCSS and CRAG [R7]. Its reported gains are study-specific and not a cross-dataset leaderboard.

MedSAM addresses a broader multi-modal medical setting. Ma et al. report fine-tuning a SAM-based promptable 2D model on 1,570,263 image--mask pairs across ten modalities and more than 30 cancer types, with 86 internal and 60 external validation tasks [R8]. The reported results remain tied to its curation, box-prompt protocol, model version, and validation design; they do not establish universal preference for every target or workflow.

## Evaluation considerations

![Original evaluation metric map](figures/evaluation_metric_map.svg)

Dice and IoU measure mask overlap; precision and recall expose different false-positive and false-negative behavior; HD/HD95 and ASD/ASSD characterize surface discrepancy. None is sufficient alone. Small structures can make overlap unstable, empty masks require a stated convention, and a low average boundary error can hide a clinically important local miss. Reported metrics also depend on 2D-versus-3D evaluation, per-case versus pooled aggregation, label definitions, and whether the test data are external. The evaluation guide in [tables/evaluation_metrics.md](tables/evaluation_metrics.md) gives formulas and reporting cautions grounded in metric literature [R10, R11].

## Evidence and citation policy

Every substantive technical claim in this review links to at least one primary paper, publisher page, preprint record, or official repository. The compact claim table records the public wording and its qualification: [tables/claim_evidence_summary.md](tables/claim_evidence_summary.md). I use reported numerical values only with their study setting. No third-party paper figure, screenshot, PDF, or dataset is included here. The three diagrams in `figures/` are original conceptual drawings, not redrawn paper figures.

## Limitations

This is a narrative, scoped review rather than a PRISMA systematic review or a meta-analysis. It does not reproduce published results. It does not compare Dice values across papers as though they were obtained under a common protocol. Some cited adaptation work remains a preprint; that status is stated in the comparison table. The literature set is deliberately selective (14 sources), favoring foundational methods, direct pathology evidence, MedSAM, adaptation terminology, and metric guidance.

## Future reproducibility plan

The next valid step is a small, transparent inference study, not retroactive performance claims. [docs/reproducibility_plan.md](docs/reproducibility_plan.md) requires a public licensed dataset, documented weights, fixed prompts and preprocessing, and metrics only when matching ground truth is available.

## Repository guide

- [Technical review](docs/technical_review.md) — focused evidence-led discussion.
- [Literature scope](docs/literature_scope.md) — inclusion logic and source status.
- [Model comparison](tables/model_comparison.md) — contextual comparison, not ranking.
- [Evaluation metrics](tables/evaluation_metrics.md) — definitions and reporting rules.

The repository intentionally has no license file. The writing and original diagrams are my work; cited literature and linked code remain subject to their own terms.
