'''
failed_bank_years.py
Emily Liu
Karena Yan, Adithya Paramasivam
CSE Modeling Data
Creates a scatterplot and a bar graph of the number of failed banks over time in years
From 2000 to 2017. 
'''
import matplotlib.pyplot as plt
import csv
import numpy as np 
import math

# A generic helper function for matplotlib.pyplot graphics
def make_PLTW_style(axes):
    for item in ([axes.title, axes.xaxis.label, axes.yaxis.label] +
             axes.get_xticklabels() + axes.get_yticklabels()):
        item.set_family('Georgia')
        item.set_fontsize(16)

###
# Get the directory name for data files
datafile = open('banklist.csv','r') #open banklist.csv, where the data is

datareader = csv.reader(datafile) #reads through file
headers = datareader.next() # read first row and store separately

####
#Creates empty arrays for select data
years=[]
dates=[]
number_banks=[]
months=[]

for row in datareader: #start collecting data from the csv
    year= ((row[5])) 
    year = '20' + str(year[-2:]) #make it in the 20-- format
    if (year not in years):
        years.append(year)  
    dates.append(row[5])
number = 0 #used as a counter to see how many is in a year
for year in years:
    for date in dates:
        if (year[-2:] == date[-2:]):
            number+=1 #t
    number_banks.append(number)
    number =0 #reset counter to 0 once the year changes 

#Create scatterplot 
fig_year, ax  = plt.subplots(1, 1)
ax.plot(years, number_banks, '-o') #'-o' connects points, ro leaves them discrete
ax.set_title('Number of Failed Banks vs. Year\n(2000-2017 U.S. Sample)')
ax.set_xlabel('Year')
plt.xticks(np.linspace(2000, 2017, 18, endpoint=True)) #changes the x-axes to be the years
ax.set_ylabel('Number of Failed Banks')
fig_year.show()

#Creates a bar graph of same data
years = list(reversed(years)) #reverses the list of years

fig, ax=plt.subplots(1,1)
width = 0.35 
bar_graph=ax.bar([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16], number_banks, width, align='center', color='blue')
ax.set_xticks(np.arange(17)+1) #number of x-axis ticks
ax.set_xticklabels(years)
ax.set_ylabel("Number of Failed Banks")
ax.set_xlabel("Year")
ax.set_title("Failed Bank Distribution in US By Year\n(2000-2017 U.S. Sample)")
plt.show()