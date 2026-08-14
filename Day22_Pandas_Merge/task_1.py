import pandas as pd

employee_file = "mock_data.csv"
department_file = "departments.csv"

employee_df = pd.read_csv(employee_file)
department_df = pd.read_csv(department_file)

new_df = employee_df.merge(
        department_df,
        on = "department_id",
        how = "left"
        )

valid_df = new_df[new_df["department"].notnull()]

invalid_department = new_df[new_df["department"].isnull()]
print(valid_df)
print(invalid_department)
