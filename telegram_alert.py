import requests
from news_scraper import get_news

TOKEN = ""
CHAT_ID = ""

def send_alert():

    news = get_news()

    message = "🐦 CyberCrow Threat Intelligence\n\n"

    for item in news:
        message += f"• {item}\n"

    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

    requests.post(url, data={
        "chat_id": CHAT_ID,
        "text": message
    })

    print("Telegram alert sent successfully.")
