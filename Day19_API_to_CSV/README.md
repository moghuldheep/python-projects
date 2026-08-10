# Day 19 – API to CSV ETL Pipeline

## 📌 Overview

Today I built my first complete API-to-CSV ETL pipeline using Python.

The pipeline extracts user data from a REST API, transforms the JSON response by selecting the required fields, and loads the processed data into a CSV file.

This session also introduced an important Data Engineering concept: **source schema changes and schema robustness**.

---

## 📚 Topics Covered

* REST API data extraction
* HTTP GET requests
* JSON response handling
* CSV file creation
* Python `csv` module
* Nested JSON objects
* Data transformation
* ETL processing
* Record-level error handling
* Pipeline-level error handling
* Logging
* Processing metrics
* Schema changes and schema robustness

---

## 🔄 ETL Pipeline

The workflow implemented today:

```text
              EXTRACT
                 │
                 ▼
        REST API / JSON
                 │
                 ▼
             TRANSFORM
        Select required fields
                 │
                 ▼
               LOAD
                 │
                 ▼
             CSV File
```

---

# 🛠 Tasks Completed

## Task 1 – Fetch API Data

Fetched user information from:

```text
https://jsonplaceholder.typicode.com/users
```

Used the Python `requests` library to:

* Send a GET request
* Set a timeout
* Validate the response
* Convert the response into Python objects using `response.json()`

---

## Task 2 – Write JSON Data to CSV

Used Python's built-in `csv` module to create a CSV file.

The selected fields were:

```text
id
name
email
```

The resulting file follows the structure:

```text
id,name,email
1,Leanne Graham,....
2,Ervin Howell,....
```

---

## Task 3 – Read the Generated CSV

After writing the file, the CSV was opened again and its contents were printed.

This helped verify that the extracted data was successfully written to the destination.

---

## Task 4 – Logging

Implemented logging to track the ETL process.

Important events logged include:

* Program started
* API fetch successful
* CSV writing started
* CSV writing completed
* Number of users written
* Program completed
* Errors during processing

---

# 🚀 Mini ETL Project

The mini project extended the basic API-to-CSV workflow.

### Extract

Fetched users from the REST API.

### Transform

Selected:

```text
id
name
email
company name
```

The API contains a nested `company` object:

```json
{
    "company": {
        "name": "Romaguera-Crona"
    }
}
```

Therefore, the company name needs to be accessed using:

```python
user["company"]["name"]
```

### Load

Created a CSV file containing:

```text
id,name,email,company
```

---

## 📊 Processing Metrics

The mini ETL tracks:

```text
Total users
Processed users
Failed users
Processing time
```

Example:

```text
========================
Total users: 10
Written: 10
Failed: 0
Time taken: ...
========================
```

This introduces an important Data Engineering practice: **measuring the outcome of a pipeline instead of only checking whether the program ran successfully.**

---

# 🧠 Important Learning – Schema Changes

A key thought exercise was:

> What happens if an API changes `name` to `full_name`?

The initial instinct was to access values by their position instead of their key.

For example:

```python
user[1]
```

However, this is not a reliable solution.

If the API changes the order of its fields, the pipeline could retrieve the wrong value while continuing to run successfully.

This can result in **silent data corruption**, which is often more dangerous than an obvious program failure.

---

## ❌ Fragile Approach

```python
user[1]
```

The position of a field should not be assumed to represent its meaning.

---

## ✅ Better Approach

Introduce a transformation layer between the source API and the destination dataset.

```text
API Schema
     │
     ▼
Transformation / Mapping
     │
     ▼
Standard Internal Schema
     │
     ▼
CSV
```

For example:

```python
name = user.get("name") or user.get("full_name")
```

The rest of the pipeline can continue working with the standardized variable:

```python
name
```

This is an early introduction to concepts such as:

* Schema validation
* Schema mapping
* Schema normalization
* Schema evolution
* Data contracts

These concepts become increasingly important when working with large-scale data pipelines.

---

# ⚠️ Error Handling

The pipeline uses different error scopes.

### Pipeline-Level Errors

Examples:

* API unavailable
* Network failure
* CSV cannot be created

### Record-Level Errors

Examples:

* Missing field
* Invalid data
* Unexpected JSON structure

Conceptually:

```text
ETL Pipeline
│
├── API Failure
│
├── File Failure
│
└── Record Processing
     ├── Record 1
     ├── Record 2
     ├── Record 3
     └── ...
```

This allows one bad record to be handled without necessarily stopping the entire pipeline.

---

# 📁 Project Structure

```text
Day19_API_to_CSV/
│
├── main.py
├── users.csv
├── logs/
│   └── processed.log
└── README.md
```

---

# 🎯 Learning Outcomes

By the end of Day 19, I can:

* Extract data from a REST API.
* Parse JSON responses.
* Navigate nested JSON objects.
* Transform API data into a required structure.
* Write structured data to CSV.
* Read and validate generated CSV files.
* Implement logging in an ETL pipeline.
* Track processed and failed records.
* Measure pipeline execution time.
* Understand the risks of source schema changes.
* Understand why schema mapping is preferable to relying on field positions.

---

# 💡 Key Takeaways

### ETL is not just about moving data.

A reliable pipeline needs to:

```text
Extract
   ↓
Validate
   ↓
Transform
   ↓
Load
   ↓
Monitor
```

### Data correctness matters more than program completion.

A pipeline that finishes successfully but writes incorrect data is still a failed pipeline.

### Schema changes must be considered.

Source systems can change field names, structures, and data types. A robust pipeline should isolate source-specific transformations from the rest of the processing logic.

---

# 🔜 Next Step

The next stage of the Python Data Engineering roadmap will focus on **data processing and transformation**, leading into:

* Pandas
* Data cleaning
* Filtering
* Missing values
* Grouping and aggregation
* Merging datasets
* Date/time processing
* Larger CSV datasets

This will eventually lead into:

```text
Python
   ↓
Pandas
   ↓
PySpark
   ↓
Spark SQL
   ↓
Databricks
   ↓
Delta Lake
   ↓
Production Data Pipelines
```

---

## 🧰 Technologies Used

* Python 3
* `requests`
* `csv`
* `logging`
* `datetime`
* REST API
* JSON
* CSV
* ETL concepts

