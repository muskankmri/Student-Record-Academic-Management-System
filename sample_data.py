students = [
    {"id": 101, "name": "Rahul", "branch": "CSE", "semester": 1},
    {"id": 102, "name": "Ananya", "branch": "CSE", "semester": 1},
    {"id": 103, "name": "Rohan", "branch": "ECE", "semester": 1},
    {"id": 104, "name": "Priya", "branch": "CSE", "semester": 1},
    {"id": 105, "name": "Arjun", "branch": "IT", "semester": 1}
]

courses = [
    ("CSE1021", "Intro to Problem Solving", 4),
    ("MAT1001", "Calculus", 4),
    ("CHY1001", "Chemistry", 2),
    ("ENG1001", "English", 2)
]

enrollment = {
    101: ["CSE1021", "MAT1001"],
    102: ["CSE1021", "MAT1001"],
    103: ["CSE1021", "CHY1001"],
    104: ["CSE1021", "ENG1001"],
    105: ["CSE1021", "MAT1001"]
}

student_marks = {
    101: {"CSE1021": 85, "MAT1001": 72},
    102: {"CSE1021": 92, "MAT1001": 88},
    103: {"CSE1021": 76, "CHY1001": 81},
    104: {"CSE1021": 68, "ENG1001": 74},
    105: {"CSE1021": 90, "MAT1001": 95}
}

attendance = {
    101: {"CSE1021": (40, 45), "MAT1001": (38, 45)},
    102: {"CSE1021": (44, 45), "MAT1001": (42, 45)},
    103: {"CSE1021": (35, 45), "CHY1001": (40, 45)},
    104: {"CSE1021": (30, 45), "ENG1001": (41, 45)},
    105: {"CSE1021": (43, 45), "MAT1001": (44, 45)}
}