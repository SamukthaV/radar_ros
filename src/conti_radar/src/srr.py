import rospy
from std_msgs.msg import String
from std_msgs.msg import Int32
from conti_radar.msg import radar_obj



def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.id) 
    if data.id == 0:
        print("Objects found on left")
    elif data.id == 1:
        print("Objects found on right") 
    # perfomring all the prepocessing required and publishing onto a new topic
    # warning = filter(data.f_DistX)
    # pub = rospy.Publisher('/srr_flag', Int32, queue_size=1000)
    # pub.publish(warning)  

# def filter(value):
#     #performing the filtering operation
#     if any(value) <8:
#         warning = 0
#     else:
#         warning = 1
#     print("###################################3",warning)
#     return warning

def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("/radar_srr_obj", radar_obj, callback)
    rospy.spin()


if __name__ == '__main__':
    listener()