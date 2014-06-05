from openravepy import *
import time
env = Environment()
env.SetViewer('qtcoin')
env.Load('environment/bullet_floor.env.xml')
raw_input('wait')
with env:
	physics = RaveCreatePhysicsEngine(env,'bullet')
	physics.SetGravity((0,0,-9.8))
	env.SetPhysicsEngine(physics)
raw_input("hhhh")
#time.sleep(100)
