import numpy as np
from mpl_toolkits.basemap import Basemap
from matplotlib.colors import rgb2hex
from matplotlib.patches import Polygon
import matplotlib.pyplot as plt
import os.path
import csv

directory = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(directory, 'banklist.csv') 
datafile = open(filename,'rb')

failures = {}
# Read data from the CSV file
datareader = csv.reader(datafile) 
headers = datareader.next() # read first row and store separately
for row in datareader:
    key = row[2]
    if key in failures:
        failures[key]+=1
    else:
        failures[key]=1
print failures

fig, ax = plt.subplots(1,1, figsize=(16,8))
usMap = Basemap(ax = ax, 
            resolution='c', 
            llcrnrlon=-119, llcrnrlat=22, urcrnrlon=-64, urcrnrlat=49,
            projection='lcc', lat_1=33, lat_2=45, lon_0=-95)

usMap.readshapefile('st99_d00', name='states', drawbounds=True)

colors={}
statenames=[]
vmax = 105.

for shapedict in usMap.states_info:
    statename = shapedict['NAME']
    if statename in failures:
        pop = failures[statename]
        if pop>40:
            colors[statename] = '#4390bc'
        elif pop>=12:
            colors[statename] = '#68a7ca'
        elif pop>=7:
            colors[statename] = '#8dbdd8'
        elif pop>=3:
            colors[statename] = '#b2d3e6'
        else:
            colors[statename] = '#d8e9f3'
    else:
        colors[statename] = '#d8e9f3'
       
    statenames.append(statename)

ax = plt.gca()
for shape, seg in enumerate(usMap.states):
    color = colors[statenames[shape]]
    poly = Polygon(seg, facecolor=color, edgecolor=color)
    ax.add_patch(poly)

fig.show()