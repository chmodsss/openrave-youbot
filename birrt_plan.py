from openravepy import *
import time
env = Environment()
env.Load('environment/bullet_no_cylinder.env.xml')
env.SetViewer('qtcoin')
robot = env.GetRobots()[0]
current_pos = robot.GetDOFValues()
init_pos = current_pos
time.sleep(2)
current_pos[0]=0.01
current_pos[1]=0.01
robot.SetDOFValues(current_pos)
time.sleep(5)
robot.SetDOFValues(([ 0.01,0.01,-0.7,1.1,1.2,0.4,0.0]))
RaveSetDebugLevel(DebugLevel.Debug)
goal_pos = [0.81,0.31,1.6,0.85,1.5]
manipprob = interfaces.BaseManipulation(robot)
manipprob.MoveManipulator(goal=goal_pos)
robot.WaitForController(0)
time.sleep(5)
