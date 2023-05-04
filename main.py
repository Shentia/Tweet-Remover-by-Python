
import tweepy
#dont forget to install tweepy
import time

# Enter your own credentials obtained from your Twitter developer account
consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

# Authenticate to Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Create API object
api = tweepy.API(auth)

# Function to delete all tweets
def delete_all_tweets():
   # Get all tweets
   tweets = api.user_timeline(count=400)
   while len(tweets) > 0:
       for tweet in tweets:
           print(f"Deleting tweet ID {tweet.id} - {tweet.text}")
           api.destroy_status(tweet.id)
           time.sleep(1)  # Add delay to avoid rate-limit issues
       tweets = api.user_timeline(count=400)

# Call the function to delete all tweets
delete_all_tweets()