# Technical review: foundation models for medical image segmentation

## 1. Scope and review questions

This document is a narrative technical review. It asks how promptable foundation models change the segmentation workflow, where direct transfer fails, and what evidence supports medical or pathology-oriented adaptation. It is not a systematic review, meta-analysis, clinical recommendation, or report of experiments performed in this repository.

## 2. From task-specific segmentation to foundation models

U-Net couples a context-capturing contracting path with an expanding path for localization; skip connections make this especially useful for dense biomedical predictions [R1]. nnU-Net shifts attention from inventing a single architecture to configuring preprocessing, network geometry, training, and post-processing to the dataset and hardware [R2]. Transformer-based systems such as TransUNet add global self-attention while retaining a decoder for fine localization [R3]; Swin-Unet is a pure Transformer U-shaped alternative [R4].

These methods are background, not a flat performance ladder. A 3D multi-organ CT task and a 2D pathology-tile task differ before any model is chosen. Foundation models alter this landscape by supplying a large pretrained representation and a target-specification interface, rather than a ready-made clinical solution.

## 3. What SAM changes

SAM consists of an image encoder, prompt encoder, and lightweight mask decoder [R5]. Sparse prompts include foreground/background points and boxes; a dense mask can also be used as a prompt. The design permits an operator, an upstream detector, or a scripted policy to specify the desired region. Its SA-1B training resource contains more than one billion masks from 11 million images [R5].

The key distinction is between being *promptable* and being *fully automatic*. A prompt helps disambiguate the target, but it can introduce user variability and may not fit semantic tasks whose labels are fixed classes rather than user-selected instances. Zero-shot transfer is consequently an empirical question tied to target morphology, image distribution, and prompting protocol.

## 4. Why medical images are different

Medical images are formed by different physical and biological processes. CT and MRI can be volumetric, ultrasound is affected by speckle and operator-dependent acquisition, and digital pathology spans tissue architecture across very large whole-slide images. Many targets are grayscale, low contrast, small relative to the field of view, or have fuzzy and annotator-dependent borders. Scanner, staining, protocol, and institution changes can shift the data distribution.

These differences interact. A 2D slice-wise method can receive 3D data but may lose through-plane context; a good overlap score on a large organ can coexist with poor detection of small lesions. Clinical cost also changes the question: a false negative, false positive, boundary displacement, and a failure to flag uncertainty do not have the same implications. This is why a natural-image pretrained model should be assessed per task rather than described as simply good or bad on “medical images.”

## 5. Pathology-oriented adaptation

Deng et al. directly evaluated zero-shot SAM on WSI pathology tasks: tumour, non-tumour tissue, and cell nuclei segmentation [R6]. They reported comparatively strong results for large connected structures but inconsistent dense-instance segmentation even with 20 clicks or boxes per image. The paper identifies resolution, multi-scale structure, prompt selection, and fine-tuning as limitations. This is direct evidence about its setting, not a general proof that SAM fails in pathology.

SAM-Path is distinct from Deng et al. Zhang et al. adapt SAM to semantic pathology segmentation without manual input prompts. Their method replaces manual prompting with trainable class prompts and combines SAM image features with a pathology foundation-model encoder [R7]. The authors evaluate on BCSS and CRAG. Against their vanilla-SAM-with-post-processing setup, the fine-tuned SAM result on CRAG is reported as a relative 27.52% Dice and 71.63% IoU improvement; adding the pathology encoder yields additional relative gains reported separately for BCSS and CRAG [R7]. These are ablation-context values, not portable model rankings.

## 6. MedSAM

MedSAM is the published 2024 Nature Communications study by Ma et al. [R8], not a generic label for any medical SAM fine-tune. It adapts SAM into a promptable 2D medical segmentation model, using bounding boxes as the main target specification. The authors describe a curated set of 1,570,263 image--mask pairs across ten modalities and more than 30 cancer types, and report 86 internal and 60 external validation tasks [R8]. It processes 3D data as 2D slices, a pragmatic design choice that does not remove the need to evaluate volumetric consistency.

The study supports the claim that medical-data adaptation can improve performance under its validation design. It does not license a universal preference for MedSAM: target definitions, prompt quality, images, and specialist baselines matter. Its official repository is included only as an implementation source, not as evidence that this repository has run the software [R13].

## 7. Adaptation strategies

Full fine-tuning updates the pretrained model for a downstream task; it is flexible but data- and compute-intensive. Parameter-efficient approaches keep much of the backbone fixed and train adapters, low-rank components, or prompt-like parameters. Medical SAM Adapter, for example, reports a medical adaptation module and 3D-aware component while updating a limited parameter subset [R9].

Prompt tuning changes learned prompt representations; prompt engineering instead selects or structures input points, boxes, or masks. Domain adaptation explicitly targets a specified source-to-target shift, while domain generalization seeks performance on unseen shifts without training on their target data. These terms should be used according to the available data and parameters, not as interchangeable praise for a method.

## 8. Evaluation

Let prediction and reference masks be \(P\) and \(G\). Dice and IoU quantify set overlap; surface metrics assess geometric discrepancy. A sound report states the unit of analysis (slice, volume, lesion, or case), aggregation rule, empty-mask convention, class treatment, image dimensionality, prompt protocol, and whether validation is external. Taha and Hanbury catalog how metric properties affect selection [R10]. Metrics Reloaded further argues for problem-aware selection and warns that small structures, class imbalance, non-independent cases, and undefined corner cases can invalidate simplistic comparisons [R11].

Therefore, Dice alone should not certify a model. Pair overlap with surface metrics where boundaries matter, precision/recall where false-positive and false-negative trade-offs matter, and robustness checks when site or protocol shift matters. Efficiency and annotation burden are additional workflow properties, not substitutes for segmentation validity.

## 9. What the literature supports

The reviewed evidence supports four bounded conclusions. First, promptability makes target specification an explicit part of segmentation. Second, direct transfer from natural-image pretraining can be limited by pathology and medical-domain characteristics. Third, pathology-specific and multi-modal medical adaptation are different responses to different task definitions. Fourth, numerical comparisons are meaningful only with their evaluation context. It does not support universal claims about a single best foundation model or any performance result for this repository.

## 10. Open questions

Important open questions include robust 3D adaptation, cross-modal and cross-institution generalization, prompt robustness, uncertainty communication, calibration, annotation efficiency, reproducible preprocessing, and deployment validation. A future project should evaluate one of these questions with a fixed public dataset and protocol rather than expanding the literature claims.
