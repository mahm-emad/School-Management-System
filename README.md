# 📚 School Management System

A simple Python-based School Management System that demonstrates core object-oriented programming (OOP) principles. This system allows the management of students, teachers, attendance, and generates structured reports.

## ✅ Features

- **Person Class (`person.py`)**
  - Base class for all individuals in the school.
  - Implements a basic `introduce()` method.

- **Student Class (`student.py`)**
  - Inherits from `Person`.
  - Adds a student ID and overrides `introduce()`.
  - Includes attendance tracking features.

- **Teacher Class (`teacher.py`)**
  - Inherits from `Person`.
  - Adds a subject field and overrides `introduce()`.
  - Includes attendance tracking features.

- **School Class (`school.py`)**
  - Manages a list of students and teachers.
  - Methods:
    - `add_person()` to register new people
    - `show_all_people()` to list introductions
    - `mark_attendance(name)` to record attendance
    - `generate_report()` to produce a table-style summary of individuals and attendance

- **Attendance System**
  - Each person has an attendance count.
  - Attendance can be marked and retrieved.

- **Report Generation**
  - Outputs a formatted report showing:
    ```
    Name        Age    Role       Attendance
    ----------------------------------------
    Ms. Ahmed   35     Teacher    10 days
    Shehab      25     Student    1 days
    ```

- **Main Script (`main.py`)**
  - Entry point for running and testing the system.
