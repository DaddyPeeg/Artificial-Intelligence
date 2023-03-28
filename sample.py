import openai
import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()

with sr.Microphone() as source:
  recognizer = sr.Recognizer()
  recognizer.energy_threshold = 400
  recognizer.dynamic_energy_threshold = False
  while True:
    audio = recognizer.listen(source, timeout=None, phrase_time_limit=None)
    print("check")
    try:
      transcription = recognizer.recognize_google(audio)
      print(transcription)
    except:
      print("Unable to hear someone")
    # engine.say(transcription.lower())
    # engine.runAndWait()
  