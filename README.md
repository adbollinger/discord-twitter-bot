## Twitter Discord Bot

This project allows users to add twitter functionality to a discord bot.

Server users can request a random tweet from a twitter account with !tweet. 
The bot will also automatically post new tweets made by the account to a specific discord channel and notify users of the new tweet.

## Project Screen Shot(s)

### Posting new tweets
![Posting a new tweet to a channel](./screenshots/twitter-bot.png)

### Requesting a random tweet
![Requesting a new tweet](./screenshots/twitter-bot-request.png)

## Installation and Setup Instructions

Clone this repository. To run it, you will need `Python` and `pip` installed globally on your machine.  

### Installation:

Install pipenv

`pip install pipenv`  

Open the pipenv shell:  

`pipenv shell`  

Install the dependancies:

`pipenv install`  

To run the app:

`py main.py`  

### Environment Variables

TOKEN - Discord bot token

KEY - Twitter api key

SECRET - Twitter api secret

ACCESS_KEY - Twitter access token

ACCESS_SECRET - Twitter access secret 

USER - User Id of the twitter account you wish to retrieve tweets from

CHANNEL_ID - The Channel Id of the discord channel you wish to post new tweets to
