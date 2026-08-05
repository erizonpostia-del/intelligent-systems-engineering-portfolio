# Two-class development scope

## Supported by retained evidence

The public two-class update is based on retained dataset manifests, YOLO11 run configurations, native training CSV files, same-v2-validation checkpoint evaluations, targeted smoke-review summaries, and scene/event governance records.

The supported public claims are limited to:

- the documented v1 and v2 dataset counts;
- three retained YOLO11s checkpoint evaluations on the same v2 validation split;
- fire/smoke class metrics from the retained evaluation summaries;
- native training progression from retained `results.csv` files;
- targeted small/distant-smoke review outcomes;
- completion of retained scene/event and novelty-review work;
- current limitations and planned next-stage model evaluation.

## Important comparison boundary

The v1 native training curve uses the v1 validation data. The v2-640 and v2-960 native curves use the v2 validation data. They must not be treated as a three-way same-split curve comparison.

The main checkpoint table is different: all three retained checkpoints were evaluated on the same v2 validation split and can therefore support the reported cross-checkpoint comparison.

## Not established

The retained evidence does not establish:

- a released dataset;
- a fully independent benchmark;
- formal diversity-24 acceptance or freeze;
- a reconciled A–E error-diagnosis distribution;
- multi-seed stability;
- video-level performance;
- temporal alarm logic;
- deployment readiness;
- YOLO26s, D-FINE-S, or RT-DETRv2-S results;
- sole individual ownership of source collection, every annotation, or every remote execution step.

## Public-data boundary

No source media, labels, weights, internal review databases, server paths, credentials, recovery records, or unreviewed qualitative images are included. Public figures are generated only from sanitized CSV tables.
