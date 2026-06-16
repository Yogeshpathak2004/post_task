""" Create a Student Registration System: 
• Create your own exception: InvalidAgeError
• Create your own exception: InvalidMarksError
• Ask user to enter: name, age, marks
• If age < 15 or age > 30 fi raise InvalidAgeError
• If marks < 0 or marks > 100 fi raise InvalidMarksError
• If valid fi print 'Student registered successfully!'
• Handle both exceptions and add finally block"""

class InvalidAgeError(Exception):
    pass


class InvalidMarksError(Exception):
    pass


try:
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    marks = float(input("Enter Marks: "))

    if age < 15 or age > 30:
        raise InvalidAgeError("Invalid Age!")

    if marks < 0 or marks > 100:
        raise InvalidMarksError("Invalid Marks!")

    print("Student registered successfully!")

except InvalidAgeError as e:
    print(e)

except InvalidMarksError as e:
    print(e)

finally:
    print("Registration Process Completed")