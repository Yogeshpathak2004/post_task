""" Set & Dictionary Operations: 
• Create a set of 6 students (with 2 duplicates)
• Print set — duplicates automatically removed
• Add 2 new students to set
• Create a dictionary of 4 students with their marks
• Loop through dictionary:
fi marks >= 75: print 'Distinction'
fi marks >= 60: print 'Pass'
fi marks < 60 : print 'Fail'"""

students = {
    "Rahul",
    "Priya",
    "Aman",
    "Rahul",
    "Sneha",
    "Aman",
    "Karan",
    "Neha"
}

print(students)

students.add("Rohit")
students.add("Pooja")

print(students)

marks = {
    "Rahul": 82,
    "Priya": 68,
    "Aman": 55,
    "Sneha": 91
}

for name, score in marks.items():

    if score >= 75:
        print(name, "Distinction")

    elif score >= 60:
        print(name, "Pass")

    else:
        print(name, "Fail")
