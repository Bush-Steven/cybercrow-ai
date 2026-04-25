from news_scraper import get_news

def generate_script():

    news = get_news()

    script = "Welcome to CyberCrow Podcast by Steven Bush.\n\n"
    script += "Today's Cybersecurity Intelligence Update:\n\n"

    for item in news:
        script += "- " + item + "\n"

    script += "\nStay cyber aware. This is CyberCrow signing off."

    return script
