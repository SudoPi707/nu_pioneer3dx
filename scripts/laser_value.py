import rospy

from sensor_msgs.msg import LaserScan


class LaserValue():

    def __init__(self):

        self.laser_value = {}
        rospy.Subscriber("/scan", LaserScan, self.get_laser_value)

    def get_laser_value(self, laser):

        global laser_list

        self.laser_value[90] = laser.ranges[540]
        self.laser_value[50] = laser.ranges[460]
        self.laser_value[30] = laser.ranges[420]
        self.laser_value[10] = laser.ranges[380]
        self.laser_value[-10] = laser.ranges[340]
        self.laser_value[-30] = laser.ranges[300]
        self.laser_value[-50] = laser.ranges[260]
        self.laser_value[-90] = laser.ranges[180]

        laser_list = [laser.ranges[540], laser.ranges[460],
                      laser.ranges[420], laser.ranges[380], laser.ranges[340], laser.ranges[300], laser.ranges[260], laser.ranges[180]]


if __name__ == "__main__":

    rospy.init_node("laser_value")

    program = LaserValue()

    laser_list = []

    while True:

        # print(program.laser_value)
        # print(laser_list)

        rospy.sleep(0.1)

        # print("-----------------------------------------")
