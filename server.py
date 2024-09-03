''' Executing this function initiates the application of emotion
    detection to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector


#Initiate the flask app
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    ''' This code receives the text from the HTML interface and 
        runs emotion detector over it using emotion_detector()
        function. The output returned shows the emotions and confidence 
        scores as well as the dominant emotion for the provided text.
    '''
    # Retrieve text to analyze from request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass response to emotion_detector function and store response
    response = emotion_detector(text_to_analyze)

    # Check if the dominant emotion is None indicating an error or invalid input
    if response['dominant_emotion'] is None:
        result = "Invalid text! Please try again!"
    else:
        # Return a formatted stringe from the sentiment label and score
        result = (f"For the given statement, the system response is 'anger': {response['anger']}, "
                  f"'disgust': {response['disgust']}, 'fear': {response['fear']}, "
                  f"'joy': {response['joy']} and 'sadness': {response['sadness']}. "
                  f"The dominant emotion is {response['dominant_emotion']}."
                  )
    return result

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
