# python-project-WeatherApp

# 🌦 Ultimate Weather App (Python GUI)

A modern **Weather Application** built using **Python (Tkinter)** that shows **real-time weather**, **5-day forecast**, **auto-location detection**, and a **Dark/Light mode toggle**.

---

## 🚀 Features

* 🌡 Real-time weather data (Temperature, Humidity, Wind)
* 📅 5-Day weather forecast
* 📍 Auto-detect user location (IP-based)
* 🌙 Dark / Light mode toggle
* 🎨 Clean and modern GUI design
* ⚠️ Error handling (invalid city, network issues)

---

## 🛠 Technologies Used

* Python
* Tkinter (GUI)
* Requests (API calls)
* OpenWeather API

---

## 📦 Installation & Setup

### 1️⃣ Install Python

Make sure Python is installed:

```bash
python --version
```

If not installed, download and install Python from the official website.

---

### 2️⃣ Install Required Library

Open terminal and run:

```bash
pip install requests
```

---

### 3️⃣ Get API Key

1. Go to OpenWeather website
2. Create a free account
3. Generate your API key

---

### 4️⃣ Configure API Key

Open the Python file and replace:

```python
API_KEY = "YOUR_API_KEY"
```

with your actual API key:

```python
API_KEY = "your_real_api_key_here"
```

---

## ▶️ How to Run

1. Open terminal in the project folder
2. Run the application:

```bash
python ultimate_weather_app.py
```

OR (if python doesn't work):

```bash
py ultimate_weather_app.py
```

---

## 🖥️ Usage

* Enter a city name (e.g., `Dhaka,BD`)
* Click **Get Weather**
* Or click **Auto Detect My City**
* Toggle between **Dark/Light mode**

---

## ⚠️ Common Issues & Fixes

### ❌ City not found

Use correct format:

```
Dhaka,BD
London,GB
New York,US
```

---

### ❌ Invalid API Key

* Make sure API key is correct
* Wait 5–10 minutes after generating

---

### ❌ Module Not Found (requests)

Run:

```bash
pip install requests
```

---

### ❌ No Internet / Network Error

Check your internet connection

---

## 📁 Project Structure

```
weather-app/
│
├── ultimate_weather_app.py
├── README.md
└── requirements.txt
```

---

## 📌 requirements.txt (optional)

Create a file named `requirements.txt`:

```
requests
```

Install using:

```bash
pip install -r requirements.txt
```

---

## 📦 Convert to EXE (Optional)

You can convert the app into a standalone `.exe` file:

### Install PyInstaller:

```bash
pip install pyinstaller
```

### Build EXE:

```bash
pyinstaller --onefile --windowed ultimate_weather_app.py
```

Find the `.exe` inside:

```
dist/
```

---

## 🏆 Project Description (for CV)

Developed a modern GUI-based Weather Application using Python and Tkinter, featuring real-time weather updates, 5-day forecast, auto-location detection, and dynamic Dark/Light mode. Integrated external API and implemented robust error handling.

---

## 👨‍💻 Author

Muhammad Talha Islam
Linkedin: [your-profile-link](https://www.linkedin.com/in/talha-islam49599/)

---

## ⭐ Future Improvements

* 🌐 Web version using Flask
* 📱 Mobile version (Kivy)
* 🎨 Advanced UI with icons & animations
* 📊 Charts for weather trends

---

## 📜 License

This project is free to use for learning and portfolio purposes.

---
