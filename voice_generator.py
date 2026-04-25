from gtts import gTTS
from ai_writer import generate_script

script = generate_script()

tts = gTTS(text=script, lang="en")
tts.save("episode.mp3")

print("CyberCrow episode created successfully.")
