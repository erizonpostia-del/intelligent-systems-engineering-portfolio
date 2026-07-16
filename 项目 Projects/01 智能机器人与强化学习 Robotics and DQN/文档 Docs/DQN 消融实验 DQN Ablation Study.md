# DQN ablation study

## Observation design

The observation study compares raw and engineered representations with one-frame and four-frame stacking. Frame stacking improved both paired comparisons across the five training seeds. Single-frame conditions did not learn effective control reliably. The raw_4frame representation provided the best observed performance and engineering-cost balance for the later studies.

The engineered feature implementation has a consistent 41-dimensional structure and no NaN, Inf, future-information, or test-information leakage. Diagnostics found one constant feature, `global_max`, and 427 highly correlated feature pairs. The results point to redundancy and lower effective information density, not a universal claim that engineered features are useless.

## Training budget

The 3,000-episode study was retained because it added useful evidence for the raw_4frame condition. The evidence did not meet the predefined motivation for extending to 4,000 episodes. The project therefore reports the observed 3,000-episode trade-off rather than claiming that more training would necessarily improve the policy.

## Algorithm structure ablation

The final 2x2 study holds the observation and training budget fixed while changing two factors: Double-DQN target selection and Dueling network structure. Each algorithm uses five paired training seeds, validation-selected checkpoints, and a 100-seed held-out final test.

| Algorithm | Mean success | Median success | SD | Parameters | Mean training time |
|---|---:|---:|---:|---:|---:|
| Vanilla DQN | 57.0% | 65.0% | 15.8% | 250,882 | 678.8 s |
| Double DQN | 52.4% | 47.0% | 11.5% | 250,882 | 653.5 s |
| Dueling DQN | 62.2% | 58.0% | 18.2% | 382,723 | 1261.4 s |
| Double Dueling DQN | 56.8% | 56.0% | 17.9% | 382,723 | 1081.4 s |

The table is a descriptive five-seed comparison. It does not establish statistical significance or a universally best DQN architecture.

## Data and figures

Run-level, paired-comparison, factorial-effect, and efficiency CSVs are in `结果 Results/强化学习 DQN Reinforcement Learning/algorithm-ablation/`. Figures in `图表 Figures/强化学习 DQN Reinforcement Learning/algorithm-ablation/` are derived from those CSVs.
