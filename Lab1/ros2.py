import hello_helpers.hello_misc as hm
import math

class MyNode(hm.HelloNode):
    def __init__(self):
        hm.HelloNode.__init__(self)

    def main(self):
        hm.HelloNode.main(self, 'my_node', 'my_node', wait_for_first_pointcloud=False)

        self.move_to_pose({
    'lift': 0.3,
    'arm': 0.0,
    'wrist_yaw': 0.0,
    'wrist_pitch': 0.0,
    'wrist_roll': 0.0,
    'joint_head_pan': 0.0,
    'joint_head_tilt': -0.8,
    'gripper_aperture': 0.0
                                }, blocking=True)   
        self.move_to_pose({'joint_arm': 0.52})
        self.move_to_pose({'joint_lift': 1.1}, blocking=True)
        self.move_to_pose({'joint_wrist_yaw': -1.0}, blocking=True)
        self.move_to_pose({'joint_wrist_pitch': -1.0}, blocking=True)
        self.move_to_pose({'joint_wrist_roll': -1.0}, blocking=True)
        self.move_to_pose({'gripper_aperture': 0.05}, blocking=True)
        self.move_to_pose({'gripper_aperture': 0.0}, blocking=True)
        self.move_to_pose({'joint_head_pan': 0.0, 'joint_head_tilt': -0.3}, blocking=True)
        self.move_to_pose({
    'lift': 0.3,
    'arm': 0.0,
    'wrist_yaw': 0.0,
    'wrist_pitch': 0.0,
    'wrist_roll': 0.0,
    'joint_head_pan': 0.0,
    'joint_head_tilt': -0.8,
    'gripper_aperture': 0.0
                                }, blocking=True)
        self.move_base_linear(0.5, blocking=True)
        self.move_base_rotation(math.pi, blocking=True)
        self.move_base_linear(0.5, blocking=True)

node = MyNode()
node.main()