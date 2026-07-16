# Literature scope and method

## Scope

This is a focused narrative technical review, not a systematic review, a PRISMA review, or a meta-analysis. It covers the conceptual move from task-specific medical segmentation to promptable foundation models, then narrows to three evidence anchors: SAM, zero-shot digital pathology evidence, and two forms of medical/pathology adaptation (SAM-Path and MedSAM).

## Source selection

I retained 14 high-relevance sources: original or archival method papers for U-Net, nnU-Net, TransUNet, Swin-Unet, and SAM; direct primary papers for Deng et al., SAM-Path, MedSAM, and Medical SAM Adapter; two evaluation references; and two official source-code repositories. Publisher, conference, arXiv, PubMed/PMC, and official repository pages were checked on 2026-07-16. The bibliography distinguishes preprints from journal and conference publications.

## Citation key

| Key | Bibliography entry |
|---|---|
| R1--R4 | U-Net; nnU-Net; TransUNet; Swin-Unet |
| R5 | Segment Anything (Kirillov et al., ICCV 2023) |
| R6 | Deng et al., *SAM for Digital Pathology* (arXiv:2304.04155) |
| R7 | Zhang et al., *SAM-Path* (arXiv:2307.09570) |
| R8 | Ma et al., *Segment anything in medical images* (Nature Communications, 2024) |
| R9 | Wu et al., *Medical SAM Adapter* (arXiv:2304.12620) |
| R10--R11 | Taha & Hanbury; Metrics Reloaded |
| R12--R13 | Official SAM and MedSAM repositories |
| R14 | Medical Segmentation Decathlon |

## Exclusions

I excluded course submissions, personal records, local path inventories, paper PDFs, paper screenshots, and figures copied from publications. I also excluded numbers whose dataset, prompt, baseline, or split could not be stated in one sentence. The old candidate chart of SAM-Path performance was removed because it did not preserve enough experimental context for safe public reuse.

## Interpretation rules

“Fine-tuning” means updating model parameters on a downstream dataset. “Parameter-efficient adaptation” updates a limited adaptation component rather than the whole model. “Domain adaptation” assumes a defined source-to-target shift, usually with some target-domain access; “domain generalization” seeks robustness to unseen domains. “Prompt engineering” changes the task input, not necessarily model parameters. “Zero-shot” means applying a model without task-specific parameter updates under the paper’s stated protocol.

Reported scores are never treated as this project’s results. Cross-paper values are not ranked because modality, task definition, label protocol, split, prompt, and aggregation may differ.
