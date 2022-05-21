import pandas as pd
import numpy as np
from regression import myregression


df = pd.read_csv('fredgraph.csv')
new_columns = ['Date', 'EFF', '10YR', '3M', '2Y']
df.columns = new_columns
df = df[new_columns[1:]].apply(pd.to_numeric, errors='coerce')
df = df.dropna()
print(df.shape)

# Regress EFF on 10yr no lag
x1 = df['EFF'].to_numpy().reshape(len(df['EFF']), 1)
y1 = df['10YR'].to_numpy().reshape(len(df['10YR']), 1)
reg1 = myregression(x=x1, y=y1, constant=True)
print(reg1)



roll1 = 1
x2 = df['EFF'].iloc[roll1:].to_numpy().reshape(len(df['EFF']) - roll1, 1)
y2 = df['10YR'].shift(roll1).iloc[roll1:].to_numpy().reshape(len(df['10YR'])- roll1, 1)
reg2 = myregression(x=x2, y=y2, constant=True)
print(reg2)

