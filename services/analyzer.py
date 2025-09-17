from .groq_client import chat_completion

def summarize_transcript(transcript: str) -> str:
    messages = [
        {"role": "system", "content": "Summarize the following customer call in 2–3 sentences, focusing only on the issue, satisfaction mentioned,or  general question  only if asked, Do not add prefaces like 'Here’s a summary'. Output only the summary."},
        {"role": "user", "content": transcript}
    ]
    return chat_completion(messages)

def analyze_sentiment(transcript: str) -> str:
    messages = [
        {"role": "system", "content": f"""
You are analyzing a customer support call.

Rules:
- If the customer describes a problem, failure, issue, or error → classify as Negative.
- If the customer is satisfied, thankful, or happy → classify as Positive.
- If the customer is only asking a neutral question without issues → classify as Neutral.

Transcript: {transcript}

Answer with only one word: Positive, Neutral, or Negative.
"""},
        {"role": "user", "content": transcript}
    ]
    return chat_completion(messages)
