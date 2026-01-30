import hello_helpers.hello_misc as hm
import math
import numpy as np

class MyNode(hm.HelloNode):
    def __init__(self):
        hm.HelloNode.__init__(self)

    def main(self):
        hm.HelloNode.main(self, 'my_node', 'my_node', wait_for_first_pointcloud=False)

        self.stow_the_robot()   
        self.move_to_pose({'joint_arm': 0.52},{'joint_lift': 1.1})
        self.move_to_pose({'joint_wrist_yaw': -1.0}, blocking=True)
        self.move_to_pose({'joint_wrist_pitch': -1.0}, blocking=True)
        self.move_to_pose({'joint_wrist_roll': -1.0}, blocking=True)
        self.move_to_pose({'gripper_aperture': 0.05}, blocking=True)
        self.move_to_pose({'gripper_aperture': 0.0}, blocking=True)
        self.move_to_pose({'joint_head_pan': 0.0, 'joint_head_tilt': -0.3}, blocking=True)
        self.stow_the_robot()
        self.move_to_pose({'translate_mobile_base': 0.5}, blocking=True)
        self.move_to_pose({'rotate_mobile_base': np.deg2rad(180)}, blocking=True)
        self.move_to_pose({'translate_mobile_base': 0.5}, blocking=True)
        self.destory_node()

if __name__ == 'main':
    node = MyNode()
    node.main()