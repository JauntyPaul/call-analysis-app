from openai import OpenAI
from config import GROQ_API_KEY, GROQ_BASE_URL

client = OpenAI(api_key=GROQ_API_KEY, base_url=GROQ_BASE_URL)

def chat_completion(messages, model="llama-3.1-8b-instant", temperature=0.3):
    try:
        resp = client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=temperature
        )
        return resp.choices[0].message.content.strip()
    except Exception as e:
        print("Groq API call failed ->", e)
        return None
