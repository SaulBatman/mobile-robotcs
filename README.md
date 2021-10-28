# mobile_robotics

## Mobile Robotics Lab2
by Mingxi Jia

### Building environment
```
cd ~/catkin_ws/src
git clone -b noetic-devel https://github.com/ROBOTIS-GIT/turtlebot3_simulations.git
cd ~/catkin_ws
catkin build
source ~/catkin_ws/devel/setup.bash

export TURTLEBOT3_MODEL=burger
roslaunch turtlebot3_gazebo turtlebot3_empty_world.launch
```

### Running code
```
cd ~/catkin_ws
catkin_make
source catkin_ws/devel/setup.bash
roslaunch turtlebot3_mr turtlebot3_lab2.launch
```
```
#In a new terminal

cd ~/catkin_ws/src/turtlebot3_mr
rosrun rviz rviz -d config/rviz.rviz

```
```
#In a new terminal

roslaunch turtlebot3_mr apriltag_gazebo.launch

```
```
#In a new terminal

rosrun turtlebot3_mr mynode.py

```
