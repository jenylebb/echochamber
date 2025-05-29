from transformers import pipeline, set_seed
import pandas as pd

set_seed(42)

# Load the model
generator = pipeline('text-generation', model='distilgpt2')

# Load neutral prompts (same as before)
neutral_prompts = [
    "How do you feel about mornings?",
    "Describe a walk in the park.",
    "What makes a good day?",
    "How would you define success?",
    "What is your favorite food and why?",
    "How do you handle stress?",
    "What are your thoughts on silence?",
    "What does comfort mean to you?",
    "How do you feel about being alone?",
    "Describe a quiet Sunday afternoon."
] * 5

# Load top Reddit posts (as exposure content)
def get_exposure_posts(filename="reddit_scored.csv", top_n=30):
    df = pd.read_csv(filename)
    df = df[df["full_text"].notna() & (df["full_text"].str.strip() != "")]
    top_df = df.sort_values(by="score", ascending=False).head(top_n)
    return top_df["full_text"].tolist()

exposure_posts = get_exposure_posts()

# Simulate exposure
print("Simulating model exposure...")
for post in exposure_posts:
    _ = generator(post, max_new_tokens=20, do_sample=True, truncation=True, pad_token_id=50256)

# Generate new responses
print("Generating post-exposure responses...")
after_responses = []
for prompt in neutral_prompts:
    generation = generator(
        prompt,
        max_new_tokens=50,
        do_sample=True,
        truncation=True,
        pad_token_id=50256,
        repetition_penalty=1.2
    )[0]['generated_text']

    response = generation.strip().replace("\n", " ")
    after_responses.append({
        "prompt": prompt,
        "response": response,
        "label": "after"
    })

# Save responses
df = pd.DataFrame(after_responses)
df.to_csv("after_responses.csv", index=False)
print("✅ Saved after_responses.csv")
