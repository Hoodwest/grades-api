# Student Grades API

## Overview

The **Student Grades API** is a simple RESTful API built using **Python and Flask**.
It allows users to retrieve and manage student grade information.

This project was created as part of a **Software Requirements Engineering Lab** exercise. The API includes a simple API contract using **OpenAPI/Swagger** and basic endpoints for accessing and adding student grades.

---

## Features

* Retrieve all student grades
* Add a new student grade
* API documentation using Swagger/OpenAPI
* Simple in-memory data storage

---

## Project Structure

```
grades-api/
│
├── app.py              # Flask application with API endpoints
├── openapi.yaml        # OpenAPI / Swagger API contract
├── README.md           # Project documentation
└── .gitignore          # Files ignored by Git
```

---

## Technologies Used

* Python
* Flask
* Swagger / OpenAPI
* Git and GitHub

---

## API Endpoints

### 1. Get All Grades

**Endpoint**

GET /grades

**Description**

Returns a list of all student grades.

**Example Response**

```
[
  {
    "student_id": "S001",
    "name": "Alice",
    "grade": 88
  },
  {
    "student_id": "S002",
    "name": "Bob",
    "grade": 74
  }
]
```

---

### 2. Add a New Grade

**Endpoint**

POST /grades

**Description**

Adds a new student grade to the system.

**Example Request**

```
{
  "student_id": "S003",
  "name": "John",
  "grade": 90
}
```

**Example Response**

```
{
  "message": "Grade added successfully"
}
```

---

## OpenAPI / Swagger Documentation

The API contract is defined in the file:

```
openapi.yaml
```

This file describes:

* API endpoints
* Request parameters
* Response formats
* Data schema

Swagger documentation allows developers to understand and interact with the API easily.

---

## Installation and Setup

### 1. Clone the Repository

```
git clone https://github.com/YOUR_USERNAME/grades-api.git
```

Move into the project folder:

```
cd grades-api
```

---

### 2. Install Dependencies

Install Flask using pip:

```
pip install flask
```

If using Python3:

```
pip3 install flask
```

---

### 3. Run the Application

Start the Flask server:

```
python app.py
```

The API will start running at:

```
http://127.0.0.1:5000
```

---

## Testing the API

### Browser

You can test the GET endpoint by visiting:

```
http://127.0.0.1:5000/grades
```

### Postman

Use Postman to test POST requests by sending JSON data to:

```
http://127.0.0.1:5000/grades
```

---

## Example API Workflow

1. Start the Flask server
2. Send a GET request to retrieve grades
3. Send a POST request to add a new grade
4. Retrieve the updated list of grades

---

## Future Improvements

* Add a database (MySQL or PostgreSQL)
* Add update and delete endpoints
* Implement authentication
* Deploy the API to a cloud server

This project was developed for academic learning purposes.
