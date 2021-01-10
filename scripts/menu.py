#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int32

rospy.init_node('menu')
rate = rospy.Rate(5)

print('あなたは時間がすごく知りたいです。正確な時間は私しか知りません。\nあなたが時間を知るためには、私が出す問題を解くか、私とじゃんけんをしなければなりません。\nどちらをやりますか？問題なら"１"、じゃんけんなら"２"を入力してください')

mode = input()

if mode == '1':
    n = 1
    pub = rospy.Publisher('select_1', Int32, queue_size = 1)
elif mode == '2':
    n = 2
    pub = rospy.Publisher('select_2', Int32, queue_size = 1)

while not rospy.is_shutdown():
    pub.publish(n)
    rate.sleep()


    
