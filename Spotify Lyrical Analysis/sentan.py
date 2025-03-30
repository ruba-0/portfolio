import pandas as pd
import re
from collections import Counter
from textblob import TextBlob
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Load dataset
def load_data(file_path):
    df = pd.read_csv(file_path)
    return df.dropna(subset=['text'])  # Remove missing lyrics

# Clean lyrics text
def clean_lyrics(text):
    text = text.lower().strip()  # Convert to lowercase
    text = re.sub(r'[^a-z\s]', '', text)  # Remove special characters
    return text

# Perform word frequency analysis while keeping 'love'
def word_frequency_analysis(df):
    common_words = {'the', 'i', 'you', 'to', 'and', 'a', 'me', 'my', 'in', 'it', 'of', 
                    'your', 'that', 'on', 'im', 'all', 'is', 'be', 'for'}
    
    all_words = ' '.join(df['text']).split()
    filtered_words = [word for word in all_words if word not in common_words or word == 'love']
    
    word_counts = Counter(filtered_words)
    return word_counts.most_common(20)  # Return top 20 words

# Generate sentiment analysis
def sentiment_analysis(df):
    df['polarity'] = df['text'].apply(lambda x: TextBlob(x).sentiment.polarity)
    df['subjectivity'] = df['text'].apply(lambda x: TextBlob(x).sentiment.subjectivity)
    return df

# Plot sentiment distribution
def plot_sentiment(df):
    plt.figure(figsize=(10, 5))
    plt.hist(df['polarity'], bins=30, color='blue', alpha=0.7, edgecolor='black')
    plt.xlabel('Sentiment Polarity')
    plt.ylabel('Frequency')
    plt.title('Sentiment Polarity Distribution')
    plt.show()

# Generate word cloud
def generate_wordcloud(df):
    text = ' '.join(df['text'])
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()

# Main function
def main(file_path):
    df = load_data(file_path)
    df['text'] = df['text'].apply(clean_lyrics)
    
    print("Top 20 most common words:")
    print(word_frequency_analysis(df))
    
    df = sentiment_analysis(df)
    plot_sentiment(df)
    generate_wordcloud(df)
    
    return df

# Run the script (Replace 'your_file.csv' with actual file path)
df_processed = main('spotify_millsongdata.csv')

