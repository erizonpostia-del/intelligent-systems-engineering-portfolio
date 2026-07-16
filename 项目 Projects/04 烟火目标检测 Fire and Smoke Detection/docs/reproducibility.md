# Reproducibility boundary

What can be reproduced here:

- regenerate the four figures from public audited CSV files;
- verify the values in the public summary tables;
- inspect the documented interpretation and evidence boundaries.

The public script regenerates the figures from audited aggregate and per-epoch CSV files. It does not reproduce model training.

What cannot currently be reproduced:

- original dataset construction or cleaning;
- original training source and environment;
- checkpoint lineage;
- complete hardware/software configuration;
- an independent held-out-split evaluation.

The original Python source was reported as binary-contaminated, with no trusted clean backup found in the archive. The public dependency list is intentionally limited to plotting libraries and does not imply that this repository trains a detector.
