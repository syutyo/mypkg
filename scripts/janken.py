#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int32

n = 0

def janken(message):
    global n
    while True:
        print('出す手を入力してください(gu,choki,parのうちのどれかを入力してください)')
        user_hand = input()
        if user_hand =='gu':
            hand = 0
        elif user_hand == 'par':
            hand = 1
        else :
            hand = 2
    
        if message.data == 0:
            cpu_hand ='gu'
        elif message.data == 1:
            cpu_hand = 'par'
        else:
            cpu_hand = 'choki'

        print('じゃん')
        rospy.sleep(2)
        print('けん')
        rospy.sleep(2)
        print('ぽん\n')
        print('あなた: ',user_hand)
        print('私 : ', cpu_hand)

        if message.data == hand:
            print('あいこもう一回！\n')
            flag = 0
        elif (message.data == 0 and hand == 1) or (message.data == 1 and hand == 2) or (message.data == 2 and hand == 0):
            n = 1
            print('あなたの勝ち！\n')
            flag = 1
        else:
            n = 2
            print('あなたの負け')
            flag = 1
        rate = rospy.Rate(5)
        if flag:
            break
    while not rospy.is_shutdown():
        pub.publish(n)
        rate.sleep()

def cb(message):
    if message.data == 2:
        sub2 = rospy.Subscriber('jankenhand', Int32, janken)
    rospy.spin()
            

rospy.init_node('janken')
pub = rospy.Publisher('answer', Int32, queue_size=1)
sub = rospy.Subscriber('select_2', Int32, cb)
rospy.spin()

