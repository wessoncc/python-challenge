import os
import csv
from pathlib import Path
import pandas as pd
import numpy as np

df = pd.read_csv("~/UCFLM201809DATA2/03-Python/Homework/Instructions/PyPoll/Resources/election_data.csv")
df2 = df['Candidate'].value_counts()
TotalVotes = len(df)
df3 = df2.reset_index(drop=False)
df4 = df3.rename(columns={"index":"Name", "Candidate":"Votes"})
Khan = df4.iloc[0, 1]
Correy = df4.iloc[1, 1]
Li = df4.iloc[2, 1]
OTooley = df4.iloc[3, 1]
# df3.sort_values(df3['Votes'], ascending=False)
Winner =  df4.iloc[0, 0]
KhanPct = float((Khan/TotalVotes) * 100)
CorreyPct = float((Correy/TotalVotes) * 100)
LiPct = float((Li/TotalVotes) * 100)
OTPct = float((OTooley/TotalVotes) * 100)

print("Election Results")
print("-------------------------------------------")
print("Total Votes: " + str(TotalVotes))
print("-------------------------------------------")
print("Khan: " + f'{KhanPct:.3f}' + "%" + "  " + "(" + str(Khan) + ")")
print("Correy: " + f'{CorreyPct:.3f}' + "%" + "  " + "(" + str(Correy) + ")")
print("Li: " + f'{LiPct:.3f}' + "%" + "  " + "(" + str(Li) + ")")
print("O'Tooley: " + f'{OTPct:.3f}' + "%" + "  " + "(" + str(OTooley) + ")")
print("-------------------------------------------")
print("Winner: " + Winner)
print("-------------------------------------------")