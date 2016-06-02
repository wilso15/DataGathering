import tweepy
import json
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
import sys

consumer_key = 'Gvgu6PPUg78ladng4BscKxUG6'
consumer_secret = 'WQD7Hs1lXNHdU9beTGzoBdQmKWeYUXoh38Pri0tQuZIrZkEjpv'
access_token = '4916062492-Wpu6ichVwwXgaamsOpv3iKmLBhiR7VncOQKkl7E'
access_secret = '8FGHpPpNswc79MedGPwZ0FEpLsC4wP5lUiqEej2Yduqz1'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

# def process_or_store():
#     print(json.dumps(tweet))

def get_user_timeline():
    for status in tweepy.Cursor(api.home_timeline).items(10):
        print(status.text)

get_user_timeline()


class MyListener(StreamListener):
    def on_data(self, data):
        try:
            with open('data.json', 'a') as file:
                file.write(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True

    def on_error(self, status):
        print(status)
        return True

twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['Trump'])
