import pandas as pd

file = "mock_data.csv"

df = pd.read_csv(file)

print(df.head(2))

print(df.tail(2))

print(df.shape)

print(df.columns)

print(df.dtypes)
