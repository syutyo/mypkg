#!//usr/bin/env python3

import rospy
from std_msgs.msg import Int32

rospy.init_node("main2")
pub = rospy.Publisher('answer', Int32, queue_size=1)
rate = rospy.Rate(5)

print('あなたは時間がすごく知りたいです。このとき、人にどのように頼みますか？\n1.時間教えろ\n2.いま何時？\n3.時間わかる？\n4.時間教えてください')

val = input()

if val == '4':
    n = 1
    print('あたり！\n')
else:
    n = 2
    print('はずれ\n')

while not rospy.is_shutdown():
    pub.publish(n)
    rate.sleep()


