from flask import Flask, request, jsonify
from services.analyzer import summarize_transcript, analyze_sentiment
from utils.file_manager import save_to_csv

app = Flask(__name__)

@app.route("/")
def home():
    return "📞 Call Analysis API is running!"

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.json
    transcript = data.get("transcript", "")

    if not transcript:
        return jsonify({"error": "Transcript is required"}), 400

    # Run analysis
    summary = summarize_transcript(transcript)
    sentiment = analyze_sentiment(transcript)

    # Save result
    file_path = save_to_csv(transcript, summary, sentiment)

    return jsonify({
        "transcript": transcript,
        "summary": summary,
        "sentiment": sentiment,
        "saved_to": file_path
    })

if __name__ == "__main__":
    app.run(debug=True)
