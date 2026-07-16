# Reproducibility boundary

What can be reproduced here:

- regenerate the four figures from public audited CSV files;
- verify the values in the public summary tables;
- inspect the documented interpretation and evidence boundaries.

The public script regenerates the figures from audited aggregate and per-epoch CSV files. It does not reproduce model training.

What cannot currently be reproduced:

- original dataset construction or cleaning;
- original training source and complete workflow;
- checkpoint lineage;
- original data provenance and evaluation protocol;
- an independent evaluation of the archived test-designated split.

## Historical training environment

Supplementary read-only evidence identifies a retained Linux GPU Docker environment with two NVIDIA RTX 4090 GPUs. The retained image records Python 3.12.3, PyTorch 2.11.0+cu128, CUDA 12.8, cuDNN 9.19.0.56, and Ultralytics 8.4.90. These values document retained infrastructure, but do not reconstruct the original interactive run, its data workflow, or its full control protocol.

## Artifact verification

The Standard and From3Class comparison checkpoints were matched to their archived run records by SHA-256:

- Standard: `EFD453EEA479108685E768CE770F072848ECE58DC80D87DCA5D1BEA7422B1CBF`
- From3Class: `E40B940BFA6897FE09821985E2A535E89A0F8C1E370C8FFC365A5622D0348308`

A server-export copy matched each corresponding archived artifact, and the archived final model copy had the same SHA-256 as the From3Class checkpoint. This establishes artifact consistency within the archived material; it does not place a checkpoint in this repository. No weights are published here.

For the confirmed Ultralytics version, the archived `best` convention uses validation mAP50-95 as its fitness basis. The public comparison applies the same metric directly to the archived per-epoch CSV rows, so the selection rule remains inspectable without loading a checkpoint.

## Test-designated-split evaluation limitation

The dataset contains an archived test-designated split, but no historical evaluation record for that split was found. The protocol cannot be reconstructed with enough confidence because prior inspection or use of that split, sequence-level leakage risk, and a safe checkpoint-loading chain remain unresolved. All current public metrics therefore remain validation-only.

The original Python source was reported as binary-contaminated, with no trusted clean backup found in the archive. The public dependency list is intentionally limited to plotting libraries and does not imply that this repository trains a detector.
