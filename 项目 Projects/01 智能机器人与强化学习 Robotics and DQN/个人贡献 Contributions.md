# Individual Contributions / 个人贡献说明

Last audit / 最近审计：2026-07-14

Evidence confirms that work products and experiment records exist; it does not by itself establish authorship of each file. Contribution labels therefore distinguish verified execution from authorship that is not independently verified.

## ROS communication

| Component | Evidence status | Current contribution label | Boundary |
|---|---|---|---|
| Publisher/subscriber | Verified | Completed by the user as a course exercise (user-confirmed) | `beginner_tutorials` is a canonical ROS tutorial/course exercise; not presented as novel work |
| AddTwoInts service/client | Verified | Completed by the user as a course exercise (user-confirmed) | Same tutorial/course provenance boundary |
| Package metadata | Report only | Not claimed as a novel deliverable | Metadata does not establish sole authorship |

## TurtleBot3 navigation

### Reactive obstacle avoidance

- Evidence: complete `house_auto_avoid.py`, launch file, runtime logs and Gazebo screenshots.
- Existing components integrated: ROS1, `sensor_msgs/LaserScan`, `geometry_msgs/Twist`, TurtleBot3 Gazebo house world.
- Contribution: `house_auto_avoid.py` was independently implemented, and `house_auto_avoid.launch` was independently modified. The available evidence supports sector-based LiDAR obstacle-avoidance logic in ROS1/Gazebo simulation; it does not establish collision-free completion across all conditions.

### Multi-waypoint navigation

- Evidence: complete `world_outer_loop.py`, raw log with two complete nine-goal successes, and correct terminal screenshot.
- Existing components integrated: ROS1 actionlib, `move_base`, `move_base_msgs`, TF quaternion conversion, AMCL/costmaps/planner.
- Contribution: `world_outer_loop.py` was independently implemented with course guidance. The verified result boundary remains nine-goal completion in ROS1/Gazebo simulation, not physical-robot completion.

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

| Component | Evidence status | Contribution boundary | Public scope |
|---|---|---|---|
| DQN network and training code | Partially verified | Contribution attribution not independently verified | Outside the current public ROS scope |
| Observation processing | Verified | Attribution not independently verified | Outside the current public ROS scope |
| Training/evaluation | Partially verified | Conducted/evaluated status is not independently verified | Outside the current public ROS scope |

## Known Attribution Boundaries

- `house_auto_avoid.py` is user-confirmed as independently implemented. `world_outer_loop.py` is user-confirmed as independently implemented with course guidance.
- `beginner_tutorials` was completed by the user as ROS foundational coursework and is not claimed as a core project contribution.
- The confirmed physical-robot contribution scope is stated above; no more granular individual allocation is claimed.
- DQN starter-code/reference provenance and personal changes are outside the current public ROS scope.
