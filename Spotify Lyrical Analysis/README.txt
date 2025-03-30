# Lyrical Analysis Project

## Overview
This project analyzes song lyrics from a dataset using Python. It focuses on cleaning the text, identifying common words, and performing sentiment analysis. Additionally, it visualizes word frequency and sentiment distribution.

## Features
- **Data Cleaning**: Converts text to lowercase, removes special characters, and filters out common words except "love."
- **Word Frequency Analysis**: Identifies the most frequently used words in lyrics after filtering.
- **Sentiment Analysis**: Assigns polarity (positive/negative sentiment) and subjectivity (opinion-based or factual) to lyrics.
- **Visualizations**: Generates a word cloud and sentiment distribution histogram.

## Requirements
- Python 3.x
- pandas
- re (Regular Expressions)
- collections (Counter for word frequency)
- textblob (Sentiment analysis)
- matplotlib (Plotting sentiment distribution)
- wordcloud (Generating word cloud visualizations)

## Installation
1. Install required libraries:
   ```sh
   pip install pandas textblob matplotlib wordcloud
   ```
2. Place your dataset (CSV file) in the project directory.


## Output
- **Top 20 filtered words** (excluding common stop words, except "love").
- **Sentiment distribution plot** (shows the polarity of lyrics).
- **Word cloud** (visual representation of frequently used words in lyrics).

## Example Results
- Most common filtered words: ['love', 'night', 'heart', 'feel', 'time', ...]
- Sentiment polarity ranges: Mostly between -1 (negative) to +1 (positive).
- Word cloud shows dominant themes in lyrics.



