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

def filterPosts(posts):
    enumPosts = enumerate(posts)
    for index, item in enumPosts:
        pass

def containsBannedWord(title):
    for word in bannedWords:
        if re.search(word, title):
            return True
    return False

# for each post in the list returned by getPosts, make a Facebook post
def post():
    posts = getPosts()
    for post in posts:
        # see configFile.py to edit the value of confi["pageAccessToken"]
        payload = {"message": post, "token": config["pageAccessToken"]}
        r = requests.post(pageURL, data=payload)

print(containsBannedWord("Real estate agent fined over $15000 for drinking milk at seller's home"))