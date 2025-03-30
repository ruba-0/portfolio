# Real-Time Twitter Analytics Dashboard

## Overview
This project fetches real-time tweets from Twitter using the **Twitter API v2**, processes the data, and displays live analytics in a **Streamlit dashboard**. It helps track engagement metrics like likes and retweets, monitor trending topics, and visualize tweet activity over time.

## Features
✅ **Real-time Tweet Fetching** – Automatically collects new tweets every 30 seconds.  
✅ **CSV Data Storage** – Stores tweets in `tweets_data.csv` for historical analysis.  
✅ **Interactive Dashboard** – Visualizes tweet engagement metrics using **Streamlit**.  
✅ **Error Handling** – Manages rate limits with retry logic.  
✅ **Customizable Queries** – Modify search terms to track specific topics.  

## Installation
### 1️⃣ Install Required Libraries
Run the following command to install dependencies:
```bash
pip install tweepy pandas streamlit matplotlib
```

### 2️⃣ Set Up Twitter API Credentials
- Sign up for a **Twitter Developer Account**.
- Get your **Bearer Token** from the Twitter Developer Portal.
- Replace `your_bearer_token` in the script with your actual token.

## How to Run
### 1️⃣ Start Tweet Collection
Run the script to fetch tweets and store them in CSV:
```bash
python fetch_tweets.py
```

### 2️⃣ Launch the Dashboard
Run the Streamlit app to visualize the tweets:
```bash
streamlit run dashboard.py
```

### 3️⃣ Open the Dashboard
After running Streamlit, open your browser and visit:  
🔗 `http://localhost:8501`

## Customization
- Modify **query** in `fetch_tweets.py` to track different topics.
- Adjust **fetch frequency** by changing `time.sleep(30)`.
- Enhance visualization in `dashboard.py` by adding sentiment analysis or hashtag tracking.

  

