class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Student Name: {self.name}")
        print(f"Student Marks: {self.marks}")


student1 = Student("Ali", 85)
student1.display()


print("\n" + "-" * 20 + "\n")

student2 = Student("Sara", 90)
student2.display()

