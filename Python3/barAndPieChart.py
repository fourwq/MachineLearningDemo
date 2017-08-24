#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 23:04:30 2017

@author: camera1
"""

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.rcParams['axes.titlesize'] = 20
mpl.rcParams['xtick.labelsize'] = 20
mpl.rcParams['ytick.labelsize'] = 20
mpl.rcParams['axes.labelsize'] = 20
mpl.rcParams['xtick.major.size'] = 0
mpl.rcParams['ytick.major.size'] = 0

speed_map = {
        'dog':(48, '#7199cf'),
        'cat':(45,'#4fc4aa'),
        'cheeetah':(120,'#e1a7a2')                   
        }

fig = plt.figure(figsize = (8,16), dpi=72,)

ax = fig.add_subplot(211)
ax.set_title('Running speed - bar chart')

xticks = np.arange(3)

bar_width = 0.5

animals = speed_map.keys()

speeds = [x[0] for x in speed_map.values()]

colors = [x[1] for x in speed_map.values()]

bars = ax.bar(xticks, speeds, width=bar_width, edgecolor = 'none')

ax.set_ylabel('speed')

ax.set_xticks(xticks +bar_width/2)

ax.set_xticklabels(animals)

ax.set_xlim([bar_width/2-0.5, 3-bar_width/2])

ax.set_ylim([0, 125])

for bar, color in zip(bars, colors):
    bar.set_color(color)

ax = fig.add_subplot(212)

ax.set_title('running speed - pie chart')


labels = ['{}\n{} km/h'.format(animal,speed) for animal, speed in zip(animals, speeds)]

ax.pie(speeds, labels = labels, colors = colors)

plt.show()




