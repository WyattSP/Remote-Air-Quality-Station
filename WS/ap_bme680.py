# Headless air quality logger: SDS011 + BME680
from sds011sensor import *
import time
from datetime import datetime
import argparse
import os
import csv
import timeit
import board
import adafruit_bme680

# -----------------------------
# Initialize hardware
# -----------------------------
sensor = SDS011("/dev/ttyUSB0")

# Initialize BME680 over I2C
i2c = board.I2C()
bme = adafruit_bme680.Adafruit_BME680_I2C(i2c, address=0x77)
bme.sea_level_pressure = 1013.25  # adjust to your location
time.sleep(30)  # warm up BME680

# -----------------------------
# Path to log
# -----------------------------
LOG_PATH = "/home/pi/Desktop/apartment_log.txt"

def log_runtime(start, end):
    with open(LOG_PATH, "a") as f:
        f.write(f"# Runtime {end - start:.2f}s ended {datetime.now()}\n")

# -----------------------------
# Argparser
# -----------------------------
parser = argparse.ArgumentParser(description="Air quality logger")
parser.add_argument(
    "-i", "--interval",
    type=int,
    default=2,
    help="Sample interval in minutes (default: 5)"
)
parser.add_argument(
    "-t", "--time",
    type=int,
    default=2,
    help="Total time to monitor in minutes (default: 60)"
)
args = parser.parse_args()
sample_interval = args.interval
total_time = args.time


# -----------------------------
# Main data collection
# -----------------------------
def air_data(interval, total_time):

    # All inputs in minutes 
    s_intervsls = interval
    s_total_time = total_time

    # Warmup
    sensor.sleep(False)
    time.sleep(15) 
    start_time = timeit.default_timer()
    os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)

    with open(LOG_PATH, "a", newline="", buffering=1) as logfile:
        writer = csv.writer(logfile,delimiter=',')

        if os.stat(LOG_PATH).st_size == 0:
            writer.writerow([
                "timestamp",
                "pm2_5",
                "pm10",
                "temperature",
                "humidity",
                "pressure",
                "gas"
            ])

        try:
            time_tracker = 0
            while (time_tracker < s_total_time):
                # SDS011 data
                data = sensor.query()
                if data:
                    pm2_5, pm10 = data
                else:
                    pm2_5 = "NA"
                    pm10 = "NA"

                # BME680 data
                temp = round(bme.temperature, 2)
                hum = round(bme.humidity, 2)
                press = round(bme.pressure, 2)
                gas = bme.gas

                # write row
                writer.writerow([
                    datetime.now().isoformat(),
                    pm2_5,
                    pm10,
                    temp,
                    hum,
                    press,
                    gas
                ])
                logfile.flush()
                time.sleep(s_intervsls)
                time_tracker += s_intervsls

        except KeyboardInterrupt:
            end_time = timeit.default_timer()
            log_runtime(start_time, end_time)
            sensor.sleep(True)
            print("Recording stopped by user")

        finally:
            end_time = timeit.default_timer()
            log_runtime(start_time, end_time)
            sensor.sleep(True)
            print("Recording finished")

# -----------------------------
# Entry point
# -----------------------------
if __name__ == "__main__":
    print("Starting air quality data collection")
    air_data(sample_interval, total_time)
