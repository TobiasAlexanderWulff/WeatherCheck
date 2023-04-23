from datetime import datetime as dt

import json
import requests as req
import schedule
import time

directory = "WeatherData/"

def to_beauty_string(obj):
    return json.dumps(obj.json(), sort_keys=True, indent=4)

def fetch():
    fileName = "WeatherData_" + dt.now().strftime("%Y-%m-%d-%H") + ".json"
    response = req.get("https://api.open-meteo.com/v1/forecast?latitude=51.67&longitude=8.34&hourly=temperature_2m,rain,showers,snowfall,cloudcover,visibility,is_day&daily=sunrise,sunset&current_weather=true&forecast_days=1&timezone=Europe%2FBerlin")

    with open(directory + fileName, "w") as outfile:
        outfile.write(to_beauty_string(response))

fetch()

schedule.every(1).hour.do(fetch)

while (1):
    schedule.run_pending()
    time.sleep(60)
