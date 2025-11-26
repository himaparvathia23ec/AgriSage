# AgriSage: AI-Enabled Smart Agriculture Monitoring System

AgriSage is an AI-enabled Smart Agriculture Monitoring and Decision-Making System designed to automate and optimize crop management. By integrating sensors, actuators, wireless communication, and voice-assistant technology, AgriSage provides a comprehensive solution for modern farming.

## Features

-   **Real-time Environmental Monitoring:**
    -   **Soil Moisture:** Uses a Capacitive Soil Moisture Sensor v1.2 to monitor soil water levels.
    -   **Light Intensity:** Uses a BH1750 digital light intensity sensor to track illumination.
-   **Automated Irrigation:**
    -   A relay module controls a water pump, automatically activating it when moisture levels fall below a specific threshold.
-   **Cloud Connectivity:**
    -   Powered by an ESP8266-01 Wi-Fi module for remote monitoring, weather updates, and data logging.
-   **Intelligent Insights:**
    -   Machine learning algorithms analyze historical data and weather patterns to provide recommendations on irrigation timing and plant health.
-   **Voice Assistant Interface:**
    -   Hands-free interaction to request updates on soil conditions, light exposure, water usage, and daily summaries.

## Hardware Components

-   **Controller:** Arduino Uno
-   **Sensors:**
    -   Capacitive Soil Moisture Sensor v1.2
    -   BH1750 Digital Light Intensity Sensor
-   **Connectivity:** ESP8266-01 Wi-Fi Module
-   **Actuators:** Relay Module, Water Pump
-   **Power:** USB Cable or 5V Adapter

## How It Works

1.  **Data Collection:** Sensors collect real-time data on soil moisture and light intensity.
2.  **Processing:** The Arduino Uno processes the data.
3.  **Action:**
    -   If soil moisture is low, the relay activates the water pump.
    -   Data is sent to the cloud via the ESP8266 module.
4.  **Interaction:** Users can query the system via voice commands for real-time status updates.

## Benefits

-   Reduces manual labor.
-   Conserves water through precision irrigation.
-   Enhances crop productivity with data-driven insights.
