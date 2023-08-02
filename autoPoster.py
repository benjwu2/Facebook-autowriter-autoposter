import requests
import configFile
import re
config = getattr(configFile, "config")
bannedWords = getattr(configFile, "bannedWords")

pageURL = 'https://graph.facebook.com/{}/feed'.format(config["pageID"])

# parse postsContent.txt for the list of post contents and return a list of post contents
def getPosts():
    with open("postsContent.txt", "r") as file:
        content = file.read()

        result = content.split("\n\n\n")
        return result

# iterates through an enumerated version of the inputted list of post contents
# and replaces the replaces element vaues in the inputted list that have banned words with an empty string
# posts: an inputted list of post contents
def filterPosts(posts):
    enumPosts = enumerate(posts)

    # for each post content...
    for index, item in enumPosts:
        # ...replaces the corresponding element in the inputted
        # list with a blank string if a banned word is found
        if containsBannedWord(item):
            posts[index] = ""
    
    return posts

# checks if a post has a banned word in it
# returns True if yes, False if no
def containsBannedWord(post):
    for word in bannedWords:
        if re.search(word, post):
            return True
    return False

# for each post in the list returned by getPosts, make a Facebook post
def post():
    posts = getPosts()
    for post in posts:
        # see configFile.py to edit the value of confi["pageAccessToken"]
        payload = {"message": post, "token": config["pageAccessToken"]}
        r = requests.post(pageURL, data=payload)

testList = ["Real estate agent fined over $15000 for drinking milk at seller's home",
            "Plunging sales of new homes show China�s real estate crisis isn�t over - CNN",
            "Grant Cardone Says Real Estate �Is a Better Investment Today Than It Was 2 Years Ago�: Here�s Why - Yahoo Finance"]

print(filterPosts(testList))