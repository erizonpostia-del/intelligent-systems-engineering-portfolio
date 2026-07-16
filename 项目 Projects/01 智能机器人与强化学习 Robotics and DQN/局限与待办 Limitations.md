# Limitations and evidence boundaries

## Robotics

- The ROS1 navigation result is verified in Gazebo simulation, not on a physical robot.
- The physical TurtleBot work is a team result in a teammate-hosted environment. The public evidence does not show a continuous target-selection-to-arrival trace, a physical-navigation success log, or a complete autonomous mission.
- The public project does not include the original ROS2 workspace, rosbag files, a custom RViz configuration, or private raw logs.

## Learning-based control

- The historical 36/50 evaluation is an archived course result. It has no retained per-episode seed list and is not interchangeable with the later standardized checkpoint re-evaluation.
- The 2x2 algorithm study contains five training seeds per algorithm. It supports descriptive comparisons in the tested environment, not formal significance claims or universal recommendations.
- Dueling DQN had the highest mean success rate in the tested configuration, while the lower-complexity configurations had fewer parameters and shorter mean training times. The project therefore reports a trade-off rather than one unconditional best algorithm.
- The feature diagnostics found one constant feature and substantial correlation among engineered features. This supports an engineering concern about redundancy, not a claim that engineered features are universally ineffective.

## Public scope

The repository excludes model weights, raw private runs, original video, private paths, course materials, and personal contact information.
