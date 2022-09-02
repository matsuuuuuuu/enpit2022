#!/usr/bin/env python
import rospy
import time

from std_msgs.msg import Header
from nav_msgs.msg import Odometry
from pos_srv.srv import pos, posResponse
from gazebo_msgs.srv import DeleteModel

x=0.0
y=0.0
#z=0.0


object = [['box1', 1.5024, 3.92435],
         ['box2', 7.9082, 2.42908],
         ['cylinder1', 7.62584, 5.74044],
         ['sphere1', 2.8558, 1.83817]]

class check_pos_server:
    def __init__(self, fnc):
        rospy.Service("Check_Pos", pos, self.check_pos)
        rospy.loginfo("create service_server!")
        self.fnc = fnc
        
    
    def check_pos(self, order):

        rospy.loginfo("recieved order")
        #rospy.loginfo("x='%5f', y='%5f'", x, y)

        px = x
        py = y

        for i in range(len(object)):
            if object[i][1]-1 < px < object[i][1]+1:
                rospy.loginfo("name=%s x='%5f', y='%5f'", object[i][0], object[i][1], object[i][2])
                if object[i][2]-1 < py < object[i][2]+1:
                    rospy.loginfo("Get!!")
                    result = object[i][0]
                    time.sleep(5)
                    res = self.fnc(object[i][0])
                    rospy.loginfo('result:{}'.format(res.success))
                    return posResponse(result)
    
        result = 'NONE'
        return posResponse(result)

def callback(msg):
    global x,y

    #rospy.loginfo("recieved pos")
    #rospy.loginfo("Message '%4f' recieved", msg.pose.pose.position.x)

    x=msg.pose.pose.position.x
    y=msg.pose.pose.position.y


def subscriber():
    subscriber=rospy.Subscriber("/mavros/global_position/local", Odometry, callback)
    rospy.loginfo("create subscriber!")

def client():
    rospy.wait_for_service('/gazebo/delete_model')
    delete_obj = rospy.ServiceProxy('/gazebo/delete_model', DeleteModel)

    return delete_obj

def main():
    rospy.init_node("pos_server_node")
    
    delete_obj = client()
    subscriber()
    server = check_pos_server(delete_obj)

    rospy.spin()    

if __name__ == "__main__":
    main()