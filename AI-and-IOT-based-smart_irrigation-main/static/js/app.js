document.addEventListener("DOMContentLoaded", function () {

    // ===========================
    // LIVE SENSOR UPDATES
    // ===========================

    let isFetching = false;

    async function updateSensors() {
        if (isFetching) return;
        isFetching = true;

        try {
            const response = await fetch("/sensor?ts=" + Date.now(), {
                cache: "no-store"
            });

            const data = await response.json();

            document.getElementById("soilMoisture").innerHTML =
                data.soil_moisture + " %";

            document.getElementById("temperature").innerHTML =
                data.temperature + " °C";

            document.getElementById("humidity").innerHTML =
                data.humidity + " %";

        } catch (err) {
            console.log("Sensor Error:", err);
        }

        isFetching = false;
    }

    // Load immediately
    updateSensors();

    // Refresh every 2 seconds
    setInterval(updateSensors, 2000);


    // ===========================
    // PREDICTION BUTTON
    // ===========================

    const predictButton = document.getElementById("predictBtn");

    predictButton.addEventListener("click", async function () {

        const crop = document.getElementById("crop").value;
        const soil = document.getElementById("soil").value;
        const stage = document.getElementById("stage").value;

        try {
            const response = await fetch("/predict", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    crop: crop,
                    soil: soil,
                    stage: stage
                })
            });

            const result = await response.json();

            console.log(result);

            // Prediction outputs ONLY (DO NOT overwrite sensors)
            document.getElementById("prediction").innerHTML =
                result.prediction;

            document.getElementById("pumpStatus").innerHTML =
                result.pump;

            document.getElementById("motorStatus").innerHTML =
                result.motor_status;

            document.getElementById("rainProbability").innerHTML =
                result.rain_probability + " %";

        } catch (err) {
            console.log("Prediction Error:", err);
        }

    });

});