import pandas as pd
import logging
import csv

file = "mock_data.csv"

df = pd.read_csv(file)

print(df.isnull())
print(df.isnull().sum())
