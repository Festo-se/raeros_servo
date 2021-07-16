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
The following command drives the Motor with 100 °/sec and stops if there is an resistance which leads to more than 900 mAmps.

```python
servo.jog(speed=100, current=900)
```
Without specified parameters `servo.jog()` the default value for the current is 700. The Speed also determines the direction. For example if you specify -100 as speed parameter `servo.jog(-100)` it drives in the opposite direction.

## Hold
## Limp
## Zeroing
## MoveAbsolute
## Reset
## Led
## Motormode
Can be `Unknown, Limp, Free Moving,Accelerating, Traveling, Decelerating, Holding, Outside limits, Stuck, Blocked, Safe Mode`
