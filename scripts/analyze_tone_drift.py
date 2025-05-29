import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt

# Load baseline and after-exposure responses
before_df = pd.read_csv("baseline_responses.csv")
after_df = pd.read_csv("after_responses.csv")

# Combine
combined = pd.concat([before_df, after_df], ignore_index=True)

# Score polarity & subjectivity
def get_tone(text):
    blob = TextBlob(str(text))
    return pd.Series([blob.sentiment.polarity, blob.sentiment.subjectivity])

combined[["polarity", "subjectivity"]] = combined["response"].apply(get_tone)

# Save combined results
combined.to_csv("tone_drift_results.csv", index=False)

# Plot average tone
avg_tone = combined.groupby("label")[["polarity", "subjectivity"]].mean()

plt.figure(figsize=(8, 5))
plt.bar(avg_tone.index, avg_tone["polarity"], alpha=0.7, label="Polarity")
plt.bar(avg_tone.index, avg_tone["subjectivity"], alpha=0.7, label="Subjectivity", bottom=avg_tone["polarity"])
plt.title("Average Tone Shift Before vs After Exposure")
plt.ylabel("Score")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("tone_drift_chart.png")
plt.show()
