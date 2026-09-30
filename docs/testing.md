# Testing

## Testing Approach

The project is tested using console-based functional testing. Each major module is tested with valid and invalid inputs to check whether the expected output is produced.

## Test Cases

| Test ID | Module | Test Case | Expected Result |
|---|---|---|---|
| TC01 | Student | Add a valid student | Student is added successfully |
| TC02 | Student | Search student by valid ID | Correct student details are displayed |
| TC03 | Student | Search invalid student ID | Student not found message is displayed |
| TC04 | Student | Search student by name | Matching student is displayed |
| TC05 | Student | Update student details | Student information is updated |
| TC06 | Student | Delete student | Student record is deleted |
| TC07 | Course | Add a valid course | Course is added successfully |
| TC08 | Course | Assign course to student | Course is assigned successfully |
| TC09 | Marks | Enter valid marks | Marks are recorded |
| TC10 | Marks | Enter invalid marks | Appropriate error message is displayed |
| TC11 | Attendance | Record attendance | Attendance is recorded |
| TC12 | Attendance | Calculate attendance percentage | Correct percentage is displayed |
| TC13 | Analysis | Calculate class average | Class average is displayed |
| TC14 | Analysis | Find topper | Top-performing student is displayed |
| TC15 | Search | Sort students by average | Students are sorted correctly |
| TC16 | Search | Remove duplicate values | Duplicate values are removed |
| TC17 | Search | Find kth-smallest value | Correct kth-smallest value is displayed |
| TC18 | Validation | Enter invalid menu option | Error message is displayed |

## Functional Testing

Each major feature of the application is tested individually to verify that it performs the intended operation and produces the expected result.

## Input Validation Testing

Invalid inputs such as incorrect menu choices, invalid student information, and inappropriate marks or attendance values are tested to ensure that the system handles them properly.

## Module Testing

The Student, Course, Marks, Attendance, Performance Analysis, and Search modules are tested separately to verify their individual functionality.

## Integration Testing

The interaction between `main.py` and the different modules is tested to ensure that the complete menu-driven workflow operates correctly.

## Expected Outcome

The system should successfully perform the required operations for valid inputs and display appropriate error messages for invalid inputs. All major modules should work correctly through the main menu.