#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist


class HouseAutoAvoid(object):
    def __init__(self):
        rospy.init_node("house_auto_avoid")

        self.cmd_pub = rospy.Publisher("/cmd_vel", Twist, queue_size=10)
        self.scan_sub = rospy.Subscriber("/scan", LaserScan, self.scan_callback)

        self.front_dist = float("inf")
        self.left_dist = float("inf")
        self.right_dist = float("inf")
        self.front_left_dist = float("inf")
        self.front_right_dist = float("inf")

        self.rate = rospy.Rate(10)
        rospy.on_shutdown(self.stop_robot)

    def valid_min(self, values):
        clean = []
        for v in values:
            if math.isnan(v) or math.isinf(v):
                continue
            if v <= 0.02:
                continue
            clean.append(v)

        if len(clean) == 0:
            return float("inf")

        return min(clean)

    def get_sector(self, ranges, start, end):
        n = len(ranges)

        if start < 0:
            start = 0
        if end > n:
            end = n

        return ranges[start:end]

    def scan_callback(self, msg):
        ranges = list(msg.ranges)
        n = len(ranges)

        # TurtleBot3 激光雷达通常是 360 度。
        # 0 度附近为正前方，因此前方需要取数组开头和末尾两部分。
        front = ranges[0:25] + ranges[n - 25:n]

        # 左前、右前、左侧、右侧区域。
        front_left = self.get_sector(ranges, 25, 75)
        left = self.get_sector(ranges, 75, 130)

        front_right = self.get_sector(ranges, n - 75, n - 25)
        right = self.get_sector(ranges, n - 130, n - 75)

        self.front_dist = self.valid_min(front)
        self.front_left_dist = self.valid_min(front_left)
        self.front_right_dist = self.valid_min(front_right)
        self.left_dist = self.valid_min(left)
        self.right_dist = self.valid_min(right)

    def run(self):
        rospy.loginfo("House auto avoid node started.")
        rospy.loginfo("Robot will move autonomously using /scan and /cmd_vel.")

        while not rospy.is_shutdown():
            cmd = Twist()

            front_safe = 0.60
            side_safe = 0.38

            rospy.loginfo_throttle(
                1.0,
                "front=%.2f front_left=%.2f front_right=%.2f left=%.2f right=%.2f",
                self.front_dist,
                self.front_left_dist,
                self.front_right_dist,
                self.left_dist,
                self.right_dist
            )

            # 情况 1：正前方太近，停止前进并转向较空的一侧。
            if self.front_dist < front_safe:
                cmd.linear.x = 0.0

                if self.front_left_dist > self.front_right_dist:
                    cmd.angular.z = 0.65
                    rospy.loginfo_throttle(1.0, "Obstacle ahead. Turning left.")
                else:
                    cmd.angular.z = -0.65
                    rospy.loginfo_throttle(1.0, "Obstacle ahead. Turning right.")

            # 情况 2：左前方太近，向右修正。
            elif self.front_left_dist < side_safe or self.left_dist < side_safe:
                cmd.linear.x = 0.10
                cmd.angular.z = -0.35
                rospy.loginfo_throttle(1.0, "Too close on left. Adjusting right.")

            # 情况 3：右前方太近，向左修正。
            elif self.front_right_dist < side_safe or self.right_dist < side_safe:
                cmd.linear.x = 0.10
                cmd.angular.z = 0.35
                rospy.loginfo_throttle(1.0, "Too close on right. Adjusting left.")

            # 情况 4：前方安全，正常前进。
            else:
                cmd.linear.x = 0.16
                cmd.angular.z = 0.0
                rospy.loginfo_throttle(1.0, "Path clear. Moving forward.")

            self.cmd_pub.publish(cmd)
            self.rate.sleep()

    def stop_robot(self):
        rospy.loginfo("Stopping robot.")
        cmd = Twist()
        self.cmd_pub.publish(cmd)


if __name__ == "__main__":
    node = HouseAutoAvoid()
    node.run()
