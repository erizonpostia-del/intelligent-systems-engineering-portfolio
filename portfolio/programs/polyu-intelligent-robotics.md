# PolyU — MSc in Intelligent Robotics Engineering

**Jiang ZhengMeng | Macau University of Science and Technology | Automation and Systems Engineering**

*Portfolio reading guide for the September 2027 application. This page is a short navigation layer; project folders retain the underlying evidence, code, results, attribution, and limitations.*

## In 30 seconds

My technical background connects robot-system integration, sensing, machine-learning experiments, and evidence-led engineering decisions. The strongest robotics evidence comes from personal ROS1/Gazebo navigation work and a separately attributed team TurtleBot3/ROS2 physical exercise. My fire/smoke detection work adds computer-vision evaluation and development-data governance; the regression study shows how I control model-selection and test-data boundaries.

**These are distinct projects:** the DQN environment is FlappyBird-v0, not a learning controller deployed on TurtleBot3. The forest-monitoring detector has not been validated as a production system.

## Suggested reading order (about two minutes)

| Priority | Read | Concrete evidence | My contribution and limits |
|---|---|---|---|
| **01 — Robotics & DQN** | [Visual overview](../../projects/01-robotics-dqn/OVERVIEW.md) | [Nine-goal ROS1 simulation result](../../projects/01-robotics-dqn/results/robotics/multi-waypoint-navigation/result-summary.md); [ROS1 source files](../../projects/01-robotics-dqn/src/robotics/tb3_course_task/); [DQN ablation](../../projects/01-robotics-dqn/docs/dqn-ablation-study.md) | Implemented the personal LiDAR/waypoint simulation work; participated in team physical TurtleBot3 integration; independently completed the DQN experimental work. Nine-goal success is **simulation-only**, while the physical result is **team-based**. |
| **04 — Fire & Smoke Detection** | [Visual overview](../../projects/04-fire-smoke-detection/OVERVIEW.md) | [Same-v2-validation checkpoint data](../../projects/04-fire-smoke-detection/results/two_class_checkpoint_metrics.csv); [per-class results](../../projects/04-fire-smoke-detection/results/two_class_per_class_metrics.csv); [scope of contributions](../../projects/04-fire-smoke-detection/docs/contribution_scope.md) | Inspected archived experiment records, built public audit tables/figures, and documented data-governance and evaluation limits. Shared historical server records do **not** establish ownership of every training action. Results are **development/validation-only**. |
| **02 — Machine Learning Evaluation** | [Visual overview](../../projects/02-ml-evaluation/OVERVIEW.md) | [Ridge/Lasso implementation](../../projects/02-ml-evaluation/src/ridge_lasso_experiment.py); [nested cross-validation](../../projects/02-ml-evaluation/src/nested_cv_demo.py) | Implemented a self-contained demonstration using synthetic regression data, train-only scaling, held-out testing, and nested cross-validation. **Not** a real-world robotics dataset or deployed model. |

For a fuller explanation, open each project's [README](../../projects/01-robotics-dqn/README.md), [fire/smoke README](../../projects/04-fire-smoke-detection/README.md), or [ML README](../../projects/02-ml-evaluation/README.md).

## Relevance to Intelligent Robotics Engineering

- **Robot Motion Planning:** the ROS1 work demonstrates operating and testing a `move_base` navigation workflow with LiDAR input and nine waypoint goals. It does **not** claim a novel planning algorithm or hardware validation of that nine-goal sequence.
- **Embodied Robot Intelligence:** the team-based TurtleBot3 exercise provides physical-system integration experience; the independent DQN study provides a separate foundation in policy evaluation. They are **not** one end-to-end embodied-learning system.
- **Computer Vision and Image Processing:** fire/smoke results illustrate how per-class recall, localization quality, difficult examples, and validation-set independence affect decisions in a perception workflow.
- **Advanced Control Technology, robot mechanisms, and soft robotics:** these are areas I aim to strengthen through postgraduate study, **not** competencies demonstrated by the published experiments.

These connections refer to the [official PolyU programme and curriculum](https://www.polyu.edu.hk/study/pg/tpg/2027/43101-ir-irt); they are an applicant's interpretation of preparation and learning goals, not a claim of course equivalence.

## How to check the evidence

1. Use the **visual overviews** for the question, system, main result, and limitations.
2. Open linked **source, machine-readable results, and attribution notes** to inspect specific claims.
3. Treat historical checkpoints, reconstructed public figures, team-owned activities, and future plans as **different evidence types**. Where retained evidence is insufficient, this portfolio states the limitation instead of inferring a stronger result.

**Public-data boundary:** no unreleased company datasets, private raw media, credentials, or internal model weights are included.

[Back to portfolio homepage](../../README.md) · [All programme guides](../README.md)
