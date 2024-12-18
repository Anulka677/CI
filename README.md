# Student Management System

This project implements a student management system, allowing the addition of students, attendance editing, and exporting/importing data to/from a text file.

## Features
- **Add Students** – Add new students to the system.
- **Edit Attendance** – Update a student's attendance status (present/absent).
- **Export to Text File** – Save the student list to a `.txt` file.
- **Import from Text File** – Load student data from a `.txt` file.
- **Unit Tests** – Verify the correctness of the implemented functionalities.

## Running Tests
To run unit tests and generate a code coverage report:
```bash
pytest --cov=. --cov-report=html
