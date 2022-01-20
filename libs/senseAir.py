from sds011sensor import *
from senseLED import *
import aqi
import time

from datetime import datetime
import argparse
import os
import csv

#Initate arg parser
my_parser = argparse.ArgumentParser(description='Input Parameters')

#Create args
my_parser.add_argument('-a',
                       type = int,
                       help = 'samples to average over (default 3)')

my_parser.add_argument('-r',
                       type = int,
                       help = 'air qulity runs (2s between samples)')

my_parser.add_argument('-n',
                       type = str,
                       help = 'name of save file')

#Execute the parse_args()
args = my_parser.parse_args()
input_a = args.a #average
input_r = args.r #runs
input_n = args.n #name

#Create sensor instance
sensor = SDS011("/dev/ttyUSB0")

#Toogle sensor on and off
#sensor.sleep(sleep = False) #on
#sensor.sleep(sleep = True) #off
#pm_2_5, pm_10 = sensor.query()

#data collection
def air_data(n = 3, runs = 1, name = "001"):
    sensor.sleep(sleep=False)
    pm_2_5 = 0
    pm_10 = 0
    time.sleep(10)
    aq_data = []

    os.chdir('/home/pi/sensor/')
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
                outp = (datetime.now(),pm_2_5,aqi_2_5,pm_10,aqi_10)
                print(outp)
                aq_data.append(outp)

        except KeyboardInterrupt:
            pass

    return

if __name__ == "__main__":
    print("runtime estimated %s" % (input_r*input_a))
    time.sleep(1)
    air_data(input_a,input_r,input_n)
    print("Testing Complete")
