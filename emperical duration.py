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
x = df['EFF'].to_numpy().reshape(len(df['EFF']), 1)
y = df['10YR'].to_numpy().reshape(len(df['10YR']), 1)

reg1 = myregression(x=x, y=y, constant=True)
print(reg1)
