import naoqi

manager = naoqi.ALProxy("ALBehaviorManager", "192.168.0.100", 9559)
running_behaviors = manager.getRunningBehaviors()
for x in running_behaviors:
    manager.stopBehavior(x)