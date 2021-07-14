#! /usr/bin/env python3

from raepy import Servo
import rospy
from rae_servo_messages.srv import zero,jog,limp,hold,moveAbsolute,motorMode,reset,led

servo = Servo()

class MotorServer(object):
    def __init__(self):
        rospy.Service("~Zero", zero, self.handle_zero_request)
        rospy.loginfo("%s: initialized" % "~Zero")
        
        rospy.Service("~Jog", jog,  self.handle_jog_request)
        rospy.loginfo("%s: initialized" % "~Jog")

        rospy.Service("~Limp", limp,  self.handle_limp_request)
        rospy.loginfo("%s: initialized" % "~Limp")

        rospy.Service("~Hold", hold, self.handle_hold_request)
        rospy.loginfo("%s: initialized" % "~Hold")

        rospy.Service("~MoveAbsolute", moveAbsolute, self.handle_movabs_request)
        rospy.loginfo("%s: initialized" % "~MoveAbsolute")

        rospy.Service("~MotorMode", motorMode, self.motor_mode_request)
        rospy.loginfo("%s: initialized" % "~MotorMode")

        rospy.Service("~Reset", reset, self.motor_reset_request)
        rospy.loginfo("%s: initialized" % "~Reset")

        rospy.Service("~Led", led, self.motor_led_to)
        rospy.loginfo("%s: initialized" % "~Led")



    def handle_zero_request(self):
        servo.set_zero_here()
        return True
    
    def handle_jog_request(self,req):
        servo.jog(speed=req.speed, current=req.current)
        return True

    def handle_limp_request(self,req):
        servo.limp()
        return True

    def handle_hold_request(self,req):
        servo.hold()
        return True

    def handle_movabs_request(self,req):
        servo.move_absolute_angle(req.position,current=req.current)
        return True

    def motor_mode_request(self,req):
        return servo.get_motor_mode()

    def motor_reset_request(self,req):
        servo.reset()
        return True

    def motor_led_to(self,req):
        servo.led_to(req.color)
        if servo.actual_LED_color() == req.color:
            return True
        else:
            return False