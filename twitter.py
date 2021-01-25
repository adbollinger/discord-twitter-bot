import tweepy
import os

CONSUMER_KEY = os.getenv('KEY')
CONSUMER_SECRET = os.getenv('SECRET')
ACCESS_KEY = os.getenv('ACCESS_KEY')
ACCESS_SECRET = os.getenv('ACCESS_SECRET')
USERS = os.getenv('USERS')
WEBOOK_URL = os.getenv('WEBOOK_URL')

class MyStreamListener(tweepy.StreamListener):
    
    def on_status(self, status):
        print(status.text)

    def on_error(self, status_code):
        if status_code == 420:
            # Returning False in on_error disconnects the stream
            return False

class TwitterAPI():
    def __init__(self, controller):
        self.controller = controller

        # Authenticate using our twitter keys 
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
        self.api = tweepy.API(auth)

        # Open a stream to listen for new 'statuses'
        myStreamListener = MyStreamListener()
        myStream = tweepy.Stream(auth = self.api.auth, listener=myStreamListener)
        myStream.filter(follow=USERS, is_async=True)

    def get_tweets_for_user(self, userid, num_tweets):
        return self.api.user_timeline(user_id=userid, count=num_tweets)

    