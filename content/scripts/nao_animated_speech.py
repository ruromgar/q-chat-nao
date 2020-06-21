from django.conf import settings

import sys
sys.path.append("/opt/pynaoqi-python2.7-2.1.2.17-linux64")
from naoqi import ALProxy

animated_speech = ALProxy("ALAnimatedSpeech", settings.NAOIP, settings.NAOPORT)

animated_speech.say(str(sys.argv[1]), {"bodyLanguageMode":"contextual"})
