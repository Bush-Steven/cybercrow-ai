import feedparser

feeds = [
"https://feeds.feedburner.com/TheHackersNews",
"https://www.bleepingcomputer.com/feed/",
"https://krebsonsecurity.com/feed/",
"https://darkreading.com/rss.xml"
]

def get_news():
    headlines = []

    for url in feeds:
        feed = feedparser.parse(url)

        for entry in feed.entries[:3]:
            headlines.append(entry.title)

    return headlines
