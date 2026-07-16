# Future reproducibility plan

## Status

This is a prospective plan. No inference, training, fine-tuning, evaluation, or hardware benchmark has been performed for this review.

## Minimal valid study

1. Select a public dataset with a documented license and an explicit segmentation task.
2. Record the exact model release, checkpoint checksum, code revision, and environment.
3. Use inference only. Do not train or fine-tune for a portfolio deadline.
4. Pre-register image preprocessing, 2D/3D handling, prompt type and source, mask post-processing, and qualitative review criteria.
5. Save inputs, prompts, masks, and errors only where redistribution is allowed.

## Ground truth and metrics

Without matching ground truth, report only qualitative observations: target ambiguity, prompt sensitivity, failure patterns, and representative outputs permitted by the dataset license. Do not calculate Dice, IoU, HD95, or other reference-based metrics.

With ground truth, define Dice, IoU, HD95, precision, recall, and any surface metric before evaluation. Report the case-level unit, empty-mask rule, 2D versus 3D implementation, aggregation, confidence intervals where feasible, and whether the evaluation is internal or external. Do not compare a new score to unrelated papers as a leaderboard.

## Resources, risks, and stop conditions

Estimate GPU memory and storage only after selecting a model and image size; retain the estimate with the run record. Stop if redistribution rights, patient-data governance, checkpoint provenance, reference labels, or prompt provenance cannot be verified. Stop rather than creating an unvalidated number.

