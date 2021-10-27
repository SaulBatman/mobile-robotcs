#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from apriltag_ros.msg import AprilTagDetectionArray
from geometry_msgs.msg import Vector3

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + data)
    #rospy.loginfo(rospy.get_caller_id() + "I heard %d", data.detections.pose.pose.position.z)

    
def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)

    sub = rospy.Subscriber("tag_detection", AprilTagDetectionArray, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
