# Call Analysis App (Flask + Groq API)

This app takes a customer call transcript and:
- Summarizes it in 2–3 sentences
- Extracts customer sentiment (Positive/Neutral/Negative)
- Saves the result into `data/call_analysis.csv`

## Setup

1. Clone the repo
2. Install dependencies:
```bash
   pip install -r requirements.txt
  ````
3. Set your Groq API key:
````bash
export GROQ_API_KEY="your_real_key"
````

4. Run the app:
```bash
python app.py
```

# Usage
1. API Endpoint (/analyze)

Send a POST request with a transcript in JSON format:
```bash
   curl -X POST http://127.0.0.1:5000/analyze \
   -H "Content-Type: application/json" \
   -d '{"transcript": "Hi, I tried to book a slot but payment failed."}'
```
Response:
```bash
{
   "transcript": "Hi, I tried to book a slot but payment failed.",
   "summary": "The customer attempted to book a slot but experienced a payment failure.",
   "sentiment": "Negative",
   "saved_to": "data/call_analysis.csv"
}
```

2. Web UI (/ui)

Visit in your browser:
```bash
http://127.0.0.1:5000/ui
```

Here you can:

* Paste a customer transcript into a text area
* Click Analyze
* Instantly see the summary and sentiment on the same page
* Data is also stored in data/call_analysis.csv in the same format as the API
