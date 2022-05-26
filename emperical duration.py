import pandas as pd
import numpy as np
from regression import myregression
import matplotlib.pyplot as plt
from mympl import mympl


df = pd.read_csv('fredgraph.csv')
new_columns = ['Date', 'EFF', '10YR', '3M', '2YR']
df.columns = new_columns

df.index = df['Date']
df.index = pd.to_datetime(df.index)
df = df[new_columns[1:]].apply(pd.to_numeric, errors='coerce')
df = df.dropna()


# Regress EFF on 10yr no lag
x1 = df['EFF'].to_numpy().reshape(len(df['EFF']), 1)
y1 = df['10YR'].to_numpy().reshape(len(df['10YR']), 1)
reg1 = myregression(x=x1, y=y1, constant=True)
dates1 = df.index
reg_values = [reg1[0] + reg1[1] * eff for eff in x1]


print(reg1)


roll1 = 10
x2 = df['EFF'].iloc[roll1:].to_numpy().reshape(len(df['EFF']) - roll1, 1)
y2 = df['10YR'].shift(roll1).iloc[roll1:].to_numpy().reshape(len(df['10YR'])- roll1, 1)

reg2 = myregression(x=x2, y=y2, constant=True)
print(reg2)

mympl()
fig, axes = plt.subplots(1,1)
#axes.plot(dates1, df['EFF'])
axes.plot(dates1, df['10YR'])
axes.plot(dates1, df['EFF'])
axes.plot(dates1, reg_values )

plt.title('Fuzzy is a bad slark')
plt.savefig('test_fig')
