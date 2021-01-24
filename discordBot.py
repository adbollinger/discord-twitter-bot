import discord
import os

TOKEN = os.getenv('TOKEN')
client = discord.Client()

@client.event
async def on_ready():
    print("Logged in!")

@client.event
async def on_message(message):
    #Don't respond to ourself
    if message.author == client.user:
        return

    if '!tweet' in message.content:
        await message.channel.send('Tweets will be coming soon')

client.run(TOKEN)