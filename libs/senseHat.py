#functions to record environmental data

from sense_hat import SenseHat
from datetime import datetime
import time

sense = SenseHat()

def get_sense_data(input_Duration = None, input_Interval = None, Path = None):

    sense_data = []

    if input_Duration is None:
        input_Duration = 10
    if input_Interval is None:
        input_Interval = 1

    timestamp = datetime.now()

    stoptime = timestamp + timedelta(seconds=input_Duration)

    if Path is not None:
        os.chdir(Path)
        with open("sensor_test.txt", "w") as csvfile:
            savefile = csv.writer(csvfile,delimiter=',')

            try:
                while True:
                    while timestamp < stoptime:
                        val = ((timestamp,sense.get_humidity(),sense.get_temperature(),sense.pressure()))
                        print(val)
                        savefile.writerow(val)
                        sense_data.append(val)
                        time.sleep(input_Interval)
                        timestamp = datetime.now()
                    break
            except KeyboardInterrupt:
                pass

    else:
        try:
            while True:
                while timestamp < stoptime:
                    val = ((timestamp,sense.get_humidity(),sense.get_temperature(),sense.pressure()))
                    print(val)
                    sense_data.append(val)
                    time.sleep(input_Interval)
                    timestamp = datetime.now()
                break
        except KeyboardInterrupt:
            pass

    return(sense_data)
