#!/usr/bin/env python  
import rospy
import numpy as np
import math
import tf2_ros
import geometry_msgs.msg
import turtlesim.srv
from scipy.linalg import solve, logm
import time

if __name__ == '__main__':
    rospy.init_node('tf2_turtle_listener')

    tfBuffer = tf2_ros.Buffer()
    listener = tf2_ros.TransformListener(tfBuffer)

    #rospy.wait_for_service('spawn')
    #spawner = rospy.ServiceProxy('spawn', turtlesim.srv.Spawn)
    #turtle_name = rospy.get_param('turtle', 'turtle2')
    #spawner(4, 2, 0, turtle_name)

    #turtle_vel = rospy.Publisher('%s/cmd_vel' % turtle_name, geometry_msgs.msg.Twist, queue_size=1)

    rate = rospy.Rate(10.0)
    while not rospy.is_shutdown():
        try:
            trans = tfBuffer.lookup_transform('base_footprint', 'tag_0', rospy.Time())
            a = trans.transform.translation
            X = np.eye(3)
            Y = np.array([[1,0,a.x-0.12],[0,1,a.y],[0,0,1]])
            break
        except (tf2_ros.LookupException, tf2_ros.ConnectivityException, tf2_ros.ExtrapolationException):
            rate.sleep()
            continue

    mymsg = geometry_msgs.msg.Twist()
    
        #msg.angular.z = 4 * math.atan2(trans.transform.translation.y, trans.transform.translation.x)
        #msg.linear.x = 0.5 * math.sqrt(trans.transform.translation.x ** 2 + trans.transform.translation.y **2) 
    
    T = 10
    
    ome = logm(solve(X,Y))/T

    mymsg.linear.x= ome[0,2]
    mymsg.angular.z = -ome[0,1]
    pub = rospy.Publisher('/cmd_vel', geometry_msgs.msg.Twist, queue_size=10)
    start_t=time.time()
    
    while not rospy.is_shutdown():
        pub.publish(mymsg)
        rate.sleep()

        if time.time()-start_t==10:
            break

    while not rospy.is_shutdown():
        mymsg.linear = [0,0,0]
        mymsg.angular = [0,0,0]
        pub.publish(mymsg)

