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
RaveSetDebugLevel(DebugLevel.Debug)
goal_pos = [0.01,0.01,0.0,1.15,1.2,0.55,0.0]
manipprob = interfaces.BaseManipulation(robot)
manipprob.MoveManipulator(goal=goal_pos)
robot.WaitForController(0)
