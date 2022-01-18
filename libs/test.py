#Test program for Pi

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from datetime import datetime
from datetime import timedelta
import time
import random
import argparse
import os
import csv

#Initate arg parser
my_parser = argparse.ArgumentParser(description='Input Parameters')

#Create args
my_parser.add_argument('-Duration',
                       type = int,
                       help = 'duration to sample (seconds)')

my_parser.add_argument('-Interval',
                       type = float,
                       help = 'interval to sample over (seconds)')

my_parser.add_argument('-Path',
                       type = str,
                       help = 'path to save directory')

#Execute the parse_args()
args = my_parser.parse_args()

input_Duration = args.Duration
input_Interval = args.Interval
input_Path = args.Path

#If inputs are None
if input_Duration is None:
    print('Set to Default duration: 120s')
if input_Interval is None:
    print('Set to Interval duration: 5s')
if input_Path is None:
    print('No save path provided: Will not save')

if input_Path is not None:
    Path = r'%s' % input_Path
    check = os.path.exists(Path)
    if check == True:
        pass
    else:
        Path = None

def test(input_Duration = None, input_Interval = None, Path = None):

    test_data = []

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

            while timestamp < stoptime:
                val = (timestamp,random.random())
                print(val)
                savefile.writerow(val)
                test_data.append(val)
                time.sleep(input_Interval)
                timestamp = datetime.now()

    else:
        while timestamp < stoptime:
            val = (timestamp,random.random())
            print(val)
            test_data.append(val)
            time.sleep(input_Interval)
            timestamp = datetime.now()

    return(print("Complete"))

#Need to set global thread to do an override and exit system...

if __name__ == "__main__":
    test(input_Duration,input_Interval,input_Path)
