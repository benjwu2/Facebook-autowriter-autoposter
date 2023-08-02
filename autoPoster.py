import requests
import configFile
config = getattr(configFile, "config")

pageURL = 'https://graph.facebook.com/{}/feed'.format(config["pageID"])

# parse postsContent.txt for the list of post contents and return a list of post contents
def getPosts():
    with open("postsContent.txt", "r") as file:
        content = file.read()

        result = content.split("\n\n\n")
        return result



# for each post in the list returned by getPosts, make a Facebook post
def post():
    posts = getPosts()
    for post in posts:
        # see configFile.py to edit the value of confi["pageAccessToken"]
        payload = {"message": post, "token": config["pageAccessToken"]}
        r = requests.post(pageURL, data=payload)