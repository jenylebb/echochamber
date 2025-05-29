import pandas as pd
from textblob import TextBlob

def score_tone(text):
    blob = TextBlob(text)
    return blob.sentiment.polarity, blob.sentiment.subjectivity

if __name__ == "__main__":
    # Load scraped Reddit data
    df = pd.read_csv("reddit_general_echochamber.csv")

    # Combine title and text
    df["full_text"] = df["title"].fillna("") + ". " + df["text"].fillna("")

    # Score tone
    print("Scoring tone...")
    df[["polarity", "subjectivity"]] = df["full_text"].apply(
        lambda x: pd.Series(score_tone(x))
    )

    # Save the scored dataset
    df.to_csv("reddit_scored.csv", index=False)
    print("✅ Tone scoring complete. Saved as reddit_scored.csv")
