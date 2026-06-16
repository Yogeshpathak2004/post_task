""" JSON — Student Database: 
• Create a list of 4 students:
Each student: name, age, city, course, marks
• Save to 'students.json' with indent=4
• Read the file back
• Print only students with marks > 70
• Print total number of students"""

import json

students = [
    {
        "name": "Rahul",
        "age": 21,
        "city": "Mumbai",
        "course": "Python",
        "marks": 85
    },
    {
        "name": "Priya",
        "age": 22,
        "city": "Pune",
        "course": "Data Science",
        "marks": 72
    },
    {
        "name": "Aman",
        "age": 20,
        "city": "Delhi",
        "course": "AI",
        "marks": 65
    },
    {
        "name": "Sneha",
        "age": 23,
        "city": "Bangalore",
        "course": "ML",
        "marks": 90
    }
]

with open("students.json", "w") as file:
    json.dump(students, file, indent=4)

with open("students.json", "r") as file:
    data = json.load(file)

print("Students with marks > 70")

for student in data:
    if student["marks"] > 70:
        print(student)

print("Total Students:", len(data))