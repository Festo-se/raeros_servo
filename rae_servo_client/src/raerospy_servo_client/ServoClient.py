from rae_servo_messages.srv import angle, calibrate, hold, jog, led, limp, motorMode, moveAbsolute, reset, zero
import rospy

class ServoClient(object):
    def __init__(self):
        rospy.wait_for_service("/rae_servo_server/Hold")
        self.hold = rospy.ServiceProxy("/rae_servo_server/Hold", hold)
        self.__jog = rospy.ServiceProxy("/rae_servo_server/Jog", jog)
        self.led_to = rospy.ServiceProxy("/rae_servo_server/Led",led)
        self.limp = rospy.ServiceProxy("/rae_servo_server/Limp", limp)
        self.motorMode = rospy.ServiceProxy("/rae_servo_server/MotorMode", motorMode)
        self.moveAbsolute = rospy.ServiceProxy("/rae_servo_server/Limp", limp)
        self.reset = rospy.ServiceProxy("/rae_servo_server/reset", reset)
        self.zero = rospy.ServiceProxy("/rae_servo_server/zero", zero)

    def jog(self,speed=50,current=700):
        self.__jog(speed,current)