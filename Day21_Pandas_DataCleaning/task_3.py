import csv
import pandas as pd

file = "mock_data.csv"

df = pd.read_csv(file)

print(df[df["salary"].isnull()])

df["salary"] = pd.to_numeric(df["salary"], errors="coerce")

invalid_df = df[df["salary"].isnull()]
valid_df = df[df["salary"].notnull()]

print(f"INVALID RECORDS")
print(invalid_df)
print(f"VALID RECORDS")
print(valid_df)

print(f"Total records: {len(df)}")
print(f"Valid records: {len(valid_df)}")
print(f"Invalid records: {len(invalid_df)}")
