from tkinter import *
import requests  # Required to fetch API data

# 1. Function to pull data from the Weather API
def fetch_weather():
    # Coordinates for West Virginia, USA (Adjust latitude/longitude as needed)
    url = "https://open-meteo.com"
    
    try:
        # Send HTTP GET request to the API
        response = requests.get(url)
        data = response.json()
        
        # Extract temperature values from the JSON response
        temp_c = data["current"]["temperature_2m"]
        temp_f = (temp_c * 9/5) + 32  # Convert Celsius to Fahrenheit
        
        # Update the canvas text dynamically
        weather_text = f"West Virginia Weather:\n{temp_f:.1f}°F ({temp_c}°C)"
        canvas1.itemconfig(weather_display, text=weather_text)
        
    except Exception as e:
        # Fallback text if the internet connection or API fails
        canvas1.itemconfig(weather_display, text="Failed to load weather data.")

# Create object
root = Tk()
root.title("Weather GUI Application")

# Adjust size (must be a valid string format)
root.geometry("1200x1200") 

# Add image file (file path must be in quotes)
bg = PhotoImage(file="BackgroundForGui.png") 

# Create Canvas
canvas1 = Canvas(root, width=400, height=400)
# 'both' and 'nw' must be uppercase strings ("both", "nw") or Tkinter constants (BOTH, NW)
canvas1.pack(fill=BOTH, expand=True) 

# Display image
canvas1.create_image(0, 0, image=bg, anchor=NW) 

# Add Static Text
canvas1.create_text(200, 200, text="Welcome to the World of Coding", font=("Arial", 16, "bold"), fill="white")

# Add Dynamic Weather Text (saved as a variable to update later)
weather_display = canvas1.create_text(200, 280, text="Fetching weather...", font=("Arial", 14), fill="white")

# Call the weather function after the GUI initializes
root.after(1000, fetch_weather)

root.mainloop()