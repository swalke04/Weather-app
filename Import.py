# Import module
from tkinter import *
import openmeteo_requests
import pandas as pd
import requests_cache
from retry_requests import retry

# Setup the Open-Meteo API client with cache and retry on error
cache_session = requests_cache.CachedSession('.cache', expire_after=3600)
retry_session = retry(cache_session, retries=5, backoff_factor=0.2)
openmeteo = openmeteo_requests.Client(session=retry_session)

# API URL and parameters
url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": 39.36,
    "longitude": -78.04,
    "daily": ["temperature_2m_max", "temperature_2m_min", "uv_index_max", "sunrise", "sunset", "moonrise", "moonset", "moon_phase"],
    "hourly": ["temperature_2m", "relative_humidity_2m", "dew_point_2m", "precipitation", "precipitation_probability", "rain", "showers", "visibility", "wind_speed_10m", "wind_speed_80m", "wind_speed_120m", "wind_speed_180m", "wind_direction_10m", "wind_direction_80m", "wind_direction_120m", "wind_direction_180m", "wind_gusts_10m", "temperature_80m", "temperature_120m", "temperature_180m"],
    "current": ["temperature_2m", "relative_humidity_2m", "is_day", "precipitation", "showers"],
}
responses = openmeteo.weather_api(url, params=params)

# Process first location
response = responses[0]

# Process current data
current = response.Current()
current_temperature_2m = current.Variables(0).Value()
current_relative_humidity_2m = current.Variables(1).Value()
current_is_day = current.Variables(2).Value()
current_precipitation = current.Variables(3).Value()
current_showers = current.Variables(4).Value()

# Format your weather text string
weather_string = (
    f"Temp: {current_temperature_2m:.1f}°C\n"
    f"Humidity: {current_relative_humidity_2m:.1f}%\n"
    f"Precipitation: {current_precipitation}"
)

# Create object
root = Tk()
root.title("Sophia's Weather App")

# Adjust size
root.geometry("600x600")

# Add image file (Ensure 'BackgroundForGui Copy.png' is in the same folder)
bg = PhotoImage(file="BackgroundForGui.png")

# Create Canvas
canvas1 = Canvas(root, width=400, height=400)
canvas1.pack(fill="both", expand=True)

# Display image
canvas1.create_image(0, 0, image=bg, anchor="nw")

# Add Static Text
canvas1.create_text(200, 200, text="Welcome to the World of Coding", font=("Arial", 25, "bold"), fill="black")

# Add Dynamic Weather Text and update it with actual data
weather_display = canvas1.create_text(200, 280, text=weather_string, font=("Arial", 20), fill="black")

root.mainloop()