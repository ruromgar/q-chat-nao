from django.conf import settings

import sys
sys.path.append("/opt/pynaoqi-python2.7-2.1.2.17-linux64")
from naoqi import ALProxy

#basic_awareness = ALProxy("ALBasicAwareness", settings.NAOIP, settings.NAOPORT)
motion = ALProxy("ALMotion", settings.NAOIP, settings.NAOPORT)

#basic_awareness.stopAwareness()
motion.rest()
