import requests
import configFile
config = getattr(configFile, "config")

pageURL = 'https://graph.facebook.com/{}/feed'.format(config["pageID"])