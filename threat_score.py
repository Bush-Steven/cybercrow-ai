from news_scraper import get_news

def threat_score():

    news = get_news()

    score = len(news) * 2

    if score > 10:
        return "HIGH"
    elif score > 5:
        return "MEDIUM"
    else:
        return "LOW"
