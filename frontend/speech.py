import speech_recognition as sr
from gtts import gTTS
import pygame
import openai
import tempfile
import os
import asyncio
from lmnt.api import Speech

# Initialize the recognizer
r = sr.Recognizer()
client = openai.OpenAI()

def listen_speech():
    """Listen for speech and return the recognized text."""
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Listening...")
        audio = r.listen(source)
        print("Done listening...")
        try:
            with open("microphone-results.wav", "wb") as f:
                f.write(audio.get_wav_data())

            with open("microphone-results.wav", "rb") as f:
                transcript = client.audio.transcriptions.create(
                    model="whisper-1", 
                    file=f,
                    response_format="text",
                    )
            print(f"Recognized: {transcript}")
            return transcript
        except sr.UnknownValueError:
            print("Could not understand audio")
            return None
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
            return None

def get_openai_response(text):
    # TODO: Attach model here
    return "Return model output here"

def speak_text(text):
    """Convert text to speech and play it."""
    tts = gTTS(text=text, lang='en')

    fp = tempfile.NamedTemporaryFile(dir=".", suffix=".mp3", delete=False)
    tts.save(fp.name)
    fp.close()
    pygame.mixer.init()
    pygame.mixer.music.load(fp.name)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        continue
    os.unlink(fp.name)  # Clean up the temp file


async def speak_text_lmnt(text):
    async with Speech() as speech:
        synthesis = await speech.synthesize(text, 'lily')
    fp = tempfile.NamedTemporaryFile(dir=".", suffix=".mp3", delete=False)
    fp.write(synthesis['audio'])
    fp.close()
    pygame.mixer.init()
    pygame.mixer.music.load(fp.name)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        continue
    os.unlink(fp.name)  # Clean up the temp file


if __name__ == "__main__":
    print("\nSay something or 'exit' to quit:")
    query = listen_speech()
    # query = "test"

    response = get_openai_response(query)
    print(f"Response: {response}")
    # speak_text(response)
    asyncio.run(speak_text_lmnt(response))
