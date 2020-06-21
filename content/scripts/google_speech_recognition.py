import io
import os
import sys

# Imports the Google Cloud client library
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types

from django.conf import settings

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = settings.GOOGLE_APPLICATION_CREDENTIALS

# Instantiates a client
client = speech.SpeechClient()

# The name of the audio file to transcribe
file_name = str(sys.argv[1])

# Loads the audio into memory
with io.open(file_name, 'rb') as audio_file:
    content = audio_file.read()
    audio = types.RecognitionAudio(content=content)

config = types.RecognitionConfig(
    encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
    sample_rate_hertz=44100,
    language_code='es-ES',
    enable_word_time_offsets=True)

# Detects speech in the audio file
response = client.recognize(config, audio)
file = open(file_name + ".txt", "w")
file2 = open(file_name + "_extra.txt", "w")

for result in response.results:
    file.write(result.alternatives[0].transcript.encode('utf-8'))

    for word_info in result.alternatives[0].words:

        word = str(word_info.word.encode('utf-8'))
        start_time = word_info.start_time.seconds + word_info.start_time.nanos * 1e-9
        end_time = word_info.end_time.seconds + word_info.end_time.nanos * 1e-9
        word_time = str((start_time + end_time)/2)

        file2.write('{} {} '.format(word, word_time))

file.close()
file2.close()


