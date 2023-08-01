import feedparser


# returns a feed object for the inputted RSS URL
def returnFeed(url):
    return feedparser.parse(url)

# returns a news article object
def returnArticle():
    pass

# returns the link from the object for a news article
def getLink():
    pass

# returns the constructed text that will be used to make a Facebook post for an article
def returnPostContent():
    pass

# writes the constructed texts for all the news articles into a separate file
def writePosts():
    pass