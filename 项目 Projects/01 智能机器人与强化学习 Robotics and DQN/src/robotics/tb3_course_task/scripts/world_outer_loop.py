#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
import rospy
import actionlib

from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from actionlib_msgs.msg import GoalStatus
from tf.transformations import quaternion_from_euler


def make_goal(x, y, yaw):
    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "map"
    goal.target_pose.header.stamp = rospy.Time.now()

    goal.target_pose.pose.position.x = x
    goal.target_pose.pose.position.y = y
    goal.target_pose.pose.position.z = 0.0

    q = quaternion_from_euler(0.0, 0.0, yaw)
    goal.target_pose.pose.orientation.x = q[0]
    goal.target_pose.pose.orientation.y = q[1]
    goal.target_pose.pose.orientation.z = q[2]
    goal.target_pose.pose.orientation.w = q[3]

    return goal


def main():
    rospy.init_node("world_outer_loop")

    client = actionlib.SimpleActionClient("move_base", MoveBaseAction)
    rospy.loginfo("Waiting for move_base server...")
    client.wait_for_server()
    rospy.loginfo("Connected to move_base.")

    # 从当前机器人附近的上中位置开始，绕九个点外围走一圈
    waypoints = [
    # 上中，作为起点
    (-0.015015787445, 1.68191111088, 0.0),

    # 右上
    (1.11619114876, 1.72195637226, -math.pi / 2.0),

    # 右中
    (1.63674664497, -0.0000000639851691631, -math.pi / 2.0),

    # 右下
    (1.12620162964, -1.741979599, math.pi),

    # 下中
    (0.00500515755266, -1.83208191395, math.pi),

    # 左下
    (-1.05612707138, -1.74197912216, math.pi / 2.0),

    # 左中
    (-1.70682132244, -0.0100110638887, math.pi / 2.0),

    # 左上
    (-1.09616947174, 1.70193397999, 0.0),

    # 回到上中，闭合一圈
    (-0.015015787445, 1.68191111088, 0.0),
]

    for i, point in enumerate(waypoints):
        x, y, yaw = point

        rospy.loginfo(
            "Sending goal %d: x=%.2f, y=%.2f, yaw=%.2f",
            i + 1,
            x,
            y,
            yaw
        )

        goal = make_goal(x, y, yaw)
        client.send_goal(goal)

        finished = client.wait_for_result(rospy.Duration(90.0))

        if not finished:
            rospy.logwarn("Goal %d timeout. Canceling.", i + 1)
            client.cancel_goal()
            break

        state = client.get_state()

        if state == GoalStatus.SUCCEEDED:
            rospy.loginfo("Goal %d reached.", i + 1)
        else:
            rospy.logwarn("Goal %d failed. State=%d", i + 1, state)
            break

    rospy.loginfo("World outer loop finished.")


if __name__ == "__main__":
    main()
