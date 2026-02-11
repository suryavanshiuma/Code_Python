#Instance attribute

class Student:

    def __init__(self, name, age):
        print("init called.")
        self.name=name
        self.age=age

    def describe(self):
        print(self.name, "is", self.age, "years old.")
        return f"{self.name} is {self.age} years old."

student=Student("Bunny", 13)
student.describe()
