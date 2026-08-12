import csv
import pandas as pd

file = "mock_data.csv"

df = pd.read_csv(file)

print(df[df["salary"].isnull()])

df["salary"] = df["salary"].fillna(0)

print(df.dtypes)


