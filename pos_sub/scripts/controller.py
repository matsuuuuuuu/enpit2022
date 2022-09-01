#!/usr/bin/env python
import rospy

from pos_srv.srv import pos
from std_msgs.msg import String


def main():
    rospy.init_node('controller')

    #init publisher 
    publisher=rospy.Publisher("/gnc_node/cmd", String, queue_size=10)
    msg = ""

    rospy.wait_for_service('Check_Pos')

    # you can use 'Check_Pos' like local function.
    check_position = rospy.ServiceProxy('Check_Pos', pos)

    rate = rospy.Rate(1)

    while not rospy.is_shutdown():
        enter = raw_input('>>')
        if enter=='r':
            msg = "start"
        elif enter=='w':
            msg = "forward"
        elif enter=='s':
            msg = "backward"
        elif enter=='a':
            msg = "left"
        elif enter=='d':
            msg = "right"
        elif enter=='z':
            msg = "grab"
        else:
            msg = "stop"
    
        rospy.loginfo("Publish: '{}'".format(msg))
        publisher.publish(msg)

        if enter=='z':
            # order 'Check_Pos' service and get response.   
            response = check_position("order")
            if response.result == 'NONE':
                 rospy.loginfo("Result: False.. ")
            else:
                rospy.loginfo("Result: Get '{}' !!".format(response.result))

        #interval
        rate.sleep()


if __name__ == "__main__":
    main()
