"""
smart_irrigation.py

Main AI Decision Engine
"""

import joblib
import pandas as pd

from weather import get_weather_data

# ==========================================
# LOAD TRAINED MODEL
# ==========================================

print("Loading AI Model...")

model = joblib.load("models/irrigation_model.pkl")

crop_encoder = joblib.load("models/crop_encoder.pkl")
soil_encoder = joblib.load("models/soil_encoder.pkl")
stage_encoder = joblib.load("models/stage_encoder.pkl")

print("Model Loaded Successfully.")

# ==========================================
# Moisture threshold for each crop (%)
# ==========================================

MOISTURE_THRESHOLDS = {
    "Groundnut": 45,
    "Tomato": 60,
    "Potato": 65,
    "Cabbage": 70,
    "Cotton": 50,
    "Rice": 80,
    "Maize": 55,
    "Wheat": 50,
    "Sugarcane": 75,
    "Chilli": 55
}

# ==========================================
# MAIN AI FUNCTION
# ==========================================

def run_irrigation(
    crop,
    soil,
    stage,
    soil_moisture,
    temperature,
    humidity
):

    # -----------------------------
    # Encode Inputs
    # -----------------------------

    crop_id = crop_encoder.transform([crop])[0]
    soil_id = soil_encoder.transform([soil])[0]
    stage_id = stage_encoder.transform([stage])[0]

    # -----------------------------
    # Create Model Input
    # -----------------------------

    input_data = pd.DataFrame([{
        "crop ID": crop_id,
        "soil_type": soil_id,
        "Seedling Stage": stage_id,
        "MOI": soil_moisture,
        "temp": temperature,
        "humidity": humidity
    }])

    # -----------------------------
    # AI Prediction
    # -----------------------------

    prediction = model.predict(input_data)[0]

    # -----------------------------
    # Weather
    # -----------------------------

    weather = get_weather_data()
    rain_probability = weather["rain_probability"]

    # Get crop moisture threshold
    threshold = MOISTURE_THRESHOLDS.get(crop, 50)

    # -----------------------------
    # Rain Check
    # -----------------------------

    if rain_probability >= 70:

        return {
            "prediction": "No Irrigation (Rain Expected)",
            "pump": "OFF",
            "duration": 0,
            "soil_moisture": soil_moisture,
            "temperature": temperature,
            "humidity": humidity,
            "rain_probability": rain_probability,
            "threshold": threshold
        }

    # -----------------------------
    # AI Decision
    # -----------------------------

    if prediction == 0:

        return {
            "prediction": "No Irrigation",
            "pump": "OFF",
            "duration": 0,
            "soil_moisture": soil_moisture,
            "temperature": temperature,
            "humidity": humidity,
            "rain_probability": rain_probability,
            "threshold": threshold
        }

    elif prediction == 1:

        return {
            "prediction": "Moderate Irrigation",
            "pump": "MEDIUM",
            "duration": 15,
            "soil_moisture": soil_moisture,
            "temperature": temperature,
            "humidity": humidity,
            "rain_probability": rain_probability,
            "threshold": threshold
        }

    else:

        return {
            "prediction": "High Irrigation",
            "pump": "HIGH",
            "duration": 30,
            "soil_moisture": soil_moisture,
            "temperature": temperature,
            "humidity": humidity,
            "rain_probability": rain_probability,
            "threshold": threshold
        }