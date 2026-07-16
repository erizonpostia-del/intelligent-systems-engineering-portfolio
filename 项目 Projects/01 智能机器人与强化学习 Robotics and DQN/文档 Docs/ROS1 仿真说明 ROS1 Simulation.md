# ROS1 simulation

## Scope

I developed this workstream in my personal Ubuntu 18.04 virtual-machine environment with ROS1 Melodic, Gazebo 9, RViz, TurtleBot3 simulation, and `move_base`. It is separate from the later team ROS2 physical deployment.

## Implemented components

- `house_auto_avoid.py` subscribes to `/scan` and publishes `geometry_msgs/Twist` commands to `/cmd_vel` from sector-based LiDAR distances.
- `house_auto_avoid.launch` starts the TurtleBot3 House Gazebo world and the obstacle-handling node.
- `world_outer_loop.py` sends nine `move_base` goals and records success or failure for each goal.

## Verified result

I completed a nine-goal multi-waypoint navigation sequence in Gazebo using the ROS `move_base` action interface. The claim is supported by the public source subset, redacted terminal evidence, and recovered log evidence. It does not establish the same result on a physical TurtleBot.

## Included and excluded material

The public package contains selected `tb3_course_task` files and paired course-provided maps. Raw logs, build outputs, the complete workspace, and private environment records remain private. The maps are simulation resources, not a personal mapping claim.
