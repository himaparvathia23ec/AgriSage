import pyttsx3
import requests
import time

# Initialize text-to-speech
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Speed
engine.setProperty('volume', 1.0)  # Volume

# ThingSpeak settings
channel_id = "3098287"  # Replace
read_api_key = "5XM4TO91HMQ3PKHT"  # Replace
url = f"https://api.thingspeak.com/channels/{channel_id}/feeds.json?api_key={read_api_key}&results=1"

def speak_status(message):
    if "dry" in message.lower():
        message += " Recommend watering immediately to prevent plant stress."
    if "not in soil" in message.lower():
        message += " Please insert sensor into soil for accurate readings."
    if "low light" in message.lower():
        message += " Suggest moving plants to a sunnier spot for better growth."
    if "not working" in message.lower():
        message += " Check light sensor wiring or replace it."
    print("Speaking: " + message)
    engine.say(message)
    engine.runAndWait()

last_soil = 0
while True:
    try:
        response = requests.get(url).json()
        if 'feeds' in response and len(response['feeds']) > 0:
            feed = response['feeds'][0]
            soil = float(feed['field1'])
            light = float(feed['field2'])
            irrigation = int(feed['field3'])
            message = f"Soil Moisture: {soil} | Light: {light} lux"
            if soil >= 1000:
                message += " | Sensor not in soil!"
            elif soil > 600:
                message += " | Soil is dry - Water now!"
            else:
                message += " | Soil is moist - No water needed."
            if light == 0:
                message += " | Light sensor not working."
            elif light < 200:
                message += " | Low light - Move plant to sunlight."
            else:
                message += " | Good light."
            if last_soil != 0 and soil < 1000:
                message += f" | Change from last: {soil - last_soil} units."
            last_soil = soil
            speak_status(message)
        else:
            print("No data from ThingSpeak.")
    except Exception as e:
        print("Error: ", e)
    time.sleep(20)  # Match ThingSpeak