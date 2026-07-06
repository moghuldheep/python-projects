# Day 8 – Exception Handling

## Objective

Learn how to write robust Python programs by handling runtime errors gracefully using exception handling. The focus is on preventing program crashes, validating user input, and building fault-tolerant programs that continue processing even when errors occur.

## Topics Covered

* `try`
* `except`
* `finally`
* Handling `ValueError`
* Handling `ZeroDivisionError`
* Handling `FileNotFoundError`
* Nested Exception Handling

## Tasks Completed

* Accept user input safely using `try` and `except`
* Build a division calculator with error handling
* Open files safely and handle missing files
* Handle multiple exceptions in a single program
* Use the `finally` block for cleanup operations
* Build a mini ETL program that skips records with invalid salary values while continuing to process valid records

## Skills Learned

* Preventing application crashes
* Handling invalid user input
* Managing file-related errors
* Writing fault-tolerant programs
* Using specific exceptions instead of generic exception handling
* Building resilient ETL workflows

## Mini Project – Employee Salary ETL

### Objective

Read employee salary records from a text file, validate salary values, and process only valid records while skipping invalid ones.

### Input

```text
101,Moghul,50000
102,Anand,ABC
103,Ravi,65000
104,Priya,72000
```

### Expected Output

```text
Employee: Moghul
Salary: 50000

Invalid Salary for Anand. Skipping the record.

Employee: Ravi
Salary: 65000

Employee: Priya
Salary: 72000
```

## Data Engineering Relevance

Real-world datasets often contain missing, incorrect, or corrupted values. Exception handling enables ETL pipelines to process large volumes of data reliably by identifying problematic records, logging errors, and continuing with valid data instead of terminating the entire workflow.

## Key Takeaways

* Use specific exceptions whenever possible.
* Avoid using a generic `except:` unless absolutely necessary.
* Handle expected errors gracefully without interrupting the program.
* Design ETL pipelines that are resilient to bad or incomplete data.

