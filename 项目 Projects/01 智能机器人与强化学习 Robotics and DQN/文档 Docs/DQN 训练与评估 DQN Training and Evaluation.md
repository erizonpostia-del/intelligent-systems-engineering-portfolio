# DQN training and evaluation

## Historical archived experiment

The archived course run used Double Dueling DQN, the 884-dimensional feature_4frame observation, and 2,000 training episodes. Its retained fixed evaluation recorded 36/50 successes at `score >= 10`, mean score 26.12, minimum 2, and maximum 171. This is a Historical Archived Result. It documents the original course outcome and the source of later reconstruction work.

## Standardized historical checkpoint re-evaluation

The saved checkpoint `best_success10_36_mean_26.12_ep_2000.pt` was later evaluated with a standardized 100-episode protocol. The re-evaluation recorded 7% success, mean score 3.84, median score 8.0, standard deviation 3.1191, and IQM 7.1. Parameter hashes matched before and after evaluation. This is a New Standardized Re-evaluation, not a replacement for the archived result.

## Controlled extension protocol

The algorithm ablation fixed raw_4frame observations, original reward, 3,000 episodes, five paired training seeds, and the same core training budget. Validation used 20 fixed seeds every 100 episodes with epsilon 0. The selected checkpoint was tested once on 100 held-out seeds. Test seeds were not used for tuning.

## Checkpoint handling

The final test evaluates the validation-selected checkpoint. Best-validation and final-training checkpoints are different concepts. The reports state which checkpoint was evaluated and preserve parameter-hash checks around final evaluation.

Detailed run summaries are available in `结果 Results/强化学习 DQN Reinforcement Learning/`.
