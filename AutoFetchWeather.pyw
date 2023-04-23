import schedule
import time

import FetchWeatherData as fwd

schedule.every(1).hour.do(fwd.fetch)

while (1):
    schedule.run_pending()
    time.sleep(1)
