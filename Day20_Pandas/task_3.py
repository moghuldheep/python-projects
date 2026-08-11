import pandas as pd

file = "mock_data.csv"

df = pd.read_csv(file)
df.info()
df.describe()

