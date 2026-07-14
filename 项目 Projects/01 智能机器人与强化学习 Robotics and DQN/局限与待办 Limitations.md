# Limitations and Pending Work / 局限与待办

Last audit / 最近审计：2026-07-13

## Resolved evidence gaps / 已解决

- Two complete PGM/YAML map pairs were recovered and verified.
- Complete ROS1 package structures for `beginner_tutorials` and `tb3_course_task` were recovered.
- 250 ROS logs were recovered and indexed.
- Nine-goal Gazebo navigation is jointly supported by source, a correct terminal screenshot and two complete success sequences in the raw log.
- A physical TurtleBot3 video was found and visually checked.
- The environments are now explicitly separated into the user's Personal ROS1 Simulation Environment and the Team-Based Physical TurtleBot Environment hosted on a teammate's computer.

## Remaining limitations / 仍存局限

- The physical video shows the robot and Navigation2/RViz in alternating shots, but not a continuous target-submission-to-arrival sequence.
- Physical screenshots and video document team experiment activity, not the user's independent configuration or ownership of the teammate-hosted PC/ROS environment.
- No physical-navigation success log was found.
- The exact ROS2 distribution, Ubuntu version, TurtleBot3 variant and original ROS2 workspace are unknown.
- No rosbag was found.
- No original `requirements.txt` or `environment.yml` was found.
- No user-created or confirmed modified RViz configuration was found. The 23 recovered files are official installed-package configs.
- Individual authorship and template/course guidance for both ROS packages still require confirmation.
- The exact composition of the DQN 884-dimensional observation still needs a concise public explanation.
- Raw logs, environment snapshots, original video and course reports contain private paths, usernames or indoor imagery and remain private.

## Corrected image attribution

The file previously copied under a descriptive “nine-goal completed” name is hash-identical to `5f0365f7-55d8-4f18-a45a-182a29c53c94.png`. It shows RViz/Gazebo integration but no Goal 1–9 terminal results. The actual completion screenshot is `b112b2a6-8876-4ca8-aab0-1aac62d1dc21.png`.

## Priority work / 优先待办

1. Confirm ROS2 OS/distribution, robot model and whether the physical video is autonomous rather than teleoperated, if the teammate-hosted environment remains accessible.
2. Confirm authorship and source/template provenance for `world_outer_loop.py`, `house_auto_avoid.py` and `beginner_tutorials`.
3. Locate the ROS2 workspace, launch/config, logs or a continuous goal-to-arrival video in the teammate-hosted team environment, if the group wishes to provide further team-level evidence.
4. Prepare redacted public derivatives of selected maps, screenshots and video; keep private originals unchanged.
5. Explain the DQN 884-dimensional input composition and contribution boundary.

## Claim control / 表述控制

Do not claim a new SLAM algorithm, a novel navigation stack, a fully proven autonomous physical-robot system, independent ownership of the teammate-hosted PC environment, or ownership of official RViz configurations. State the personal ROS1 simulation and team-based physical evidence separately, while accurately crediting the user's substantial physical-deployment contributions.
