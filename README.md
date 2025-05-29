# EchoChamber: Modeling Identity Drift in AI Through Social Feedback

What happens when artificial intelligence is fed the same diet we consume every day — the viral posts, the highly upvoted opinions, the emotional confessions, the crowd-approved jokes?

**EchoChamber** is a thought experiment and technical simulation born out of that question.

This project explores whether large language models (LLMs) — like GPT — subtly adapt their tone, emotionality, and subjectivity when repeatedly exposed to popular, positively reinforced content from platforms like Reddit. Just like humans may begin to mirror the tone of their peers for validation, we ask: do AI agents, when rewarded with highly engaged content, begin to "speak" differently?

Using sentiment-scored Reddit posts as an artificial environment, we simulate an agent exposed to this data and track changes in how it responds to neutral prompts — both **before** and **after** exposure. This isn't about what the agent knows, but how it chooses to express.

It’s part psychology, part NLP, and part social experiment.
 
---

## Highlights

-  Simulates an LLM agent exposed to high-engagement Reddit content (e.g., top posts from `r/AskReddit`, `r/funny`, etc.)
-  Tracks response tone before and after exposure using sentiment analysis
-  Visualizes tone drift in terms of polarity (emotional charge) and subjectivity (personal bias)
-  Raises questions about the psychological effects of reward systems — even in artificial agents

---

## Project Structure

| File / Folder              | Purpose                                                           |
|---------------------------|-------------------------------------------------------------------|
| `scripts/reddit_scraper.py` | Gathers Reddit posts and metadata via Reddit API                 |
| `scripts/analyze_tone.py`   | Applies sentiment analysis (TextBlob) to collected data          |
| `scripts/generate_baseline.py` | Generates pre-exposure GPT responses to neutral prompts        |
| `scripts/generate_after_exposure.py` | Feeds Reddit content to GPT and generates new responses     |
| `scripts/compare_tone_visuals.py` | Creates side-by-side tone comparison plots                  |
| `data/`                    | Contains `.csv` files of prompts, responses, and tone scores     |
| `plots/`                   | Stores generated charts comparing tone drift                     |

---

## Visualizations

Plots include:
- **Tone Comparison** (`polarity`): Before vs After vs Reddit data
- **Subjectivity Comparison**: Measures personal vs impersonal style shifts
- **Drift Trajectories**: Traces how tone evolves across exposure rounds

> You'll find these under the `/plots` directory.

---

## Run It Yourself

1. Clone the repo:

```bash
git clone https://github.com/jenylebb/echochamber.git
cd echochamber
Install dependencies:

pip install -r requirements.txt
Run the pipeline in order:

python scripts/reddit_scraper.py
python scripts/analyze_tone.py
python scripts/generate_baseline.py
python scripts/generate_after_exposure.py
python scripts/compare_tone_visuals.py
