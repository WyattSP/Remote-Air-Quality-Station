from sds011sensor import *
import aqi
import time

from datetime import datetime
import argparse
import os
import csv
import timeit

from sense_hat import SenseHat

#Initate arg parser
my_parser = argparse.ArgumentParser(description='Input Parameters')

#Create args
my_parser.add_argument('-a',
                       type = int,
                       help = 'samples to average over (default 3)')

my_parser.add_argument('-r',
                       type = int,
                       help = 'air qulity runs (2s between samples)')

#Execute the parse_args()
args = my_parser.parse_args()
input_a = args.a #average
input_r = args.r #runs

#Create sensor instance
sensor = SDS011("/dev/ttyUSB0")

#Initate sense HAT
sense = SenseHat()

#Define LEDs
def start_program():
    sense.clear()
    sense.show_letter(str('S'))
    time.sleep(3)
    sense.clear()
    return

def exit_program():
    sense.clear()
    sense.show_letter(str('X'))
    time.sleep(3)
    sense.clear()
    return

def log_senser_time(start_time,end_time):
    with open("/sensor/sds_log.txt", 'a') as file:
        t = end_time-start_time
        file.write('Runtime: %s' % t)

#data collection
def air_data(n = 3, runs = 1):
    start_program()

    sensor.sleep(sleep=False)
    start = timeit.default_timer()
    pm_2_5 = 0
    pm_10 = 0
    time.sleep(10)
    aq_data = []

    os.chdir('/home/pi/AQ/sensor/')
    with open("aq_log_%s.txt" % name, "w") as csvfile:
        savefile = csv.writer(csvfile,delimiter=',')

        try:

            for i in runs:
                for j in range(n):
                    x = sensor.query()
                    pm_2_5 =  pm_2_5 + x[0]
                    pm_10 = pm_10 + x[1]
                    time.sleep(2)
                pm_2_5 = round(pm_2_5/n, 1)
                pm_10 = round(pm_10/n, 1)
                aqi_2_5 = aqi.to_iaqi(aqi.POLLUTANT_PM25, str(pm_2_5))
                aqi_10 = aqi.to_iaqi(aqi.POLLUTANT_PM10, str(pm_10))
                outp = (datetime.now(),pm_2_5,aqi_2_5,pm_10,aqi_10,sense.get_humidity(),sense.get_temperature(),sense.pressure())
                print(outp)
                aq_data.append(outp)

        except KeyboardInterrupt:
            exit_program()
            print(" Sampling Terminated")
            pass

    sensor.sleep(sleep=True)
    end = timeit.default_timer()
    log_senser_time(start,end)
    return(print("Testing Complete"))

if __name__ == "__main__":
    print("runtime estimated %s" % (input_r*input_a))
    time.sleep(1)
    air_data(input_a,input_r)
    print("Results saved to aq_log")
