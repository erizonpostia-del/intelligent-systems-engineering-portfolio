# DQN reproduction notes

## What is available

The public subset includes configurations, source modules, result CSVs, figures, and documentation. It excludes model weights, raw private run directories, virtual environments, and original course material.

## Safe reading path

1. Read [dqn-system.md](dqn-system.md) for the representation and algorithm structure.
2. Read [dqn-training-and-evaluation.md](dqn-training-and-evaluation.md) for historical and controlled protocols.
3. Inspect the algorithm-ablation CSVs before interpreting figures.
4. Use [final_recommended_config.yaml](../configs/dqn/final_recommended_config.yaml) only as a documented low-complexity baseline, not as an unconditional recommendation.

## Environment dependencies

The reconstructed dependency list names PyTorch, NumPy, Gymnasium, Pygame, and Flappy Bird Gymnasium. Exact reproduction of the archived course runtime is not promised because the historical environment and weights are not published.

## Public seed-manifest provenance

`configs/dqn/runs/validation_seeds_20.json` and `configs/dqn/runs/standard_test_seeds_100.json` are reconstructed/normalized protocol records from the retained private experiment archive. Their seed values and ordering were verified against the retained validation and standardized-test experiment records. They are not byte-identical copies of the original historical JSON artifacts; the public files preserve the verified protocol content without presenting themselves as original archive files.

## Safety

The public source subset is intended for code reading and component-level inspection. Do not run historical training or evaluation scripts against the public result directories. Any local experiment should use a new user-chosen output directory and separate seed manifests.
