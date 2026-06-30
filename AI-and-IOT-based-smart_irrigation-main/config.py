# Flask Configuration

SECRET_KEY = "smart_irrigation_project"

# Database

DATABASE = "database/irrigation.db"

# Weather

LATITUDE = 18.0316
LONGITUDE = 79.5817

# ESP32

ESP32_TIMEOUT = 10

# AI Model

MODEL_PATH = "models/irrigation_model.pkl"
CROP_ENCODER = "models/crop_encoder.pkl"
SOIL_ENCODER = "models/soil_encoder.pkl"
STAGE_ENCODER = "models/stage_encoder.pkl"