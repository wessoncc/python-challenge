import os
import csv
import pandas as pd
csvpath = os.path.join('X:/Users/cwess_000/Data_Bootcamp/UCFLM201809DATA2/03-Python/Homework/Instructions/PyBank/Resources/', 'budget_data.csv')
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')


df = pd.read_csv('budget_data.csv', delimiter=',')
print(df)