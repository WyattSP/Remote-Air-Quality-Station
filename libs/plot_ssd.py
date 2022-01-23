"""
Created on Tue Jan 18 23:11:24 2022

@author: wyattpetryshen
"""

import pandas as pd
import plotly.express as px
import plotly.offline

import argparse

my_parser = argparse.ArgumentParser(description="Plot AQ Data")

my_parser.add_argument('-t',
                       type = str,
                       help = 'Data input')

args = my_parser.parse_args()
input_t = args.t

#Import Data
path = r'Path'
data = pd.read_csv(path+'aq_log.txt', sep=",", header=None)

def plot_data(Data_input):

    try:

        if str(Data_input) == str('AQ'):


            #Set column names
            data.columns = ["Time", "PM2.5", "AQI 2.5", "PM10", "AQI PM 10"]

            #Plot data
            fig = px.line(data, x="Time", y=data.columns,
                          hover_data={"Time": "|%B %d, %Y %H:%M:%S"},
                          title='Air Quality Sensor Data')
            fig.update_xaxes(
                tickformat="%H:%M:%S")

            plotly.offline.plot(fig)


        if str(Data_input) == str('ENV'):


            #Set column names
            data.columns = ["Time", "Humidity", "Temperature", "Pressure"]

            #Plot data
            fig = px.line(data, x="Time", y=data.columns,
                          hover_data={"Time": "|%B %d, %Y %H:%M:%S"},
                          title='Environmental Sensor Data')
            fig.update_xaxes(
                tickformat="%H:%M:%S")

            plotly.offline.plot(fig)


        if str(Data_input) == str('ALL'):


            #Set column names
            data.columns = ["Time", "PM2.5", "AQI 2.5", "PM10", "AQI PM 10", "Humidity", "Temperature", "Pressure"]

            #Plot data
            fig = px.line(data, x="Time", y=data.columns,
                          hover_data={"Time": "|%B %d, %Y %H:%M:%S"},
                          title='Air Quality Sensor Data')
            fig.update_xaxes(
                tickformat="%H:%M:%S")

            plotly.offline.plot(fig)


    except:
        print("Data Input Required")
        pass

if __name__ == "__main__":
    plot_data(input_t)
