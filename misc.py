p = RaveCreatePhysicsEngine(env,'bullet')
env.SetPhysicsEngine(p)
robot = env.GetRobots()[0]
robot.SetDOFValues([2.58, 0.547, 133, -0.7],[0,1,2,3])
robot.GetDOFValues()
mug = env.GetBodies()[2]
gmodel = databases.grasping.GraspingModel(robot,mug)
init_values = robot.GetDOFValues(gmodel.manip.GetArmIndices())







---------- Unwanted ----------------------------
robot = env.ReadRobotXMLFile('robots/pr2-beta-static.zae')
env.Add(robot)
target = env.ReadKinBodyXMLFile('data/mug2.kinbody.xml')
env.Add(target)
env.Remove(robot)
env.RemoveKinBody(target)
target.SetConfigurationValues([1,1,1,3,3,4,1])
target.SetZeroConfiguration()
gmodel.manip.GetName()
gmodel.manip.GetIndependentLinks()[0]
