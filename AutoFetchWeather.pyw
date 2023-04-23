import json
import schedule
import time
import requests as req
import datetime as dt

directory = "WeatherData/"

def to_beauty_string(obj):
    return json.dumps(obj, sort_keys=True, indent=4)

def fetch():
    fileName = "WeatherData_" + dt.now().strftime("%Y-%m-%d-%H") + ".json"
    response = req.get("https://api.open-meteo.com/v1/forecast?latitude=51.67&longitude=8.34&hourly=temperature_2m,rain,showers,snowfall,cloudcover,visibility,is_day&daily=sunrise,sunset&current_weather=true&forecast_days=1&timezone=Europe%2FBerlin")

    with open(directory + fileName, "w") as outfile:
        outfile.write(to_beauty_string(response.json()))

fetch()
schedule.every(1).hour.do(fetch)

minute = 60
while (1):
    schedule.run_pending()
    time.sleep(minute)
