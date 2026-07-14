# Experimental Environments / 实验环境说明

Last audit / 最近审计：2026-07-14

## Environment A: Personal ROS1 Simulation Environment / 个人 ROS1 仿真环境

- OS: Ubuntu 18.04.6 LTS (verified by environment snapshot)
- ROS: ROS1 Melodic (`ROS_VERSION=1`, `ROS_DISTRO=melodic`)
- Simulator: Gazebo 9
- Visualization: RViz
- Robot model used in simulation: TurtleBot3, with Waffle Pi selected in the course-task launch file
- Navigation/mapping components evidenced: `move_base`, AMCL, map_server, gmapping-related environment, costmaps and DWA planner
- Workspace/packages: `catkin_ws`, `beginner_tutorials`, `tb3_course_task`
- Languages: C++ and Python
- Maps: `house_map_full` and `world_map`, each with verified PGM/YAML members
- Evidence: environment snapshot, package metadata, source, 250 logs, maps and simulation screenshots

This was the user's personal Ubuntu virtual machine for individual course experiments, including ROS1, Gazebo, RViz, source execution/debugging, mapping, and multi-waypoint navigation.

`Environment_Snapshot.txt` was generated during evidence recovery. It is not an original Python `requirements.txt`.

## Environment B: Team-Based Physical TurtleBot Environment / 小组 TurtleBot 真机环境

- ROS generation: ROS2
- Navigation: Navigation2
- Localization: AMCL/Navigation2 localization state visible
- Project form: collaborative physical-robot experiment hosted on a teammate's computer
- Physical evidence: entity TurtleBot3 appears in a 51.77-second video; Navigation2/RViz appears in alternating shots
- OS: unknown
- ROS2 distribution: unknown
- Robot model: TurtleBot3, exact variant unknown
- Original ROS2 workspace/configuration: not recovered
- Navigation success boundary: target submission and explicit arrival are not continuously recorded

The physical TurtleBot mapping and navigation experiments were completed collaboratively in a separate team environment hosted on a teammate's computer. This PC/ROS environment is distinct from the user's personal ROS1 Ubuntu virtual machine and must not be described as an environment maintained solely by the user. The screenshots and mapping outputs evidence the team's physical-robot work, not an independently configured personal PC environment.

## Environment C: Double Dueling DQN

- Deep-learning framework: PyTorch; exact version pending confirmation
- Environment: FlappyBird-v0
- Raw observation: 180-dimensional LiDAR
- Frame stack: 4
- Final observation dimension: 884
- Training episodes: 2000
- OS/Python/device: pending confirmation in the public audit documents

## Missing environment artifacts

- ROS1/ROS2 rosbag: Missing
- Original `requirements.txt`: Missing
- Original `environment.yml` / `environment.yaml`: Missing
- User-created RViz config: Missing
- Official ROS1 RViz package configs: Found (23), attributed to installed packages
- Complete ROS2 environment snapshot/workspace: Missing
