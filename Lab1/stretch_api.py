import time
import numpy as np
import stretch_body.robot
robot = stretch_body.robot.Robot()
robot.startup()

#1
robot.stow()
robot.push_command()
robot.wait_command()

#2
robot.arm.move_to(0.52)
robot.lift.move_to(1.1)
robot.push_command()
robot.wait_command()

#3
robot.end_of_arm.move_to('wrist_yaw', np.radians(10))
robot.push_command()
robot.wait_command()
robot.end_of_arm.move_to('wrist_pitch', np.radians(10))
robot.push_command()
robot.wait_command()
robot.end_of_arm.move_to('wrist_roll', np.radians(60))
robot.push_command()
robot.wait_command()
robot.end_of_arm.move_to('stretch_gripper', 50)
robot.push_command()
robot.wait_command()
robot.end_of_arm.move_to('stretch_gripper', 0)
robot.push_command()
robot.wait_command()
robot.head.move_by('head_pan', np.radians(45)) 
robot.head.move_by('head_tilt', np.radians(45)) 
robot.push_command()
robot.wait_command()

#4
robot.stow()
robot.push_command()
robot.wait_command()

#5
robot.base.translate_by(0.5)
robot.push_command()
robot.wait_command()
robot.base.rotate_by(np.radians(180))
robot.push_command()
robot.wait_command()
robot.base.translate_by(0.5)
robot.push_command()
robot.wait_command()

time.sleep(1.0)
print("-"*15)
print('Done')

robot.stop()
