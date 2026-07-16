# DQN public build report

The public DQN workstream is built from audited summary artifacts rather than raw private runs. It contains sanitized source components, configuration snapshots, result CSVs, figures derived from those CSVs, and reader-facing documentation.

The public source subset is intentionally smaller than the private archive. Historical training and evaluation entry scripts were not retained as public defaults because they reference historical output flow or checkpoints. The documented components remain available for inspection without a default command that writes into published result directories.

The 2026-07-16 cleanup removed only a duplicate generated export after byte-level verification. The canonical public directories are `代码 Source/强化学习 DQN Reinforcement Learning`, `配置 Configs/强化学习 DQN Reinforcement Learning`, `结果 Results/强化学习 DQN Reinforcement Learning`, and `图表 Figures/强化学习 DQN Reinforcement Learning`.
