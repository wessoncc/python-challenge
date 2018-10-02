import os
import csv
csvpath = os.path.join('X:/Users/cwess_000/Data_Bootcamp/UCFLM201809DATA2/03-Python/Homework/Instructions/PyBank/Resources/', 'budget_data.csv')
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    for row in csvreader:
        print(row)