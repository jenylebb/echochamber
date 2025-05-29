import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt

class Agent:
    def __init__(self, name):
        self.name = name
        self.polarity = random.uniform(-0.5, 0.5)
        self.subjectivity = random.uniform(0.2, 0.8)
        self.history = [(self.polarity, self.subjectivity)]

    def react(self, post):
        # Move tone slightly toward the post's tone, weighted by upvotes
        weight = min(post['score'] / 1000, 1.0)  # normalize
        self.polarity += 0.1 * weight * (post['polarity'] - self.polarity)
        self.subjectivity += 0.1 * weight * (post['subjectivity'] - self.subjectivity)
        self.history.append((self.polarity, self.subjectivity))

    def get_history(self):
        return pd.DataFrame(self.history, columns=["polarity", "subjectivity"])

def simulate_rounds(data, num_agents=5, rounds=100):
    agents = [Agent(f"Agent_{i}") for i in range(num_agents)]

    for r in range(rounds):
        # Pick top posts for this round (simulate feed)
        batch = data.sample(n=10, weights='score')

        for agent in agents:
            for _, post in batch.iterrows():
                agent.react(post)

    return agents

if __name__ == "__main__":
    df = pd.read_csv("reddit_scored.csv")
    df = df.dropna(subset=["polarity", "subjectivity", "score"])

    print("Simulating agents...")
    agents = simulate_rounds(df, num_agents=5, rounds=100)

    # Plot results
    plt.figure(figsize=(10, 6))
    for agent in agents:
        hist = agent.get_history()
        plt.plot(hist["polarity"], hist["subjectivity"], label=agent.name)
    plt.xlabel("Polarity (emotion)")
    plt.ylabel("Subjectivity (personal tone)")
    plt.title("EchoChamber: Agent Tone Drift Over Time")
    plt.legend()
    plt.grid(True)
    plt.savefig("tone_drift_plot.png")
    plt.show()
