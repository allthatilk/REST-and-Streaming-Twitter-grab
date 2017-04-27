# Getting Tweets

This is a couple of small files that get info from the RESTful and Streaming Twitter APIs.

## To run:

* git clone this repo
* enter your Twitter keys and tokens and secrets
* run the python REPL and import the file you want

## Dependencies

You will need the following libraires: 

* tweepy
* json
* os

streaming.py prints current tweets filtered by what you tell it to track in the command line. To stop the twitter stream press CTRL+C

rest.py writes recent tweets that fit your search query to the file you specify
