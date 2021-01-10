#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32

rospy.init_node('janken_r')
pub = rospy.Publisher('jankenhand', Int32, queue_size=1)
rate = rospy.Rate(5)

n=0
while not rospy.is_shutdown():
    pub.publish(n)
    n += 1
    if n>2:
        n=0
    rate.sleep()
