import matplotlib.pyplot as plt
import os.path
import csv

def makePie(y):
    if y>=0 and y <10:
        y = '0' + str(y)
    else:
        y = str(y)
        
    directory = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(directory, 'banklist.csv') 
    datafile = open(filename,'rb')
    
    acq_banks = {}
    total = 0
    # Read data from the CSV file
    datareader = csv.reader(datafile) 
    for row in datareader:
        year= ((row[5]))
        if year[-2:] == y:
            key = row[4]
            total+=1
            if key in acq_banks:
                acq_banks[key]+=1
            else:
                acq_banks[key]=1
    sort_banks = sorted(acq_banks.items(), key=lambda x:x[1])
    if len(sort_banks) > 6:
        sort_banks = sort_banks[len(sort_banks)-7:len(sort_banks)-1]
        top_list = [item[1] for item in sort_banks]
        sort_banks.append(('Other',total-sum(top_list)))
    
    labels = [item[0] for item in sort_banks]
    sizes = [item[1] for item in sort_banks]
    colors = ['#442D65','#775BA3','#91C5A9','#F8E1B4','#F98A5F','#666666','#25AAA0','#66C3BC','#41D4CF']
    
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')
    plt.title('Proportion of Failed Banks Acquired by Various Institutions, Year 20' + y)
    plt.show()