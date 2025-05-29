import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load datasets
reddit_df = pd.read_csv("reddit_scored.csv")
before_df = pd.read_csv("baseline_responses.csv")
after_df = pd.read_csv("after_responses.csv")

# Preprocess: select top 100 reddit posts by score
top_reddit = reddit_df.sort_values(by="score", ascending=False).head(100)

# Ensure necessary columns are present
required_cols = ['polarity', 'subjectivity']
if not all(col in top_reddit.columns for col in required_cols):
    raise ValueError("reddit_scored.csv must include 'polarity' and 'subjectivity' columns.")

# Add source labels
top_reddit['source'] = 'reddit_top100'
before_df['source'] = 'ai_before'
after_df['source'] = 'ai_after'

# If polarity/subjectivity missing from AI responses, compute using TextBlob
try:
    before_df[['polarity', 'subjectivity']]
except KeyError:
    from textblob import TextBlob
    before_df['polarity'] = before_df['response'].apply(lambda x: TextBlob(x).sentiment.polarity)
    before_df['subjectivity'] = before_df['response'].apply(lambda x: TextBlob(x).sentiment.subjectivity)

try:
    after_df[['polarity', 'subjectivity']]
except KeyError:
    from textblob import TextBlob
    after_df['polarity'] = after_df['response'].apply(lambda x: TextBlob(x).sentiment.polarity)
    after_df['subjectivity'] = after_df['response'].apply(lambda x: TextBlob(x).sentiment.subjectivity)

# Combine for visualization
combined = pd.concat([top_reddit[['polarity', 'subjectivity', 'source']],
                      before_df[['polarity', 'subjectivity', 'source']],
                      after_df[['polarity', 'subjectivity', 'source']]])

# Plot tone (polarity)
plt.figure(figsize=(10, 5))
sns.boxplot(x='source', y='polarity', data=combined, palette='Set2')
plt.title("Polarity Comparison: Reddit vs AI (Before & After Exposure)")
plt.ylabel("Polarity (Tone)")
plt.xlabel("Source")
plt.tight_layout()
plt.savefig("tone_comparison.png")
plt.show()

# Plot subjectivity
plt.figure(figsize=(10, 5))
sns.boxplot(x='source', y='subjectivity', data=combined, palette='Set3')
plt.title("Subjectivity Comparison: Reddit vs AI (Before & After Exposure)")
plt.ylabel("Subjectivity")
plt.xlabel("Source")
plt.tight_layout()
plt.savefig("subjectivity_comparison.png")
plt.show()
