#!//usr/bin/env python3

import rospy
from std_msgs.msg import Int32

i = 0

def cb(message):
    global i
    if message.data ==1:
        print('問題:あなたが時間が知りたい時、人にどのように頼みますか？ 正しいと思う数字を入力してください\n1.時間教えろ\n2.いま何時？\n3.時間わかる？\n4.時間教えてください')
        val = input()
        if val == '4':
            i = 1
            print('あたり！\n')
            
        else:
            i = 2
            print('はずれ\n')

        rate = rospy.Rate(5)

        while not rospy.is_shutdown():
            pub.publish(i)
            rate.sleep()

rospy.init_node("problem")
pub = rospy.Publisher('answer', Int32, queue_size=1)
sub = rospy.Subscriber('select_1', Int32, cb)
rospy.spin()

