"""Create an Inheritance program using School System: 
• Class Person -> walk(), talk()
• Class Teacher(Person) -> teach()
• Class Student(Person) ->study()
Create objects of Teacher and Student, call all methods including inherited ones.

"""

class Person:
    def walk(self):
        print("Person is walking")

    def talk(self):
        print("Person is talking")


class Teacher(Person):
    def teach(self):
        print("Teacher is teaching")


class Student(Person):
    def study(self):
        print("Student is studying")


teacher = Teacher()
teacher.walk()
teacher.talk()
teacher.teach()

student = Student()
student.walk()
student.talk()
student.study()