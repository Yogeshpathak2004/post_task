"""File Handling — Employee System: 
• Create 'employees.txt' and write 5 employees with salary
• Read and print the file
• Append 2 more employees
• Read and print updated file
• Check if file exists using os.path.exists()
• Delete the file"""

import os

with open("employees.txt", "w") as file:
    file.write("Rahul - 25000\n")
    file.write("Priya - 30000\n")
    file.write("Aman - 28000\n")
    file.write("Sneha - 35000\n")
    file.write("Karan - 27000\n")

print("Initial Data:")
with open("employees.txt", "r") as file:
    print(file.read())

with open("employees.txt", "a") as file:
    file.write("Rohit - 32000\n")
    file.write("Pooja - 29000\n")

print("Updated Data:")
with open("employees.txt", "r") as file:
    print(file.read())

if os.path.exists("employees.txt"):
    print("File exists")

os.remove("employees.txt")
print("File deleted")