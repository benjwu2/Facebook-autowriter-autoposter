import requests
import configFile
config = getattr(configFile, "config")

pageURL = 'https://graph.facebook.com/{}/feed'.format(config["pageID"])

# parse postsContent.txt for the list of post contents
def getPosts():
    with open("postsContent.txt", "r") as file:
        content = file.read()

        result = content.split("\n\n\n")
        return result


print(getPosts()[9])