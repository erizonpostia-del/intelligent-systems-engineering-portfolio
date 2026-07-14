# Individual Contributions / 个人贡献说明

Last audit / 最近审计：2026-07-13

Evidence confirms that work products and experiment records exist; it does not by itself establish who authored each file. Until the user confirms provenance, contribution labels remain conservative.

## ROS communication

| Component | Evidence status | Current contribution label | Boundary |
|---|---|---|---|
| Publisher/subscriber | Complete source and runtime screenshots found | To be confirmed | `beginner_tutorials` is a canonical ROS tutorial/course exercise; do not present it as novel work |
| AddTwoInts service/client | Complete source/interface and runtime screenshot found | To be confirmed | Same tutorial/course provenance boundary |
| Package metadata | `package.xml` and `CMakeLists.txt` found | Course/basic exercise context | Metadata contains a local maintainer identifier but that is not proof of sole authorship |

## TurtleBot3 navigation

### Reactive obstacle avoidance

- Evidence: complete `house_auto_avoid.py`, launch file, runtime logs and Gazebo screenshots.
- Existing components integrated: ROS1, `sensor_msgs/LaserScan`, `geometry_msgs/Twist`, TurtleBot3 Gazebo house world.
- Current contribution label: To be confirmed.
- Required confirmation: independently written, written with course guidance, or adapted from a template/example.

### Multi-waypoint navigation

- Evidence: complete `world_outer_loop.py`, raw log with two complete nine-goal successes, and correct terminal screenshot.
- Existing components integrated: ROS1 actionlib, `move_base`, `move_base_msgs`, TF quaternion conversion, AMCL/costmaps/planner.
- Current contribution label: To be confirmed.
- Verified result boundary: nine-goal completion in ROS1/Gazebo simulation, not physical-robot completion.

### Team-based physical TurtleBot deployment

- Project form and environment: collaborative physical-robot work in a ROS/terminal environment hosted on a teammate's computer, separate from the user's personal ROS1 Ubuntu virtual machine.
- Substantial contributions: TurtleBot assembly and hardware preparation; network configuration, connection testing, and troubleshooting; robot-host communication setup; mapping-data acquisition and related processing; and key mapping and navigation operations during the team experiments.
- Evidence: ROS2 topic/communication/mapping/localization/path screenshots and a visually verified 51.77-second robot/Nav2 video.
- Attribution boundary: these records support the team's physical-robot experiment and the user's stated substantial contributions. They do not establish that the user independently configured the teammate-hosted PC environment or solely implemented the complete physical navigation workflow.
- Verified result boundary: entity robot and Navigation2 activity are shown; continuous goal submission through explicit arrival is not shown.

## Official/configuration components

- The 23 recovered `.rviz` files are official installed ROS1 package configurations.
- They may be described as integrated/used environment components only.
- They must not be listed as individually authored deliverables.

## Reinforcement learning

| Component | Evidence status | Current contribution label | Needed confirmation |
|---|---|---|---|
| DQN network and training code | Complete code/material set found | To be confirmed | Starter-code and reference provenance |
| Observation processing | 180-D LiDAR, four-frame stack and 884-D final input recorded | To be confirmed | Exact added feature dimensions and author |
| Training/evaluation | Structured results and figures found | Conducted/evaluated, pending confirmation | Individual vs team role and evaluation design |

## User confirmations still required

1. Authorship category for `world_outer_loop.py` and `house_auto_avoid.py`.
2. Whether all `beginner_tutorials` files are course/ROS tutorial exercises.
3. Physical-robot role split beyond the confirmed substantial contributions listed above, if a more granular breakdown is needed.
4. Starter-code/reference provenance and personal changes in the DQN implementation.
