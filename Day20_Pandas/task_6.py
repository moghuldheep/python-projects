import pandas as pd

file = "mock_data.csv"

df = pd.read_csv(file)

df["bonus"] = df["salary"].apply( lambda salary: salary * 0.10 if salary >= 70000 else salary * 0.05)

df["high_salary"] = df["salary"] >= 70000

print(df)
