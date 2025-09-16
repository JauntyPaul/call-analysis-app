import pandas as pd
import os

def save_to_csv(transcript: str, summary: str, sentiment: str, file_path="data/call_analysis.csv"):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    row = {"Transcript": transcript, "Summary": summary, "Sentiment": sentiment}
    df = pd.DataFrame([row])

    if not os.path.exists(file_path):
        df.to_csv(file_path, index=False)
    else:
        df.to_csv(file_path, mode="a", header=False, index=False)

    return file_path
