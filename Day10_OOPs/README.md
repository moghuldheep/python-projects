# Day 10 - Object-Oriented Programming (OOP)

## 📌 Topics Covered
- Introduction to Classes and Objects
- Constructors (`__init__`)
- Instance Attributes
- Instance Methods
- The `self` Keyword
- Creating Multiple Objects
- Reading CSV Data into Objects
- Processing Objects using Loops
- Object State Modification

---

## 📝 Tasks Completed

### Task 1
Created an `Employee` class with:
- Name
- Salary

Created multiple Employee objects and displayed their values.

---

### Task 2
Added a `display()` method to print employee details.

---

### Task 3
Implemented a `calculate_bonus()` method.

Business Logic:
- Salary >= 50,000 → 10% Bonus
- Salary < 50,000 → 5% Bonus

---

### Task 4
Implemented `is_high_salary()` method.

Returns:
- `True` if salary >= 70,000
- `False` otherwise

---

### Task 5
Read employee data from a CSV file.

For every record:
- Read CSV row
- Create an Employee object
- Store the object inside a list

---

### Task 6
Processed all Employee objects by calling:
- `display()`
- `calculate_bonus()`
- `is_high_salary()`

using a loop.

---

## 🚀 Mini Project

Developed a simple Employee ETL Processor.

Workflow:

CSV File
↓
Read Records
↓
Create Employee Objects
↓
Store Objects in List
↓
Process Every Employee

Features:
- Display Employee Details
- Calculate Bonus
- Check High Salary Status
- Give Salary Raise

---

## 🎯 Key Learnings

- Difference between Class and Object
- Importance of `__init__()`
- Purpose of `self`
- Methods vs Attributes
- Why OOP is useful in Data Engineering
- Creating one object for each CSV record
- Processing collections of objects

---

## 💡 Real Data Engineering Connection

Instead of processing CSV rows as lists or dictionaries, each record can be represented as an object.

This approach improves:
- Code readability
- Reusability
- Maintainability
- Scalability

This pattern is commonly used while processing:
- CSV files
- API Responses
- Database Records
- ETL Pipelines

---

## 📂 Files

- `employee.py`
- `employees.csv`
- `main.py`

---

## ✅ Status

Completed ✔️
