# Evidence Inventory / 项目证据清单

Last audit / 最近审计：2026-07-14

## Robotics and ROS / 机器人与 ROS

| Claim / 表述 | Evidence / 证据 | Status / 状态 | Strength / 强度 | Public handling / 公开处理 |
|---|---|---|---|---|
| ROS topic communication was implemented and run | Complete `beginner_tutorials` source plus talker/listener terminal screenshots | Verified | Strong for execution; completed by the user as a course exercise (user-confirmed) | Report only; explain tutorial provenance and redact identifiers |
| ROS service communication was implemented and run | AddTwoInts source/interface plus server/client runtime screenshot | Verified | Strong for execution; completed by the user as a course exercise (user-confirmed) | Report only; explain tutorial provenance and redact identifiers |
| Reactive LiDAR obstacle avoidance was implemented | `house_auto_avoid.py`, `house_auto_avoid.launch`, runtime decision logs and Gazebo screenshot | Verified | Strong for implementation; script independently implemented and launch file independently modified (user-confirmed) | Do not claim collision-free completion |
| Multi-waypoint navigation was implemented | `world_outer_loop.py` uses `move_base` Action goals | Verified | Strong for implementation; independently implemented with course guidance (user-confirmed) | State official ROS dependencies; do not claim a novel navigation algorithm |
| Nine-goal navigation completed in Gazebo | Correct terminal screenshot, source and `world_outer_loop.log`; log contains two complete Goal 1–9 success sequences | Verified | Strong | Redact username/path; state simulation explicitly |
| Two ROS1 map pairs were recovered | `house_map_full.{pgm,yaml}` and `world_map.{pgm,yaml}`; YAML image fields match existing PGM files | Report only | Strong | Course/example-provided simulation resources; publish only paired, path-redacted copies and do not claim personal mapping output |
| ROS logs were recovered | 250 private log files; 13 contain target status keywords | Partially verified | Mixed | Raw logs remain private |
| ROS1 environment was Ubuntu 18.04.6 / ROS Melodic | `Environment_Snapshot.txt`, ROS_VERSION=1, Gazebo 9 package record | Verified | Medium | Publish a redacted summary only |
| ROS1 RViz/Gazebo integration was active | Verified integration screenshot with map, scan/model and costmap/path displays | Verified | Medium | Does not alone prove navigation completion |
| Team-based TurtleBot3 Burger and ROS2 activity were recorded | 51.77 s video visually shows the robot and RViz/Nav2 in alternating shots; manual teleoperation is visible | Team evidence | Medium | Burger variant is user-confirmed. Evidence originated in the team environment hosted on a teammate's computer; private original, with redacted derivative if used |
| Team-based RViz goal-directed movement was demonstrated | User-confirmed team report and private video record | Team evidence | Medium | The current public evidence does not independently verify a continuous target-selection-to-arrival sequence |
| Complete end-to-end autonomous physical navigation mission succeeded | No continuous target-selection-to-arrival record or physical-navigation success log is available in the current evidence set | Not claimed | — | Not claimed |
| Team-based ROS2 localization/path planning was active | Navigation2 screenshots show active localization/navigation and planned paths | Team evidence | Medium | Team environment used Ubuntu 22.04, ROS2 Humble, TurtleBot3 Burger, and Cartographer (user-confirmed); no entity robot in screenshot |
| User-created independent RViz config exists | None found | Not recovered | — | 23 recovered files are official package configs only |
| rosbag exists | No `.bag`, `.db3` or `.mcap` found | Not recovered | — | Not claimed |
| Original `requirements.txt` / `environment.yml` exists | None found | Not recovered | — | Environment snapshot is not a substitute |

Physical TurtleBot evidence comes from a team-based ROS/terminal environment hosted on a teammate's computer. It must not be merged with the user's personal ROS1 Ubuntu 18.04 / Melodic simulation environment, nor used to claim that the user independently configured that PC environment or solely completed the physical navigation workflow. It documents the team's experiment, alongside the user's stated substantial contributions to assembly, networking/connection troubleshooting, robot-host communication, mapping data work, and key operations.

## Reinforcement Learning / 强化学习

| Claim / 表述 | Evidence / 证据 | Status / 状态 |
|---|---|---|
| Double Dueling DQN was implemented | Complete code and training/evaluation material in the private project source set | Partially verified; contribution attribution not independently verified |
| Fixed-seed result reached score ≥10 in 36/50 episodes | Evaluation JSON/figure and report materials | Verified |
| Mean score 26.12 and maximum score 171 | Evaluation material and report summary | Verified |
| Final observation dimension was 884 | Configuration/code description | Verified; dimensional breakdown is outside the current public ROS scope |

## Rule / 使用规则

Claims enter the public portfolio only when the evidence supports the exact scope. Simulation success is not physical-robot success; software activity is not target arrival; official package configuration is not an individual contribution; and team-based physical evidence does not prove sole ownership of the teammate-hosted PC environment or sole implementation of the workflow.
