# DQN public build report

The public DQN workstream is built from audited summary artifacts rather than raw private runs. It contains sanitized source components, configuration snapshots, result CSVs, figures derived from those CSVs, and reader-facing documentation.

The public source subset is intentionally smaller than the private archive. Historical training and evaluation entry scripts were not retained as public defaults because they reference historical output flow or checkpoints. The documented components remain available for inspection without a default command that writes into published result directories.

The 2026-07-16 cleanup retained the verified CSV-derived figures and reorganized their public assets. The canonical public directories are `src/dqn`, `configs/dqn`, `results/dqn`, and `figures/dqn`.
