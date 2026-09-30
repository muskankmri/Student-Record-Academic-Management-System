# System Design

## 1. System Architecture

The Student Record and Academic Management System follows a modular architecture. The application is developed using Python and is divided into separate modules for different academic management functions.

The main program, `main.py`, provides the menu-driven interface and connects all major modules. Each module performs a specific task such as managing students, courses, marks, attendance, performance analysis, and search operations.

The main modules are:

- `main.py` – Controls the main menu and program flow
- `student.py` – Manages student records
- `courses.py` – Manages courses and student-course assignments
- `marks.py` – Manages marks and grades
- `attendance.py` – Manages attendance records
- `analysis.py` – Performs academic performance analysis
- `searching.py` – Performs searching, sorting, and data operations
- `utilities.py` – Provides common utility functions
- `sample_data.py` – Provides sample data for testing

The modular design makes the system easier to understand, maintain, test, and extend.

## 2. System Workflow

The application starts by running `main.py`. The main menu is displayed and the user selects the required operation. Based on the selected option, the appropriate module is executed.

After completing the operation, the result is displayed to the user and the application returns to the main menu. The user can continue performing operations or choose the exit option.

```text
Start
  |
  v
Main Menu
  |
  v
Select Operation
  |
  +--> Student Management
  |
  +--> Course Management
  |
  +--> Marks Management
  |
  +--> Attendance Management
  |
  +--> Performance Analysis
  |
  +--> Search and Data Operations
  |
  v
Process Operation
  |
  v
Display Result
  |
  v
Return to Main Menu
  |
  v
Exit

## 2. Data Storage Design

The system uses Python data structures to store and manage student academic information during program execution.

The main data structures used are:

- **Lists** – Used to store collections of student, course, marks, and attendance records.
- **Dictionaries** – Used to store structured information such as student details and academic data.
- **Tuples** – Used where a fixed group of related values is required.
- **Sets** – Used for operations such as removing duplicate values.

The data is processed by the appropriate module based on the operation selected by the user. This structure allows the system to perform student management, course management, marks processing, attendance calculations, performance analysis, and search operations efficiently.

## 3. Design Decisions

The project uses a modular design where different functionalities are separated into individual Python files. This makes the code easier to understand, maintain, and test.

A menu-driven console interface is used so that users can easily select the required operation. Python data structures such as lists, dictionaries, tuples, and sets are used for storing and processing different types of academic information.

Searching and selection sort are included for data-processing operations. Input validation and error handling are used to handle invalid inputs and improve the reliability of the application.

The modular structure also makes it possible to add new features or modify existing modules without significantly affecting the complete system.

## 4. System Diagram

The overall system consists of the main program and separate modules for each major functionality.

```text
                    +----------------+
                    |    main.py     |
                    |   Main Menu    |
                    +-------+--------+
                            |
          +-----------------+-----------------+
          |        |        |        |        |
          v        v        v        v        v
      Student   Course    Marks   Attendance Analysis
      Module    Module    Module    Module    Module
          |        |        |        |        |
          +--------+--------+--------+--------+
                            |
                            v
                   +----------------+
                   |   searching.py |
                   | Search & Sort   |
                   +----------------+
                            |
                            v
                   +----------------+
                   | utilities.py   |
                   | Validation     |
                   +----------------+

## Dataflow

User
  |
  v
Main Menu
  |
  v
Select Operation
  |
  v
Input Data
  |
  v
Validation
  |
  v
Relevant Module
  |
  v
Data Processing
  |
  v
Result
  |
  v
Display Output
  |
  v
Main Menu

