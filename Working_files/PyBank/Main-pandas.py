import os
import csv
import pandas as pd
import numpy as np
csvpath = os.path.join('X:/Users/cwess_000/Data_Bootcamp/UCFLM201809DATA2/03-Python/Homework/Instructions/PyBank/Resources/', 'budget_data.csv')
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')


df = pd.read_csv('budget_data.csv', delimiter=',')
PandL = df['Profit/Losses'].values
average_change = PandL[1:] - PandL[:-1]
#average_change = (df["Profit/Losses"[i]] - df["Profit/Losses"[i + 1]])
sum_of_change = sum(average_change) 
TotalAvgChange = (sum_of_change/(len(df) - 1))
    


print("Financial Analysis")
print("-------------------------------------------")
print("Total Months: " + str(len(df)))
print("Total: $" + str(sum(df["Profit/Losses"])))
print("Average change: $" + str(round(TotalAvgChange, 2)))


