from openravepy import *
import time
env = Environment()
env.Load('environment/kuka-youbot-hires.zae')
env.SetViewer('qtcoin')
'''robot = env.GetRobots()[0]
box = env.GetBodies()[2]
val = robot.GetDOFValues()
time.sleep(20)
val[0]=0.01
val[1]=0.01
robot.SetDOFValues(val)
time.sleep(5)
robot.SetDOFValues([0.01,0.01,0.0,-0.9,-1.4,-1.9,0.0])'''
time.sleep(10)
