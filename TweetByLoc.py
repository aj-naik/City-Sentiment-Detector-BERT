# This file contains functions of interacting with twitter api through tweepy wrapper and also has functions for mining tweets by providing location

import tweepy
import csv

class StreamListener(tweepy.StreamListener):

    def __init__(self, city):
        super(StreamListener, self).__init__()
        self.city = city

    def on_status(self, status):
        with open(self.city+".csv", 'a') as f:
            writer = csv.writer(f)
            writer.writerow([status.text])

    def on_error(self, status_code):
        if status_code == 420:
            return False

class TweetHandler:

# Function for authenctication
    def __init__(self, consumer_key, consumer_secret,
                 access_token, access_token_secret, city_name):
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)

        self.api = tweepy.API(auth, wait_on_rate_limit=True)
        self.streamListener = StreamListener(city_name)

 # Function for streaming tweets
    def stream_twitter(self, locations=None, track=None, is_async=True):
        stream = tweepy.Stream(auth=self.api.auth, listener=self.streamListener)
        stream.filter(track=track, locations=locations, is_async=is_async)


 # Function for mining tweets based on location and limiting mining to 1000 tweets
    def get_tweets_by_location(self, lat, long, radius):
        tweets = []
        counter = 0
        for tweet in tweepy.Cursor(self.api.search, q='', geocode='{},{},{}km'.format(lat,long,radius)).items():
            tweets.append(tweet.text)
            counter += 1
            if counter == 1000:
                break
        return tweets