import praw
import pandas as pd
import time
from dotenv import load_dotenv
import os

load_dotenv()
reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent=os.getenv("REDDIT_USER_AGENT")
)

#import praw
import pandas as pd
import time

# Initialize Reddit API
reddit = praw.Reddit(
    client_id="h89pWzTHOIdZEfTS9vXKJg",
    client_secret="iJ2SfFHmPOs00UNKjGXVCG-i13xSdg",
    user_agent="echochamber_sim by /u/No_Reception7303"
)

# Scrape top posts from a subreddit
def scrape_subreddit(subreddit_name, limit=500):
    subreddit = reddit.subreddit(subreddit_name)
    data = []
    for submission in subreddit.top(limit=limit, time_filter='all'):
        if not submission.stickied:
            data.append({
                "subreddit": subreddit_name,
                "title": submission.title,
                "text": submission.selftext,
                "score": submission.score,
                "num_comments": submission.num_comments,
                "url": submission.url,
                "created_utc": submission.created_utc
            })
        time.sleep(0.1)  # Respect Reddit's rate limits
    print(f"✅ r/{subreddit_name}: {len(data)} posts collected.")
    return pd.DataFrame(data)

# Scrape from multiple subreddits
def scrape_multiple_subreddits(subreddits, per_subreddit=500):
    all_data = []
    for name in subreddits:
        print(f"Scraping r/{name}...")
        df = scrape_subreddit(name, limit=per_subreddit)
        all_data.append(df)
    return pd.concat(all_data, ignore_index=True)

# Main script
if __name__ == "__main__":
    subreddits_to_scrape = ["funny", "AskReddit", "gaming", "worldnews", "todayilearned"]
    df = scrape_multiple_subreddits(subreddits_to_scrape, per_subreddit=500)
    df.to_csv("reddit_general_echochamber.csv", index=False)
    print("🎉 Scraped", len(df), "posts in total.")
