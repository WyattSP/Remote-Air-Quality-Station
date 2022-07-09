#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 20:52:16 2022

@author: wyattpetryshen
"""

import PySimpleGUI as sg
import psutil

import aqi

#Sense Hat Imports
#from sense_hat import SenseHat
from datetime import datetime
import time
from datetime import timedelta
import numpy as np

import os
import csv

#Create sensor instance
#sense = SenseHat()

#Create air quality sensor instance
#sensor = SDS011("/dev/ttyUSB0")

#Define Save location for log
#def log_senser_time(start_time,end_time):
#    with open("/sensor/sds_log.txt", 'a') as file:
#        t = end_time-start_time
#        file.write('Runtime: %s' % t)
###

if __name__ == '__main__':

    sg.theme('Reddit')

    layout = [[sg.Text('Environmental Pi')],
              #Select things to monitor
              [sg.Checkbox('Temperature', key = 'Temp'), sg.Checkbox('Pressure', key='Pressure'), sg.Checkbox('Humidity', key = 'Humidity'), sg.Checkbox('Air Quality', key = 'AQ')],
              #Select time duration to monitor
              [sg.Text('Sample Duration'), sg.Input(key='Dur', enable_events=True), sg.Text(size=(15, 1), font=('Helvetica', 12), text_color='#000000', key='timeout')],
              [sg.Text('Sample Interval'), sg.Input(key='Int', enable_events=True), sg.Text(size=(15, 1), font=('Helvetica', 12), text_color='#000000', key='intout')],
              #Display realtime printout
              #Display Letters on Senset Hat
              [sg.Text('SenseHat Character'), sg.Input(key='Char', enable_events=True), sg.Text(size=(15, 1), font=('Helvetica', 12), text_color='#000000', key='character')],
              #Output
              [sg.Text(size=(60, 1), font=('Helvetica', 12), text_color='#000000', key='Out')],
              [sg.Submit(button_color=('white', 'green'), pad=((15, 0), 0), key='-Sub-'), sg.Button('Stop',button_color=('white', 'blue'), pad=((15, 0), 0), key='-stop-'), sg.Exit(button_color=('white', 'firebrick4'), pad=((15, 0), 0))]]


    window = sg.Window('Pi Sensor', layout, auto_size_buttons=False, keep_on_top=True, grab_anywhere=True)

        # ----------------  main loop  ----------------
    while True:
        event, values = window.read(timeout=10)


            # --------- Do Button Operations --------
        if event == sg.WIN_CLOSED or event == 'Exit':
            break

        if event == '-Sub-':
            window['timeout'].update(values['Dur'])
            window['intout'].update(values['Int'])
            window['character'].update(values['Char'])
            try:
                duration = float(values['Dur'])
                interval = float(values['Int'])
            except:
                pass

            try:
                #sense_data = []

                timestamp = datetime.now()

                stoptime = timestamp + timedelta(seconds=duration)

                data_out = []

                data_out_index = int(duration/interval)

                for i in np.arange(0,data_out_index):

                    if event == '-stop-':
                        break

                    vals = []
                    if values['Temp'] == True:
                        #temp = sense.get_temperature()
                        temp = np.random.random()
                        temp = round(temp,2)
                        vals.append(temp)
                    if values['Pressure'] == True:
                        #pres = sense.get_pressure()
                        pres = np.random.random()
                        pres = round(pres,2)
                        vals.append(pres)
                    if values['Humidity'] == True:
                        #hum = sense.get_humidity()
                        hum = np.random.random()
                        hum = round(hum,2)
                        vals.append(hum)
                    if values['AQ'] == True:
                        #Collect AQ data
                        #Initite vector
                        pm_2_5 = np.random.random()
                        pm_10 = np.random.random()
                        #Sample
                        #x = senor.query()
                        #pm_2_5 = pm_2_5 + x[0]
                        #pm_10 = pm_10 + x[1]
                        aqi_2_5 = aqi.to_iaqi(aqi.POLLUTANT_PM25, str(pm_2_5))
                        aqi_10 = aqi.to_iaqi(aqi.POLLUTANT_PM10, str(pm_10))
                        pm_2_5 = round(pm_2_5,2)
                        pm_10 = round(pm_10,2)
                        vals.append(pm_2_5)
                        vals.append(aqi_2_5)
                        vals.append(pm_10)
                        vals.append(aqi_10)

                    vals.append(datetime.now().strftime('%H:%M:%S.%f'))

                    data_out.append(vals)
                    #Works but only printing last entry
                    window['Out'].update(vals)
                    window.refresh()

                    time.sleep(interval)
                    timestamp = datetime.now()

            except:
                if values['Char'] == True:
                    window['Out'].update('Text on SenseHat')
                    #sense.show_letter(str(values['Char']))
                else:
                    window['Out'].update('Not Running')


    window.close()
