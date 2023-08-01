import feedparser
import re

# returns a list of URLs for RSS feeds parsed from inputFeeds.txt
def returnFeedURLs():
    with open("inputFeeds.txt", "r") as file:
        result = []

        # stores the text content of inputFeeds.txt after the triple hyphens
        unparsedList = file.read().split("---")[1]
        
        return re.findall("http.*", unparsedList)


# returns a feed object for the inputted RSS URL
def returnFeed(url):
    return feedparser.parse(url)

# returns a list of news article objects from an inputted feed object
def returnArticles(feed):
    return feed.entries

#! deprecated
# returns a dictionary containig the title and link from the object for an inputted news article object
# def getInfo(article):
#     return {"title": article.title, "link": article.link}

# returns the constructed text for the post for the inputted article object 
def returnPostContent(article):
    return "\n{}\n{}\n".format(article.title, article.link)

# writes the output of returnPostContent to a separate txt file
def writePostContent(content):
    with open("postsContent.txt", "a") as file:
        file.write(content)

# * This is the second-highest level function
# constructs the text for the posts for all the news articles in the RSS corresponding to the URL inputted and writes it into
# a separate file
# url: the URL of the RSS feed
def writePosts(url):
    feed = returnFeed(url)
    
    # write the content of a post for each article in the list
    for article in returnArticles(feed):
        content = returnPostContent(article)
        writePostContent(content)


print(returnFeedURLs())
