import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os

# Format quarterly income table
income = pd.read_excel("quarterlyincome.xls")
income = income[income.columns[::-1]]
income.set_index('time', inplace=True)
income = income.transpose()
selected_income = income.loc['2000Q1':, 'Domestic office loans':'Other interest income']
selected_income['times'] = list(selected_income.index.values)
banklist = pd.read_csv("banklist.csv")

closes = list(banklist["Closing Date"])
quarters = []

for y in range(2000,2017):
    for q in range(1,5):
        dates = []
        for c in closes:
            if str(y) in c and (c.startswith(str(3*q-2)+'/') or c.startswith(str(3*q-1)+'/') or c.startswith(str(3*q)+'/')):
                dates.append(c)
        quarters.append(len(dates))
quarters = quarters[:-1]
quarters = [i * 10 for i in quarters]

plt.style.use('seaborn-darkgrid')

my_dpi=96
plt.figure(figsize=(480/my_dpi, 480/my_dpi), dpi=my_dpi)

# multiple line plot
for column in selected_income.drop('times', axis=1):
    plt.xticks(list(range(67)), list(selected_income['times']), rotation=60)
    plt.plot(list(range(67)), list(selected_income[column]), marker='', color='grey', linewidth=1, alpha=0.4)

# Add the interesting curve, but bigger with distinct color
plt.xticks(list(range(67)), list(selected_income['times']), rotation=60)
plt.plot(list(range(67)), income.loc['2000Q1':, 'Total interest income'], marker='', color='orange', linewidth=4, alpha=0.7)

plt.xticks(list(range(67)), list(selected_income['times']), rotation=60)
plt.scatter(list(range(67)), [-15000]*67, s=quarters, c='orange')

# Add legend
plt.legend(loc=2, ncol=2)

# Add titles
plt.xlabel("Quarter")
plt.ylabel("Income ($ millions)")

# Display graph
plt.show()
