import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load tweet data
csv_file = "tweets_data.csv"

st.title("📊 Real-Time Twitter Analytics Dashboard")

# Load data if CSV exists
if csv_file:
    df = pd.read_csv(csv_file)

    # Show raw data
    st.subheader("Latest Tweets")
    st.write(df.tail(10))  # Show last 10 tweets

    # Engagement Metrics
    st.subheader("Tweet Engagement")
    fig, ax = plt.subplots()
    ax.bar(df['created_at'], df['likes'], color="blue", label="Likes")
    ax.bar(df['created_at'], df['retweets'], color="red", label="Retweets", alpha=0.7)
    ax.set_xticklabels(df['created_at'], rotation=45)
    ax.legend()
    st.pyplot(fig)

    # Top Liked Tweets
    st.subheader("🔥 Most Liked Tweet")
    top_tweet = df.loc[df['likes'].idxmax()]
    st.write(f"💬 {top_tweet['text']} (❤️ {top_tweet['likes']})")

else:
    st.write("No data available yet. Fetching tweets...")

