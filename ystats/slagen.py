#!/usr/bin/env python
# turn test.csv to proper time serie

from __future__ import print_function

import datetime

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib import animation

matplotlib.style.use('ggplot')

fig = plt.figure()

# read data
df = pd.read_csv("test2.csv", names=["time", "values"])
# convert time column to proper time
ts = pd.Series(data=df["values"].values,
               index=df.apply(lambda row: datetime.datetime.strptime(row['time'], '%Y-%m-%d %H:%M:%S'),
                              axis=1).values)

ts = ts[-50:]
# tsr=ts.resample("1H").max().ffill()
tsr = ts

# create the figure for monoplot & plot bar on the same axis

# first plot the line
ax = plt.axes(xlim=[tsr.index[0], tsr.index[-1]], ylim=[min(tsr) * 0.75, max(tsr) * 1.25])
ax.xaxis_date()
line2d = ax.plot(tsr.index, tsr, zorder=1)
bar = ax.bar([], [])


def get_tse(tsr, win):
    # tse=tsr.resample("%dH"%win).max().bfill()
    # tse=tse.rolling(window=win,center=True).max()
    # tse=tse.resample("1H").max().bfill()
    offset = pd.tseries.offsets.Hour(win)
    tsrr = tsr.resample("1H").bfill()
    tse = pd.Series(index=tsrr.index)

    start = tsr.index[0]
    end = tsr.index[-1]
    for i in range(0, int((end - start) / offset)):
        range_max = np.max(tsrr[(start + i * offset):(start + (i + 1) * offset)].values)
        tse[(start + i * offset):(start + (i + 1) * offset)] = range_max

    tse[(start + (i + 1) * offset):end] = np.max(tsrr[(start + (i + 1) * offset):end].values)

    # print(tse)
    return tse


def get_plot(win):
    # get the axis and set them up
    tse = get_tse(tsr, win + 1)
    # then display the bar on the same axis
    # bar, = ax1.plot([], [], width=0.041, axes=line2d[0].axes)
    bar = ax.bar(tse.index, tse, width=1/24.0, zorder=1)
    return bar


def init():
    return line2d


get_plot(2)

#anim = animation.FuncAnimation(fig, get_plot, init_func=init, frames=20, interval=300, blit=True)
#anim.save('basic_animation.mp4',)
plt.show()
