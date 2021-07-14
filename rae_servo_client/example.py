#! /usr/bin/env python3

from raerospy_servo_client.ServoClient import ServoClient
import time
import rospy


if __name__ == "__main__":

    s = ServoClient()

    while True:
        s.jog(speed=100,current=900)
        time.sleep(1)
        s.jog(speed=-100,current=900)
        time.sleep(1)
        s.limp()
        time.sleep(1)
        s.led_to("green")
        time.sleep(1)
        s.led_to("cyan")
        time.sleep(1)
        s.led_to("yellow")