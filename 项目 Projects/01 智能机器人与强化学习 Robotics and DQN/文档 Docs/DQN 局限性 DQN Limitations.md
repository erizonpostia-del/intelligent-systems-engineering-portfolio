# DQN limitations

- The archived historical evaluation lacks a retained per-episode seed list.
- The standardized re-evaluation and archived fixed evaluation are different experiments and have different outcomes.
- The controlled algorithm ablation has five training seeds per algorithm. It supports descriptive comparisons, not significance testing.
- The final public source subset omits model weights and raw private runs. It supports inspection of the implementation and documented result artifacts, not exact one-command recreation of every historical condition.
- The results are specific to FlappyBird-v0, the raw_4frame observation, original reward, and the saved training settings.
