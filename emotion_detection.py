import requests

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

    # Returning the API response as text
    return response.text