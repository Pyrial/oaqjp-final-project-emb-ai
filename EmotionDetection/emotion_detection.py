import requests  # Import the requests library to handle HTTP requests
import json # Import the json library to handle json formatting

def emotion_detector(text_to_analyse):  # Define a function named emotion_detector that takes a string input (text_to_analyse)
    # Query constructor
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'  # URL of the emotion detection service
    myobj = { "raw_document": { "text": text_to_analyse } }  # Create a dictionary with the text to be analyzed
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}  # Set the headers required for the API request

    response = requests.post(url, json = myobj, headers=header)  # Send a POST request to the API with the text and headers
    
    # Response processing
    formatted_response = json.loads(response.text) # Convert response to json
    
    emotions = formatted_response['emotionPredictions'][0]['emotion']

    results = {
        'anger': emotions['anger'],
        'disgust': emotions['disgust'],
        'fear': emotions['fear'],
        'joy': emotions['joy'],
        'sadness': emotions['sadness'],
        'dominant_emotion': max(emotions, key=emotions.get)
    }
    return (results)

