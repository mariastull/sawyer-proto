"""sawyer_test1 controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot

# create the Robot instance.
robot = Robot()

# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())


right_j0 = robot.getDevice("right_j0")
head_pan = robot.getDevice("head_pan")
right_j1 = robot.getDevice("right_j1")
right_j2 = robot.getDevice("right_j2")
right_j3 = robot.getDevice("right_j3")
right_j4 = robot.getDevice("right_j4")
right_j5 = robot.getDevice("right_j5")
right_j6 = robot.getDevice("right_j6")
l_finger_joint = robot.getDevice("right_gripper_l_finger_joint")
r_finger_joint = robot.getDevice("right_gripper_r_finger_joint")

print("Number of devices", robot.getNumberOfDevices())
def byIndexSetUp():

    deviceList = [right_j0, head_pan, right_j1, right_j2, 
    right_j3, right_j4, right_j5, right_j6,  
    l_finger_joint, r_finger_joint]
    nameList = ["right_j0", "head_pan", "right_j1", "right_j2", 
    "right_j3", "right_j4", "right_j5", "right_j6", 
    "right_gripper_l_finger_joint", "right_gripper_r_finger_joint"]

    for i in range(robot.getNumberOfDevices()):
        
        # Odd-indexed devices are sensors in our proto
        if i%2 != 0:
            continue
            
        tag = robot.getDeviceByIndex(i)
        
        try:
            ind = nameList.index(tag.getName())
            
            device = deviceList[ind]
            
            device = tag
            
        except:
            ind = -1
 
if head_pan is None:
    byIndexSetUp()


r_finger_joint.setPosition(r_finger_joint.getMaxPosition())
l_finger_joint.setPosition(l_finger_joint.getMinPosition())
print("Grasping")
for i in range(20):
    robot.step(timestep)
print("Moving arm")
right_j1.setPosition(-1)

right_j0.setPosition(1)

# Main loop:
# - perform simulation steps until Webots is stopping the controller
while robot.step(timestep) != -1:
    # Read the sensors:
    # Enter here functions to read sensor data, like:
    #  val = ds.getValue()

    # Process sensor data here.

    # Enter here functions to send actuator commands, like:
    #  motor.setPosition(10.0)
    pass

# Enter here exit cleanup code.
