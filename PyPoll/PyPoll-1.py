import os
import csv
import pandas as pd
import numpy as np
csvpath = os.path.join('X:/Users/cwess_000/Data_Bootcamp/UCFLM201809DATA2/03-Python/Homework/Instructions/PyPoll/Resources/', 'election_data.csv')
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for i,row in enumerate(csvreader):
        print(row)
        if(i >= 9):
            break