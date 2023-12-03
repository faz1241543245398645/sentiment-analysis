from flask import Flask, request
from textblob import TextBlob

app = Flask(__name__)

@app.route("/")
def index():
    return """
        <form action="/analyze" method="get">
            <input type="text" name="text">
            <input type="submit" value="analyse">
        </form>
    """

@app.route("/analyze")
def analyze():
    text = request.args.get("text", "")
    if text:
        blob = TextBlob(text)
        sentiment_score = blob.sentiment.polarity

        # Classify sentiment based on score
        if sentiment_score > 0:
            return "Positive"
        elif sentiment_score < 0:
            return "Negative"
        else:
            return "Neutral"
    else:
        return "Please enter some text to analyze."

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
