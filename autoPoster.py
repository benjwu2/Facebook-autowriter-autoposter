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
def returnPostContent(article):
    return "\n{}\n{}\n".format(article.title, article.link)



# constructs the text for the posts for all the news articles in the RSS corresponding to the URL inputted and writes it into
# a separate file
def writePosts(url):
    feed = returnFeed(url)

    with open("postsContent.txt", "a") as file:
        returnPostContent()
        
        for article in returnArticles(feed):
            info = getInfo(article)
            title = info.title
            link = info.link

            file.write(title + "\n" + text + "\n")
    
