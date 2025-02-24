"""
server.py - Flask Web Application for Emotion Detection

This module sets up a Flask web server that provides an API for detecting emotions in text.
It utlizes the `emotion_detector` function and returns a formatted response based on the 
detected emotions.

Routes:
- `/` : Serves the index page.
- `/emotionDetector` : Accepts a text query parameter (`textToAnalyze`), processes it through 
  the emotion detection model, and returns the detected emotions or an error message.

Error Handling:
- If no text is provided, returns "Invalid text! Please try again!".
- If the API returns a 400 status code, all emotion values are set to `None`.

Author: Neftali Rosado Bermudez
Date: 02/23/2025
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/")
def render_index_page():
    """Renders the home page."""
    return render_template('index.html')

@app.route("/emotionDetector")
def emotion_detect():
    """Handles emotion analysis requests."""

    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)

    # Error handling when dominant_emotion is None
    if response["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    #Formats the response as per example
    result_text = (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, 'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, 'joy': {response['joy']}, and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )

    return result_text

# Run Flask app if executed directly
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
