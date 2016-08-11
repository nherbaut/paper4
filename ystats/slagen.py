#!/usr/bin/env python
# turn test.csv to proper time serie

from __future__ import print_function

import datetime

import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


matplotlib.style.use('ggplot')
# read data
df = pd.read_csv("test2.csv", names=["time", "values"])
#convert time column to proper time
ts=pd.Series(data=df["values"].values,index=df.apply(lambda row: datetime.datetime.strptime(row['time'], '%Y-%m-%d %H:%M:%S'), axis=1).values)


tsr=ts.resample("1H").bfill()
tse=tsr.resample("3H").max().ffill().resample("1H").max().ffill()

#create the figure for monoplot & plot bar on the same axis
plt.figure(1)
#first plot the line
line2d=plt.plot(tsr.index,tsr, )
#get the axis and set them up
ax1=line2d[0].axes
ax1.set_ylim([min(tsr)*0.75,max(tsr)*1.25])
ax1.set_xlim(tsr.index[0], tsr.index[-1])
ax1.xaxis_date()

#then display the bar on the same axis
plt.bar(tse.index,tse, width=0.041,axes=line2d[0].axes)


#finally, display the graph
plt.show()
