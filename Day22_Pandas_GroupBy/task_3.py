import pandas as pd

df = pd.read_csv("mock_data.csv")

print(df.groupby("job").agg(
    employee_count=("name","count"),
    average_salary=("salary","mean"),
    maximum_salary=("salary","max"),
    minimum_salary=("salary","min")
    )
      )
