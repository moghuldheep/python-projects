files = [
    "customers.csv",
    "employees.xlsx",
    "orders.csv",
    "notes.txt",
    "sales.csv"
]

for i in files:
    if i.endswith("csv"):
        print(i)
