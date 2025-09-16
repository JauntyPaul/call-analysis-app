import os
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_BASE_URL = os.getenv("GROQ_BASE_URL", "https://api.groq.com/openai/v1")

if not GROQ_API_KEY:
    raise ValueError("❌ GROQ_API_KEY not found. Set it in .env or environment variables.")
