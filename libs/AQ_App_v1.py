#Jan 1, 2023
#Plots only single value for AQI
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import PySimpleGUI as sg
import matplotlib, time, threading
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

#Imports needed for aqi
import aqi
import psutil
from sds011sensor import *

#Create sensor instance
sensor = SDS011("/dev/ttyUSB0")

def data_aquire():

    timestamp = datetime.now()
    stoptime = timestamp + timedelta(seconds=duration)
    data_out = []
    data_out_index = int(duration/interval)

    for i in np.arange(0,data_out_index):
        if event == '-stop-':
            break
    vals = []
    #Data Acquisition
    if values['Temp'] == True:
        temp = np.random.random()
        temp = round(temp,2)
        vals.append(temp)
    if values['Pressure'] == True:
        pres = np.random.random()
        pres = round(pres,2)
        vals.append(pres)
    if values['Humidity'] == True:
        hum = np.random.random()
        hum = round(hum,2)
        vals.append(hum)

    vals.append(datetime.now().strftime('%H:%M:%S.%f'))

    data_out.append(vals)
    #Works but only printing last entry
    window['Out'].update(vals)
    window.refresh()

    time.sleep(interval)
    timestamp = datetime.now()

def simple_data_retrival():
    vals = []
    if values['AQ'] == True:
        #pres = np.random.random()
        #pres = round(pres,2)
        #vals.append(pres)
        x = sensor.query()
        pm_2_5 = pm_2_5 + x[0]
        pm_10 = pm_10 + x[1]
        aqi_2_5 = aqi.to_iaqi(aqi.POLLUTANT_PM25, str(pm_2_5))
        aqi_10 = aqi.to_iaqi(aqi.POLLUTANT_PM10, str(pm_10))
        pm_2_5 = round(pm_2_5,2)
        pm_10 = round(pm_10,2)
        vals.append(pm_2_5)
        vals.append(aqi_2_5)
        vals.append(pm_10)
        vals.append(aqi_10)
    vals.append(datetime.now().strftime('%H:%M:%S.%f'))
    return vals

def fig_maker(window,fig_vals): # this should be called as a thread, then time.sleep() here would not freeze the GUI
    plt.rcParama["figure.figsize"] = [4,2]
    frame1 = plt.plot([x[-1] for x in fig_vals],[x[1] for x in fig_vals],label = 'AQI 2.5')
    frame2 = plt.plot([x[-1] for x in fig_vals],[x[3] for x in fig_vals],label = 'AQI 10')
    frame1 = plt.ylabel("Air Quality")
    frame1 = plt.xlabel("Time")
    window.write_event_value('-THREAD-', 'done.')
    time.sleep(1)
    return plt.gcf()


def draw_figure(canvas, figure, loc=(0, 0)):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg


def delete_fig_agg(fig_agg):
    fig_agg.get_tk_widget().forget()
    plt.close('all')


if __name__ == '__main__':
    # define the window layout
    layout = [[sg.Text('Environmental Pi')],#Select things to monitor
    [sg.Checkbox('Air Quality', key = 'AQ')],
    [sg.Button('update'), sg.Button('Stop', key="-STOP-"), sg.Button('Exit', key="-EXIT-")],
    [sg.Radio('Keep looping', "RADIO1", default=True, size=(12,3),key="-LOOP-"),sg.Radio('Stop looping', "RADIO1", size=(12,3), key='-NOLOOP-')],
    [sg.Text('PM 2.5 PM 10 Plot', font='Any 18')],
    [sg.Canvas(size=(320,240), key='canvas')]]

    # create the form and show it without the plot
    window = sg.Window('Air Quality App',
                       layout, finalize=True)

    fig_agg = None

    fig_vals = []

    while True:
        event, values = window.read()
        if event is None:  # if user closes window
            break

        if event == "update":
            if fig_agg is not None:
                    delete_fig_agg(fig_agg)
            vals = simple_data_retrival()
            fig_vals.append(vals)
            fig = fig_maker(window,fig_vals)
            fig_agg = draw_figure(window['canvas'].TKCanvas, fig)

        if event == "-THREAD-":
            print('Acquisition: ', values[event])
            time.sleep(1)
            if values['-LOOP-'] == True:
                if fig_agg is not None:
                    delete_fig_agg(fig_agg)
                vals = simple_data_retrival()
                fig_vals.append(vals)
                fig = fig_maker(window,fig_vals)
                fig_agg = draw_figure(window['canvas'].TKCanvas, fig)
                window.Refresh()

        if event == "-STOP-":
            window['-NOLOOP-'].update(True)

        if event == "-EXIT-":
            break


    window.close()
