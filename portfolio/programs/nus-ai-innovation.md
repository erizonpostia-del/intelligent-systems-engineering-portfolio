# NUS — MSc (Artificial Intelligence & Innovation)

**Jiang ZhengMeng | Automation and Systems Engineering, Macau University of Science and Technology**

An applicant-curated reading guide for the **2027 intake**. Start with the evidence below; the linked project folders, not this summary, are the source of technical results.

## Why these projects

The common theme is **moving from a promising model result to an evidence-based engineering decision**: choosing an evaluation method, identifying data limitations, and understanding the conditions required before an AI solution could be useful. This aligns with my interest in interdisciplinary AI application and innovation, not with a claim that I have launched a commercial product.

| Read first | Evidence to inspect | What it demonstrates |
|---|---|---|
| **04 — Fire & Smoke Detection** | [Visual overview](../../projects/04-fire-smoke-detection/OVERVIEW.md) · [checkpoint comparison](../../projects/04-fire-smoke-detection/results/two_class_checkpoint_metrics.csv) | A real engineering problem framed around data quality, fire/smoke error trade-offs, and deciding what **not** to infer from aggregate validation scores |
| **02 — Machine Learning Evaluation** | [Visual overview](../../projects/02-ml-evaluation/OVERVIEW.md) · [nested-CV code](../../projects/02-ml-evaluation/src/nested_cv_demo.py) | Reproducible choices about preprocessing, model selection, and held-out evaluation |
| **01 — Robotics & DQN** | [Visual overview](../../projects/01-robotics-dqn/OVERVIEW.md) · [contribution notes](../../projects/01-robotics-dqn/docs/contributions.md) | Systems integration and the separate discipline of controlled reinforcement-learning experiments |

## Programme alignment and learning goals

The official programme combines **AI evaluation, innovation management, entrepreneurship, governance/ethics, and machine-learning foundations**. Project 04 illustrates why an AI application needs trustworthy data and evaluation before adoption; Project 02 supports the model-evaluation foundation; Project 01 gives a contrasting sensor/robotics setting.

What I still want to develop is the **nontechnical translation from prototype to value**: stakeholders, product validation, AI governance, organisational adoption, and measurable impact. The portfolio does **not** evidence startup incorporation, users, commercial revenue, or production deployment.

[Official NUS programme](https://scale.nus.edu.sg/programmes/graduate/msc-(artificial-intelligence-innovation)) · [All project evidence](../../README.md) · [Portfolio homepage](../../README.md)

## Attribution and evidence limits

- Fire/smoke metrics are **validation-stage** findings. Some historical actions were on a shared server and are not attributed entirely to me; [contribution scope](../../projects/04-fire-smoke-detection/docs/contribution_scope.md) details the boundary.
- The regression study uses **synthetic data**.
- ROS1 nine-goal navigation is **simulation-only**; physical TurtleBot3 work is **team-based**; DQN was evaluated in **FlappyBird-v0**, not on the robot.
