# CUHK-Shenzhen — MSc in Artificial Intelligence (Agentic AI direction)

**Jiang ZhengMeng** | Automation and Systems Engineering, Macau University of Science and Technology

My interest in **Agentic AI** stems from practical questions of goal-directed systems: how to structure tasks, interface with tools and environments, evaluate outcomes and recover from failure. The current public portfolio gives **adjacent foundations**, not evidence of a completed LLM-agent product.

## Evidence to read

| Priority | Project | Relevance |
|---|---|---|
| **1** | [Robotics & DQN](../../projects/01-robotics-dqn/OVERVIEW.md) · [DQN evaluation](../../projects/01-robotics-dqn/docs/dqn-ablation-study.md) | Decision-making under a defined environment and objective; controlled comparisons of reinforcement-learning agents. The DQN agent is **not** an LLM agent. |
| **2** | [Machine Learning Evaluation](../../projects/02-ml-evaluation/OVERVIEW.md) · [Reproducibility](../../projects/02-ml-evaluation/docs/reproducibility.md) | Selection/evaluation separation, experiment reliability and reproducible metrics—important habits for future agent evaluation. |
| **3** | [Fire & Smoke Detection](../../projects/04-fire-smoke-detection/OVERVIEW.md) · [Contribution scope](../../projects/04-fire-smoke-detection/docs/contribution_scope.md) | Real-world data quality, operational constraints and the difference between plausible model outputs and verified system performance. |

## Why this direction

ROS navigation exposed me to the coupling of perception, planning, state and action. Separate reinforcement-learning experiments gave me a controlled way to study learning-based decisions. Industrial computer vision then showed why a system needs traceable inputs and constrained claims before its actions can be trusted.

I want to move toward **tool-using and workflow-oriented AI systems** built on a better foundation in machine learning, software systems, agent planning, evaluation, and safety. I am particularly interested in turning useful prototypes into reliable applications and, longer-term, AI engineering roles that connect technical capabilities with real customer workflows.

## What this guide does not claim

- DQN in **FlappyBird-v0** is not a large-language-model agent, tool-calling system or multi-agent architecture.
- ROS navigation was not coupled to that DQN experiment; the nine-waypoint task was simulated, with separate team-based physical robot work.
- This repository does not currently demonstrate an evaluated autonomous LLM agent, production agent orchestration or a commercially deployed agent application.
- Industrial fire/smoke results are validation-stage records, not a field-ready real-time agent.

[Robotics & Intelligent Systems track](../tracks/robotics-intelligent-systems.md) · [AI Innovation / Deployment track](../tracks/ai-innovation-deployment.md) · [All programme guides](../README.md)
