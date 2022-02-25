# Sawyer Proto
For Webots

## How to use
Add Sawyer.proto and the entire Sawyer_Meshes folder into the "Protos" folder of a webots project; then, to add Sawyer to the world, select `Add New > Proto Nodes (Current Project) > Sawyer (Robot)`

### Directory
grasp_setup.wbt is a world with a table and a small object, which along with sawyer_test1.py demonstrates a very simple successful grasp

### Joints 
`right_j0, right_j1` through `right_j6` are the main joints along the arm, where joint 0 is the base and joint 6 is the wrist

`head_pan` rotates the screen

`right_gripper_l_finger_joint` and `right_gripper_r_finger_joint` operate the gripper. (They have a very small opening; I will look to see if the gripper xacro has an option to set them in a wider position)

### Known issues:
Need to regenerate with tighter bounding boxes

One mesh is lost, will add to meshes folder
