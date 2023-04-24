import logging as log

import json
import schedule
import time
import requests as req
from datetime import datetime as dt

today = dt.today().strftime("%Y-%m-%d")

log.basicConfig(filename="log/AutoFetch_" + today + ".log", encoding="utf-8", format='%(levelname)s:%(asctime)s: %(message)s', level=log.DEBUG)
log.info("AutoFetching of WeatherData started")

directory = "WeatherData/"


def to_beauty_string(obj):
    return json.dumps(obj, sort_keys=True, indent=4)


def fetch():
    log.info("Start fetching..")
    
    fileName = "WeatherData_" + dt.now().strftime("%Y-%m-%d-%H") + ".json"
    
    response = req.get("https://api.open-meteo.com/v1/forecast?latitude=51.67&longitude=8.34&hourly=temperature_2m,rain,showers,snowfall,cloudcover,visibility,is_day&daily=sunrise,sunset&current_weather=true&forecast_days=1&timezone=Europe%2FBerlin")
    log.debug("Success!")

    with open(directory + fileName, "w") as outfile:
        log.debug("Saving to File..")
        outfile.write(to_beauty_string(response.json()))
        log.debug("Saving successful!")
    log.info("Fetching successful!")

fetch()
schedule.every(1).hour.do(fetch)
log.info("Fetching scheduled to be every hour on minute " + dt.now().strftime("%m") + ".")

minute = 60
while (1):
    schedule.run_pending()
    time.sleep(minute)
