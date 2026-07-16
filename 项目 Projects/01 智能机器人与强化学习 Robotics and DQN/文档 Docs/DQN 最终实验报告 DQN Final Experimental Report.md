# DQN final experimental report

## What the final evidence supports

The strongest current evidence comes from the controlled extension studies rather than the archived single evaluation. These studies use saved configurations, multiple training seeds, validation-selected checkpoints, held-out test seeds, and integrity checks.

## Historical context

The 36/50 success and mean score 26.12 record is preserved as a Historical Archived Result from the 2,000-episode course run. The later 100-episode standardized re-evaluation is reported separately. Neither number is substituted for the other.

## Algorithm trade-offs

| Dimension | Leader under the tested configuration | Evidence |
|---|---|---|
| Performance leader | Dueling DQN | Highest five-run mean test success rate: 62.2% |
| Stability leader | Double DQN | Lowest cross-run success-rate standard deviation: 11.5% |
| Efficiency leader | Double DQN | Lowest mean training time: 653.5 s, tied for fewest parameters |
| Low-complexity performance trade-off | Vanilla DQN | 250,882 parameters and the highest median success rate, 65.0%, among the lower-parameter pair |

Dueling DQN achieved the highest average success rate under the tested configuration. Double DQN was more stable and faster across the five runs. Vanilla DQN retained the smaller network and a stronger median outcome than Double DQN. Double Dueling DQN did not dominate the other variants under this configuration.

## Recommended configuration file

`final_recommended_config.yaml` remains a documented low-complexity baseline rather than a universal best algorithm. It uses a lower-parameter filter and then the higher median success rate within that lower-parameter pair. The report keeps the performance, stability, efficiency, and complexity trade-offs visible so that a reader can select a configuration for a stated engineering goal.

## Engineering conclusions

Frame stacking was more consistently useful than the engineered feature expansion in the tested observation study. The controlled results favor raw_4frame as a practical state representation. They also show that architecture changes should be evaluated by more than a single best score: mean outcome, cross-seed variation, model size, and training time all matter.

## Limits

The conclusions are specific to FlappyBird-v0, the saved reward and training settings, five training seeds per algorithm, and the stated evaluation protocol. The study does not claim a novel RL method or a result that generalizes to all environments.
