class Student:
    def __init__(self, name, age, university):
        self.name = name
        self.age = age
        self.university = university

    def introduce(self):
        return f"My name is {self.name}, I am {self.age} years old."


student = Student("Alex", 21, "University of Cassino")
print(student.introduce())
