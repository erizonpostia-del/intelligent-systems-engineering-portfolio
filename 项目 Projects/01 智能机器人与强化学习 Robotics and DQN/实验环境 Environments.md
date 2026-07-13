# Experimental Environments

# 实验环境说明

## Environment A: ROS1 Communication and Simulation

## 环境 A：ROS1 通信与仿真

- Operating system / 操作系统：Ubuntu 18.04.6
- ROS distribution / ROS 发行版：Melodic
- ROS generation / ROS 版本体系：ROS1
- Robot model / 机器人模型：TurtleBot3 Waffle Pi
- Simulator / 仿真器：Gazebo
- Visualization / 可视化：RViz
- Main languages / 主要语言：C++ and Python
- Verification required / 待核实：具体软件包版本

## Environment B: Physical TurtleBot3 Deployment

## 环境 B：TurtleBot3 真机部署

- Operating system / 操作系统：待确认
- ROS distribution / ROS 发行版：待确认
- ROS generation / ROS 版本体系：ROS2
- Robot model / 机器人型号：待确认
- Host computer / 主机环境：待确认
- Robot computer / 机器人端环境：待确认
- Network setup / 网络配置：待确认

## Environment C: Double Dueling DQN

## 环境 C：Double Dueling DQN

- Operating system / 操作系统：待确认
- Python version / Python 版本：待确认
- Deep learning framework / 深度学习框架：PyTorch，版本待确认
- Environment / 实验环境：FlappyBird-v0
- Raw observation / 原始观测：180-dimensional LiDAR
- Frame stack / 帧堆叠：4
- Final observation dimension / 最终输入维度：884
- Training episodes / 训练回合：2000
- CPU or GPU / 训练设备：待确认

## Important Consistency Issue / 重要一致性问题

The ROS1 simulation environment and ROS2 physical deployment environment must be documented separately.

ROS1 仿真环境与 ROS2 真机部署环境必须分开记录，不能混写为同一套环境。
