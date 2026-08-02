# Day 17 – Working with HTTP POST Requests using Python

## 📌 Overview

Today I learned how to send data to a server using HTTP **POST** requests. Until now, I had been retrieving data from APIs using GET requests. This session introduced the concept of creating new resources on a server by sending JSON data through Python's `requests` library.

I also implemented logging, exception handling, response validation, and built a mini ETL project that simulates a new employee registration system.

---

## 📚 Topics Covered

* HTTP POST Requests
* Difference between GET and POST
* Sending JSON data using `requests.post()`
* The `json` parameter in the `requests` library
* HTTP Status Code `201 Created`
* Handling API request failures
* Logging API operations
* Measuring processing time
* Building a POST-based ETL workflow

---

## 🛠 Tasks Completed

### Task 1

* Created a Python dictionary representing a new user.

### Task 2

* Sent the dictionary to a REST API using an HTTP POST request.

### Task 3

* Printed:

  * HTTP Status Code
  * JSON response returned by the server

### Task 4

* Added structured logging for:

  * Program start
  * Sending request
  * Successful request
  * Failed request

### Task 5

* Implemented exception handling using:

```python
requests.exceptions.RequestException
```

to gracefully handle API failures.

---

## 🚀 Mini ETL Project – Employee Registration

Developed a mini ETL application that:

* Accepts employee details from the user
* Creates a Python dictionary
* Sends the data to a REST API using POST
* Handles request failures
* Logs every important step
* Displays the created employee information
* Displays the generated employee ID
* Measures total execution time
* Prints a processing summary

---

## 💡 Key Concepts Learned

### GET vs POST

| GET                                    | POST                             |
| -------------------------------------- | -------------------------------- |
| Retrieves data                         | Creates new data                 |
| Usually does not modify server data    | Sends new data to the server     |
| Parameters are often passed in the URL | Data is sent in the request body |

---

### Sending JSON

Instead of manually converting dictionaries into JSON strings, the `requests` library automatically performs the conversion using:

```python
response = requests.post(url, json=new_user)
```

This also sets the appropriate `Content-Type: application/json` header.

---

### HTTP Status Code 201

Learned that a successful POST request commonly returns:

```text
201 Created
```

indicating that the server successfully created a new resource.

---

### Exception Handling

Implemented robust API error handling using:

```python
try:
    ...
except requests.exceptions.RequestException:
    ...
```

to handle connection failures, HTTP errors, and network-related exceptions.

---

### Logging

Logged important processing events including:

* User input received
* Sending POST request
* Successful employee creation
* Request failures
* Program completion

---

## 📁 Project Structure

```text
Day17_POST_Requests/
│
├── main.py
├── logs/
│   ├── task.log
│   └── mini_etl.log
└── README.md
```

---

## 🎯 Learning Outcome

By the end of Day 17, I can:

* Send HTTP POST requests using Python.
* Create JSON payloads from Python dictionaries.
* Submit data to REST APIs.
* Validate API responses.
* Handle API failures gracefully.
* Log API operations for debugging.
* Build a complete POST-based ETL workflow.

---

## 🧠 Key Takeaways

* POST requests are used to create resources on a server.
* JSON payloads can be sent directly using the `json=` parameter.
* Proper logging and exception handling make applications more reliable.
* Production APIs often validate incoming data before creating new records.
* Preventing duplicate records may involve techniques such as unique constraints, business rules, idempotency keys, or hashing depending on the use case.

---

## 🔜 Next Steps

In the next session, I will learn:

* API Authentication
* API Keys
* Bearer Tokens
* Authorization Headers
* Accessing protected APIs securely
* Best practices for managing API credentials

---

## 📖 Technologies Used

* Python 3
* requests
* logging
* datetime
* JSON
* REST API
* HTTP POST

