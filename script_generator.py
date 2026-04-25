from news_scraper import get_news

def create_script():

    news = get_news()

    script = "Welcome to CyberCrow Podcast by Steven Bush.\n\n"

    for item in news:
        script += f"Today's cyber update: {item}\n"

    script += "\nStay cyber aware."

    return script
