import json
import youtubesearch
from vidpy import Clip, Composition
from twython import Twython

with open('creds.json') as infile:
    creds = json.load(infile)

APP_KEY = creds["APP_KEY"]
APP_SECRET = creds['APP_SECRET']
OAUTH_TOKEN = creds['OAUTH_TOKEN']
OAUTH_TOKEN_SECRET = creds['OAUTH_TOKEN_SECRET']

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

wordFile = open("words.txt", "r")
searchTerm = wordFile.readlines()

resultVidID = youtubesearch.youtube_search(results=1, query=searchTerm[0])

youtubeLink = "https://www.youtube.com/watch?v=" + resultVidID

twitter.update_status(status=searchTerm[0] + "\n" + youtubeLink)

with open('words.txt', 'r') as fin:
    data = fin.read().splitlines(True)
with open('words.txt', 'w') as fout:
    fout.writelines(data[1:])
