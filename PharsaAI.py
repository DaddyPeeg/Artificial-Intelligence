import openai
import pyttsx3
import speech_recognition as sr

openai.api_key = "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"

engine = pyttsx3.init()
voice = engine.getProperty('voices')
engine.setProperty('voice', voice[1].id)

def transcribe_audio_to_text(filename):
  recognizer = sr.Recognizer()
  with sr.AudioFile(filename) as source:
    audio = recognizer.record(source)
  try:
    return recognizer.recognize_google(audio)
  except:
    print("Skipping unknown error")

def generate_response(prompt):
  response = openai.Completion.create(
    engine = "text-davinci-003",
    prompt = prompt,
    max_tokens = 4000,
    n = 1,
    stop = None,
    temperature = 0.5,
  )
  return response["choices"][0]["text"]

def speak_text(text):
  engine.say(text)
  engine.runAndWait()

def main():
  while True:
    try:
      filename = "input.wmv"
      print("Say your question...")
      with sr.Microphone() as source:
        recognizer = sr.Recognizer()
        source.pause_threshold = 1
        audio = recognizer.listen(source, phrase_time_limit=None, timeout=None)
        with open(filename, "wb") as f:
          f.write(audio.get_wav_data())

      text = transcribe_audio_to_text(filename)
      if text:
        print("You said: {text}")

        response = generate_response(text)
        print(f"Pharsa says: {response}")

        speak_text(response)
    except Exception as e:
      print("An Error occured: {}".format(e))


if __name__ == "__main__":
  main()
