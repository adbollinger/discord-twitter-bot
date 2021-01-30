import tweepy
import os

CONSUMER_KEY = os.getenv('KEY')
CONSUMER_SECRET = os.getenv('SECRET')
ACCESS_KEY = os.getenv('ACCESS_KEY')
ACCESS_SECRET = os.getenv('ACCESS_SECRET')
USER = os.getenv('USER')
WEBOOK_URL = os.getenv('WEBOOK_URL')

class MyStreamListener(tweepy.StreamListener):

    def on_connect(self):
        print('Connected to Twitter API')
    
    def on_status(self, status):
        self.controller_instance.send_tweet_to_channel(status)

    def on_error(self, status_code):
        if status_code == 420:
            # Returning False in on_error disconnects the stream
            return False

    @property
    def controller_instance(self):
        return self._controller_instance

    @controller_instance.setter
    def controller_instance(self, value):
        self._controller_instance = value

class TwitterAPI():
    def __init__(self, controller):
        self.controller = controller

        # Authenticate using our twitter keys 
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
        self.api = tweepy.API(auth)

        # Open a stream to listen for new 'statuses'
        myStreamListener = MyStreamListener()
        myStreamListener.controller_instance = controller
        myStream = tweepy.Stream(auth = self.api.auth, listener=myStreamListener)
        
        users_to_follow = []
        users_to_follow.append(str(USER))
        myStream.filter(follow=users_to_follow, is_async=True)

    def get_tweets_for_user(self, userid, num_tweets):
        return self.api.user_timeline(user_id=userid, count=num_tweets)