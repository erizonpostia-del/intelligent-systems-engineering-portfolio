# Code Attribution / 代码来源与归属

The table records file provenance and contribution boundaries without inferring authorship beyond the available evidence.

| File | Function | Original Source | User Contribution | Modification Level | Evidence Status | Notes |
|---|---|---|---|---|---|---|
| `tb3_course_task/scripts/house_auto_avoid.py` | Sector-based LiDAR obstacle avoidance | Recovered from the user's personal ROS1 workspace | Independently implemented (user-confirmed) | Public copy retains algorithm logic unchanged | Verified | Project-specific script; no external source attribution was recovered. |
| `tb3_course_task/scripts/world_outer_loop.py` | Nine-goal `move_base` action sequence | Recovered from the user's personal ROS1 workspace | Independently implemented with course guidance (user-confirmed) | Public copy retains algorithm logic unchanged | Verified | Terminal evidence verifies execution in simulation; no novel navigation algorithm is claimed. |
| `tb3_course_task/launch/house_auto_avoid.launch` | Starts TurtleBot3 House simulation and avoidance node | Recovered from the user's personal ROS1 workspace | Independently modified (user-confirmed) | Public copy retains launch logic unchanged | Verified | Depends on official TurtleBot3 Gazebo packages. |
| `tb3_course_task/CMakeLists.txt` | Catkin package build metadata | Recovered package metadata | Not claimed as a novel deliverable | Unchanged | Report only | Contains standard Catkin template structure. |
| `tb3_course_task/package.xml` | Package dependencies | Recovered package metadata | Not claimed as a novel deliverable | Maintainer identifier redacted in public copy | Report only | Original license field was incomplete; no license is asserted by this reconstruction. |
| `house_map_full.{pgm,yaml}` and `world_map.{pgm,yaml}` | ROS1 simulation maps | Course/example-provided simulation resources (user-confirmed) | Not claimed as personal mapping output | Public copies use relative image paths only | Report only | Included only as paired simulation configuration resources. |
| `beginner_tutorials/*` | Publisher/subscriber/service tutorial exercises | ROS foundational coursework material | Completed by the user as course exercises (user-confirmed) | N/A | Verified | Excluded from the public package because it is not a core deliverable. |
| Recovered `.rviz` files | Installed package visualisation configurations | Official ROS1 package-share configurations | Not claimed as a personal deliverable | N/A | Not claimed | No user-created or confirmed modified RViz configuration was recovered. |

“Partially verified” identifies a recovered course-project artifact whose execution or workspace origin is evidenced, while independent-versus-course-guided authorship is not independently verified. A user-confirmed contribution category is recorded as “Verified”; neither status is evidence of independently authored novel ROS infrastructure.
