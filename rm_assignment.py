from openravepy import *
import time
env = Environment()
env.Load('environment/bullet_no_cylinder.env.xml')
env.SetViewer('qtcoin')
robot = env.GetRobots()[0]
target = env.GetKinBody('box')
init_pos = robot.GetDOFValues()
taskmanip = interfaces.TaskManipulation(robot)
taskmanip.ReleaseFingers()
gmodel = databases.grasping.GraspingModel(robot,target)
if not gmodel.load():
	gmodel.autogenerate()

validgrasps, validindices = gmodel.computeValidGrasps(returnnum=1)
gmodel.moveToPreshape(validgrasps[0])
Tgoal = gmodel.getGlobalGraspTransform(validgrasps[0],collisionfree=True)
basemanip = interfaces.BaseManipulation(robot)
basemanip.MoveToHandPosition(matrices=[Tgoal])
robot.WaitForController(0)
taskmanip = interfaces.TaskManipulation(robot)
taskmanip.CloseFingers()
robot.SetDOFValues(([ 0.01,0.01,-0.7,1.1,1.2,0.4,0.0]))
robot.WaitForController(0)
