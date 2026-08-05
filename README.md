# Intelligent Systems and Engineering Portfolio

**智能系统与工程作品集**

This repository presents a selected portfolio in robotics, machine learning, computer vision, and evidence-led engineering practice. The projects originate from university coursework, independent extensions, and engineering work, but the repository is not a raw archive of every exercise or intermediate file.

The public version is organised around four questions:

1. What problem was being solved?
2. What work is directly supported by retained evidence?
3. What was learned from the result or failure mode?
4. What remains outside the reproducible or attributable scope?

The portfolio follows a progression from automation and system engineering toward intelligent systems: robot integration and reinforcement learning, controlled machine-learning evaluation, technical review of medical segmentation, and an evolving fire/smoke detection workflow.

---

## Project map

| Project | Main focus | Public evidence scope |
|---|---|---|
| [01 — Robotics and DQN](项目%20Projects/01%20智能机器人与强化学习%20Robotics%20and%20DQN/) | ROS navigation, TurtleBot3 mapping, and reinforcement-learning coursework | Separates personal ROS1 simulation, team physical-robot work, and independently completed DQN coursework |
| [02 — Machine Learning Evaluation](项目%20Projects/02%20机器学习模型评估%20Machine%20Learning%20Evaluation/) | Ridge/Lasso comparison and model-selection methodology | Reproducible evaluation pipeline with train-only standardisation, validation-based selection, and 5×3 nested cross-validation |
| [03 — Medical Segmentation Review](项目%20Projects/03%20医学图像分割综述%20Medical%20Segmentation%20Review/) | Medical image-segmentation methods and literature synthesis | Technical review and method comparison; no model-training or reproduction claim |
| [04 — Fire and Smoke Detection](项目%20Projects/04%20烟火目标检测%20Fire%20and%20Smoke%20Detection/) | Object detection, data governance, difficult-target diagnosis, and split independence | Connects an earlier five-class YOLO11 experiment with the current two-class fire/smoke engineering workflow |


---

## Engineering through-line

Although the projects use different datasets and tools, they share a consistent working method.

### 1. Define the system boundary

Each project states what belongs to the task and what does not. Simulation and physical-robot work are separated; literature review is not presented as model training; validation observations are not described as independent benchmark results.

### 2. Build an inspectable evaluation path

The repository favours explicit splits, train-only preprocessing, declared metric-selection rules, retained configurations, readable result tables, and scripts that rebuild public figures from sanitized data.

### 3. Diagnose failure rather than report one score

The projects examine model-selection instability, class-level behaviour, difficult-target coverage, evidence gaps, and data leakage risk. A stronger aggregate number is not automatically treated as a stronger engineering result.

### 4. Preserve attribution and publication boundaries

Team work, individual work, reconstruction, inference, and retained evidence are labelled separately. Restricted datasets, model weights, internal paths, credentials, and unreviewed private imagery are excluded from the public repository.

---

## Portfolio snapshot

### 01 — Robotics and DQN

The robotics project combines three distinct evidence scopes:

- personal ROS1 simulation work in an Ubuntu virtual machine;
- team-based TurtleBot3 physical mapping and goal-point movement in ROS2 Humble;
- DQN coursework completed in a self-defined Python environment.

The public account does not claim continuous end-to-end autonomous navigation, unsupported obstacle-avoidance behaviour, or sole ownership of the team robot experiment.

### 02 — Machine Learning Evaluation

This project compares Ridge and Lasso under a controlled preprocessing and model-selection workflow. The public version documents validation-based hyperparameter selection, training-range standardisation, and a 5×3 nested cross-validation extension. It is the most directly reproducible statistical-learning project in the portfolio.

### 03 — Medical Segmentation Review

This project is a literature- and method-level technical review of medical image segmentation. Its contribution lies in organising architectures, evaluation considerations, and application constraints. It is not described as a trained, fine-tuned, or experimentally reproduced segmentation system.

### 04 — Fire and Smoke Detection

This is the most active engineering thread in the portfolio. It now presents a coherent project evolution:

- an earlier five-class YOLO11 initialization comparison established the first audited experimental foundation;
- the current two-class track narrows the task to `fire` and `smoke` and expands the work into source-media governance, duplicate control, annotation review, same-split checkpoint evaluation, class-specific error analysis, targeted difficult-smoke review, and scene/event-aware split planning.

The published snapshot includes YOLO11s v1-640, v2-640, and v2-960 evidence. It does not claim that development-v3, video-level alert logic, or deployment readiness is complete. The next planned model sequence is YOLO26s, D-FINE-S, and RT-DETRv2-S; no public performance claim is made before retained evaluation evidence exists.

---

## Repository structure

```text
.
├── README.md
├── 项目 Projects/
│   ├── 01 智能机器人与强化学习 Robotics and DQN/
│   ├── 02 机器学习模型评估 Machine Learning Evaluation/
│   ├── 03 医学图像分割综述 Medical Segmentation Review/
│   └── 04 烟火目标检测 Fire and Smoke Detection/
├── 研究 Research/
├── 经历 Experience/
├── 公共素材 Shared Assets/
├── 模板 Templates/
└── 脚本 Scripts/
```

Not every top-level directory is expected to contain a finished public artefact. Project-specific README files are the primary entry points for evidence, methods, limitations, and reproducibility notes.

---

## Technical scope

The portfolio currently includes work with:

- Python and C;
- Linux, Git, and reproducible project organisation;
- ROS1, ROS2, Gazebo, RViz, TurtleBot3, and Cartographer;
- reinforcement learning and DQN;
- scikit-learn pipelines, regularisation, validation, and nested cross-validation;
- computer vision, YOLO-based object detection, dataset review, and error diagnosis;
- technical literature review and engineering documentation.

This list describes demonstrated project scope, not a claim of equal depth across every tool.

---

## Evidence and attribution policy

The repository uses the following conventions:

- **Individual work** is identified when the retained evidence supports individual completion.
- **Team work** states the team setting and the specific personal contribution.
- **Archived evidence** is preserved as a bounded historical result rather than rewritten as a fully reproducible experiment.
- **Reconstructed material** is labelled when original source files are incomplete or unavailable.
- **Planned work** is separated from completed work.
- **Private or restricted assets** are not published merely to make the repository appear more complete.

For this reason, some projects contain aggregate tables and regeneration scripts but exclude datasets, weights, raw images, videos, internal logs, or environment-specific paths.

---

## Reading order

For a concise review of the portfolio:

1. Start with [Project 01](项目%20Projects/01%20智能机器人与强化学习%20Robotics%20and%20DQN/) for robotics integration and contribution boundaries.
2. Read [Project 02](项目%20Projects/02%20机器学习模型评估%20Machine%20Learning%20Evaluation/) for the clearest reproducible evaluation workflow.
3. Use [Project 03](项目%20Projects/03%20医学图像分割综述%20Medical%20Segmentation%20Review/) as the literature and method-synthesis example.
4. Finish with [Project 04](项目%20Projects/04%20烟火目标检测%20Fire%20and%20Smoke%20Detection/) for the most developed data-governance and computer-vision engineering workflow.

---

## Scope of the public repository

This repository is a technical portfolio, not a production software release. Unless a project README explicitly states otherwise, the materials should not be interpreted as:

- a deployable safety system;
- an independently audited benchmark;
- a complete release of the original dataset or training environment;
- proof that all planned extensions have been completed;
- evidence that team outcomes were produced by one person alone.

The goal is to make the supported engineering work inspectable without expanding claims beyond the retained evidence.
