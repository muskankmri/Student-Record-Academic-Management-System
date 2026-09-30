# System Diagrams

## 1. Use Case Diagram

```text
                         +----------------------------------+
                         | Student Record & Academic        |
                         | Management System                |
                         |                                  |
User ------------------->| Student Management               |
                         | Course Management                |
                         | Marks Management                 |
                         | Attendance Management            |
                         | Performance Analysis             |
                         | Search & Data Operations         |
                         +----------------------------------+

## 2. System component diagram

                         +-------------+
                         |   main.py   |
                         |  Main Menu  |
                         +------+------+
                                |
        +-----------------------+-----------------------+
        |          |            |           |           |
        v          v            v           v           v
   +---------+ +---------+ +---------+ +-----------+ +---------+
   | student | | courses | |  marks  | | attendance| |analysis |
   +---------+ +---------+ +---------+ +-----------+ +---------+
        |          |            |           |           |
        +----------+------------+-----------+-----------+
                                |
                                v
                         +-------------+
                         | searching.py|
                         +-------------+
                                |
                                v
                         +-------------+
                         | utilities.py|
                         +-------------+

## 3. Process flow diagram

Start
  |
  v
Main Menu
  |
  v
Select Operation
  |
  v
Validate Input
  |
  +------ Invalid ------> Display Error
  |                           |
  |                           v
  |                      Return to Menu
  |
  +------ Valid --------> Process Operation
                              |
                              v
                         Display Result
                              |
                              v
                       Return to Menu
                              |
                              v
                             Exit

##4. Student management flow

User
  |
  v
Student Management
  |
  v
Select Operation
  |
  +--> Add Student
  +--> Display Students
  +--> Search Student
  +--> Update Student
  +--> Delete Student
  |
  v
Process Student Data
  |
  v
Display Result

## 5. Marks and attendance flow

Student Academic Data
          |
          v
    Marks / Attendance
          |
          v
     Validate Input
          |
          v
     Process Data
          |
          v
Calculate Percentage
          |
          v
 Display Academic Result

 ## 6. Overall data flow

 User Input
    |
    v
Main Program
    |
    v
Input Validation
    |
    v
Relevant Module
    |
    v
Data Processing
    |
    v
Output
    |
    v
User