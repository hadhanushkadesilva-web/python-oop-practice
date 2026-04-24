class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        return f"Hi I am {self.name} and I am {self.age} years old"

class Student(Person):
    def __init__(self, name, age, grade):
        self.grade = grade
        super().__init__(name, age)
    
    def introduce(self):
        return f"Hi I am {self.name}, I am {self.age} years old and my grade is {self.grade}"

class Teacher(Person):
    def __init__(self, name, age, subject):
        self.subject = subject
        super().__init__(name, age)
    
    def introduce(self):
        return f"Hi I am {self.name}, I am {self.age} years old and I teach {self.subject}"

s = Student("Ahmed", 20, "A")
t = Teacher("Sara", 35, "Math")
print(s.introduce())
print(t.introduce())
