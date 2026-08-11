import pandas as pd

file = "mock_data.csv"

df = pd.read_csv(file)
transformed_df = df[df["salary"] > 80000]
double_transform = transformed_df[transformed_df["job"] == "Data Engineer"]

print(transformed_df)

print(double_transform)
