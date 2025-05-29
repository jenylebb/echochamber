from transformers import pipeline, set_seed
import pandas as pd

set_seed(42)

# Load the GPT-2 generator
generator = pipeline('text-generation', model='distilgpt2')

# 50 neutral prompts
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
] * 5  # 10 prompts x 5 = 50

# Generate and save baseline responses
baseline_responses = []

print("Generating baseline responses...")
for prompt in neutral_prompts:
    generation = generator(
        prompt,
        max_new_tokens=50,
        do_sample=True,
        truncation=True,
        pad_token_id=50256,           # EOS token for GPT2
        repetition_penalty=1.2        # Avoids excessive repetition
    )[0]['generated_text']
    
    response = generation.strip().replace("\n", " ")
    baseline_responses.append({
        "prompt": prompt,
        "response": response,
        "label": "before"
    })

df = pd.DataFrame(baseline_responses)
df.to_csv("baseline_responses.csv", index=False)
print("✅ Saved baseline_responses.csv")
