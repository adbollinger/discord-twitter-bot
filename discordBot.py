import discord
import os
import random

TOKEN = os.getenv('TOKEN')
USER = os.getenv('USER')

class DiscordBot:
    get_tweets_for_user = None

    def __init__(self, controller):
        self.controller = controller

    def run_bot(self):
        client = discord.Client()

        @client.event
        async def on_ready():
            print('We have logged in as {0.user}'.format(client))

        @client.event
        async def on_message(message):
            #Don't respond to ourself
            if message.author == client.user:
                return

            if message.content.startswith('!tweet'):
                tweet = self.get_random_tweet(USER)
                await message.channel.send(tweet.text)

        client.run(TOKEN)

    def get_random_tweet(self, USER, num_tweets=20):
        tweets = self.controller.get_tweets_for_user(USER, num_tweets)
        index = random.randint(0, num_tweets - 1)
        return tweets[index]
