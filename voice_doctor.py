import os
from gtts import gTTS

def text_to_speech_with_gtts_old(input_text, output_filepath):
    language="en"

    audioobj= gTTS(
        text=input_text,
        lang=language,
        slow=False
    )
    audioobj.save(output_filepath)

input_text="testing 1,2,3"
#text_to_speech_with_gtts_old(input_text=input_text, output_filepath="gtts_testing.mp3")

import elevenlabs
from elevenlabs.client import ElevenLabs

ELEVENLABS_API_KEY=os.environ.get("ELEVENLABS_API_KEY")

def text_to_speech_with_elevenlabs_old(input_text, output_filepath):
    client=ElevenLabs(api_key=ELEVENLABS_API_KEY)
    audio=client.generate(
        text= input_text,
        voice= "Callum",
        output_format= "mp3_22050_32",
        model= "eleven_turbo_v2"
    )
    elevenlabs.save(audio, output_filepath)

#text_to_speech_with_elevenlabs_old(input_text, output_filepath="elevenlabs_testing.mp3") 


from playsound import playsound

def text_to_speech_with_gtts(input_text, output_filepath):
    language = "en"
    audioobj = gTTS(
        text=input_text,
        lang=language,
        slow=False
    )
    audioobj.save(output_filepath)
    
    # Use playsound to play the audio file (works on Windows, macOS, and Linux)
    try:
        playsound(output_filepath)
        print("Audio played successfully")
    except Exception as e:
        print(f"An error occurred while trying to play the audio: {e}")


input_text = "Hello, this is Manas, testing auto play"
# text_to_speech_with_gtts(input_text=input_text, output_filepath="gtts_testing_autoplay.mp3")


def text_to_speech_with_elevenlabs(input_text, output_filepath):
    client=ElevenLabs(api_key=ELEVENLABS_API_KEY)
    audio=client.generate(
        text= input_text,
        voice= "Callum",
        output_format= "mp3_22050_32",
        model= "eleven_turbo_v2"
    )
    elevenlabs.save(audio, output_filepath)
    try:
        playsound(output_filepath)
        print("Audio played successfully")
    except Exception as e:
        print(f"An error occurred while trying to play the audio: {e}")

text_to_speech_with_elevenlabs(input_text, output_filepath="elevenlabs_testing_autoplay.mp3")