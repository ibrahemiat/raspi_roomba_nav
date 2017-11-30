
#!/usr/bin/env python
from __future__ import print_function
import rospy
from pycreate2 import Create2
import time

from std_msgs.msg import Int32,String
#define the display text
port = '/dev/ttyUSB0'
baud = {
    'default': 115200,
    'alt': 19200  # shouldn't need this unless you accident$
}
bot = Create2(port=port, baud=baud['default'])

bot.start()

bot.full()

bot.drive_straight(-35)
time.sleep(2)

def callback(data):
    m = data.data.split()
    print(m)
    if (int(m[0])>100):
        bot.drive_direct(-35, 35)
    elif (int(m[1])>100):
        bot.drive_direct(-35, 35)
    elif (int(m[2])>100):
        bot.drive_direct(-35, 35)
    elif (int(m[3])>100):
        bot.drive_direct(35, -35)
    elif (int(m[4])>100):
        bot.drive_direct(35, -35)
    elif (int(m[5])>100):
        bot.drive_direct(35, -35)
    else:
        bot.drive_straight(35)


#define the subscriber
def random_subscriber():
    rospy.init_node('wheel_subscriber')
    rospy.Subscriber('sensor_values',String, callback)
    rospy.spin()

if __name__=='__main__':
    random_subscriber()

