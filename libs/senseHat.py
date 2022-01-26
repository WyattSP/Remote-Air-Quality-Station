#functions to record environmental data
from sense_hat import SenseHat
from datetime import datetime
import time
from datetime import timedelta

import os
import csv

import argparse

my_parser = argparse.ArgumentParser(description='Input Parameters')

#Create args
my_parser.add_argument('-a',
                       type = int,
                       help = 'Duration of testing (Default 60 s)')

my_parser.add_argument('-r',
                       type = int,
                       help = 'Interval to test at (Default 1 s)')

#Execute the parse_args()
args = my_parser.parse_args()
input_a = args.a #average
input_r = args.r #runs


sense = SenseHat()

def start_program():
    sense.clear()
    sense.show_letter(str('S'))
    time.sleep(3)
    sense.clear()
    return

def exit_program():
    sense.clear()
    sense.show_letter(str('C'))
    time.sleep(3)
    sleep.clear()
    return

def get_sense_data(input_Duration = 60, input_Interval = 1):

    sense_data = []

    timestamp = datetime.now()

    stoptime = timestamp + timedelta(seconds=input_Duration)

    os.chdir('/home/pi/AQ/sensor/')
    with open("env_log_%s.txt", "w") as csvfile:
        savefile = csv.writer(csvfile,delimiter=',')

        try:
            while True:
                while timestamp < stoptime:

                    temp = sense.get_temperature()
                    hum = sense.get_humidity()
                    press = sense.get_pressure()

                    val = (timestamp,temp,hum,press)
                    print(val)
                    savefile.writerow(val)

                    time.sleep(input_Interval)
                    timestamp = datetime.now()

        except KeyboardInterrupt:
            exit_program()
            print(" Sampling Terminated")
            pass

    return(print("ENV Testing Complete"))

if __name__ == "__main__":
    start_program()
    print("runtime estimated %s" % (input_r*input_a+20))
    time.sleep(1)
    get_sense_data(input_a,input_r)
    print("Results saved to env_log")
