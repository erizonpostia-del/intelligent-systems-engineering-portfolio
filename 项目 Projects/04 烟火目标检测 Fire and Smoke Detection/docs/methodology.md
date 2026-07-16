# Methodology and metric selection

The public result files were derived directly from archived `results.csv` files and checked against their accompanying `args.yaml` configurations. The formal five-class runs contain epochs 1 through 50, and both configurations specify validation evaluation.

The repository separates three metric views:

1. **Highest validation mAP50-95 row** — the pre-declared main comparison rule.
2. **Highest validation mAP50 row** — retained as a separate row because its epoch differs.
3. **Final complete epoch** — epoch 50 for both five-class runs.

The peak metrics are not spliced together. Standard reaches its mAP50 peak at epoch 45 and mAP50-95 peak at epoch 40; From3Class reaches them at epochs 41 and 40, respectively. Precision and recall shown for each selection are values from that same source row.

The per-epoch public CSVs retain training losses, validation losses, precision, recall, mAP50, mAP50-95, and the first recorded learning-rate column. No data path, username, model artifact, or environment field is copied.
