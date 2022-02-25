# Sawyer Proto
For Webots

10 joints: 
right_j0, right_j1, ...., right_j6 where j0 is the base and j6 is the wrist

head_pan rotates the screen

right_gripper_l_finger_joint and right_gripper_r_finger_joint operate the gripper. (They have a very small opening; I will look to see if the gripper xacro has an option to set them in a wider position)

Known issues:
Need to regenerate with tighter bounding boxes
One mesh is lost, will add to meshes folder
