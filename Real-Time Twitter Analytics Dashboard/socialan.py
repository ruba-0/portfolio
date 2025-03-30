import tweepy
import pandas as pd

# Set up API credentials
BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAADUK0QEAAAAADkc%2B7Pgw7tFManV9YNo%2F8Uybdek%3D9Zer1eqeg4GWL37Jlhq7tb2EOZ9eTYG2GeNnZXhXao4pNP6xfu"

# Authenticate with Twitter API
client = tweepy.Client(bearer_token=BEARER_TOKEN)

# Define search query (exclude retweets, English only)
query = "AI trends -is:retweet lang:en"

# Fetch recent tweets
tweets = client.search_recent_tweets(
    query=query, 
    max_results=10, 
    tweet_fields=["created_at", "author_id", "public_metrics"]
)

# Store data
tweet_data = []
if tweets.data:
    for tweet in tweets.data:
        tweet_data.append({
            "id": tweet.id,
            "text": tweet.text,
            "author_id": tweet.author_id,
            "created_at": tweet.created_at,
            "retweets": tweet.public_metrics["retweet_count"],
            "likes": tweet.public_metrics["like_count"]
        })

    # Convert to DataFrame
    df = pd.DataFrame(tweet_data)

    # Save
    df.to_csv("tweets_data.csv", index=False)

    print("Data saved to tweets_data.csv")
else:
    print("No tweets found for the given query.")
