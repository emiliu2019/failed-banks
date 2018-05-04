import pandas as pd
import seaborn as sns
import os

print os.getcwd()
income = pd.read_excel("quarterlyincome.xls")
print income.columns
