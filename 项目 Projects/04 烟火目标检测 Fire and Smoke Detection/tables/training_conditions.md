# Training conditions

| Condition | Model | Initialization | Dataset scope | Epochs | Image size | Batch | Seed | Resume | Evaluation | Run count | Comparability |
|---|---|---|---|---:|---:|---:|---:|---|---|---:|---|
| Standard | YOLO11s | Started from `yolo11s.pt` | Archived five-class clean dataset | 50 | 640 | 16 | 0 | No | Validation | 1 | Partially controlled; initialization differs. |
| From3Class | YOLO11s | Continued from an archived three-class checkpoint | Archived five-class clean dataset | 50 | 640 | 16 | 0 | Yes | Validation | 1 | Partially controlled; resume state differs. |

Both conditions share the documented requested epoch count, image size, batch size, seed, and archived dataset reference. The evidence does not support a strict controlled-ablation interpretation or repeated-run claim.
