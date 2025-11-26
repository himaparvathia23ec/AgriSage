import serial
import pyttsx3
import time
from flask import Flask, jsonify
from threading import Thread

app = Flask(__name__)

# Global variable to store latest soil data
latest_data = {"moisture": 0, "status": "Not in soil!", "message": "The sensor isn't in the soil"}

@app.route('/data')
def get_data():
    return jsonify(latest_data)

def run_flask():
    app.run(host='0.0.0.0', port=5000)

# Start Flask server in a separate thread
flask_thread = Thread(target=run_flask)
flask_thread.daemon = True
flask_thread.start()

engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('volume', 1.0)

try:
    ser = serial.Serial('COM5', 9600, timeout=2)  # Increased timeout
    ser.flush()  # Clear serial buffer
    print("Connected to COM5")
except serial.SerialException as e:
    print(f"Failed to open COM5: {e}")
    exit()

def speak(message):
    print("Speaking: " + message)
    engine.say(message)
    engine.runAndWait()

last_soil = 0
is_in_soil = False  # Track if sensor is in soil

while True:
    try:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8', errors='ignore').strip()
            if line.startswith("Soil:"):
                parts = line.split("|")
                try:
                    soil = float(parts[0].split(":")[1])
                    status = parts[1]
                    message = f"Soil Moisture: {soil} | {status}"

                    # Update web app data
                    latest_data["moisture"] = soil
                    latest_data["status"] = status

                    # Detect insertion into soil
                    if soil < 1000 and not is_in_soil:
                        latest_data["message"] = message
                        speak(message)
                        is_in_soil = True
                    # Detect removal from soil
                    elif soil >= 1000 and is_in_soil:
                        message = "The sensor isn't in the soil"
                        latest_data["message"] = message
                        speak(message)
                        is_in_soil = False
                    # Update status while in soil
                    elif soil < 1000 and is_in_soil:
                        if abs(soil - last_soil) > 50:  # Speak on significant change
                            latest_data["message"] = message
                            speak(message)
                    last_soil = soil
                except (IndexError, ValueError) as e:
                    print(f"Invalid data format: {line}, Error: {e}")
            elif line.startswith("Arduino"):
                print(line)
            else:
                print("No data received, waiting...")
            except Exception as e:
            print("Error:", e)
            ser.close()  # Close port on error
            try:
                ser = serial.Serial('COM5', 9600, timeout=2)  # Reopen port
                ser.flush()  # Clear buffer
                print("Reconnected to COM5")
            except serial.SerialException as e:
                print(f"Failed to reconnect to COM5: {e}")
                exit()
        time.sleep(0.2)  # Check every 0.2s for quick response