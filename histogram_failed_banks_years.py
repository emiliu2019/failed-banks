'''
histogram_age_income.py 
reads data from the age_income_feb14.csv
and creates two histograms: the age distribution and the income 
distribution. The data are from U.S. Census Bureau's February 2014 
Current Population Survey. 

(c) 2014 Project Lead The Way
'''
import matplotlib.pyplot as plt
import csv

# A generic helper function for matplotlib.pyplot graphics
def make_PLTW_style(axes):
    for item in ([axes.title, axes.xaxis.label, axes.yaxis.label] +
             axes.get_xticklabels() + axes.get_yticklabels()):
        item.set_family('Georgia')
        item.set_fontsize(16)

###
# Get the income/age data from CSV
###
# Get the directory name for data files
# import os.path
# directory = os.path.dirname(os.path.abspath(__file__))
# # Build an absolute filename from directory + filename
# filename = os.path.join(directory, 'banklist.csv')
datafile = open('banklist.csv','r')
#data = datafile.readlines()

datareader = csv.reader(datafile) 
headers = datareader.next() # read first row and store separately

####
# Transform the data from strings to signed integers
####
years=[]
dates=[]
number_banks=[]

for row in datareader:
    year= ((row[5]))
    if ('20'+year[-2:] not in years):
        years.append('20'+year[-2:])  
    dates.append(row[5])
print years
number = 0
for year in years:
    for date in dates:
        if (year[-2:] == date[-2:]):
            number+=1
    number_banks.append(number)
    number =0
print number_banks

#Create scatterplot 
fig, ax  = plt.subplots(1, 1)
ax.plot(years, number_banks, '-o') #'-o' connects points, ro leaves them discrete
ax.set_title('Number of Failed Banks vs. Year\n(2000-2017 U.S. Sample)')
ax.set_xlabel('Year')
ax.set_ylabel('Number of Failed Banks')

fig.show()

#Histogram 1
fig_year, ax  = plt.subplots(1, 1)
a = ax.hist(number_banks, color='cyan', bins=range(2000,2017,1)) 
ax.set_title('Failed Bank Distribution in 2000-2017 U.S. Sample')
ax.set_xlabel('Year')
ax.set_ylabel('Number of Failed Banks')
make_PLTW_style(ax)
fig_year.show()

#Bar graph
plt.bar(years, number_banks)
plt.xticks(years, years)
plt.ylabel("Number of Failed Banks")
plt.xlabel("Year")
plt.title("Failed Bank Distribution in US By Year")
plt.show()