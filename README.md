# 🌱 AI and IoT Based Smart Irrigation System

## 📌 Overview

The **AI and IoT Based Smart Irrigation System** is an intelligent agriculture solution that automates irrigation using IoT sensors and Artificial Intelligence. The system continuously monitors environmental conditions such as soil moisture, temperature, and humidity to determine the optimal watering schedule, reducing water wastage and improving crop productivity.

This project demonstrates how IoT devices and AI can work together to enable precision farming and support sustainable agriculture.

---

## 🚀 Features

* 🌱 Real-time soil moisture monitoring
* 🌡️ Temperature and humidity sensing
* 💧 Automatic water pump control
* 🤖 AI-based irrigation decision making
* 📡 IoT-based remote monitoring
* 💾 Data collection for analysis
* ⚡ Reduced water consumption
* 🌍 Sustainable and smart farming solution

---

## 🛠️ Technologies Used

* Python
* Arduino / ESP32 / NodeMCU
* IoT Sensors
* Machine Learning
* Jupyter Notebook
* C/C++
* Joblib
* Random Forest Algorithm

---

## 📂 Project Structure

```text
AI-and-IOT-based-smart_irrigation/
│
├── farm model.ipynb          # Machine Learning model training
├── centralcontroller.py      # Main controller program
├── irrigation_system.ino     # Arduino/ESP32 firmware
├── new.joblib                # Trained ML model
├── testst.csv                # Dataset
└── README.md
```

---

## ⚙️ System Workflow

1. Sensors collect real-time environmental data.
2. IoT device sends sensor readings to the controller.
3. The AI model predicts whether irrigation is required.
4. If watering is needed, the water pump is turned ON automatically.
5. Otherwise, the pump remains OFF to conserve water.

---

## 📊 Machine Learning

The project uses the **Random Forest** algorithm to predict irrigation requirements based on environmental parameters.

### Input Parameters

* Soil Moisture
* Temperature
* Humidity
* Weather Conditions (if available)

### Output

* Pump ON
* Pump OFF

---

## 🔧 Hardware Requirements

* ESP32 / NodeMCU / Arduino
* Soil Moisture Sensor
* DHT11/DHT22 Temperature & Humidity Sensor
* Relay Module
* Water Pump
* Power Supply
* Jumper Wires

---

## 💻 Software Requirements

* Python 3.x
* Arduino IDE
* Jupyter Notebook
* VS Code (optional)

### Python Libraries

```bash
pip install pandas
pip install numpy
pip install scikit-learn
pip install joblib
```

---

## ▶️ How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/Koushikreddy2005/AI-and-IOT-based-smart_irrigation.git
```

### 2. Open the Project

```bash
cd AI-and-IOT-based-smart_irrigation
```

### 3. Train or Load the Model

Run the Jupyter Notebook:

```bash
farm model.ipynb
```

or load the trained model:

```python
new.joblib
```

### 4. Upload the Arduino Code

Open:

```text
irrigation_system.ino
```

Upload it to your ESP32/Arduino using the Arduino IDE.

### 5. Run the Controller

```bash
python centralcontroller.py
```

---

## 📈 Advantages

* Saves water
* Reduces manual effort
* Improves crop yield
* Enables smart farming
* Low-cost automation
* Environment-friendly solution

---

## 🔮 Future Enhancements

* Mobile application
* Cloud dashboard
* Weather API integration
* SMS/Email notifications
* Solar-powered irrigation
* Deep Learning-based prediction

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository.
2. Create a new feature branch.
3. Commit your changes.
4. Submit a Pull Request.

---

## 📜 License

This project is developed for educational and research purposes. You are welcome to use and modify it with proper attribution.

---

## 👨‍💻 Author

**Koushik Reddy**

GitHub: https://github.com/Koushikreddy2005

---

### ⭐ If you found this project useful, please give it a Star on GitHub!
