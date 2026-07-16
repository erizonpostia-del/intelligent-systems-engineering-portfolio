# Evaluation metrics: definitions and reporting rules

Let \(P\) be a predicted binary mask and \(G\) the reference mask. Counts \(TP\), \(FP\), and \(FN\) are defined at the stated unit of analysis.

| Metric | Definition | What it captures | Essential reporting caution |
|---|---|---|---|
| Dice coefficient | \(2|P \cap G|/(|P|+|G|)\) | Overlap; equivalent to F1 for a binary mask | Can be unstable for very small structures; define the empty-mask convention. |
| IoU / Jaccard | \(|P \cap G|/|P \cup G|\) | Stricter overlap | Do not compare values unless label, dimensionality, and aggregation match. |
| Precision | \(TP/(TP+FP)\) | How often predicted positives are correct | A high value can coexist with missed targets. |
| Recall / sensitivity | \(TP/(TP+FN)\) | Fraction of reference positives detected | A high value can coexist with over-segmentation. |
| Hausdorff distance (HD) | \(\max\{\sup_{p\in\partial P}\inf_{g\in\partial G}d(p,g),\sup_{g\in\partial G}\inf_{p\in\partial P}d(g,p)\}\) | Worst-case surface discrepancy | Sensitive to a single outlier; state voxel spacing and surface extraction. |
| HD95 | 95th percentile of directed/symmetric surface distances under the stated convention | Robust high-percentile boundary error | “HD95” is not fully comparable without its directed/symmetric and spacing definition. |
| ASD / ASSD | Mean (symmetric) nearest-surface distance | Typical boundary discrepancy | Can conceal a clinically important extreme error. |

## Why one number is not enough

Small targets, severe class imbalance, empty-reference cases, and uncertain annotations can make overlap metrics misleading. A 2D slice average is not equivalent to a 3D volume score. A pooled pixel score is not equivalent to an equal-weight per-patient average. For external validation, report site/protocol differences rather than merging all cases without disclosure. Taha and Hanbury provide a metric taxonomy [R10]; Metrics Reloaded recommends problem-aware selection and explicit treatment of aggregation and corner cases [R11].

For future work in this repository: report overlap plus surface error when boundaries matter; report precision and recall when missed versus extra tissue have different consequences; and add robustness, efficiency, and annotation burden as separate dimensions. No metric in this table was computed by this project.

