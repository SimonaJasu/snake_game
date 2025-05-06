import json
import os

SCORE_FILE = "scores.json"

def load_scores():
    if os.path.exists(SCORE_FILE):
        with open(SCORE_FILE, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return {}
    return {}

def save_scores(scores):
    with open(SCORE_FILE, "w") as f:
        json.dump(scores, f, indent=4)

def get_top_scores(scores, n=3):
    return sorted(scores.items(), key=lambda x: x[1], reverse=True)[:n]