import pandas as pd

file = "employee.csv"

df = pd.read_csv(file)
total_count = len(df)

duplicates = df[df.duplicated(subset=["employee_id"],keep="last")]
clean_df = df.drop_duplicates(subset=["employee_id"],keep="last")

duplicate_count = len(duplicates)
clean_count = len(clean_df)

print(f"-----Data Quality-----")
print(f"Total records: {total_count}")
print(f"Clean Data: {clean_count}")
print(f"Duplicate Data: {duplicate_count}")
