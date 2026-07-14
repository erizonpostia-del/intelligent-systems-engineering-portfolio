# Code Attribution / 代码来源与归属

The table records file provenance and contribution boundaries without inferring authorship beyond the available evidence.

| File | Function | Original Source | User Contribution | Modification Level | Public Status | Notes |
|---|---|---|---|---|---|---|
| `tb3_course_task/scripts/house_auto_avoid.py` | Sector-based LiDAR obstacle avoidance | Recovered from the user's personal ROS1 workspace | Exact independent-versus-course-guided authorship pending confirmation | Public copy retains algorithm logic unchanged | Publish with attribution caution | Project-specific script; no external source attribution was recovered. |
| `tb3_course_task/scripts/world_outer_loop.py` | Nine-goal `move_base` action sequence | Recovered from the user's personal ROS1 workspace | Exact independent-versus-course-guided authorship pending confirmation | Public copy retains algorithm logic unchanged | Publish with attribution caution | Project-specific script; terminal evidence supports execution in simulation. |
| `tb3_course_task/launch/house_auto_avoid.launch` | Starts TurtleBot3 House simulation and avoidance node | Recovered from the user's personal ROS1 workspace | Integrated into the course task; detailed authorship pending | Unchanged | Publish with attribution caution | Depends on official TurtleBot3 Gazebo packages. |
| `tb3_course_task/CMakeLists.txt` | Catkin package build metadata | Recovered package metadata | Not a claimed novel deliverable | Unchanged | Publish with attribution caution | Contains standard Catkin template structure. |
| `tb3_course_task/package.xml` | Package dependencies | Recovered package metadata | Not a claimed novel deliverable | Maintainer identifier redacted in public copy | Publish with attribution caution | Original license field was `TODO`; no license is asserted by this reconstruction. |
| `beginner_tutorials/*` | Publisher/subscriber/service tutorial exercises | ROS foundational coursework material | Not included as a core deliverable | N/A | Do not publish | Could dilute the project and authorship is not established. |
| Recovered `.rviz` files | Installed package visualisation configurations | Official ROS1 package-share configurations | Not a personal deliverable | N/A | Do not publish | No user-created or confirmed modified RViz configuration was recovered. |

“Publish with attribution caution” means the file is publicly shown as a recovered course-project artifact, not as evidence of independently authored novel ROS infrastructure.
