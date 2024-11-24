from transformers import pipeline

# Load a pre-trained sentiment analysis model
sentiment_pipeline = pipeline("sentiment-analysis")

def analyze_sentiment(text):
    """
    Analyze the sentiment of the given text.
    :param text: The input text to analyze.
    :return: A dictionary with sentiment label and score.
    """
    try:
        print(f"Analyzing sentiment for: {text}")
        result = sentiment_pipeline(text)
        sentiment = result[0]  # Get the first result
        print(f"Sentiment analysis result: {sentiment}")
        return sentiment
    except Exception as e:
        print(f"Error in sentiment analysis: {e}")
        return {"label": "error", "score": 0.0}

# Example usage
if __name__ == "__main__":
    test_text = "I love robots! They're amazing and will make life so much easier."
    sentiment_result = analyze_sentiment(test_text)
    print(sentiment_result)

