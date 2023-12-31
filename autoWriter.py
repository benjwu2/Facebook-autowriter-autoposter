import feedparser
import re

# * This script runs the function writeAllFeedPosts(), which takes the list of RSS feeds in inputFeeds.txt,  
# * and writes the title and link for all the articles from all the listed feeds into postsContent.txt

# parses inputFeeds.txt, then constructs and returns a list of dictionaries for each RSS feed entry 
# containing a descriptive keyword/phrase and the link for the RSS feed
def returnEntries():
    with open("inputFeeds.txt", "r") as file:
        result = []

        # stores the text content of inputFeeds.txt after the triple hyphens
        unparsedList = file.read().split("---")[1]

        # stores the list of entries regex'd from the text content of inputFeeds.txt
        entries = re.findall(r".*\shttp.*", unparsedList)

        for entry in entries:
            # create a dictionary for each RSS feed entry and append it to the result array
            result.append(createEntryDict(entry))
    
    return result

# creates a dictionary with the link and keyword/phrase for an RSS feed entry from inputFeeds.txt
def createEntryDict(entry):
    result = {}

    # the keyword is on the first line
    # the link is on the second after the line break
    result["keyword"] = entry.split("\n")[0]
    result["link"] = entry.split("\n")[1]

    return result

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
def returnPostContent(article, hashtag):
    return "{}\n{}\n\n{}\n\n\n".format(article.title, article.link, hashtag)

# writes the output of returnPostContent to a separate txt file
def writePostContent(content):
    with open("postsContent.txt", "a") as file:
        file.write(content)

# * This is the second-highest level function
# constructs the text for the posts for all the news articles in the RSS corresponding to the URL inputted and writes it into
# a separate file
# entryDictionary: a dictionary with the keywords and link stored in it, from the list of dictionaries from returnEntries
def writePosts(entryDictionary):
    feed = returnFeed(entryDictionary["link"])

    hashtag = "#" + re.sub(r"\s", "", entryDictionary["keyword"])
    
    # write the content of a post for each article in the list
    for article in returnArticles(feed):
        content = returnPostContent(article, hashtag)
        writePostContent(content)

# * This is the highest level function
# from the inputFeeds.txt file, for all the articles from all the RSS feeds listed, writes the text for a Facebook post sharing the articles
# into postsContent.txt
def writeAllFeedPosts():
    feedList = returnEntries()

    # for feed list entry dictionary, write the posts for all the articles in the feed into postsContent.txt
    for entry in feedList:
        writePosts(entry)

# writeAllFeedPosts()
test = """US mortgage
http://fetchrss.com/rss/64c81e7dfe869a426a63018264c85954b4347851371a7e12.xml"""

writeAllFeedPosts()

