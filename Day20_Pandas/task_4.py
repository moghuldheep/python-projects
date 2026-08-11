import pandas as pd

file = "mock_data.csv"

df = pd.read_csv(file)

#print(df[["name","salary"]].dtypes)

print(df["name"].dtypes)
