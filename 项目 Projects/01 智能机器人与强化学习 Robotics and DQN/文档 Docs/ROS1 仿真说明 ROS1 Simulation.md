# ROS1 Simulation / ROS1 仿真说明

## Environment

This material was recovered from the user's personal Ubuntu 18.04 virtual machine. The verified environment record identifies ROS1 Melodic, Gazebo 9, RViz, a catkin workspace, TurtleBot3 simulation, and `move_base`-based navigation components.

## Public scope

The public package contains selected `tb3_course_task` files only. The paired ROS1 maps are course-provided simulation resources, not a personal mapping deliverable. `beginner_tutorials`, installed-package RViz configurations, raw logs, build outputs, and private environment artifacts are excluded.

## Included functions

- `house_auto_avoid.py` subscribes to `/scan` and publishes `geometry_msgs/Twist` commands to `/cmd_vel` using sector-based LiDAR distances.
- `world_outer_loop.py` sends nine `move_base` action goals and records a success/failure result for each goal.
- `house_auto_avoid.launch` starts the TurtleBot3 House Gazebo world and the obstacle-avoidance node.

## Verified Result Boundary

The available terminal evidence verifies a nine-goal sequence in Gazebo simulation. It is not evidence of a physical TurtleBot completing the same sequence.

## Known Limitations

The original full workspace, build command, launch invocation, and custom RViz configuration were not recovered. These omissions do not change the verified ROS1 simulation result.
