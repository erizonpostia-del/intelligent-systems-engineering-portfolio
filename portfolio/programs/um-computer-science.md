# University of Macau — MSc in Computer Science

**Jiang ZhengMeng** | BSc in Automation and Systems Engineering, Macau University of Science and Technology

This guide connects my undergraduate work to **software systems, computational methods, and AI-enabled applications**. The strongest evidence is in experiment design, software/sensor integration and reproducibility; I am not presenting myself as a graduate of a computer-science undergraduate programme.

## Suggested reading order

| Read | Inspect | Evidence and relevance |
|---|---|---|
| **02 — Machine Learning Evaluation** | [Visual overview](../../projects/02-ml-evaluation/OVERVIEW.md) · [Runnable nested CV](../../projects/02-ml-evaluation/src/nested_cv_demo.py) · [Methods](../../projects/02-ml-evaluation/docs/methodology.md) | Python-based experiment implementation, preprocessing boundaries, model selection and reproducible evaluation. |
| **01 — Robotics & DQN** | [Visual overview](../../projects/01-robotics-dqn/OVERVIEW.md) · [Contribution record](../../projects/01-robotics-dqn/docs/contributions.md) | Interfaces between Linux/ROS, sensing, communication and navigation; an independent reinforcement-learning experiment. |
| **04 — Fire & Smoke Detection** | [Visual overview](../../projects/04-fire-smoke-detection/OVERVIEW.md) · [Attribution notes](../../projects/04-fire-smoke-detection/docs/contribution_scope.md) | Practical data workflow, archived experiment auditing and interpretation of class-specific validation results. |

## Why Computer Science

My automation background started with components, signals and system integration. Building ROS navigation workflows and evaluating ML experiments made the software side of these systems increasingly important: repeatable execution, interface design, testing, and the relationship between an algorithm and its operating environment. Computer Science is the next step in developing stronger foundations in algorithms, software engineering, computing systems and scalable AI applications.

UM's stated learning outcomes emphasise **efficient software solutions, designing and evaluating computer-based systems, and professional responsibility**. I want to improve my ability to build reliable end-to-end systems rather than describe isolated algorithm results.

## Scope and gaps

- The regression example uses **synthetic `sklearn.make_regression` data**; its value is methodological, not predictive performance in production.
- ROS1 nine-waypoint navigation was **simulation-only**; ROS2/TurtleBot3 evidence is **team work**; DQN was trained on **FlappyBird-v0**, not a robot.
- The fire/smoke repository records **development validation**, not a verified independent test result or deployed detector.
- This portfolio does not yet establish large-scale distributed-system expertise or a production full-stack software service. These are learning goals.

[UM programme list](https://www.fst.um.edu.mo/academics/programs/) · [UM postgraduate learning outcomes](https://www.fst.um.edu.mo/academics/current-students/graduate-students/pilos/) · [All project evidence](../README.md) · [Portfolio homepage](../../README.md)
