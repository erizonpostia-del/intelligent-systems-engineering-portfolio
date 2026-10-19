# HKU — MSc(Eng) in Robotics and Intelligent Systems

**Jiang ZhengMeng | Automation and Systems Engineering, Macau University of Science and Technology**

A technical reading guide for a robotics programme emphasizing **modelling, sensing, planning, control, intelligence, and integration**.

## Priority evidence

| Read | Direct evidence | Connection to the programme |
|---|---|---|
| **01 — Robotics & DQN** | [Visual walkthrough](../../projects/01-robotics-dqn/OVERVIEW.md) · [ROS1 simulation](../../projects/01-robotics-dqn/docs/ros1-simulation.md) · [team physical contribution](../../projects/01-robotics-dqn/docs/team-physical-deployment.md) | ROS-based navigation, LiDAR, and software/hardware integration; a separate controlled learning experiment |
| **04 — Fire & Smoke Detection** | [Visual walkthrough](../../projects/04-fire-smoke-detection/OVERVIEW.md) · [checkpoint evidence](../../projects/04-fire-smoke-detection/results/two_class_checkpoint_metrics.csv) | Perception engineering, error analysis, model limits, and repeatable development decisions |
| **02 — Machine Learning Evaluation** | [Visual walkthrough](../../projects/02-ml-evaluation/OVERVIEW.md) · [experiment code](../../projects/02-ml-evaluation/src/ridge_lasso_experiment.py) | Explicit model-selection discipline and held-out evaluation, not an applied robotics benchmark |

## Fit and intended development

My undergraduate systems-engineering background supports the connection among sensors, communication, control interfaces, and software. The ROS example provides evidence of **using** navigation components; it does **not** demonstrate invention of a novel planner. HKU's broader emphasis on robot modelling, control, collaborative integration, and applied projects identifies areas where I want more advanced, physical-system experience.

## Evidence boundaries

- The nine-waypoint navigation sequence is from **personal ROS1 simulation**.
- Physical TurtleBot3 work was **team-based** and is attributed accordingly.
- DQN results are from **FlappyBird-v0**, not physical robot control.
- Fire/smoke checkpoints have **development/validation** limitations; Project 02 is **synthetic**.

[Official HKU programme](https://www.dase.hku.hk/teaching-and-learning/prospective-students/master-of-science-in-engineering-in-robotics-and-intelligent-systems) · [Robotics track](../tracks/robotics-intelligent-systems.md) · [Portfolio homepage](../../README.md)
