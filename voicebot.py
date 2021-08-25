import requests
from colorama import Fore, Back, Style
from gtts import gTTS
import playsound
import random
import speech_recognition as sr 

# Function which takes input in voice (English)
def ask_bot():
    r = sr.Recognizer()
    with sr.Microphone() as source: 
        # this line are to sperate noice from are voice 
        audio = r.adjust_for_ambient_noise(source)
        r.pause_threshold=1
        print("Speak Anything :")
        audio = r.listen(source)        
    try:
        # it is a recorgnizer provide by google (their are many more provide on Docs of speech recorgnition)
        text = r.recognize_google(audio)
        print("You said : {}".format(text))
        return text
    except:
        print("Sorry could not recognize your voice")
        return "Try again"

# function create for voice output from the bot
# for voice output google text to speech is used
def speak(text):
    r1 = random.randint(1,10000000)
    r2 = random.randint(1,10000000)
    randfile = "sounds\\"+str(r2)+"randomtext"+str(r1) +".mp3"
    mytext = text
    language = 'en'
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save(randfile)
    playsound.playsound(randfile)

sender = input("What is your name?\n")
print("Initializing Bot.\nTO know more about the bot type: Who are you?")
bot_message=""
while bot_message != "Bye":
    print('=' * 80)
    # message=input(sender+": ",)
    print("Sender:", end=" ")
    message=ask_bot()
    # sending post request to the rasa server for geeting response of the intents extrated from voice input
    r = requests.post('http://localhost:5002/webhooks/rest/webhook', json={"sender": sender, "message": message})
    print("Bot:",end=" ")
    for i in r.json():
        bot_message = i['text']
        print(f"{i['text']}")
        speak(i['text'])
