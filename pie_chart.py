import matplotlib.pyplot as plt
import os.path
import csv

directory = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(directory, 'banklist.csv') 
datafile = open(filename,'rb')

acq_banks = {}
total = 0
# Read data from the CSV file
datareader = csv.reader(datafile) 
headers = datareader.next() # read first row and store separately
for row in datareader:
    key = row[4]
    total+=1
    if key in acq_banks:
        acq_banks[key]+=1
    else:
        acq_banks[key]=1
sort_banks = sorted(acq_banks.items(), key=lambda x:x[1])
sort_banks = sort_banks[len(sort_banks)-10:len(sort_banks)]
top_list = [item[1] for item in sort_banks]
sort_banks.append(('Other',total-sum(top_list)))

labels = [item[0] for item in sort_banks]
sizes = [item[1] for item in sort_banks]
colors = ['#c0c0c0','#5da5da', '#faa43a','#60bd68','#f17cb0','#b2912f','#b27cb2','#decf3f','#f15854','#ffb6c1','#68a7ca']
explode = (0,0,0,0,0,0,0,0,0,0,0.1)

plt.pie(sizes, explode=explode,labels=labels, colors=colors, autopct='%1.1f%%',startangle=140)
plt.axis('equal')
plt.title('Proportion of Failed Banks Acquired by Various Institutions')
plt.show()