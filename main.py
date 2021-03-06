from twitter import TwitterAPI
from discordBot import DiscordBot

class ParentController:
    def get_tweets_for_user(self, user_id, num_tweets):
        return self.twitter_instance.get_tweets_for_user(user_id, num_tweets)

    def send_tweet_to_channel(self, tweet):
        self.discord_instance.send_tweet_to_channel(tweet)

    # Twitter instance
    @property
    def twitter_instance(self) -> TwitterAPI:
        return self._twitter_instance

    @twitter_instance.setter
    def twitter_instance(self, value: TwitterAPI):
        self._twitter_instance = value

    # Discord instance
    @property
    def discord_instance(self) -> DiscordBot:
        return self._discord_instance

    @discord_instance.setter
    def discord_instance(self, value: DiscordBot):
        self._discord_instance = value

if __name__ == "__main__":
    controller = ParentController()

    discord_bot = DiscordBot(controller)
    controller.discord_instance = discord_bot

    twitter_api = TwitterAPI(controller)
    controller.twitter_instance = twitter_api

    # Run the bot last
    discord_bot.run_bot()