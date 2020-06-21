from django.conf import settings

import sys
sys.path.append("/opt/pynaoqi-python2.7-2.1.2.17-linux64")
from naoqi import ALProxy

myProxyTTS = ALProxy("ALTextToSpeech", settings.NAOIP, settings.NAOPORT)

sentence = "\RSPD=100\ \VCT=100\ " + str(sys.argv[1]) + "\RST\ "
myProxyTTS.post.say(str(sentence))
