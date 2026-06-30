import requests

# Hanamkonda coordinates
LATITUDE = 18.0316
LONGITUDE = 79.5817

def get_weather_data():

    url = (
        f"https://api.open-meteo.com/v1/forecast?"
        f"latitude={LATITUDE}"
        f"&longitude={LONGITUDE}"
        f"&current=temperature_2m,relative_humidity_2m"
        f"&hourly=precipitation_probability"
    )

    response = requests.get(url)
    data = response.json()

    current = data["current"]

    rain_probability = data["hourly"]["precipitation_probability"][0]

    return {

        "temperature": current["temperature_2m"],

        "humidity": current["relative_humidity_2m"],

        "rain_probability": rain_probability

    }

if __name__ == "__main__":

    weather = get_weather_data()

    print(weather)