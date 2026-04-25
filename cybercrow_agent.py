from voice_generator import *
from telegram_alert import send_alert

print("Generating podcast...")
exec(open("voice_generator.py").read())

print("Sending alerts...")
send_alert()

print("CyberCrow episode ready.")
