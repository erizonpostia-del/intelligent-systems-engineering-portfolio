# Fire and Smoke Detection for Forest Monitoring — Visual Evidence Overview

This project traces a forest-monitoring detection effort from an archived five-class experimental foundation to a two-class fire/smoke engineering workflow. The central question is not which single aggregate score is largest, but what the retained evidence says about data quality, checkpoint choice, and class-specific behaviour.

## At a glance

| Item | Summary |
|---|---|
| Question | How should fire/smoke detector development proceed when aggregate metrics hide class-specific weakness? |
| My role | Rechecked retained records, separated evaluation contexts, prepared public tables and figures, and documented governance and attribution boundaries. |
| Main methods/system | Archived YOLO11 five-class comparison; two-class v1/v2 development; same-v2-validation checkpoint comparison; per-class and targeted review. |
| Key outcome | The retained snapshot keeps v1 as the published development baseline while treating v2 and resolution changes as diagnostic evidence, not deployment results. |
| Evidence boundary | Validation-only development evidence; no released dataset, independent test result, video alarm evaluation, or deployment-readiness claim. |

## Evidence chain

```text
five-class experimental foundation
          ↓
data governance and dataset evolution
          ↓
same-split checkpoint comparison
          ↓
class-specific diagnosis
      ↙                 ↘
per-class metrics    targeted smoke review
      \                 /
       \               /
        baseline / next-step decision
```

### A — Experimental foundation

The earlier five-class archive established the initial comparison and reporting discipline. This figure compares Standard and From3Class at each run's highest validation mAP50-95 epoch. It is useful as the starting point for the story, but it is not numerically comparable with the later two-class development track: the label spaces, dataset histories, checkpoint lineages, and evaluation contexts differ.

![Archived validation mAP comparison](figures/validation_map_comparison.png)

The surviving five-class records include per-epoch CSVs, separate mAP50 and mAP50-95 selection views, and final-epoch values. [Validation results](tables/validation_results.md) and [experiment scope](docs/experiment_scope.md) keep those views separate. The figure therefore establishes an audited foundation, not a universal model ranking or an independent benchmark.

### B — From model comparison to data engineering

The two-class development track broadens the question from model scores to the conditions that make scores interpretable. The governance schematic records source-media registration, exact-duplicate control, modality and semantic review, annotation review, temporal grouping, scene/event adjudication, cluster-aware split planning, freeze planning, and evaluation.

![Data governance pipeline](figures/data_governance_pipeline.png)

The dataset-evolution figure shows the retained v1 and v2 counts: positive and negative samples, fire boxes, and smoke boxes. Together, these views explain why duplicate control, source governance, scene/event considerations, and difficult-smoke coverage belong in the engineering story. They do not establish a strict chronology in which one review artifact directly caused one later run; they are mutually informative development evidence.

![Two-class dataset evolution](figures/two_class_dataset_evolution.png)

See [data governance](docs/data_governance.md), [contribution scope](docs/contribution_scope.md), and the retained [dataset statistics](results/two_class_dataset_statistics.csv) for the evidence boundary.

### C — Aggregate metrics were not enough

All three retained two-class checkpoints were evaluated on the same v2 validation split, which makes this the core cross-checkpoint comparison. The v2-640 checkpoint raises mAP50 from 0.4777 for v1-640 to 0.4868, but lowers mAP50-95 from 0.2443 to 0.2334. The v2-960 checkpoint records 0.4463 mAP50 and 0.2196 mAP50-95, so the higher input resolution does not improve the overall retained result.

![Two-class checkpoints on the same v2 validation split](figures/two_class_checkpoint_comparison.png)

The per-class views explain why the aggregate result is insufficient. Fire recall rises across the displayed checkpoints, reaching 0.6204 for v2-960, while smoke recall falls to 0.3562. Smoke mAP50-95 also falls to 0.1540, below the fire value of 0.2852. The increase in overall recall at 960 is therefore not uniform improvement across the two classes.

![Per-class recall on the same v2 validation split](figures/two_class_per_class_recall.png)

![Per-class localization quality on the same v2 validation split](figures/two_class_per_class_map50_95.png)

The suffixes `v1-640`, `v2-640`, and `v2-960` identify dataset version and image size, not duration. Native best-checkpoint semantics are also separate from later same-v2-validation evaluation:

| Run | Requested | Completed | Native best | Later checkpoint origin |
|---|---:|---:|---:|---|
| v1-640 | 50 | 48 | 33 | `best.pt` from epoch 33 |
| v2-640 | Not recoverable | 50 | 50 | `best.pt` from epoch 50 |
| v2-960 | Not recoverable | 50 | 50 | `best.pt` from epoch 50 |

These values are recorded in [two-class development scope](docs/two_class_development_scope.md) and [checkpoint metrics](results/two_class_checkpoint_metrics.csv). The v2 runs must not be described as having a recovered requested count of 50.

### D — Data review changed the next decision

The targeted review screens 396 candidate samples: 15 positive, 237 negative, 14 ambiguous, and 130 excluded. Only 10 positives are visible at full-image scale and five require an enlarged view or crop; the review retains 16 smoke boxes. This low positive yield indicates that difficult-smoke coverage remains a data problem, not merely a question of selecting a different aggregate metric.

![Targeted small and distant smoke review outcomes](figures/targeted_smoke_review_outcomes.png)

This review and the resolution comparison should be read as mutually informative evidence. The retained records do not justify a strict claim that the review directly caused a particular resolution run, or the reverse. The supported engineering decision for this snapshot is to retain v1 as the published development baseline rather than selecting a checkpoint from one aggregate metric alone.

## Additional evidence and boundaries

The following figures remain available for detailed inspection but are omitted from this short visual walkthrough: [precision/recall comparison](figures/precision_recall_comparison.png), [Standard progression](figures/training_progression_standard.png), [From3Class progression](figures/training_progression_from3class.png), [v1 native progression](figures/v1_native_training_progression.png), [v2 mAP50 progression](figures/v2_map50_training_progression.png), and [v2 mAP50-95 progression](figures/v2_map50_95_training_progression.png). The full per-epoch and final records are in [results](results/) and the figure builder is [build_two_class_figures.py](src/build_two_class_figures.py).

No test-designated sample count is presented as an independent test evaluation. No deployment readiness, video-level performance, temporal alarm logic, multi-seed stability, released dataset, or full individual ownership is claimed. [Reproducibility](docs/reproducibility.md) records what can be regenerated from the public sanitized tables.

[Back to project README](README.md)
