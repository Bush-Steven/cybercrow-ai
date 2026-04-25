#!/bin/bash

echo "Installing CyberCrow AI..."

python3 -m venv cybercrow-env
source cybercrow-env/bin/activate

pip install feedparser requests pydub gtts python-telegram-bot

echo "Setup complete. Run: python cybercrow_agent.py"
