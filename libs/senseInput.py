#functions to record environmental data

from sense_hat import SenseHat
from datetime import datetime
import time

sense = SenseHat()

def get_sense_data(duration=None,interval=None):

    sense_data = []

    if duration is None:
        duration = 120
    if interval is None:
        interval = 5

    timestamp = datetime.datetime.now()

    stoptime = timestamp + datetime.timedelta(seconds=duration)

    while timestamp < stoptime:
        sense_data.append((timestamp,sense.get_humidity(),sense.get_temperature(),sense.pressure()))
        time.sleep(interval)
        timestamp = datetime.datetime.now()

    return(sense_data)
