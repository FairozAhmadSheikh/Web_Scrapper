import feedparser

# BBC News RSS Feed URL
RSS_FEED_URL = "http://feeds.bbci.co.uk/news/rss.xml"

def fetch_news():
    # Parse the RSS feed
    feed = feedparser.parse(RSS_FEED_URL)
    
    print(f"\n🔹 {feed.feed.title} 🔹\n")  # Print the feed title (BBC News)
    
    # Loop through each news entry
    for i, entry in enumerate(feed.entries[:10], start=1):  # Get top 10 news
        print(f"{i}. 📰 {entry.title}")  # Print headline
        print(f"   📎 {entry.link}")     # Print link to full news
        print(f"   📝 {entry.summary[:150]}...")  # Print summary (first 150 chars)
        print("-" * 80)

if __name__ == "__main__":
    fetch_news()
