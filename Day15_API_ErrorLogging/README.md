# Day 15 – Working with APIs using Python (`requests`)

## 📌 Overview

Today I learned how to communicate with external servers using Python's `requests` library. Instead of reading data from local CSV files, I fetched real-time JSON data from a public REST API and processed it just like an ETL pipeline.

I also learned how to make API calls production-ready by implementing exception handling, logging, timeouts, and response validation.

---

## 📚 Topics Covered

* Introduction to REST APIs
* Installing and using the `requests` library
* Making HTTP GET requests
* Understanding the `Response` object
* HTTP Status Codes
* Parsing JSON responses using `response.json()`
* Working with JSON Arrays and Objects
* Using `raise_for_status()`
* Request timeouts
* Exception handling with `RequestException`
* Logging API operations
* Building a simple API ETL pipeline

---

## 🛠 Tasks Completed

### Task 1

* Installed the `requests` library inside a Python virtual environment.

### Task 2

* Sent an HTTP GET request to a public REST API.

### Task 3

* Retrieved and displayed the HTTP response status code.

### Task 4

* Converted the JSON response into Python objects using `response.json()`.

### Task 5

* Extracted and displayed:

  * First user's name
  * Email
  * Phone number

### Task 6

* Looped through all users returned by the API.
* Displayed formatted user information.

---

## 🚀 Mini ETL Project

Built a mini ETL pipeline that:

* Configures logging
* Sends an HTTP GET request
* Uses a request timeout
* Validates the response using `raise_for_status()`
* Converts JSON into Python objects
* Processes every user record
* Logs successful processing
* Handles processing failures
* Generates a processing summary
* Measures total execution time

---

## 💡 Key Concepts Learned

### HTTP GET

Used GET requests to retrieve data from a REST API.

### Response Object

Learned that the response returned by `requests.get()` is a **Response object**, which contains:

* Status Code
* Headers
* Response Body
* Cookies
* Metadata

The actual JSON data is extracted using:

```python
response.json()
```

### JSON

Learned that:

* JSON Objects become Python dictionaries.
* JSON Arrays become Python lists.

### Exception Handling

Used production-style exception handling:

```python
try:
    ...
except requests.exceptions.RequestException:
    ...
```

instead of generic exception handling.

### Logging

Recorded important events such as:

* Program start
* Successful API fetch
* Record processing
* Errors
* Program completion

---

## 📁 Project Structure

```text
Day15_API_Error_Handling/
│
├── main.py
├── logs/
│   ├── processed.log
│   └── mini_etl.log
└── README.md
```

---

## 🎯 Learning Outcome

By the end of Day 15, I can:

* Fetch data from public APIs.
* Parse JSON responses into Python objects.
* Navigate nested JSON structures.
* Handle API failures gracefully.
* Build reliable API-based ETL programs using logging, exception handling, and processing summaries.

---

## 🔜 Next Steps

In the next session, I will learn:

* Query Parameters
* API Authentication
* POST Requests
* Working with real-world APIs
* Saving API responses to files and databases
* Building more advanced API ETL pipelines

---

## 📖 Technologies Used

* Python 3
* requests
* logging
* datetime
* JSON
* REST API

