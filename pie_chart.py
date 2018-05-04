'''Creates a pie chart illustrating proportion of failed banks between 
2000 and 2017 acquired by various institutions. Top ten most frequest 
institutions displayed individually; remainder grouped into Other slice.'''

import matplotlib.pyplot as plt
import os.path
import csv

#establish file path
directory = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(directory, 'banklist.csv') 
datafile = open(filename,'rb')

acq_banks = {} #initialize dictionary
total = 0 #count of total failed banks
# Read data from the CSV file
datareader = csv.reader(datafile) 

#parse through each row in file
for row in datareader:
    key = row[4] #obtain acquiring institution
    total+=1 #increment number of failures
    if key in acq_banks:
        acq_banks[key]+=1 #increment count for existing institution
    else:
        acq_banks[key]=1 #add new institution
        
#obtain top ten institutions with most banks acquired
sort_banks = sorted(acq_banks.items(), key=lambda x:x[1])
sort_banks = sort_banks[len(sort_banks)-10:len(sort_banks)]

#calculate number of banks acquired by top ten institutions
top_list = [item[1] for item in sort_banks]

#add other slice for remaining bank failures
sort_banks.append(('Other',total-sum(top_list)))

labels = [item[0] for item in sort_banks] #list of bank names
sizes = [item[1] for item in sort_banks] #list of number of acquisitions
colors = ['#c0c0c0','#5da5da', '#faa43a','#60bd68','#f17cb0','#b2912f',
'#b27cb2','#decf3f','#f15854','#ffb6c1','#68a7ca'] #list of colors
explode = (0,0,0,0,0,0,0,0,0,0,0.1)

#create pie chart and set title
plt.pie(sizes, explode=explode,labels=labels, colors=colors, autopct='%1.1f%%',startangle=140)
plt.axis('equal') 
plt.title('Proportion of Failed Banks Acquired by Various Institutions')

#display chart
plt.show()