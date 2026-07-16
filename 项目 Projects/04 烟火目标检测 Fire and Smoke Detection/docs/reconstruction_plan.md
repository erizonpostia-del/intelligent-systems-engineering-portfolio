# Clean-room reconstruction plan

The following is a future plan, not completed work.

1. Confirm licenses and redistribution rights for every data source.
2. Select public data with explicit compatible licenses.
3. Build group-aware or video-aware splits to reduce leakage risk.
4. Lock YOLO11, Python, PyTorch, CUDA, and Ultralytics versions.
5. Write a clean training pipeline rather than reusing contaminated source.
6. Record seeds, commands, configurations, and dataset versions.
7. Run at least 3–5 repetitions per condition.
8. Evaluate an independent held-out split.
9. Report means, standard deviations, and confidence intervals.
10. Publish a data card and model card after governance review.
