#Test program for Pi

# -*- coding: utf-8 -*-

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

#Execute the parse_args()
args = my_parser.parse_args()

input_Duration = args.Duration
input_Interval = args.Interval

#If inputs are None
if input_Duration is None:
    print('Set to Default duration: 3s')
if input_Interval is None:
    print('Set to Interval duration: 1s')

def test(input_Duration = None, input_Interval = None):

    test_data = []

    if input_Duration is None:
        input_Duration = 3
    if input_Interval is None:
        input_Interval = 1

    timestamp = datetime.now()

    stoptime = timestamp + timedelta(seconds=input_Duration)

    try:
        while timestamp < stoptime:
            val = (timestamp,random.random())
            print(val)
            test_data.append(val)
            time.sleep(input_Interval)
            timestamp = datetime.now()

    except KeyboardInterrupt:
        print(" Test Terminated")
        pass

    return(print("Test Complete"))

#Need to set global thread to do an override and exit system...

if __name__ == "__main__":
    print("Test Duration %s" % input_Duration)
    test(input_Duration,input_Interval)
