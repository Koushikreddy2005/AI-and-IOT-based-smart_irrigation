#include <DHT.h>

// ===============================
// Pin Configuration
// ===============================

#define SOIL_PIN 34          // Analog pin
#define DHT_PIN 4            // DHT22 Data Pin
#define RELAY_PIN 26         // Relay Control

#define DHTTYPE DHT22

DHT dht(DHT_PIN, DHTTYPE);

// Pump timings

const unsigned long MEDIUM_TIME = 15000;   //15 seconds
const unsigned long HIGH_TIME = 30000;     //30 seconds

void setup()
{
    Serial.begin(115200);

    dht.begin();

    pinMode(RELAY_PIN, OUTPUT);

    // Relay OFF initially
    digitalWrite(RELAY_PIN, HIGH);

    Serial.println("ESP32 Smart Irrigation Started");
}

void loop()
{
    // ===============================
    // Read Soil Moisture
    // ===============================

    int rawValue = analogRead(SOIL_PIN);

    // Convert to percentage

    float moisture = map(rawValue, 4095, 1200, 0, 100);

    moisture = constrain(moisture, 0, 100);

    // ===============================
    // Read DHT22
    // ===============================

    float temperature = dht.readTemperature();

    float humidity = dht.readHumidity();

    if (isnan(temperature) || isnan(humidity))
    {
        Serial.println("Sensor Error");
        delay(2000);
        return;
    }

    // ===============================
    // Send Data to Python
    // Format:
    // moisture,temp,humidity
    // ===============================

    Serial.print(moisture);
    Serial.print(",");
    Serial.print(temperature);
    Serial.print(",");
    Serial.println(humidity);

    // ===============================
    // Wait for AI Decision
    // ===============================

    unsigned long startTime = millis();

    while (millis() - startTime < 3000)
    {
        if (Serial.available())
        {
            String command = Serial.readStringUntil('\n');

            command.trim();

            Serial.print("Received: ");
            Serial.println(command);

            if (command == "OFF")
            {
                digitalWrite(RELAY_PIN, HIGH);

                Serial.println("Pump OFF");
            }

            else if (command == "MEDIUM")
            {
                Serial.println("Pump ON (15 sec)");

                digitalWrite(RELAY_PIN, LOW);

                delay(MEDIUM_TIME);

                digitalWrite(RELAY_PIN, HIGH);

                Serial.println("Pump OFF");
            }

            else if (command == "HIGH")
            {
                Serial.println("Pump ON (30 sec)");

                digitalWrite(RELAY_PIN, LOW);

                delay(HIGH_TIME);

                digitalWrite(RELAY_PIN, HIGH);

                Serial.println("Pump OFF");
            }

            break;
        }
    }

    delay(5000);
}