import pandas as pd
df = pd.read_csv('budget_data.csv', delimiter=',')
print(df)
print("Total Months: " + str(len(df)))
print("Total: $" + str(sum(df["Profit/Losses"])))

