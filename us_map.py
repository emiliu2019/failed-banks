from mpl_toolkits.basemap import Basemap
from matplotlib.colors import rgb2hex
from matplotlib.patches import Polygon
import matplotlib.pyplot as plt
import os.path
import csv

fig, ax = plt.subplots(1,1, figsize=(16,8))
usMap = Basemap(ax = ax, 
            resolution='c', 
            llcrnrlon=-119, llcrnrlat=22, urcrnrlon=-64, urcrnrlat=49,
            projection='lcc', lat_1=33, lat_2=45, lon_0=-95)
usMap.drawcoastlines()
usMap.drawcountries()
usMap.drawstates()

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

fig.show()