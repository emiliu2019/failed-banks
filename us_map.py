'''Creates a map of US with states colorized based on number of bank failures
between 2000 and 2017. A darker color indicates more failures.'''

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import os.path
import csv

#establish file path
directory = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(directory, 'banklist.csv') 
datafile = open(filename,'rb')

failures = {} #initialize dictionary
# Read data from the CSV file
datareader = csv.reader(datafile) 

#parse through each row in file
for row in datareader:
    key = row[2] #obtain state
    if key in failures: 
        failures[key]+=1 #increment failure count for state
    else:
        failures[key]=1 #add state to dictionary

#plot map of United States
fig, ax = plt.subplots(1,1, figsize=(16,8))
usMap = Basemap(ax = ax, 
            resolution='c', 
            llcrnrlon=-119, llcrnrlat=22, urcrnrlon=-64, urcrnrlat=49,
            projection='lcc', lat_1=33, lat_2=45, lon_0=-95)
#draw state boundaries using reference file
usMap.readshapefile('st99_d00', name='states', drawbounds=True)
plt.title('US States Colorized Based on Number of Bank Failures, 2000-2017')

colors={}
statenames=[]

#parse through list of US states
for shapedict in usMap.states_info:
    statename = shapedict['NAME']
    if statename in failures:
        fail = failures[statename] #obtain number of failurs
        #assign color to state based on number of failures
        if fail>40:
            colors[statename] = '#4390bc'
        elif fail>=12:
            colors[statename] = '#68a7ca'
        elif fail>=7:
            colors[statename] = '#8dbdd8'
        elif fail>=3:
            colors[statename] = '#b2d3e6'
        else:
            colors[statename] = '#d8e9f3'
    #if no failures in state
    else:
        colors[statename] = '#ffffff'  
    statenames.append(statename)

#parse through plottable "patches" of states from reference file
for shape, seg in enumerate(usMap.states):
    #downscale size of Alaska and translate to bottom of map
    if statenames[shape] == 'Alaska':
        seg =list(map(lambda (x,y): (0.3*x + 1000000, 0.3*y - 1100000), seg))
    #translate Hawaii to bottom of map and eliminate small islands
    if statenames[shape] == 'Hawaii' and len(seg)>20:
        seg = list(map(lambda (x, y):(x+5200000, y-1400000), seg))    
    color = colors[statenames[shape]] #obtain assigned color for state
    #plot state patch with assigned color
    poly = mpatches.Polygon(seg, facecolor=color, edgecolor='black', linewidth=0.75)
    ax.add_patch(poly)

#create color legend for map
patch1 = mpatches.Patch(color='#4390bc', label='>40 failures')
patch2 = mpatches.Patch(color='#68a7ca', label='12-40 failures')
patch3 = mpatches.Patch(color='#8dbdd8', label='8-11 failures')
patch4 = mpatches.Patch(color='#b2d3e6', label='4-7 failures')
patch5 = mpatches.Patch(color='#d8e9f3', label='1-3 failures')
patch6 = mpatches.Patch(color='#ffffff', label='0 failures')
ax.legend(fontsize=8.5, handles=[patch1, patch2, patch3, patch4, patch5, patch6])

#display map
fig.show()