# DQN system

## Scope

I implemented the DQN workflow for FlappyBird-v0 and later extended the experimental record with controlled studies. The public material separates the historical course result, standardized historical checkpoint re-evaluation, observation and feature studies, training-budget evidence, and algorithm-structure ablation.

## State representation

The historical course condition used 180 LiDAR values, 41 engineered features, and four-frame stacking for an 884-dimensional input. The controlled algorithm ablation fixed the observation to raw_4frame, which stacks four 180-dimensional LiDAR observations for 720 dimensions.

## Algorithm structures

The controlled study compares Vanilla DQN, Double DQN, Dueling DQN, and Double Dueling DQN. Vanilla and Double DQN use a single Q-value stream. Dueling variants separate value and advantage streams. Double variants choose the next action with the online network and evaluate it with the target network.

## Engineering controls

The later studies use fixed training seeds, validation-based checkpoint selection, held-out test seeds, parameter-hash checks during final evaluation, and CSV summaries. This structure prevents the test set from driving model selection.

See [training and evaluation](DQN%20%E8%AE%AD%E7%BB%83%E4%B8%8E%E8%AF%84%E4%BC%B0%20DQN%20Training%20and%20Evaluation.md) and [ablation study](DQN%20%E6%B6%88%E8%9E%8D%E5%AE%9E%E9%AA%8C%20DQN%20Ablation%20Study.md).
