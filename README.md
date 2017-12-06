# Poject 4: Roomba Control Algorithm for Obstacle Avoidance Using ROS

- Group 4: 
  - Ibrahim Ahmed
  - Danny Asmaro
  - Sharon Obiefuna

## About

For this project, the ROS package is used to establish an obstacle avoidance ROS navigation node as shown in the figure below.

<img width="595" alt="capture" src="https://user-images.githubusercontent.com/31410235/33640046-4cfa3654-d9fc-11e7-9b90-45acca5eea6e.PNG">

- **Publisher Node:** to publish six obstacle sensors’ reading 
- **Subscriber Node:** to drive left and right wheels of the Roomba depending on the sensor reading. 

## Getting Started

- To begin the user must download the ROS kinetic package for Ubuntu. [Click hrere to download ROS Kinetic](http://wiki.ros.org/kinetic/Installation/Ubuntu). *Please make sure to install the Desktop Full (Recommended) version.*

*Note: this project is to auto navigate the irobot roomba using ROS in raspberrypi, so after you install ros kinetic follow the instructions below:

- Next the user needs to create a 'work space' and a ' package'. To do so please follow steps (4.1 ,4.2) in the link below:
[ROS Kinetic Publisher and Subscriber In Python](https://www.intorobotics.com/ros-kinetic-publisher-and-subscriber-in-python/).

Then save the two files found in here inside /your_work_space/src/your_pakage_name/src/

- After, go to /your_work_spase directory and type:


```
$rosdep update

$rosdep install --from-paths src -i -y

$catkin_make

$source ./devel/setup.bash

$pip install pycreate2
```
- In a new session/shell type to intiate roscore:
```
$cd /your_work_space
$source ./devel/setup.bash
$export ROS_MASTER_URI=http://[pi_ip_address]:11311
$export ROS_IP=[pi_ip_address]
$roscore
```
- Now in the original session type to run the publishers:
```
$cd /your_work_space/src/your_pakage_name/src/
$chmod u+x 'file_names.py'
$sudo usermod -a -G dialout $USER  #give permission to the USB port to serial
$rosrun 'your_pakage_name' 'file_name.py'
```

- In a new session/shell type to run the subscriber:
```
$cd /your_work_space
$source ./devel/setup.bash
$export ROS_MASTER_URI=http://[pi_ip_address]:11311
$export ROS_IP=[pi_ip_address]
$cd /your_work_space/src/your_pakage_name/src/
$chmod u+x 'file_names.py'
$rosrun 'your_pakage_name' 'file_name.py'
```

*Note to Professor/TA: Instead of a video there will be a demo.*
