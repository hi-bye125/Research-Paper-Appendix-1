# -*- coding: utf-8 -*-
"""Satellite2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xWkwHNve2srqAWqB4-MWa-W4v8jxwzlt

Setup Numpy, Pandas, MatPlotLib and mount Google Drive
"""

!pip install -U -q PyDrive
from google.colab import drive
drive.mount('/content/gdrive')
#may not be required if running on local machine
import pandas as pd
from matplotlib import pyplot as plt
import numpy

from google.colab import drive
drive.mount('/content/gdrive', force_remount=True)

"""Next step imports all the CSV files to Pandas Dataframes"""

alt_300=pd.read_csv('/content/gdrive/MyDrive/csv/300km.csv')
alt_500=pd.read_csv('/content/gdrive/MyDrive/csv/500km altitude var.csv')
alt_550=pd.read_csv('/content/gdrive/MyDrive/csv/550km.csv')
alt_600=pd.read_csv('/content/gdrive/MyDrive/csv/600km.csv')
alt_650=pd.read_csv('/content/gdrive/MyDrive/csv/650km.csv')
alt_700=pd.read_csv('/content/gdrive/MyDrive/csv/700km.csv')
altitude_files=[alt_300, alt_500, alt_550, alt_600, alt_650, alt_700]
#be careful to change location to the correct file path

flux_75 = pd.read_csv('/content/gdrive/MyDrive/newdata/75.csv')
flux_100=pd.read_csv('/content/gdrive/MyDrive/newdata/100.csv')
flux_125=pd.read_csv('/content/gdrive/MyDrive/newdata/125.csv')
flux_150=pd.read_csv('/content/gdrive/MyDrive/newdata/150.csv')
flux_175=pd.read_csv('/content/gdrive/MyDrive/newdata/175.csv')
flux_200=pd.read_csv('/content/gdrive/MyDrive/newdata/200.csv')
flux_225=pd.read_csv('/content/gdrive/MyDrive/newdata/225.csv')
flux_250=pd.read_csv('/content/gdrive/MyDrive/newdata/250.csv')
flux_275=pd.read_csv('/content/gdrive/MyDrive/newdata/275.csv')
flux_300=pd.read_csv('/content/gdrive/MyDrive/newdata/300.csv')
flux_files=[flux_75, flux_100, flux_125, flux_150, flux_175, flux_200, flux_225, flux_250, flux_275, flux_300]

area_5 = pd.read_csv('/content/gdrive/MyDrive/newdata/5m2.csv')
area_15 = pd.read_csv('/content/gdrive/MyDrive/newdata/15m2.csv', sep='\s+')
area_30 = pd.read_csv('/content/gdrive/MyDrive/newdata/30m2.csv')
area_45 = pd.read_csv('/content/gdrive/MyDrive/newdata/45m2.csv')
area_60 = pd.read_csv('/content/gdrive/MyDrive/newdata/60m2.csv')
area_files=[area_5, area_15, area_30,area_45, area_60]

"""Make all the charts for altitude Variation"""

new_altitude_files=[]
for i in altitude_files:
  filemod=i.query('`AltitudeVar.Earth.Altitude` >= 100')
  new_altitude_files.append(filemod)

#adjusts end point to 100km

for i in new_altitude_files:
  plt.plot(i['AltitudeVar.ElapsedSecs']/31536000,i['AltitudeVar.Earth.Altitude'])
plt.title("Altitude against Time")
plt.xlabel("Elapsed Time/years")
plt.ylabel("Altitude/km")
plt.legend(['300km','500km','550km','600km','650km','700km'],bbox_to_anchor=(1.0, 1.0), loc='upper right')

time_to_decay_altitude =[]
for i in new_altitude_files:
  timevar=i['AltitudeVar.ElapsedSecs'].iloc[-1]
  time_to_decay_altitude.append(timevar)
time_to_decay_altitude_days = [x//31536000 for x in time_to_decay_altitude]

heights=[300,500,550,600,650,700]
plt.errorbar(heights, time_to_decay_altitude_days,yerr=0.04,fmt='.')
plt.plot(heights, time_to_decay_altitude_days)
plt.title("Altitude against Time")
plt.title("Time to decay against initial altitude")
plt.xlabel("Initial Altitude/km")
plt.ylabel("Decay time/days")

log_decay=numpy.log(time_to_decay_altitude_days)
plt.plot(heights, log_decay)
plt.title("Log of time to decay against initial altitude")
plt.xlabel("Initial Altitude/km")
plt.ylabel("Log of decay time/lg-year")

"""Make plots for Solar Flux Variation"""

for i in flux_files:
  plt.plot(i['solarfluxvar.ElapsedSecs']/31536000,i['solarfluxvar.Earth.Altitude'])
plt.title("Altitude against Time(Varying Solar Flux)")
plt.xlabel("Elapsed Time/years")
plt.ylabel("Altitude/km")
plt.legend(['75sfu','100sfu','125sfu','150sfu','175sfu','200sfu', '225sfu', '250sfu', '275sfu','300sfu'], bbox_to_anchor=(1.0, 1.0), loc='upper right')

time_to_decay_flux =[]
for i in flux_files:
  timevar=i['solarfluxvar.ElapsedSecs'].iloc[-1]
  time_to_decay_flux.append(timevar)
time_to_decay_flux_days = [x//31536000 for x in time_to_decay_flux]
flux=[75,100,125,150,175,200, 225, 250, 275, 300]
plt.plot(flux,time_to_decay_flux_days)
plt.errorbar(flux, time_to_decay_flux_days,yerr=0.04,fmt='.')
plt.title("Time to decay against Solar Flux")
plt.xlabel("Average Solar Flux @10.7cm/ W m-² Hz⁻¹")
plt.ylabel("Time to decay/ years")

log_decay=numpy.log(time_to_decay_flux_days)
plt.plot(flux, log_decay)
plt.title("Log of time to decay against solar flux")
plt.xlabel("Initial Altitude/km")
plt.ylabel("Log of decay time/lg-year")

"""Make graphs for area variation"""

for i in area_files:
  plt.plot(i['AreaVar.ElapsedSecs']/31536000,i['AreaVar.Earth.Altitude'])

plt.title("Altitude against Time(Varied Cross sectional area)")
plt.xlabel("Elapsed Time/years")
plt.ylabel("Altitude/km")
plt.legend(['5m²','15m²','30m²','45m²','60m²'], bbox_to_anchor=(1.0, 1.0), loc='upper right')

time_to_decay_area =[]
for i in area_files:
  timevar=i['AreaVar.ElapsedSecs'].iloc[-1]
  time_to_decay_area.append(timevar)
time_to_decay_area_days = [x//31536000 for x in time_to_decay_area]
area=[5,15,30,45,60]
plt.plot(area,time_to_decay_area_days)
plt.errorbar(area, time_to_decay_area_days,yerr=0.04,fmt='.')
plt.title("Time to decay against Cross sectional area")
plt.xlabel("Cross sectional area/ m²")
plt.ylabel("Time to decay/years")

log_decay=numpy.log(time_to_decay_area_days)
plt.plot(area, log_decay)
plt.title("Log of time to decay against cross-sectional area")
plt.xlabel("Initial Altitude/km")
plt.ylabel("Log of decay time/lg-year")