import json
import requests as req

from datetime import datetime as dt

response = req.get("https://api.open-meteo.com/v1/forecast?latitude=51.67&longitude=8.34&hourly=temperature_2m,rain,showers,snowfall,cloudcover,visibility,is_day&daily=sunrise,sunset&current_weather=true&forecast_days=1&timezone=Europe%2FBerlin")

directory = "WeatherData/"
fileName = "WeatherData_" + dt.now().strftime("%Y-%m-%d-%H") + ".json"

def toBeautyString(obj):
    return json.dumps(obj.json(), sort_keys=True, indent=4)

with open(directory + fileName, "w") as outfile:
    outfile.write(toBeautyString(response))
