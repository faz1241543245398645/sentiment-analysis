from flask import Flask, request
from textblob import TextBlob

app = Flask(__name__)

@app.route("/")
def index():
    # Display a form for text input with some basic styling using CSS
    return """
        <head>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    margin: 20px;
                }
                form {
                    margin-bottom: 20px;
                }
                input[type="text"] {
                    padding: 8px;
                    width: 300px;
                }
                input[type="submit"] {
                    padding: 8px 16px;
                    background-color: #4CAF50;
                    color: white;
                    border: none;
                    cursor: pointer;
                }
                .sentiment {
                    font-size: 18px;
                    margin-top: 20px;
                }
                .positive {
                    color: #008000;
                }
                .negative {
                    color: #FF0000;
                }
                .neutral {
                    color: #0000FF;
                }
            </style>
        </head>
        <body>
            <h1>Sentiment Analysis</h1>
            <form action="/analyze" method="get">
                <input type="text" name="text" placeholder="Enter text...">
                <input type="submit" value="Analyze">
            </form>
            <div class="sentiment" id="sentiment">
                <!-- Sentiment result will appear here -->
            </div>
        </body>
    """

@app.route("/analyze")
def analyze():
    text = request.args.get("text", "")

    if text:
        blob = TextBlob(text)
        sentiment_score = blob.sentiment.polarity
        if sentiment_score > 0:
            sentiment =  "Positive"
        elif sentiment_score < 0:
            sentiment =   "Negative"
        else:
            sentiment =   "Neutral"

    return f'<div class="sentiment {sentiment.lower()}">Sentiment: {sentiment}</div>'

        # Classify sentiment based on score

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
