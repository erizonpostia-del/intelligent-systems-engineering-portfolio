# Experimental environments

## Personal ROS1 simulation

My personal simulation environment used Ubuntu 18.04.6, ROS1 Melodic, Gazebo 9, RViz, TurtleBot3 simulation, and `move_base`. The recovered project includes `tb3_course_task`, paired course-provided maps, and evidence for mapping and multi-waypoint navigation.

## Team physical TurtleBot deployment

The team physical environment used Ubuntu 22.04, ROS2 Humble, TurtleBot3 Burger, and Cartographer. It was hosted on a teammate's computer. The public record describes the team setting and my contribution boundary; it does not publish the original ROS2 workspace.

## DQN environments

The historical course experiment used FlappyBird-v0 through the third-party Flappy Bird Gymnasium package, Python 3.11.15, and PyTorch 2.12.0. The historical observation combined 180 LiDAR values, 41 engineered features, and four-frame stacking for 884 dimensions. Later controlled algorithm ablation used raw_4frame with 720 dimensions.

The public DQN source is a documented subset. It does not include model weights, virtual environments, or a claim that a reader can reproduce an identical historical runtime without the private artifacts.
