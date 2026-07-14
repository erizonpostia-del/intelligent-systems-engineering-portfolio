# Reproduction / 复现说明

## Confirmed environment information

- Ubuntu 18.04.
- ROS1 Melodic.
- Gazebo 9 and RViz.
- Catkin workspace and the `tb3_course_task` package.
- TurtleBot3 simulation, with Waffle Pi selected by the retained course launch file.
- Navigation components evidenced in the environment: `move_base`, AMCL, map server, costmaps, and DWA planner.

## Package dependencies

The public `package.xml` and `CMakeLists.txt` list the recovered Catkin dependencies: `actionlib`, `actionlib_msgs`, `geometry_msgs`, `move_base_msgs`, `nav_msgs`, `rospy`, `sensor_msgs`, and `tf`. Dependency versions and the original full workspace are not available.

## Verified execution evidence

The retained terminal screenshot shows the following confirmed application command after ROS setup:

```bash
rosrun tb3_course_task world_outer_loop.py
```

It records connection to `move_base`, nine successful goals, and completion of the outer loop.

## Known Reproduction Limitations

- **Not recovered:** the original workspace build command; no reliable recollection is available to support a specific command claim.
- **Not independently verified:** the original command used to invoke `house_auto_avoid.launch`.
- **Not recovered:** the original map-server launch and map-loading command.
- **Not recovered:** the executable-permission state of the recovered Python scripts.

These details are not stated as reproduction steps. This repository does not fabricate a `requirements.txt`, rosbag, environment file, or custom RViz configuration.

## Maps

The two public PGM/YAML pairs are course/example-provided ROS1 simulation resources. Their public YAML copies use relative image paths; the private source files were not modified. They are not presented as personal mapping output.
