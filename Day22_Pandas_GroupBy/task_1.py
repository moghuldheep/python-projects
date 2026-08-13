import pandas as pd

df = pd.read_csv("mock_data.csv")

print(df.groupby("job")["salary"].mean())
