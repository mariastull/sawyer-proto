# Sawyer Proto
For Webots

## How to use
Add Sawyer.proto and the entire Sawyer_Meshes folder into the "Protos" folder of a webots project; then, to add Sawyer to the world, select `Add New > Proto Nodes (Current Project) > Sawyer (Robot)`. Sawyer_test1.py is a basic controller that enables all motors.

### Directory
grasp_setup.wbt is a world with a table and a small object, which along with sawyer_test1.py demonstrates a very simple successful grasp

### Joints 
`right_j0, right_j1` through `right_j6` are the main joints along the arm, where joint 0 is the base and joint 6 is the wrist

`head_pan` rotates the screen

`right_gripper_l_finger_joint` and `right_gripper_r_finger_joint` operate the gripper. 

### Known issues:
Gripper is set at smallest possible opening; investigating  config options

One mesh is lost, will add to meshes folder

May need to regenerate with tighter bounding boxes if collision issues occur.


