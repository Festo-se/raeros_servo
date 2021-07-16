# About
The `raeros_servo` package is based on ROS and consists of several ROS-services to access the functionalities of the Lynsmotion LSS Smartservo. 
More information about the servomotor you get [here](https://www.robotshop.com/info/wiki/lynxmotion/view/lynxmotion-smart-servo/).

# Installation
Install it from source with:

```bash
cd ~/catkin_ws/src &&
git clone -b melodic https://github.com/romzn/raeros_servo.git &&
cd ../../ &&
catkin_make
```
# Functions
First of all create a ros-package and open a new python file inside the `scripts` folder.
```python
from raerspy_servo_client.ServoClient import ServocClient()
import rospy

if __name__ == "__main__":
    rospy.init_node()
    servo = ServoClient()
    # User code
```
## Jogging
Jogging let drives the servomotor with an specified velocity. 
The following command drives the Motor with 100 °/sec and stops if there is an resistance which leads to more than 900 mAmps. After stopping it holds the Position with 400 mAmps.

```python
servo.jog(speed=100, current=900)
```
Without specified parameters `servo.jog()` the default value for the current is 700. The Speed also determines the direction. For example if you specify -100 as speed parameter `servo.jog(-100)` the servo drives in the opposite direction.

## Hold
The Servomotor holds the current position with a maximum of 400 mA which is about 3 Nm stall torque.
```python
servo.hold()
```

## Limp
The servomotor turns the current off so that rotating the shaft by hand is possible
```python
servo.limp()
```

## Zeroing
Sets the current position to zero. This is important for absolute position commands.
```python
servo.zero()
```

## MoveAbsolute
```python
servo.moveAbsolute(position=2000, current=900)
```
## Reset
Resets the motor. This is necessary to recover the motor when it is in error state.
```python
servo.reset()
```
## Led
Change the color of the servo LED to your preffered color.
```python
servo.led_to(color)
```
avaliable colors : [black, red, green, blue, yellow, cyan, magenta, white]

## Motormode
Returns the motor mode as string.
```python
servo.motorMode()
```
Can be `Unknown, Limp, Free Moving, Accelerating, Traveling, Decelerating, Holding, Outside limits, Stuck, Blocked, Safe Mode`
