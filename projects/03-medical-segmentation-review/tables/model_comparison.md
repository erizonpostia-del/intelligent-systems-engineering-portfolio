# Model comparison — context, not ranking

| Model | Year / status | Primary domain | Adaptation type | Prompt type | Training / evaluation data | Metrics reported | Evaluation setting | Main limitation | Source |
|---|---|---|---|---|---|---|---|---|---|
| U-Net | 2015, published | Biomedical microscopy | Task-specific training | None | ISBI biomedical tasks | Challenge task metrics | Study-specific | Requires task data and design choices | [R1] |
| nnU-Net | 2021, published | Biomedical segmentation | Self-configuring task-specific pipeline | None | 23 public challenge datasets | Dataset-specific challenge metrics | Multi-dataset benchmark | Not a zero-shot foundation model | [R2] |
| TransUNet | 2021, preprint | Medical segmentation | Transformer--U-Net hybrid | None | Multi-organ and cardiac tasks | Paper-specific | Task-specific experiments | Values are not directly comparable across tasks | [R3] |
| SAM | 2023, ICCV | Natural images | Natural-image pretraining | Point, box, mask | SA-1B; broad zero-shot evaluation | Task-dependent | Promptable / zero-shot | Domain and prompt mismatch can limit transfer | [R5] |
| Deng et al. | 2023, preprint | Digital pathology WSI | Direct zero-shot assessment | Clicks / boxes | Tumour, tissue, nuclei tasks | Paper-specific | Per-study pathology evaluation | Dense instances remained difficult | [R6] |
| SAM-Path | 2023, preprint | Digital pathology semantic segmentation | Fine-tuning + class prompts + pathology encoder | Trainable class prompts | BCSS, CRAG | Dice, IoU | In-paper comparison and ablation | Preprint; task-specific semantic setup | [R7] |
| MedSAM | 2024, Nature Communications | Multi-modal medical imaging | Medical-data fine-tuning | Mainly boxes | 1,570,263 pairs; 10 modalities | Study metrics | 86 internal, 60 external tasks | 2D promptable design; protocol-specific results | [R8] |
| Medical SAM Adapter | 2023, preprint | Medical imaging | Parameter-efficient adapter | Prompt-conditioned adapter | 17 tasks | Paper-specific | In-paper benchmark | Preprint; claims depend on its setup | [R9] |

No bold “best” label is used. Dataset, task, prompt protocol, split, and aggregation must be checked before comparing a value from any two rows.

