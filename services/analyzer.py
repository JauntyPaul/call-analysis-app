from .groq_client import chat_completion

def summarize_transcript(transcript: str) -> str:
    messages = [
        {"role": "system", "content": "Summarize the following customer call in 2-3 sentences."},
        {"role": "user", "content": transcript}
    ]
    return chat_completion(messages)

def analyze_sentiment(transcript: str) -> str:
    messages = [
        {"role": "system", "content": "Classify sentiment as Positive, Neutral, or Negative."},
        {"role": "user", "content": transcript}
    ]
    return chat_completion(messages)
