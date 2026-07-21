# Day 12 - Virtual Environments & Package Management

## 📌 Topics Covered

- Virtual Environments (`venv`)
- Why Virtual Environments are Required
- Activating and Deactivating Virtual Environments
- Python Package Manager (`pip`)
- Installing Third-Party Packages
- Package Isolation
- `requirements.txt`
- Professional Python Project Structure

---

## 📝 Tasks Completed

### Task 1

Created a new Python project folder.

Created a virtual environment using:

```bash
python3 -m venv .venv
```

Verified that the `.venv` directory was created successfully.

---

### Task 2

Activated the virtual environment.

```bash
source .venv/bin/activate
```

Verified activation by observing the terminal prompt.

Also verified the active Python and pip executables using:

```bash
which python
which pip
```

---

### Task 3

Explored installed packages using:

```bash
pip list
```

Observed the default packages available inside a newly created virtual environment.

---

### Task 4

Installed the first external Python package.

Package Installed:

- requests

Verified the installation using:

```python
import requests

print(requests.__version__)
```

---

### Task 5

Generated the project dependency file.

Command Used:

```bash
pip freeze > requirements.txt
```

Observed that installing one package (`requests`) also installed its required dependencies.

---

### Task 6

Practiced activating and deactivating the virtual environment.

Commands:

```bash
deactivate

source .venv/bin/activate
```

---

## 🚀 Mini Project

Created a professional Python project structure.

```
employee_project/

├── .venv/
├── main.py
├── requirements.txt
├── README.md
└── logs/
```

Developed a simple application that:

- Imported `requests`
- Imported `logging`
- Logged Program Started
- Displayed installed Requests version
- Logged Program Completed

Generated `requirements.txt` for project dependency management.

---

## 🎯 Key Learnings

- What a Virtual Environment is
- Why every Python project should have its own virtual environment
- Difference between System Python and Virtual Environment Python
- How activation changes the Python interpreter
- Installing packages using `pip`
- Managing project dependencies using `requirements.txt`
- Why `.venv` should not be committed to GitHub
- Importance of dependency isolation in professional software development

---

## 💡 Real Data Engineering Connection

Most production Data Engineering projects depend on external Python libraries such as:

- requests
- pandas
- pyspark
- numpy
- kafka-python
- snowflake-connector-python
- azure-storage-blob

Virtual environments ensure that each project maintains its own isolated dependencies, preventing version conflicts and making projects reproducible across different development environments.

---

## 📂 Files

- `main.py`
- `requirements.txt`
- `README.md`

---

## ✅ Status

Completed ✔️
