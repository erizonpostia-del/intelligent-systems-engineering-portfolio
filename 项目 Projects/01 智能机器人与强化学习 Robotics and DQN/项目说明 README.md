# Learning-Based Autonomous Systems with ROS and Double Dueling DQN

# 基于 ROS 与 Double Dueling DQN 的学习型自主系统

## Project Status / 项目状态

Portfolio conversion and evidence audit in progress.

正在进行作品集转换与成果证据审计。

This project was completed as Intelligent Robotics exchange coursework at Wuhan University.

本项目完成于武汉大学交换学习期间的智能机器人课程。

Home academic background: Automation and Systems Engineering.

本科专业背景：自动化与系统工程。

## Project Overview / 项目概述

The project connects three technical layers:

本项目连接三个技术层次：

1. ROS communication and modular robot software / ROS 通信与模块化机器人软件
2. TurtleBot3 mapping, localization and navigation / TurtleBot3 建图、定位与导航
3. LiDAR-based learning control using Double Dueling DQN / 基于激光雷达和 Double Dueling DQN 的学习型控制

## Currently Verified Results / 当前已核实结果

- Implemented ROS topic communication and service communication.
- 完成 ROS 话题通信和服务通信。

- Implemented reactive obstacle avoidance using segmented LiDAR readings.
- 使用分区激光雷达数据实现反应式避障。

- Implemented multi-waypoint navigation through the move_base action interface.
- 通过 move_base Action 接口实现多目标点导航。

- Integrated TurtleBot3 mapping, localization and path-planning workflows.
- 集成 TurtleBot3 建图、定位与路径规划流程。

- Trained a Double Dueling DQN agent for 2,000 episodes.
- 完成 Double Dueling DQN 智能体 2,000 回合训练。

- Achieved score at least 10 in 36 of 50 fixed-seed evaluation episodes.
- 固定种子 50 局评估中，有 36 局达到不低于 10 分。

- Recorded a mean score of 26.12 and a maximum score of 171.
- 平均分为 26.12，最高分为 171。

- Conducted three random-seed evaluations with success results of 38 of 50, 35 of 50 and 34 of 50.
- 完成三组随机种子测试，成功结果分别为 38/50、35/50 和 34/50。

## Repository Documents / 项目文档

- 证据清单 Evidence.md
- 个人贡献 Contributions.md
- 实验环境 Environments.md
- 局限与待办 Limitations.md

## Important Notice / 重要说明

All technical claims will be reviewed against source code, logs, figures, reports or demonstration media before public release.

所有技术表述在公开前，都将通过源代码、日志、图表、原始报告或演示媒体进行核验。
