from sds011sensor import *
import aqi
import time

#Create sensor instance
sensor = SDS011("/dev/ttyUSB0")

#Toogle sensor on and off
#sensor.sleep(sleep = False) #on
#sensor.sleep(sleep = True) #off
#pm_2_5, pm_10 = sensor.query()

#data collection
def air_data(n = 3, runs = 1):
    sensor.sleep(sleep=False)
    pm_2_5 = 0
    pm_10 = 0
    time.sleep(10)
    aq_data = []

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
            print(pm_2_5,aqi_2_5,pm_10,aqi_10)
            aq_data.append((pm_2_5,aqi_2_5,pm_10,aqi_10))

    except KeyboardInterrupt:
        pass

    return(aq_data)
