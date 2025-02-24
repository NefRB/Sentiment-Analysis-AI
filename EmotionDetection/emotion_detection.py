import requests, json

def emotion_detector(text_to_analyze):

    """
    Function to analyze emotions in a given text using IBM Watson NLP API.
    
    Parameters:
    text_to_analyze (str): The input text to be analyzed for emotions.

    Returns:
    str: The API response in text format containing detected emotions.
    """

    # API endpoint for Watson Emotion Detection service
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"

    # Headers containing metadata required by the Watson API
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # JSON payload with the text input for emotion analysis
    myobj = { "raw_document": { "text": text_to_analyze } }

    # Sending a POST request to the Watson API with the text and headers
    response = requests.post(url, json = myobj, headers=header)

    # Parsing the JSON response from the API
    formatted_response = json.loads(response.text)

    # Extracting emotion score from the response
    if formatted_response.get("emotionPredictions") and len(formatted_response["emotionPredictions"]) > 0:
        emotions = formatted_response["emotionPredictions"][0]["emotion"]

        # Extract emotion scores
        anger_score = emotions.get("anger", 0) #Gets the value of anger if it exists, otherwise sets to zero
        disgust_score = emotions.get("disgust", 0)
        fear_score = emotions.get("fear", 0)
        joy_score = emotions.get("joy", 0)
        sadness_score = emotions.get("sadness", 0)

        # Determine the dominant emotion
        dominant_emotion = max(emotions, key=emotions.get)  # Gets the emotion with the highest score

        # Return the structured dictionary
        return {
            "anger": anger_score,
            "disgust": disgust_score,
            "fear": fear_score,
            "joy": joy_score,
            "sadness": sadness_score,
            "dominant_emotion": dominant_emotion
        }
    else:
        return {"error": "No emotion predictions found"}
    