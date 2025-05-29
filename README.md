# EchoChamber: Modeling Tone Drift in AI from Social Exposure

This project explores whether large language models (LLMs) adapt their tone after repeated exposure to socially validated content. Using Reddit data as a simulation of “rewarded” information, we track emotional and stylistic shifts in GPT-style agent responses.

---

##  Highlights

-  Simulates an AI agent exposed to top Reddit posts
-  Tests for tone change before vs after exposure
-  Visualizes shifts in polarity and subjectivity

---

##  Files

| File                          | Purpose                                 |
|------------------------------|-----------------------------------------|
| `baseline_responses.csv`     | Agent's answers before exposure         |
| `after_responses.csv`        | Agent's answers after exposure          |
| `reddit_scored.csv`          | Top 100 Reddit posts with sentiment     |
| `compare_tone_visuals.py`    | Side-by-side tone visualizations        |
| `echochamber_analysis.ipynb` | Full experiment (code + results)        |

---

##  Run It Yourself

### Install dependencies:
pip install -r requirements.txt
