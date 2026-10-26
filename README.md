
# Python API Testing Framework

An automated API testing project built with Python, pytest, and Requests. It tests REST API responses, validates JSON data, and checks error handling using JSONPlaceholder.

## Features

- GET request and status-code validation
- JSON response validation
- POST request testing
- Negative testing for missing and invalid resources
- Reusable pytest fixture with a Requests session
- Automated tests suitable for CI

## Tech Stack

- Python 3.11
- pytest
- Requests
- JSONPlaceholder REST API

## Setup

Create and activate a virtual environment in Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```powershell
python -m pip install -r requirements.txt
```

Run tests:

```powershell
python -m pytest -v
```

## Test Coverage

The test suite checks successful GET requests, response JSON structure, missing resources, POST responses, and invalid resource IDs.

## Important Note

JSONPlaceholder is a demo API. POST requests simulate resource creation and do not permanently store new resources. These tests require internet access.

## Author

Harshal Mahajan
