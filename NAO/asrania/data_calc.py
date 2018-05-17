#! /usr/bin/env python
# -*- encoding: UTF-8 -*-

import audio_sense as ad
import argparse
import qi
import naoqi
import time
import sys

def doJoke(MySoundProcessingModule):
    manager = naoqi.ALProxy("ALBehaviorManager", "192.168.0.100", 9559)

    current_behavior = manager.getRunningBehaviors()
    for x in current_behavior:
        manager.stopBehavior(x)
    
    behavior_name = "too-lazy-to-make-branch-05092018-0f50fa/ROMANCE/tinderHuman"
    manager.startBehavior(behavior_name)
    print "Behavior ==== " + str(behavior_name)

    sound_level = MySoundProcessingModule.startProcessing()

    print "Sound Average ==== " + str(sound_level)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="192.168.0.100",
                        help="Robot IP address. On robot or Local Naoqi: use '127.0.0.1'.")
    parser.add_argument("--port", type=int, default=9559,
                        help="Naoqi port number")

    args = parser.parse_args()
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

    doJoke(MySoundProcessingModule)

if __name__ == "__main__":
    main()
