import discord
import os
import random
import datetime

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
                tweet = self.get_random_tweet(USER, 100)
                
                embed = discord.Embed(
                    description=tweet.text
                )
                embed.set_author(
                    name=f'{tweet.user.name} (@{tweet.user.screen_name})',
                    icon_url=tweet.user.profile_image_url
                )
                embed.set_footer(
                    text=f"Twitter • {tweet.created_at.strftime('%d, %b %Y')}",
                    icon_url="https://abs.twimg.com/icons/apple-touch-icon-192x192.png"
                )
                await message.channel.send(f'https://twitter.com/twitter/statuses/{tweet.id}', embed=embed)

        client.run(TOKEN)

    def get_random_tweet(self, USER, num_tweets=20):
        tweets = self.controller.get_tweets_for_user(USER, num_tweets)
        index = random.randint(0, num_tweets - 1)
        return tweets[index]


