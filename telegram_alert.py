import requests
from news_scraper import get_news

TOKEN = "8734906416:AAG8_gzlmfR_20h5LWefDp1Mdm9rGz5Irk8"
CHAT_ID = "1518491557"

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
