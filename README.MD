# tech task - Articles API endpoints tests

## Purpose

This project contains tests for the two Articles API endpoints.

The tests are written in Python utilising the [requests](https://docs.python-requests.org) library and [pytest](https://docs.pytest.org/) framework. 

## Setup

### Clone repository

Clone the project to a suitable location and change to the root directory of the project. 

```python
git clone https://github.com/carlsmith101/tech-task.git

cd techtask
```

### Install packages

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install required packages.

```python
pip install -r requirements.txt
```

## Run tests

```python
python -m pytest
```

## Notes

Tests are included for all HTTP actions - GET, POST, PUT, DELETE - on both endpoints.

The task instructions suggested that POST, PUT and DELETE actions on both endpoints should return a 404 error, though a 400 is returned for a DELETE or PUT on an unspecified resource and a POST on a specified resource. I included tests for these scenarios and asserted the 400 to verify that a bad request had been handled sufficiently.

Tests are included to assert that the structure and validity of the response is as expected. This includes asserting all keys are present and that all required values are present and of the correct type.

I included a test for the 'Content-Type' header of the response from each endpoint. Other headers could be asserted as present or non-present according to specification.
For example, the 'X-Powered-By' header should not typically be included in the response as this reveals information to the user which could aid them in determining security vulnerabilities. 