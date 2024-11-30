def get_sentiment(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    return sentiment

df['sentiment'] = df['cleaned_text'].apply(get_sentiment)
print(df[['cleaned_text', 'sentiment']].head())
