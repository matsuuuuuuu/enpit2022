#!/usr/bin/env python
import rospy


from std_msgs.msg import Header
from nav_msgs.msg import Odometry
from pos_srv.srv import pos, posResponse
#from geometry_msgs.msgs import Point
#from geometry_msgs.msgs import Quaternion

x=0.0
y=0.0
#z=0.0

object = [['box1', 1.5024, 3.92435],
         ['box2', 7.9082, 2.42908],
         ['cylinder1', 7.62584, 5.74044],
         ['sphere1', 2.8558, 1.83817]]

def callback(msg):
    global x,y

    #rospy.loginfo("recieved pos")
    #rospy.loginfo("Message '%4f' recieved", msg.pose.pose.position.x)

    x=msg.pose.pose.position.x
    y=msg.pose.pose.position.y

def check_pos(order):
    global x,y

    rospy.loginfo("recieved order")
    rospy.loginfo("x='%5f', y='%5f'", x, y)

    px = x
    py = y

    for i in range(len(object)):
        if object[i][1]-1 < px < object[i][1]+1:
            rospy.loginfo("name=%s x='%5f', y='%5f'", object[i][0], object[i][1], object[i][2])
            if object[i][2]-1 < py < object[i][2]+1:
                rospy.loginfo("Get!!")
                result = object[i][0]
                return posResponse(result)

    
    result = 'NONE'
    return posResponse(result)

def server():
    rospy.Service("Check_Pos", pos, check_pos)
    rospy.loginfo("create service_server!")

def subscriber():
    subscriber=rospy.Subscriber("/mavros/global_position/local", Odometry, callback)
    rospy.loginfo("create subscriber!")

def main():
    rospy.init_node("pos_server_node")
    subscriber()
    server()
    rospy.spin()    

if __name__ == "__main__":
    main()