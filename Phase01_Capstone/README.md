# Phase 1 Capstone - Employee Management ETL System

## 📌 Overview

This project is the Phase 1 Capstone of my Python for Data Engineering learning journey.

The application simulates a real-world Employee ETL (Extract, Transform, Load) pipeline by reading employee records from a CSV file, validating the data, creating Employee objects, handling invalid records gracefully, and logging all important events.

---

## 🚀 Features

- Read employee data from a CSV file
- Object-Oriented Design using an `Employee` class
- Exception handling for invalid records
- Continue processing even if one record fails
- Logging using Python's `logging` module
- Processing summary with total, successful, and failed records
- Modular project structure

---

## 📂 Project Structure

```
Phase01_Capstone/
│
├── data/
│   └── employees.csv
│
├── logs/
│   └── employee.log
│
├── employee.py
├── file_utils.py
├── main.py
├── README.md
└── requirements.txt
```

---

## ⚙️ Technologies Used

- Python 3
- Object-Oriented Programming (OOP)
- File Handling
- Exception Handling
- Logging
- Virtual Environment (`venv`)

---

## 📖 Workflow

```
employees.csv
      │
      ▼
Read Employee File
      │
      ▼
Validate Records
      │
      ▼
Create Employee Objects
      │
      ▼
Store Objects in Memory
      │
      ▼
Display Employee Details
      │
      ▼
Generate Processing Summary
      │
      ▼
Write Logs
```

---

## 📝 Sample Input

```
employee_id,name,job,salary
101,Moghul,Data Engineer,60000
102,Anand,Developer,45000
103,Ravi,Tester,52000
104,Priya,Analyst,abc
105,John,Manager,85000
```

---

## 📊 Sample Output

```
Employee ETL System initialized successfully

Employee details
----------------
Name: Moghul
Job: Data Engineer
Salary: 60000
----------------

...

===============================
Employee ETL System Summary
===============================
Total Records: 5
Processed Records: 4
Failed Records: 1
===============================
```

---

## 📋 Concepts Demonstrated

- Variables
- Functions
- Loops
- Lists
- Classes & Objects
- Modules
- File Handling
- Exception Handling
- Logging
- ETL Fundamentals

---

## 🎯 Learning Outcome

Through this project, I learned how to:

- Build a modular Python application
- Apply Object-Oriented Programming
- Handle real-world data validation
- Log application events professionally
- Design a simple ETL pipeline
- Structure Python projects for maintainability

---

## 👨‍💻 Author

**Moghul Dheep B**

Learning Python for Data Engineering one project at a time.
