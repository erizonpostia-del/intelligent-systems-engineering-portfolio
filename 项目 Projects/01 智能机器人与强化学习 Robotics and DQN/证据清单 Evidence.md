# Evidence Inventory / 项目证据清单

Last audit / 最近审计：2026-07-14

## Robotics and ROS / 机器人与 ROS

| Claim / 表述 | Evidence / 证据 | Status / 状态 | Strength / 强度 | Public handling / 公开处理 |
|---|---|---|---|---|
| ROS topic communication was implemented and run | Complete `beginner_tutorials` source plus talker/listener terminal screenshots | Found and verified | Strong for execution; authorship pending | Explain tutorial provenance and redact identifiers |
| ROS service communication was implemented and run | AddTwoInts source/interface plus server/client runtime screenshot | Found and verified | Strong for execution; authorship pending | Explain tutorial provenance and redact identifiers |
| Reactive LiDAR obstacle avoidance was implemented | `house_auto_avoid.py`, launch file, runtime decision logs and Gazebo screenshot | Found and verified | Strong for implementation; Medium for runtime outcome | Confirm authorship; do not claim collision-free completion |
| Multi-waypoint navigation was implemented | `world_outer_loop.py` uses `move_base` Action goals | Found and verified | Strong | Confirm authorship and explain official ROS dependencies |
| Nine-goal navigation completed in Gazebo | Correct terminal screenshot, source and `world_outer_loop.log`; log contains two complete Goal 1–9 success sequences | Found and verified | Strong | Redact username/path; state simulation explicitly |
| Two ROS1 map pairs were recovered | `house_map_full.{pgm,yaml}` and `world_map.{pgm,yaml}`; YAML image fields match existing PGM files | Found and verified | Strong | Publish only paired, path-redacted copies |
| ROS logs were recovered | 250 private log files; 13 contain target status keywords | Found and verified; requires selective use | Mixed | Raw logs remain private |
| ROS1 environment was Ubuntu 18.04.6 / ROS Melodic | `Environment_Snapshot.txt`, ROS_VERSION=1, Gazebo 9 package record | Found and verified | Medium | Publish a redacted summary only |
| ROS1 RViz/Gazebo integration was active | Verified integration screenshot with map, scan/model and costmap/path displays | Found and verified | Medium | Does not alone prove navigation completion |
| Team-based physical TurtleBot3 and ROS2 Navigation2 activity were recorded | 51.77 s video visually shows the robot and RViz/Nav2 in alternating shots | Found and verified | Medium | Evidence from the team environment hosted on a teammate's computer; private original, with redacted derivative if used |
| Complete autonomous physical navigation succeeded | Video does not continuously show target submission through explicit arrival; no success log | Missing | — | Do not claim |
| Team-based ROS2 localization/path planning was active | Navigation2 screenshots show active localization/navigation and planned paths | Found but not fully verified | Medium | Team environment hosted on a teammate's computer; no entity robot in screenshot |
| User-created independent RViz config exists | None found | Missing | — | 23 recovered files are official package configs only |
| rosbag exists | No `.bag`, `.db3` or `.mcap` found | Missing | — | Do not fabricate |
| Original `requirements.txt` / `environment.yml` exists | None found | Missing | — | Environment snapshot is not a substitute |

Physical TurtleBot evidence comes from a team-based ROS/terminal environment hosted on a teammate's computer. It must not be merged with the user's personal ROS1 Ubuntu 18.04 / Melodic simulation environment, nor used to claim that the user independently configured that PC environment or solely completed the physical navigation workflow. It documents the team's experiment, alongside the user's stated substantial contributions to assembly, networking/connection troubleshooting, robot-host communication, mapping data work, and key operations.

## Reinforcement Learning / 强化学习

| Claim / 表述 | Evidence / 证据 | Status / 状态 |
|---|---|---|
| Double Dueling DQN was implemented | Complete code and training/evaluation material in the private project source set | Found; contribution attribution pending |
| Fixed-seed result reached score ≥10 in 36/50 episodes | Evaluation JSON/figure and report materials | Found and verified |
| Mean score 26.12 and maximum score 171 | Evaluation material and report summary | Found and verified |
| Final observation dimension was 884 | Configuration/code description | Found and verified; dimensional breakdown still needs explanation |

## Rule / 使用规则

Claims enter the public portfolio only when the evidence supports the exact scope. Simulation success is not physical-robot success; software activity is not target arrival; official package configuration is not an individual contribution; and team-based physical evidence does not prove sole ownership of the teammate-hosted PC environment or sole implementation of the workflow.
