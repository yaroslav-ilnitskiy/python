import json

from student import Student

print("Welcome to the club body")

name = input("Enter name")
student = Student(name)

student.set_phone(input("Enter Phone"))
student.set_year(int(input("Enter Year")))
student.set_gender(input("Enter Gender"))

print("Student successfully created")

jsonData = student.serialize()

print(jsonData)
print(Student.unserialize(json.loads(jsonData)))

print("Student successfully serialize and unserialize")
