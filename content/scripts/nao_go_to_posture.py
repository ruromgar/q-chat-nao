from django.conf import settings

import sys
sys.path.append("/opt/pynaoqi-python2.7-2.1.2.17-linux64")
from naoqi import ALProxy

robot_posture = ALProxy("ALRobotPosture", settings.NAOIP, settings.NAOPORT)

# str(sys.argv[1]) should be a posture.
# Valid postures: Crouch, LyingBack, LyingBelly, Sit, SitRelax, Stand, StandInit, StandZero

robot_posture.goToPosture(str(sys.argv[1]), 1.0)

