# Verified DQN Metrics

## Verified from Raw Results

- The final `formal_07_features_stack4_2000ep` evaluation records 50 scores with success threshold `score >= 10`.
- Recalculation confirms 36/50 successes (72%), mean 26.12, median 19.5, population standard deviation 27.8256, minimum 2, maximum 171.
- Four retained random-seed evaluations recompute to 38/50, 38/50, 35/50, and 34/50 successes. The public summary reports all four recovered files.
- The training CSV includes all 2,000 episode rows and 20 evaluation checkpoints.

## Verified from Source Configuration

- Environment: `FlappyBird-v0` with LiDAR enabled.
- Final input: 884 = 4 × (180 raw LiDAR + 41 engineered features).
- Final run: 2,000 episodes; Adam learning rate 1e-4; gamma 0.99; replay capacity 50,000; target hard-update interval 750 steps; hidden dimensions [256, 256].
- The network and TD target implement Double Dueling DQN.
- Evaluation is greedy and calls the environment with no additional reward shaping.

## Reported but Not Independently Verified

- Exact historical command line and exact evaluator revision that generated the retained fixed-seed file.
- The recovered fixed-seed JSON omits its per-episode seed list, although the retained evaluator source now documents the expected evaluation path.

## Instructor-Confirmed Attribution

The instructor confirmed that I independently completed the DQN implementation and experimental work, excluding the provided tutorial and referenced third-party dependencies. The sanitized source copy is included under `代码 Source/强化学习 DQN Reinforcement Learning/src`.

## Inconsistencies

- Earlier material stated replay capacity 100,000 and target update interval 50. The final retained configuration records 50,000 and 750, respectively.
- Earlier material described three random-seed groups; four random-seed result files were recovered, including two separate 38/50 runs.
- No explicit source handling for NaN or Inf was found; the sanitizer casts to float32 and clips to [0, 1].
