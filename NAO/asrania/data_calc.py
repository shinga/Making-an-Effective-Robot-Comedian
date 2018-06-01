#! /usr/bin/env python
# -*- encoding: UTF-8 -*-

import audio_sense as ad
import frame_sense as fs
import argparse
import qi
import naoqi
import time
import sys

def doJoke(MySoundProcessingModule, state):
    manager = naoqi.ALProxy("ALBehaviorManager", "192.168.0.100", 9559)
    sound_level = 0.0
    running_behaviors = manager.getRunningBehaviors()
    for x in running_behaviors:
        manager.stopBehavior(x)
    
    dict_behavior = {"expointro-a9caec/calibrateFunnyRobot": 0.0, 
                     "expointro-a9caec/calibrateLameRobot": 0.0 ,
                     "expointro-a9caec/topics": 0.0,
                     "expointro-a9caec/askJobs": 0.0,
                     "expointro-a9caec/askAging": 0.0,
                     "expointro-a9caec/askRomance": 0.0, }

    list_behavior = ["expointro-a9caec/calibrateFunnyRobot", 
                    "expointro-a9caec/calibrateLameRobot",
                    "expointro-a9caec/topics",
                    "expointro-a9caec/askJobs",
                    "expointro-a9caec/askAging",
                    "expointro-a9caec/askRomance"]

    print "Got state ---- " + state     

    for behav in list_behavior:
        manager.startBehavior(behav)
        sound_level = MySoundProcessingModule.startProcessing()
        dict_behavior[behav] = sound_level

        print "Behavior ---- " + str(behav)
        print "Sound Average ---- " + str(sound_level)

    if (dict_behavior["expointro-a9caec/askAging"] > dict_behavior["expointro-a9caec/askJobs"] and 
    dict_behavior["expointro-a9caec/askAging"] > dict_behavior["expointro-a9caec/askRomance"]): 
        manager.runBehavior("expointro-a9caec/confirmAging")
        if state == "h":
            manager.runBehavior("expointro-a9caec/interactAging")
            manager.startBehavior("expointro-a9caec/setAgingHuman")
            sound_level = MySoundProcessingModule.startProcessing()
            print "Behavior ---- " + "expointro-a9caec/setAgingHuman"
            print "Sound Average ---- " + str(sound_level)

        else:
            manager.runBehavior("expointro-a9caec/interactAging")
            manager.startBehavior("expointro-a9caec/setAgingRobot")
            sound_level = MySoundProcessingModule.startProcessing()
            print "Behavior ---- " + "expointro-a9caec/setAgingRobot"
            print "Sound Average ---- " + str(sound_level)

    elif (dict_behavior["expointro-a9caec/askJobs"] > dict_behavior["expointro-a9caec/askAging"] and 
    dict_behavior["expointro-a9caec/askJobs"] > dict_behavior["expointro-a9caec/askRomance"]): 
        manager.runBehavior("expointro-a9caec/confirmJobs")
        if state == "h":
            manager.runBehavior("expointro-a9caec/interactJobs")
            manager.startBehavior("expointro-a9caec/setJobsHuman")
            sound_level = MySoundProcessingModule.startProcessing()
            print "Behavior ---- " + "expointro-a9caec/setJobsHuman"
            print "Sound Average ---- " + str(sound_level)

        else:
            manager.runBehavior("expointro-a9caec/interactJobs")
            manager.startBehavior("expointro-a9caec/setJobsRobot")
            sound_level = MySoundProcessingModule.startProcessing()
            print "Behavior ---- " + "expointro-a9caec/setJobsRobot"
            print "Sound Average ---- " + str(sound_level)

    else:
        manager.runBehavior("expointro-a9caec/confirmRomance")
        if state == "h":
            manager.runBehavior("expointro-a9caec/interactRomance")
            manager.startBehavior("expointro-a9caec/setRomanceHuman")
            sound_level = MySoundProcessingModule.startProcessing()
            print "Behavior ---- " + "expointro-a9caec/setRomanceHuman"
            print "Sound Average ---- " + str(sound_level)

        else:
            manager.runBehavior("expointro-a9caec/interactRomance")
            manager.startBehavior("expointro-a9caec/setRomanceRobot")
            sound_level = MySoundProcessingModule.startProcessing()
            print "Behavior ---- " + "expointro-a9caec/setRomanceRobot"
            print "Sound Average ---- " + str(sound_level)

    if(sound_level - dict_behavior["expointro-a9caec/calibrateFunnyRobot"] 
        < sound_level - dict_behavior["expointro-a9caec/calibrateLameRobot"]):
        manager.runBehavior("expointro-a9caec/crowdReportLame")

    else:
        manager.runBehavior("expointro-a9caec/crowdReportFunny")

    



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="192.168.0.100",
                        help="Robot IP address. On robot or Local Naoqi: use '127.0.0.1'.")
    parser.add_argument("--port", type=int, default=9559,
                        help="Naoqi port number")
    parser.add_argument("--state", type=str, default="robot",
                        help="Insert robot or human")

    args = parser.parse_args()
    state = args.state
    try:
        # Initialize qi framework.
        connection_url = "tcp://" + args.ip + ":" + str(args.port)
        app = qi.Application(["SoundProcessingModule", "--qi-url=" + connection_url])
    except RuntimeError:
        print ("Can't connect to Naoqi at ip \"" + args.ip + "\" on port " + str(args.port) +".\n"
               "Please check your script arguments. Run with -h option for help.")
        sys.exit(1)

    MySoundProcessingModule = ad.SoundProcessingModule(app)
    app.session.registerService("SoundProcessingModule", MySoundProcessingModule)

    doJoke(MySoundProcessingModule, state)

if __name__ == "__main__":
    main()
