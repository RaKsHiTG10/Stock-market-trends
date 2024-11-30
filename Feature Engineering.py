stock_symbols = ['AAPL', 'TSLA', 'GOOG', 'AMZN']

def count_stock_mentions(text, symbols):
    return sum(symbol in text for symbol in symbols)

df['stock_mentions'] = df['cleaned_text'].apply(lambda x: count_stock_mentions(x, stock_symbols))
print(df[['cleaned_text', 'stock_mentions']].head())
