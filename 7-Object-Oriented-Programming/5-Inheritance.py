class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_data(self, name, age):
        self.name = name
        self.age = age
    def put_data(self):
        print(self.name)
        print(self.age)

class ScienceStudent(Student):
    def science(self):
        print("This is a science method")

a = ScienceStudent("", "")
a.science()
name = input("Enter name:")
age = input("Enter age:")
a.get_data(name, age)
a.put_data()