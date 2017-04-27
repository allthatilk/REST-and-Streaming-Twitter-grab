import tweepy
import json
import os

ckey="CONSUMER_KEY"
csecret="CONSUMER_SECRET"
atoken="ACCESS_TOKEN"
asecret="ACCESS_TOKEN_SECRET"

auth = tweepy.OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

api = tweepy.API(auth)

# Specify your search parameters here
results = api.search(q="query", lang="en", count="130", result_type="recent")

filename = 'YOUR_FILE'

with open(filename, 'w') as file:
    for result in results:
        # If you want other things from the tweet object you can specify it here
        file.write(result.text + os.linesep)
