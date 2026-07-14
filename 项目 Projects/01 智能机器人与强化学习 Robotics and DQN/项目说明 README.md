# Learning-Based Autonomous Systems with ROS and Double Dueling DQN

## Overview

This portfolio project presents verified ROS coursework evidence and a clearly scoped record of a team physical-robot experiment. The public ROS reconstruction contains only selected, sanitized ROS1 simulation materials. Private originals, raw logs, and unredacted media are not included.

## Project Scope

The repository separates two different environments and does not treat them as one deployment:

- **Personal ROS1 Simulation Environment:** the user's Ubuntu 18.04 virtual machine with ROS Melodic, Gazebo, RViz, `move_base`, and a catkin workspace.
- **Team-Based Physical TurtleBot Deployment:** a collaborative experiment hosted on a teammate's computer. Its ROS, terminal, Navigation, and RViz environment was not the user's personal VM or PC environment.

## Part I: ROS1 Simulation

The public reconstruction includes the `tb3_course_task` ROS package, paired simulation maps, a reactive LiDAR obstacle-avoidance script, and a multi-waypoint `move_base` action client. The exact independent-versus-course-guided authorship of the scripts remains documented in [Code Attribution.md](文档%20Docs/代码来源与归属%20Code%20Attribution.md).

## Part II: Team-Based Physical TurtleBot Deployment

The physical TurtleBot work was completed collaboratively in an environment hosted on a teammate's computer. My substantial contributions included TurtleBot assembly and hardware preparation; network configuration, connection testing and troubleshooting; robot-host communication; mapping-data acquisition and related processing; and key mapping and navigation operations. I do not claim sole ownership of that PC environment or sole implementation of the entire physical workflow. See [Team Physical Deployment.md](文档%20Docs/小组真机贡献%20Team%20Physical%20Deployment.md).

## Part III: Reinforcement Learning

**DQN public reconstruction in progress.** No DQN source, model, or result files are included in this public ROS reconstruction.

## Verified Results

- A nine-goal sequence was executed in the ROS1 Gazebo simulation through the `move_base` action interface.
- The retained terminal evidence records `Goal 1 reached` through `Goal 9 reached` and `World outer loop finished`.
- The RViz/Gazebo screenshot shows ROS1 simulation integration; it does not independently prove the nine-goal outcome.

## My Contributions

The ROS1 material comes from the personal simulation environment. The physical-robot contribution boundary is team-based and is stated above and in the linked deployment note. No claim is made that the physical system was independently configured or independently completed.

## Environment Separation

Simulation success is not physical-robot success. The public team screenshot shows Navigation2 context only; it does not prove a complete target-submission-to-arrival sequence, autonomous operation, or a user-owned PC environment.

## Repository Structure

- `代码 Source/ROS1 仿真 ROS1 Simulation/tb3_course_task`: selected ROS1 package files.
- `配置 Configs/ROS1 仿真 ROS1 Simulation/地图 Maps`: paired public simulation-map copies.
- `结果 Results/ROS1 仿真 ROS1 Simulation/多目标点导航 Multi-Waypoint Navigation`: verified result summary.
- `媒体 Media`: selected redacted simulation and team-context evidence.
- `文档 Docs`: reproduction, attribution, evidence, safety, and build records.

## Reproduction

Only confirmed information is recorded in [Reproduction.md](文档%20Docs/复现说明%20Reproduction.md). Commands not directly confirmed by evidence are marked `TODO: verify exact command` rather than inferred.

## Attribution

See [Code Attribution.md](文档%20Docs/代码来源与归属%20Code%20Attribution.md). The excluded `beginner_tutorials` package is a ROS foundational exercise and is not presented as a core project deliverable.

## Limitations

This reconstruction does not include a user-created RViz configuration, physical navigation success log, rosbag, full ROS2 workspace, or a continuous physical goal-to-arrival recording.

## Current Status

The ROS1 public reconstruction was prepared from selected evidence on 2026-07-14. No Git staging, commit, or push operation was performed.
