import pyttsx3

engine =pyttsx3.init()
voices = engine.getProperty('voices')
Id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
for voice in voices:
    print(voice.id)
    print(voice.name)