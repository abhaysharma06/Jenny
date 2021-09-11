# Mental_health_bot
It is a friendly conversational AI based friend in deep learning framework Rasa that help you in your harsh time of pandemic.
The bot provided here has only one story line up related COVID19 awareness  soon I add more story line related to jobless people, students etc.

# Step required for setup

1 created python virtual environment.

2 Install all packages required => 
  ** SpeechRecognition
  ** Google text to speech
  ** Pyaudio
  ** Rasa 

3 To start rasa backend run in virtual env terminal => rasa run -m models --endpoints endpoints.yml --port 5002 --credentials credentials.yml

4 To run action server => rasa run actions (action server helps to create own actions like redirecting to website)
 
5 Run you voicebot.py file.

6 Train the model story as per your need

