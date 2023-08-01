import feedparser


# returns a feed object for the inputted RSS URL
def returnFeed(url):
    return feedparser.parse(url)

# returns a list of news article objects from an inputted feed object
def returnArticles(feed):
    return feed.entries

# returns a dictionary containig the title and link from the object for an inputted news article object
def getInfo(article):
    return {"title": article.title, "link": article.link}

# returns the constructed text that will be used to make a Facebook post for an article
def returnPostContent():
    pass

# writes the constructed texts for all the news articles into a separate file
def writePosts(url):
    feed = returnFeed(url)


    
