from flask import Flask, render_template, request, jsonify
import pandas as pd
import serial
import time

from smart_irrigation import run_irrigation

app = Flask(__name__)

# ==========================================
# Latest Sensor Values
# ==========================================

last_sensor = {
    "soil_moisture": 0,
    "temperature": 0,
    "humidity": 0
}

# ==========================================
# ESP32 Connection
# ==========================================

try:
    esp = serial.Serial("COM17", 115200, timeout=1)

    time.sleep(2)

    esp.reset_input_buffer()
    esp.reset_output_buffer()

    print("✅ ESP32 Connected")

except Exception as e:

    print("⚠ ESP32 Not Connected")
    print(e)

    esp = None


# ==========================================
# Read Sensor Values
# ==========================================

def read_sensor():

    global esp
    global last_sensor

    if esp is None:
        return last_sensor

    try:

        # Read ALL available lines and keep the newest one
        while esp.in_waiting > 0:

            line = esp.readline().decode(errors="ignore").strip()

            if not line:
                continue

            print("ESP32:", line)

            values = line.split(",")

            if len(values) != 3:
                continue

            try:

                last_sensor = {

                    "soil_moisture": round(float(values[0]), 2),
                    "temperature": round(float(values[1]), 2),
                    "humidity": round(float(values[2]), 2)

                }

            except ValueError:

                print("Invalid Sensor Data:", line)

                continue

    except Exception as e:

        print("Serial Error:", e)

    return last_sensor


# ==========================================
# Load Dataset
# ==========================================

df = pd.read_csv("cropdata_expanded_with_soils.csv")

crops = sorted(df["crop ID"].unique())
soils = sorted(df["soil_type"].unique())
stages = sorted(df["Seedling Stage"].unique())


# ==========================================
# Home Page
# ==========================================

@app.route("/")
def home():

    return render_template(
        "index.html",
        crops=crops,
        soils=soils,
        stages=stages
    )


# ==========================================
# Prediction API
# ==========================================

@app.route("/predict", methods=["POST"])
def predict():

    data = request.get_json()

    crop = data["crop"]
    soil = data["soil"]
    stage = data["stage"]

    sensor = read_sensor()

    result = run_irrigation(
        crop,
        soil,
        stage,
        sensor["soil_moisture"],
        sensor["temperature"],
        sensor["humidity"]
    )

    # Send command to ESP32

    if esp is not None:

        try:

            command = f'{result["pump"]},{result["threshold"]}\n'

            esp.write(command.encode())

            esp.flush()

            print("Sent to ESP32:", command.strip())

        except Exception as e:

            print("Serial Error:", e)

    # Motor Status

    result["motor_status"] = (
        "Motor ON"
        if result["pump"] != "OFF"
        else "Motor OFF"
    )

    print("Sending to webpage:", result)

    return jsonify(result)


# ==========================================
# Live Sensor API
# ==========================================

@app.route("/sensor")
def sensor():

    sensor_data = read_sensor()

    return jsonify(sensor_data)


# ==========================================
# Run Flask
# ==========================================

if __name__ == "__main__":

    app.run(
        debug=True,
        use_reloader=False,
        host="0.0.0.0",
        port=5000
    )