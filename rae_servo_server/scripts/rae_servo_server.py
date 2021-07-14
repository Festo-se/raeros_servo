#! /usr/bin/env python3

import rospy


from raerospy_servo.Servo import MotorServer



if __name__ == "__main__":
    rospy.init_node('rae_servo_server')
    MotorServer()
    rospy.spin()   