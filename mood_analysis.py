from textblob import TextBlob

def analyze_mood(text):
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity
    if polarity > 0.2:
        return "Happy 😊"
    elif polarity < -0.2:
        return "Sad 😢"
    else:
        return "Neutral 😐"
