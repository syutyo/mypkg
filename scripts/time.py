#!/usr/bin/env python3

import rospy
import datetime
from std_msgs.msg import Int32

def cb(message):
    if message.data ==1:
        time_easy = datetime.datetime.now()
        print('現在時刻はこちらです：',time_easy)
        rospy.sleep(1000)
    else:
        time_hard = rospy.get_time()
        print('現在時刻はこれ、自分で計算して: ',time_hard)
        rospy.sleep(1000)
        
rospy.init_node('time')
sub = rospy.Subscriber('answer',Int32,cb)
rospy.spin()




