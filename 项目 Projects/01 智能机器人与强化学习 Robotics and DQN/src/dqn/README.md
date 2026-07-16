# Public DQN source subset

This directory contains the inspected student implementation components used by the DQN workstream. It does not include model weights, raw runs, virtual environments, third-party environment source, or a one-command training pipeline.

## Files

| File | Purpose | Input and output behavior | Training or overwrite risk |
|---|---|---|---|
| `src/00_env_check.py` | Optional environment health check | Uses a caller-provided seed and prints environment metadata. It does not write files. | No training and no overwrite. It requires a separately installed Flappy Bird Gymnasium environment. |
| `src/wrappers.py` | Observation sanitization, frame stacking, and environment construction | Provides Python modules to other code. | No direct output. |
| `src/replay_buffer.py` | Replay-memory implementation | Provides Python modules to other code. | No direct output. |
| `src/networks.py` | Q-network and Dueling-network definitions | Provides Python modules to other code. | No direct output. |
| `src/algorithms.py` | Vanilla, Double, Dueling, and Double Dueling target and topology selection | Provides Python modules to other code. | No direct output. |
| `src/extension_core.py` | Extension experiment helpers | Provides Python modules to other code. When called by a separate runner, it creates a unique run directory and writes only inside that directory. | No direct command, no overwrite of an existing run directory. |

## Safe use

Use this subset to inspect the components behind the documented experiments. The archived training, evaluation, auto-experiment, plotting, and demonstration entry scripts are intentionally excluded because they were tied to historical output locations, checkpoints, or internal experiment flow. They are retained as private evidence, not as public defaults.

If you adapt these components for a new experiment, use a new output directory, a new run identifier, and separate validation and test seed manifests. Do not write into `results/` or `figures/`, which are published result artifacts.

## Dependencies

See `requirements-reconstructed.txt`. Flappy Bird Gymnasium, Gymnasium, PyTorch, and NumPy are third-party dependencies.
