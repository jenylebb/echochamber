import pandas as pd

def get_exposure_posts(filename, top_n=30):
    df = pd.read_csv(filename)
    
    # Keep only rows with non-empty text
    df = df[df["full_text"].notna() & (df["full_text"].str.strip() != "")]
    
    # Sort by score to simulate validation
    top_df = df.sort_values(by="score", ascending=False).head(top_n)
    
    return top_df["full_text"].tolist()

if __name__ == "__main__":
    posts = get_exposure_posts("reddit_scored.csv", top_n=30)
    print(f"Loaded {len(posts)} exposure posts.")
    for i, post in enumerate(posts[:3]):
        print(f"\nPost {i+1}:\n{post}")
