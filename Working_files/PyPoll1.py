import os
import csv
from pathlib import Path
import pandas as pd
import numpy as np
#PyPollFile = ('Users/Wesson/UCFLM201809DATA2/03-Python/Homework/Instructions/PyPoll/Resources/election_data.csv')


df = pd.read_csv("~/UCFLM201809DATA2/03-Python/Homework/Instructions/PyPoll/Resources/election_data.csv")
#print(df)

df3 = df['Candidate'].value_counts()
df2 = df.groupby(df['Candidate'])
Khan = len(df[['Candidate'] == "Khan"])
#print(Khan)
TotalVotes = len(df)
# df3 = df3.reset_index(drop=False)
# df3 = df3.rename(columns={"index":"Name", "Candidate":"Votes"})
print(df3)
print('Khan')
Khan = df3['Khan']
Correy = df3['Correy']
Li = df3['Li']
OTooley = df3["O'Tooley"]
#Candidates = {'Khan':Khan, 'Correy':Correy, 'Li':Li, 'OTooley':OTooley}
Winner = (max(df3['Votes']))





print("Election Results")
print("-------------------------------------------")
print("Total Votes: " + str(TotalVotes))
print("-------------------------------------------")
# print("Total: $" + str(sum(df["Profit/Losses"])))
# print("Average Change: $" + str(round(TotalAvgChange, 2)))
# print("Greatest Increase in Profits: ")
# print("Greatest Decrease in Profits: ")
print("Khan: " + f'{KhanPct:.3f}' + "%" + "  " + "(" + str(Khan) + ")")
print("Correy: " + f'{CorreyPct:.3f}' + "%" + "  " + "(" + str(Correy) + ")")
print("Li: " + f'{LiPct:.3f}' + "%" + "  " + "(" + str(Li) + ")")
print("O'Tooley: " + f'{OTPct:.3f}' + "%" + "  " + "(" + str("O'Tooley") + ")")
print("-------------------------------------------")
print("Winner: ")



