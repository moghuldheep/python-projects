# Day 11 - Logging in Python

## 📌 Topics Covered

- Introduction to Logging
- Why Logging is Preferred over print()
- Logging Levels
- Logging Format
- Writing Logs to Console
- Writing Logs to Files
- Exception Logging
- Logging in ETL Pipelines

---

## 📝 Tasks Completed

### Task 1

Created the first logging program.

Logged:
- Program Started

---

### Task 2

Explored all logging levels:

- DEBUG
- INFO
- WARNING
- ERROR
- CRITICAL

Observed how logging level configuration affects output.

---

### Task 3

Configured custom log formatting.

Included:
- Timestamp
- Log Level
- Message

---

### Task 4

Read employee records from a CSV file.

Logged every employee before processing.

---

### Task 5

Handled invalid salary values using exception handling.

Logged errors using:

- `logging.error()`

Continued processing remaining records.

---

### Task 6

Configured logging to write into a log file.

Verified log generation.

---

## 🚀 Mini Project

Enhanced the Employee ETL Processor with Logging.

Workflow:

Program Started
↓
Read Employee CSV
↓
Create Employee Objects
↓
Log Employee Processing
↓
Calculate Bonus
↓
Handle Invalid Records
↓
Program Completed

---

## 🎯 Key Learnings

- Difference between `print()` and `logging`
- Importance of application logs
- Logging levels
- Custom log formatting
- Writing logs to files
- Logging exceptions
- Using logs to debug ETL applications

---

## 🛠 Debugging Experience

During the mini project, encountered an issue caused by:

- Calling `append()` on an object instead of the list.
- Using a generic `except:` block which masked the real error.

Resolved by:
- Appending Employee objects to the employees list.
- Using specific exception types (`FileNotFoundError`, `ValueError`).
- Understanding why generic exception handling can make debugging difficult.

This exercise demonstrated how logging can significantly simplify debugging.

---

## 💡 Real Data Engineering Connection

Production ETL jobs process millions of records.

Logging helps engineers:

- Monitor execution
- Identify failed records
- Debug production issues
- Maintain audit trails

Logging is a fundamental skill for Data Engineers working with large-scale data pipelines.

---

## 📂 Files

- `main.py`
- `employees.csv`
- `processed.log`

---

## ✅ Status

Completed ✔️
