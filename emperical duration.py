import pandas as pd
import numpy as np
from regression import myregression
import matplotlib.pyplot as plt


df = pd.read_csv('fredgraph.csv')
new_columns = ['Date', 'EFF', '10YR', '3M', '2YR']
df.columns = new_columns

df.index = df['Date']
df.index = pd.to_datetime(df.index)
df = df[new_columns[1:]].apply(pd.to_numeric, errors='coerce')
df = df.dropna()
print(df.head(10))

# Regress EFF on 10yr no lag
x1 = df['EFF'].to_numpy().reshape(len(df['EFF']), 1)
y1 = df['10YR'].to_numpy().reshape(len(df['10YR']), 1)
reg1 = myregression(x=x1, y=y1, constant=True)
print(reg1)


roll1 = 10
x2 = df['EFF'].iloc[roll1:].to_numpy().reshape(len(df['EFF']) - roll1, 1)
y2 = df['10YR'].shift(roll1).iloc[roll1:].to_numpy().reshape(len(df['10YR'])- roll1, 1)
reg2 = myregression(x=x2, y=y2, constant=True)
print(reg2)

fig, axes = plt.subplots(1,1, figsize=(12,9))
axes.plot(df.index, df['EFF'])
axes.plot(df.index, df['10YR'])
plt.title('Fuzzy is a bad slark')
plt.savefig('test_fig')
