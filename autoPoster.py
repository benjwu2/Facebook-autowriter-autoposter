import feedparser


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
def writePosts(url):
    feed = returnFeed(url)
        
    for article in returnArticles(feed):
        content = returnPostContent(article)
        writePostContent(content)


feed1 = returnFeed("http://fetchrss.com/rss/64c81e7dfe869a426a63018264c85954b4347851371a7e12.xml")
entry1 = feed1.entries[0]
writePostContent(returnPostContent(entry1))
