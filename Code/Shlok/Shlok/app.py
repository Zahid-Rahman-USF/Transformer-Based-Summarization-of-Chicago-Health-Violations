from flask import Flask, request, jsonify, render_template
from model_loader import load_model_and_tokenizer
from inference import summarize_violation
from chicago_fetcher import fetch_chicago_violations, search_chicago_violations
from preprocessing import preprocess_violation

app = Flask(__name__)

# Load model once when the server starts
MODEL_PATH = "D:/T An/flan_t5_small_plain_lora"  # Change this path if needed
model, tokenizer = load_model_and_tokenizer(MODEL_PATH)

@app.route("/summarize_violation", methods=["POST"])
def summarize_violation_api():
    data = request.json
    text = data.get("text", "")
    if not text:
        return jsonify({"error": "No text provided"}), 400
    
    summary = summarize_violation(text, model, tokenizer)
    return jsonify({"summary": summary})

@app.route("/fetch_and_summarize", methods=["GET"])
def fetch_and_summarize_api():
    records = fetch_chicago_violations()
    results = []

    for record in records:
        raw_text = preprocess_violation(record)
        summary = summarize_violation(raw_text, model, tokenizer)
        results.append({
            "original": raw_text,
            "summary": summary
        })

    return jsonify(results)

@app.route("/search_and_summarize", methods=["POST"])
def search_and_summarize_api():
    data = request.json
    query = data.get("query", "")
    if not query:
        return jsonify({"error": "No query provided"}), 400

    records = search_chicago_violations(query)

    if not records:
        return jsonify({"error": "No violations found for the given search criteria."}), 404

    results = []

    for record in records:
        raw_text = preprocess_violation(record)
        summary = summarize_violation(raw_text, model, tokenizer)
        results.append({
            "original": raw_text,
            "summary": summary
        })

    return jsonify(results)


@app.route("/")
def home():
    return "<h2>Restaurant Violations Summarizer is Running!</h2>"

if __name__ == "__main__":
    app.run(debug=True)