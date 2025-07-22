import pandas as pd

df = pd.read_csv('dinoDatasetCSV.csv')
df1 = pd.read_csv('dz.csv')
print(df.head())
print(df.info())
print(df.describe())
print(df1.describe())