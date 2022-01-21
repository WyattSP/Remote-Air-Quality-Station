# -*- coding: utf-8 -*-
"""
@author: wyattpetryshen
"""

import pandas as pd
import plotly.express as px
import plotly.offline


#Import Data
path = r'Path'
data = pd.read_csv(path+'aq_log.txt', sep=",", header=None)

#Set column names
data.columns = ["Time", "PM 2.5", "AQI 2.5", "PM 10", "AQI 10"]

#Plot data
fig = px.line(data, x="Time", y=data.columns,
              hover_data={"Time": "|%B %d, %Y %H:%M:%S"},
              title='Air Quality Sensor Data')
fig.update_xaxes(
    tickformat="%H:%M:%S")

plotly.offline.plot(fig)
