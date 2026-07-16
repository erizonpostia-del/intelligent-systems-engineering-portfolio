# Fire and Smoke Detection under Different YOLO11 Training Conditions

*An audited comparison of archived YOLO11 validation runs in a five-class forest-monitoring setting.*

## Project overview

This repository is an evidence-led reconstruction of archived object-detection experiments. Its central interest is fire and smoke detection in a forest-monitoring context, while `animal`, `person`, and `vehicle` were included as additional scene categories. The resulting task is therefore a five-class detection setting, rather than a binary fire-versus-smoke study or an operational fire-warning system.

The public materials were rebuilt from archived training records after an audit of the run configurations and metric CSV files. They intentionally contain no dataset, image, label, video, model weight, training environment, or original training source code. The archived Python source was reported as binary-contaminated and no trusted clean backup was available. The only code here, [`src/build_figures.py`](src/build_figures.py), regenerates figures from the audited public CSV files; it does not train, evaluate, or run a YOLO model.

## Experimental question

> Under the archived training setup, how did a standard YOLO11s initialization compare with continued training from a three-class checkpoint after moving to a five-class dataset?

This question is deliberately narrow. The evidence supports a **partially controlled, single-run archived comparison**, not a universal ranking of models. Both conditions requested 50 epochs with image size 640, batch size 16, seed 0, and the same archived five-class dataset path. The Standard condition started from `yolo11s.pt`; the From3Class condition continued from an archived three-class checkpoint. The differing initialization and resume state prevent a strict controlled-ablation claim.

I focused on this comparison because it captures a practical transfer question: whether a checkpoint first trained on a narrower three-class task could provide a useful initialization after the dataset expanded to five classes.

## Dataset scope and governance

The archived clean dataset contains 22,899 images and 22,899 matching YOLO label files: 16,459 training, 2,002 validation, and 4,438 held-out images. The classes are `fire`, `smoke`, `animal`, `person`, and `vehicle`.

The held-out split exists, but no independently audited evaluation record for it was found. All reported values in this repository come from archived configurations marked `split: val`. Data are not released because source licenses, merged-data provenance, redistribution rights, and privacy review are incomplete. In particular, person and vehicle imagery may contain faces, license plates, or surveillance contexts. See [data governance](docs/data_governance.md) for the full boundary.

## Training conditions

The archived configuration evidence points to YOLO11. The sanitized comparison conditions are in [results/training_conditions.csv](results/training_conditions.csv) and summarized in [tables/training_conditions.md](tables/training_conditions.md). Environment versions, hardware details, and an independently verified source-code revision were not recoverable from the audited evidence.

## Audited validation results

The main comparison uses a pre-declared selection rule: **for each condition, report the epoch with the highest archived validation mAP50-95**. This avoids mixing the strongest mAP50 value from one epoch with the strongest mAP50-95 value from another. The two maxima occur at different epochs for both five-class conditions, so both rules are retained in [validation_best_metrics.csv](results/validation_best_metrics.csv).

| Condition | mAP50-95-selected epoch | Precision | Recall | Validation mAP50 | Validation mAP50-95 |
|---|---:|---:|---:|---:|---:|
| Standard | 40 | 0.58295 | 0.53123 | 0.53969 | 0.31296 |
| From3Class | 40 | 0.63734 | 0.53157 | 0.56365 | 0.32864 |

For this selection rule, the archived From3Class run records higher validation mAP50 and mAP50-95. The recall difference is small, and the experiment contains only one archived run per condition. I therefore treat the result as evidence that the initialization strategy was promising in this setup, not as proof of a generally superior training procedure.

![Validation mAP comparison](figures/validation_map_comparison.png)

![Validation precision and recall comparison](figures/precision_recall_comparison.png)

The final complete training epoch tells a different, complementary story. At epoch 50, Standard records precision 0.62883, recall 0.50296, mAP50 0.53512, and mAP50-95 0.30997. From3Class records precision 0.63911, recall 0.52584, mAP50 0.54876, and mAP50-95 0.31786. Both best-epoch and final-epoch values are published in [tables/validation_results.md](tables/validation_results.md); this repository does not present only the more favorable checkpoint rows.

![Standard training progression](figures/training_progression_standard.png)

![From3Class training progression](figures/training_progression_from3class.png)

## Interpretation boundary

The results are archived validation results from one recorded run per condition. No repeated-seed summary, uncertainty interval, or independent held-out-split evaluation is available in the audited materials. The appropriate interpretation is therefore limited to the observed records: under this archived setup, the From3Class condition had higher recorded validation mAP values at the documented mAP50-95 selection epoch, while precision and recall should still be read as a trade-off rather than a blanket win.

Reconstructing the experiment changed how I think about model comparison. A small metric improvement is difficult to interpret when the evaluation protocol, repeated runs, environment versions, and data provenance are incomplete. For the public version, I chose to preserve that uncertainty rather than present the strongest available number without context.

## Reproducibility boundary

The public CSV files preserve only audited aggregate and per-epoch metrics. They can be checked directly and used to rebuild the figures:

```powershell
python -m pip install -r requirements.txt
python src\build_figures.py
```

The public script regenerates the figures from audited aggregate and per-epoch CSV files. It does not reproduce model training. The archived dataset construction, original environment, checkpoint lineage, and independent held-out evaluation remain outside the reproducible scope. A clean-room route for future work is described in [docs/reconstruction_plan.md](docs/reconstruction_plan.md).

## Repository guide

- [`results/`](results/): audited, sanitized validation tables and per-epoch metrics.
- [`figures/`](figures/): plots regenerated only from the public CSV files.
- [`tables/`](tables/): readable condition, result, and evidence-boundary summaries.
- [`docs/experiment_scope.md`](docs/experiment_scope.md): scope and non-claims.
- [`docs/methodology.md`](docs/methodology.md): metric-selection and audit method.
- [`docs/data_governance.md`](docs/data_governance.md): data, privacy, and leakage boundary.
- [`docs/contribution_scope.md`](docs/contribution_scope.md): evidence-based attribution boundary.
- [`docs/reproducibility.md`](docs/reproducibility.md): what this repository can and cannot reproduce.
