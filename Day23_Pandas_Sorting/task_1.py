import pandas as pd

file = "employee.csv"

df = pd.read_csv(file)

clean_df = df.drop_duplicates(subset=["employee_id"],keep="last")

sorted_df = clean_df.sort_values(
        by = ["salary", "employee_name"],
        ascending = [False, True]
        ).head(3)

print("====== Top 3 Employees ======")

for rank, (_, employee) in enumerate(sorted_df.iterrows(), start=1):
    print(f"Rank {rank}")
    print(f"Employee Id: {employee['employee_id']}")
    print(f"Name: {employee['employee_name']}")
    print(f"Salary: {employee['salary']}")
    print()
