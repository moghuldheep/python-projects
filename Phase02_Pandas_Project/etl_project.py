import pandas as pd
from datetime import datetime

employee_file = "employee.csv"
department_file = "department.csv"

employee_df = pd.read_csv(employee_file)
department_df = pd.read_csv(department_file)

total_count = len(employee_df)

employee_df["salary"] = pd.to_numeric(employee_df["salary"],errors="coerce")

valid_salary_df = employee_df[employee_df["salary"].notnull()]
invalid_salary_df = employee_df[employee_df["salary"].isnull()]

invalid_salary_count = len(invalid_salary_df)

duplicate_df = valid_salary_df.duplicated(subset=["employee_id"],keep="last")
clean_df = valid_salary_df.drop_duplicates(subset=["employee_id"],keep="last")

duplicate_count = duplicate_df.sum()

combined_df = clean_df.merge(
        department_df,
        on = ["department_id"],
        how = "left"
        )
invalid_department_df = combined_df[combined_df["department_name"].isnull()]
valid_df = combined_df[combined_df["department_name"].notnull()].copy()

valid_count = len(valid_df)
invalid_department_count = len(invalid_department_df)

valid_df["bonus"] = valid_df["salary"].apply(lambda salary: salary * 0.10 if salary >= 70000 else salary * 0.05)
valid_df["high_Salary"] = valid_df["salary"] >= 90000

print(valid_df)
print(f"====== ETL Summary ======")
print(f"Total Input Records: {total_count}")
print(f"Invalid Salary Records: {invalid_salary_count}")
print(f"Duplicate Records: {duplicate_count}")
print(f"Valid Employee Records: {valid_count}")
print(f"Invalid Department Records: {invalid_department_count}")

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

print(f"====== Department Summary ======")
print(valid_df.groupby("department_name").agg(
    employee_count=("employee_name","count"),
    average_salary=("salary","mean"),
    maximum_salary=("salary","max"),
    minimum_salary=("salary","min"),
    total_bonus=("bonus","sum")
    )
      )


