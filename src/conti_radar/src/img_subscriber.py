import rospy
from std_msgs.msg import String
from conti_radar.msg import radar_img
from datetime import datetime


def callback(data):
    timestamp = datetime.now()
    timestamp = timestamp.strftime("%H:%M:%S.%f")
    print(timestamp)
    print("x_range: {} , y_dist:  {} " .format(len(data.x_dist),len(data.y_dist)))




def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber('/radar_img', radar_img, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
