# DQN reproduction notes

## What is available

The public subset includes configurations, source modules, result CSVs, figures, and documentation. It excludes model weights, raw private run directories, virtual environments, and original course material.

## Safe reading path

1. Read `DQN System.md` for the representation and algorithm structure.
2. Read `DQN Training and Evaluation.md` for historical and controlled protocols.
3. Inspect the algorithm-ablation CSVs before interpreting figures.
4. Use `final_recommended_config.yaml` only as a documented low-complexity baseline, not as an unconditional recommendation.

## Environment dependencies

The reconstructed dependency list names PyTorch, NumPy, Gymnasium, Pygame, and Flappy Bird Gymnasium. Exact reproduction of the archived course runtime is not promised because the historical environment and weights are not published.

## Safety

The public source subset is intended for code reading and component-level inspection. Do not run historical training or evaluation scripts against the public result directories. Any local experiment should use a new user-chosen output directory and separate seed manifests.
