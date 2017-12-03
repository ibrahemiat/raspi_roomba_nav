# raspi_roomba_nav
# poject 4

To begin the user must download the ROS kinetic package for Ubuntu using the link below. Please make sure to install the Desktop Full (Recommended) version.

http://wiki.ros.org/kinetic/Installation/Ubuntu

*this project is to auto navigate the irobot roomba using ROS in raspberrypi, so after you install ros kinetic follow the instructions below:

Next the user needs to create a 'work space' and a ' package'. To do so please follow steps (4.1 ,4.2) in the link below:
https://www.intorobotics.com/ros-kinetic-publisher-and-subscriber-in-python/

Then save the two files found in here inside /your_work_space/src/your_pakage_name/src/

After, go to /your_work_spase directory and type:


```
$rosdep update

$rosdep install --from-paths src -i -y

$catkin_make

$source ./devel/setup.bash

$pip install pycreate2
```
In a new session/shell type to intiate roscore:
```
$cd /your_work_space
$source ./devel/setup.bash
$export ROS_MASTER_URI=http://[pi_ip_address]:11311
$export ROS_IP=[pi_ip_address]
$roscore
```
Now in the original session type to run the publishers:
```
$cd /your_work_space/src/your_pakage_name/src/
$chmod u+x 'file_names.py'
$sudo usermod -a -G dialout $USER  #give permission to the USB port to serial
$rosrun 'your_pakage_name' 'file_name.py'
```

In a new session/shell type to run the subscriber:
```
$cd /your_work_space
$source ./devel/setup.bash
$export ROS_MASTER_URI=http://[pi_ip_address]:11311
$export ROS_IP=[pi_ip_address]
$cd /your_work_space/src/your_pakage_name/src/
$chmod u+x 'file_names.py'
$rosrun 'your_pakage_name' 'file_name.py'
```

instead of a video there will be a demo
