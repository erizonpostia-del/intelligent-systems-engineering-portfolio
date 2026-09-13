# Intelligent Systems Engineering Portfolio

An admissions-oriented portfolio at the intersection of automation and systems engineering, intelligent systems, perception, and learning.

I build and evaluate engineering workflows across robotics, statistical learning, computer vision, and technical review. The common thread is system thinking: connect software, sensing, algorithms, and evidence; then state clearly what the retained material does and does not prove.

## Choose a reading path

| Application direction | Suggested order | Start here |
|---|---|---|
| Robotics & Intelligent Systems | 01 → 04 → 02 | [Robotics & Intelligent Systems](portfolio/tracks/robotics-intelligent-systems.md) |
| AI for Science / Health | 03 → 02 → 04 | [AI for Science / Health](portfolio/tracks/ai-for-science-health.md) |
| AI Innovation / Deployment | 04 → 02 → 01 | [AI Innovation / Deployment](portfolio/tracks/ai-innovation-deployment.md) |

Programme-specific reading guides are collected in [`portfolio/programs/`](portfolio/programs/). They are navigation aids, not personal statements.

## Selected projects

| Project | What it demonstrates | Evidence boundary |
|---|---|---|
| [01 — Robotics & DQN](projects/01-robotics-dqn/) | ROS1 simulation, TurtleBot3 integration context, LiDAR navigation, DQN implementation, controlled evaluation | Simulation and team physical work are separate; DQN runs are configuration-specific and descriptive |
| [02 — Machine Learning Evaluation](projects/02-ml-evaluation/) | Train-only preprocessing, validation-based selection, held-out testing, and nested cross-validation | Synthetic `make_regression` data; not real-world domain research |
| [03 — Medical Segmentation Review](projects/03-medical-segmentation-review/) | Literature synthesis, foundation-model adaptation analysis, evaluation literacy, and original schematics | Technical review only; no patient-data experiment, training, fine-tuning, or project-generated medical metrics |
| [04 — Fire & Smoke Detection](projects/04-fire-smoke-detection/) | YOLO11 result auditing, dataset governance, class-level diagnosis, and development decision-making | Validation/development evidence only; no released dataset, independent benchmark, or deployment-readiness claim |

## 30-second profile

- **Systems:** personal ROS1/Gazebo navigation plus team-based ROS2 TurtleBot3 physical deployment work.
- **Learning:** DQN source implementation and controlled comparisons across observation, budget, and architecture choices.
- **Evaluation:** explicit split logic, train-only preprocessing, validation selection, nested CV, seed-aware summaries, and failure analysis.
- **Perception:** fire/smoke detection workflow with dataset governance, class-specific metrics, difficult-target review, and split-independence planning.
- **Evidence practice:** distinguish individual work, team work, archived results, reconstruction, literature evidence, and planned work.

## Repository map

```text
.
├── README.md
├── projects/
│   ├── 01-robotics-dqn/
│   ├── 02-ml-evaluation/
│   ├── 03-medical-segmentation-review/
│   └── 04-fire-smoke-detection/
└── portfolio/
    ├── README.md
    ├── tracks/
    └── programs/
```

Each project folder is the canonical evidence layer for its own methods, results, figures, code, attribution, limitations, and reproducibility notes. The navigation pages select and contextualise these canonical materials; they do not duplicate experimental truth.

## Evidence policy

- Reported results remain tied to their source configuration, split, seed, and evaluation context.
- Team outcomes identify the team setting and the specific contribution supported by retained evidence.
- Literature claims are kept separate from experiments performed in this repository.
- Private datasets, raw media, model weights, internal paths, credentials, and unreviewed imagery are not published merely to make the portfolio look more complete.

## Scope

This is an engineering portfolio, not a production release or a universal benchmark. Some figures can be rebuilt from retained public tables, while original datasets, weights, and full historical environments remain outside the public boundary. Planned extensions are labelled as planned and are not presented as completed results.
