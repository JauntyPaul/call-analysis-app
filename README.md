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
