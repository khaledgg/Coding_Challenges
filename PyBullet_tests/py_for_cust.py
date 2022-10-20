import numpy as np
import pybullet as p
import pybullet_data
import time

p.connect(p.DIRECT) #use p.DIRECT for faster than realtime simulationm p.GUI to see whats going on
p.resetSimulation()
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)
p.setRealTimeSimulation(0)

# time.sleep(5.01)
pos1 = [0,0,0.8]
pos2= [-1.5,0,0.8]
start_pos = pos2

#Load assets
p.loadURDF("plane.urdf",[0,0,0],[0,0,0,1]) #pass orientation as a quarternian
targid = p.loadURDF("table/table.urdf",[0,0,0],[0,0,0,1], useFixedBase=True)
ball_id = p.loadURDF("sphere_small.urdf",start_pos,[0,0,0,1])
obj_of_focus = ball_id

#give initial velocity
# p.resetBaseVelocity(model, [x1, y1, z1], [x2, y2, z2]) #[x1,..] linear velocity [x2,.] angular velocity
p.resetBaseVelocity(obj_of_focus, [5, 0, 0], [0, 0, 0])

#change bouncyness
p.changeDynamics(obj_of_focus, -1, restitution=0.9)
p.changeDynamics(targid, -1, restitution=0.9) #need to make table bouncy as well


startTime = time.time()*1000
for step in range(75):
    focus_position, _ = p.getBasePositionAndOrientation(targid)
    # p.resetDebugVisualizerCamera(cameraDistance = 4, cameraYaw=0, cameraPitch = -40, cameraTargetPosition=focus_position)
    p.stepSimulation()
    time.sleep(0.01)
endTime=time.time()*1000
print(endTime - startTime)

