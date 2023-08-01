import feedparser

## parses the RSS into a list of dictionaries for the properties of the RSS
## the entries key has a value of a list of objects, one for each news item 
feed = feedparser.parse("http://fetchrss.com/rss/64c81e7dfe869a426a63018264c85954b4347851371a7e12.xml")

# saves the first news item in the list
feedEntry = feed.entries[0]

# lists the keys associated with each dictionary
print(feedEntry.keys())
