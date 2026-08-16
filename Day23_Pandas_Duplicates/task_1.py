import pandas as pd

file = "employee.csv"

df = pd.read_csv(file)

duplicates = df[df.duplicated(subset=["employee_id"],keep="last")]

clean_df = df.drop_duplicates(subset=["employee_id"],keep="last")

print(f"Clean Data: \n{clean_df}")
print(f"Duplicate Data: \n{duplicates}")
