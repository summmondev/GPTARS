import tweepy
import os
from dotenv import load_dotenv

load_dotenv()

def start_twitter_bot():
    # Authenticate
    auth = tweepy.OAuthHandler(os.getenv("TWITTER_API_KEY"), os.getenv("TWITTER_API_SECRET"))
    auth.set_access_token(os.getenv("ACCESS_TOKEN"), os.getenv("ACCESS_TOKEN_SECRET"))
    api = tweepy.API(auth)
    
    # List of tracked accounts
    from tracked_accounts import tracked_accounts
    for account in tracked_accounts:
        tweets = api.user_timeline(screen_name=account, count=5)
        for tweet in tweets:
            print(f"{account}: {tweet.text}")

