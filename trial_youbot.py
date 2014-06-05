from openravepy import *
import time
env = Environment()
env.Load('environment/bullet_no_cylinder.env.xml')
env.SetViewer('qtcoin')
robot = env.GetRobots()[0]
box = env.GetBodies()[2]
current_pos = robot.GetDOFValues()
init_pos = current_pos
time.sleep(2)
current_pos[0]=0.01
current_pos[1]=0.01
robot.SetDOFValues(current_pos)
time.sleep(5)
#robot.SetDOFValues([0.01,0.01,0.0,0.8,1.3,0.7,0.0])
#robot.SetDOFValues([0.01,0.01,0.0,-0.9,-1.4,-1.9,0.0])
goal_pos = [0.01,0.01,0.0,1.15,1.2,0.55,0.0]
robot.SetDOFValues(goal_pos)
time.sleep(10)
