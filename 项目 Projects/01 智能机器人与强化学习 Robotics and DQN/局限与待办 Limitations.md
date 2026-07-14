# Known Limitations and Evidence Boundaries / 已知局限与证据边界

Last audit / 最近审计：2026-07-14

## Resolved evidence gaps / 已解决

- Two complete PGM/YAML map pairs were recovered and verified.
- Complete ROS1 package structures for `beginner_tutorials` and `tb3_course_task` were recovered.
- 250 ROS logs were recovered and indexed.
- Nine-goal Gazebo navigation is jointly supported by source, a correct terminal screenshot and two complete success sequences in the raw log.
- A physical TurtleBot3 video was found and visually checked.
- The environments are now explicitly separated into the user's Personal ROS1 Simulation Environment and the Team-Based Physical TurtleBot Environment hosted on a teammate's computer.

## Remaining limitations / 仍存局限

- The physical video includes manual teleoperation and a user-confirmed RViz goal-directed movement demonstration, but the current public evidence does not provide a continuous, independently verifiable target-selection-to-arrival trace.
- Physical screenshots and video document team experiment activity, not the user's independent configuration or ownership of the teammate-hosted PC/ROS environment.
- No physical-navigation success log was recovered in the current evidence set.
- The team environment used Ubuntu 22.04, ROS2 Humble, TurtleBot3 Burger, and Cartographer (user-confirmed). The original ROS2 workspace has not yet been incorporated; a team-held archive has been reported.
- Physical enclosed-space obstacle avoidance is user-reported but is not claimed because no video or log was recovered.
- No rosbag was found.
- No original `requirements.txt` or `environment.yml` was found.
- No user-created or confirmed modified RViz configuration was found. The 23 recovered files are official installed-package configs.
- Individual authorship and template/course guidance for both ROS packages still require confirmation.
- The exact composition of the DQN 884-dimensional observation still needs a concise public explanation.
- Raw logs, environment snapshots, original video and course reports contain private paths, usernames or indoor imagery and remain private.

## Corrected image attribution

The file previously copied under a descriptive “nine-goal completed” name is hash-identical to `5f0365f7-55d8-4f18-a45a-182a29c53c94.png`. It shows RViz/Gazebo integration but no Goal 1–9 terminal results. The actual completion screenshot is `b112b2a6-8876-4ca8-aab0-1aac62d1dc21.png`.

## Evidence Status Summary

- **Not recovered:** physical-navigation success log and physical enclosed-space obstacle-avoidance recording.
- **Not independently verified:** a continuous physical RViz target-selection-to-arrival trace.
- **Not claimed:** a complete end-to-end autonomous physical navigation mission or physical obstacle-avoidance outcome.
- **Not claimed:** complete physical goal-to-arrival navigation, ownership of the teammate-hosted PC environment, a custom RViz configuration, or a novel SLAM/navigation algorithm.
- **Outside the current public scope:** DQN input-composition and contribution-boundary documentation.

## Claim control / 表述控制

Do not claim a new SLAM algorithm, a novel navigation stack, a fully proven autonomous physical-robot system, independent ownership of the teammate-hosted PC environment, or ownership of official RViz configurations. State the personal ROS1 simulation and team-based physical evidence separately, while accurately crediting the user's substantial physical-deployment contributions.
