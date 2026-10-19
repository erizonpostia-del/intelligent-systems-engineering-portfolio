# Intelligent Systems Engineering — Technical Portfolio

**Jiang ZhengMeng** · BSc student in **Automation and Systems Engineering**, Faculty of Innovation Engineering, **Macau University of Science and Technology (MUST)**

**Focus:** robotics and intelligent systems · computer vision and model evaluation · AI for science and health · applied AI engineering.

I work on the engineering questions that sit between an algorithm and a trustworthy result: how data are prepared, how sensing and software are integrated, what an experiment actually measures, and where its conclusions stop. This repository is a curated record of selected undergraduate projects, not an invented end-to-end product or a universal benchmark.

## Start here — find your programme (2027 intake)

The same four projects support different interests. Each guide prioritises **specific evidence and attribution**, with a short explanation of its fit and limitations. The eight pages below reflect my current programme-focused portfolio and are **not** claims that every application has been submitted.

| University | MSc programme / focus | Application reading guide |
|---|---|---|
| **NUS** | Artificial Intelligence & Innovation | [AI evaluation and innovation](portfolio/programs/nus-ai-innovation.md) |
| **NUS Medicine** | Precision Health and Medicine × AI | [Medical-AI literature and methods](portfolio/programs/nus-precision-health-ai.md) |
| **NTU** | Robotics and Intelligent Systems | [Robot-system integration](portfolio/programs/ntu-robotics-intelligent-systems.md) |
| **HKU** | MSc(Eng) in Robotics and Intelligent Systems | [Sensing, navigation and systems](portfolio/programs/hku-robotics-intelligent-systems.md) |
| **CUHK** | Artificial Intelligence for Science | [Scientific AI and evidence](portfolio/programs/cuhk-ai-for-science.md) |
| **HKUST** | AI and Entrepreneurship | [Applied AI and feasibility](portfolio/programs/hkust-ai-entrepreneurship.md) |
| **PolyU** | Intelligent Robotics Engineering | [Robotics engineering — selected evidence](portfolio/programs/polyu-intelligent-robotics.md) |
| **CityUHK** | Artificial Intelligence for Sciences · intended Track 4: Applied AI | [Applied AI and embodied systems](portfolio/programs/cityu-ai-for-sciences-applied-ai.md) |

Or browse one of the three broader paths:

- **[Robotics & Intelligent Systems](portfolio/tracks/robotics-intelligent-systems.md)** — 01 → 04 → 02
- **[AI for Science / Health](portfolio/tracks/ai-for-science-health.md)** — 03 → 02 → 04
- **[AI Innovation / Deployment](portfolio/tracks/ai-innovation-deployment.md)** — 04 → 02 → 01

## Four selected projects

| Project and fast visual entry | My main contribution | What it does **not** prove |
|---|---|---|
| **01 · [Robotics & DQN](projects/01-robotics-dqn/OVERVIEW.md)** | Personal ROS1/Gazebo LiDAR and nine-waypoint navigation; attributed team ROS2/TurtleBot3 physical work; independent DQN implementation and controlled evaluation | Nine-waypoint success was in simulation; team robot work is not solely mine; DQN ran on FlappyBird-v0, **not** the robot |
| **02 · [Machine Learning Evaluation](projects/02-ml-evaluation/OVERVIEW.md)** | Implemented Ridge/Lasso comparison, train-only scaling, held-out evaluation and nested CV | The data come from `sklearn.make_regression`, **not** a deployed prediction task |
| **03 · [Medical Segmentation Review](projects/03-medical-segmentation-review/OVERVIEW.md)** | Synthesised SAM, SAM-Path, MedSAM and medical-domain adaptation/evaluation literature; prepared original concept diagrams and comparisons | **Not** a patient-data experiment, fine-tuning run, or an original medical segmentation benchmark |
| **04 · [Fire & Smoke Detection](projects/04-fire-smoke-detection/OVERVIEW.md)** | Audited archived YOLO11 experiments; reviewed development-data governance and class-sensitive findings; prepared public metrics, figures and attribution notes | **Not** an independently audited test benchmark, production detector, or demonstration of sole authorship of all shared-server training |

Each link opens a **visual evidence overview**. For implementation details, source, original scope, results tables, and reproducibility limitations, continue to the [project documentation index](portfolio/README.md).

## What the evidence shows

- **Robot systems:** ROS1 `move_base`, LiDAR inputs, navigation interfaces, Gazebo/RViz; separately documented ROS2/TurtleBot3 team work.
- **Learning and evaluation:** DQN architecture/budget comparisons; reproducible train/validation/test logic; seed-aware analysis and nested cross-validation.
- **Applied perception:** YOLO11 validation comparisons, data-quality decisions, small/distant-smoke review, and per-class error analysis.
- **Research literacy:** structured reading, technical comparison and metric caveats for foundation models in medical-image segmentation.
- **Engineering accountability:** explicit separation of individual and team work, historical records and reconstructions, external literature and my experiments, completed results and planned extensions.

## Read results in context

1. **Project-specific source is authoritative.** The programme guides are navigation, not independent experiment reports.
2. **Methods and metrics have boundaries.** Model rankings are conditional on data, split, checkpoint, seed, task and evaluation protocol. Different historical tasks are not silently compared.
3. **Attribution matters.** Personal ROS1 work, team TurtleBot3 work, DQN experiments, literature review, and archived industrial-server records are separate evidence streams.
4. **Publication rights and privacy matter.** Restricted media, internal company datasets, unreviewed images, unpublished model weights, credentials, and private paths are not published to make the portfolio appear larger.
5. **Gaps remain explicit.** Future tests, full reproduction of some historical experiments, physical verification, industry deployment and commercial validation are not represented as completed work.

[Browse all application guides](portfolio/README.md) · [Robotics track](portfolio/tracks/robotics-intelligent-systems.md) · [AI for Science / Health track](portfolio/tracks/ai-for-science-health.md) · [AI Innovation / Deployment track](portfolio/tracks/ai-innovation-deployment.md)
