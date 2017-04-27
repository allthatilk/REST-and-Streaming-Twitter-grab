from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json

ckey="CONSUMER_KEY"
csecret="CONSUMER_SECRET"
atoken="ACCESS_TOKEN"
asecret="ACCESS_TOKEN_SECRET"

class listener(StreamListener):

    def on_data(self, data):

        all_data = json.loads(data)
        # If you don't want tweet text you can specify other things from the
        # tweet object here
        tweet = all_data["text"]

        print(tweet)
        return(True)

    def on_error(self, status):
        print(status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
# Specify your filter here
twitterStream.filter(track=["query"])
