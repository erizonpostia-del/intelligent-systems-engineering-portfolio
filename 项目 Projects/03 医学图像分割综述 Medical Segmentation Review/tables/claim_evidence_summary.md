# Claim--evidence summary

| Public claim | Primary source | Support | Qualification |
|---|---|---|---|
| SAM is a promptable segmentation model using point, box, or mask inputs. | Kirillov et al. [R5] | Direct | Zero-shot transfer is a design goal, not a guarantee for every medical domain. |
| SA-1B contains over 1B masks on 11M images. | Kirillov et al. [R5] | Direct | The data source is natural imagery. |
| In Deng et al., zero-shot SAM was more successful on large connected pathology objects than dense instances. | Deng et al. [R6] | Direct | Applies to the reported WSI tasks and prompting setup. |
| “20 prompts” in Deng et al. means 20 clicks or boxes per image. | Deng et al. [R6] | Direct | It is a paper-specific evaluation observation. |
| SAM-Path uses trainable class prompts and a pathology encoder for pathology semantic segmentation. | Zhang et al. [R7] | Direct | Preprint; evaluated on BCSS and CRAG. |
| MedSAM reports 1,570,263 image--mask pairs, 10 modalities, 86 internal and 60 external tasks. | Ma et al. [R8] | Direct | Values belong to the Nature Communications paper and its protocol. |
| Overlap and surface metrics answer different evaluation questions. | Taha & Hanbury [R10]; Maier-Hein et al. [R11] | Direct | Metric choice and aggregation must follow the biomedical question. |

