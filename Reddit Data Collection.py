def fetch_reddit_data(subreddit_name, limit=100):
    subreddit = reddit.subreddit(subreddit_name)
    data = []
    for submission in subreddit.hot(limit=limit):
        data.append({
            "title": submission.title,
            "score": submission.score,
            "num_comments": submission.num_comments,
            "created_utc": submission.created_utc,
            "selftext": submission.selftext
        })
    return pd.DataFrame(data)

# Example: Fetch 100 posts from WallStreetBets
df = fetch_reddit_data("wallstreetbets", limit=100)
print(df.head())
