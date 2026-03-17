import tkinter as tk
from tkinter import messagebox
import requests

# =========================
# CONFIGURATION
# =========================
API_KEY = "f21f0c2356b1d58f8fd9b5a08a9d1e5c"  # Replace with your OpenWeather API key
BASE_WEATHER = "https://api.openweathermap.org/data/2.5/weather"
BASE_FORECAST = "https://api.openweathermap.org/data/2.5/forecast"
IP_API = "http://ip-api.com/json/"  # For auto-location

# =========================
# THEME COLORS
# =========================
dark_bg = "#1e1e2f"
dark_fg = "white"
light_bg = "#36d7d7"
light_fg = "black"
current_theme = "dark"

# =========================
# GET USER LOCATION
# =========================
def get_user_city():
    try:
        res = requests.get(IP_API).json()
        return res.get("city", "")
    except:
        return ""

# =========================
# GET WEATHER FUNCTION
# =========================
def get_weather(city=None):
    global current_theme
    if not city:
        city = city_entry.get().strip()
    if not city:
        city = get_user_city()
        if not city:
            messagebox.showwarning("Input Error", "Please enter a city name or check your internet!")
            return

    try:
        params = {"q": city, "appid": API_KEY, "units": "metric"}
        res = requests.get(BASE_WEATHER, params=params).json()
        if str(res.get("cod")) != "200":
            messagebox.showerror("Error", "City not found!")
            return

        temp = res["main"]["temp"]
        hum = res["main"]["humidity"]
        wind = res["wind"]["speed"]
        cond = res["weather"][0]["main"]
        desc = res["weather"][0]["description"].title()
        country = res["sys"]["country"]

        emoji = {"Clear":"☀️","Clouds":"☁️","Rain":"🌧",
                 "Snow":"❄️","Thunderstorm":"⛈"}.get(cond,"🌤")

        # 5-day forecast
        fore_res = requests.get(BASE_FORECAST, params=params).json()
        forecast_text = ""
        shown_days = []
        for item in fore_res["list"]:
            dt_txt = item["dt_txt"]
            date = dt_txt.split()[0]
            if dt_txt.endswith("12:00:00") and date not in shown_days:
                shown_days.append(date)
                temp_min = item["main"]["temp_min"]
                temp_max = item["main"]["temp_max"]
                desc_day = item["weather"][0]["main"]
                emoji_day = {"Clear":"☀️","Clouds":"☁️","Rain":"🌧",
                             "Snow":"❄️","Thunderstorm":"⛈"}.get(desc_day,"🌤")
                forecast_text += f"{date}: {temp_min}°C/{temp_max}°C {emoji_day}\n"

        result = f"""
{emoji} Weather in {city.title()}, {country}
🌡 Temp: {temp}°C
💧 Humidity: {hum}%
🌬 Wind: {wind} m/s
🌥 Condition: {desc}

📅 5-Day Forecast:
{forecast_text}
        """
        result_label.config(text=result)

    except Exception as e:
        messagebox.showerror("Error", "Network error or invalid API key!")

# =========================
# TOGGLE DARK/LIGHT MODE
# =========================
def toggle_theme():
    global current_theme
    if current_theme == "dark":
        root.configure(bg=light_bg)
        title_label.configure(bg=light_bg, fg=light_fg)
        city_entry.configure(bg="white", fg="black")
        search_button.configure(bg="#4e9af1", fg="white")
        result_label.configure(bg=light_bg, fg=light_fg)
        footer.configure(bg=light_bg, fg="gray")
        toggle_btn.configure(bg="#cccccc", fg="black")
        current_theme = "light"
    else:
        root.configure(bg=dark_bg)
        title_label.configure(bg=dark_bg, fg=dark_fg)
        city_entry.configure(bg="#333333", fg="white")
        search_button.configure(bg="#4e9af1", fg="white")
        result_label.configure(bg=dark_bg, fg=dark_fg)
        footer.configure(bg=dark_bg, fg="gray")
        toggle_btn.configure(bg="#555555", fg="white")
        current_theme = "dark"

# =========================
# GUI DESIGN
# =========================
root = tk.Tk()
root.title("Ultimate Weather App")
root.geometry("450x600")
root.resizable(False, False)
root.configure(bg=dark_bg)

title_label = tk.Label(root, text="Ultimate Weather App", font=("Helvetica", 22, "bold"), bg=dark_bg, fg=dark_fg)
title_label.pack(pady=20)

city_entry = tk.Entry(root, font=("Helvetica", 14), width=25, bd=0, justify="center", bg="#333333", fg="white")
city_entry.pack(pady=10, ipady=8)

search_button = tk.Button(root, text="Get Weather", font=("Helvetica", 12, "bold"), bg="#4e9af1", fg="white",
                          command=lambda: get_weather())
search_button.pack(pady=10)

toggle_btn = tk.Button(root, text="Toggle Dark/Light Mode", font=("Helvetica", 10), bg="#555555", fg="white",
                       command=toggle_theme)
toggle_btn.pack(pady=5)

auto_btn = tk.Button(root, text="Auto Detect My City", font=("Helvetica", 10), bg="#4e9af1", fg="white",
                     command=lambda: get_weather())
auto_btn.pack(pady=5)

result_label = tk.Label(root, text="", font=("Helvetica", 12), bg=dark_bg, fg=dark_fg, justify="left")
result_label.pack(pady=20)

footer = tk.Label(root, text="Developed by Talha & Wafa", font=("Helvetica", 9), bg=dark_bg, fg="gray")
footer.pack(side="bottom", pady=10)

# Automatically fetch user location at start
city_entry.insert(0, get_user_city())
get_weather()

root.mainloop()



