"""
sensor_api.py

Reads live sensor values from ESP32.
If ESP32 is unavailable, demo values are returned.
"""

import serial
import time

# ==========================================
# ESP32 Configuration
# ==========================================

SERIAL_PORT = "COM17"      # Change to your ESP32 COM Port
BAUD_RATE = 115200

serial_connection = None

try:
    serial_connection = serial.Serial(
        SERIAL_PORT,
        BAUD_RATE,
        timeout=2
    )

    time.sleep(2)

    print("✅ ESP32 Connected")

except Exception:

    print("⚠ ESP32 Not Connected")
    print("Using Demo Sensor Values")


# ==========================================
# Read Sensor Data
# ==========================================

def get_sensor_data():

    if serial_connection:

        try:

            line = serial_connection.readline().decode().strip()

            print("ESP32:", line)

            values = line.split(",")

            if len(values) == 3:

                return {

                    "soil_moisture": float(values[0]),
                    "temperature": float(values[1]),
                    "humidity": float(values[2])

                }

        except Exception:

            pass

    # ----------------------------------
    # Demo Values
    # ----------------------------------

    return {

        "soil_moisture": 90.0,
        "temperature": 28.5,
        "humidity": 75.0

    }