# 8. The super() Function
# Create a class Person with a constructor that sets the name.
# Inherit a class Teacher from it, add a subject field, and use super() to call the base class constructor.

class Person:
    def __init__(self, name, age):
        self.age = age
        self.name = name
        print(f"Person created with name: {self.name} and age: {self.age}")


class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)    # Call the constructor of the base class (Person)
        self.subject = subject
        print(f"Teacher created with subject: {self.subject}")
        print(f"Name: {self.name} | Age: {self.age} | Subject: {self.subject}")

teacher1 = Teacher("Sir Arif", 35, "Software Engineer")

# Output:
# Person created with name: Sir Arif and age: 35
# Teacher created with subject: Software Engineer
# Name: Sir Arif | Age: 35 | Subject: Software Engineer

