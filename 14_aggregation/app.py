# 14. Aggregation
# Create a class Department and a class Employee.
#  Use aggregation by having a Department object store a reference to
#  an Employee object that exists independently of it.

class Employee:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def get_details(self):
        return f"{self.name} - {self.role}"


class Department:
    def __init__(self, dept_name, employee):
        self.dept_name = dept_name
        self.employee = employee  # Aggregation: Just holding reference

    def show_employee(self):
        print(f"📂 Department: {self.dept_name}")
        print(f"👨‍💼 Employee: {self.employee.get_details()}")


# --- Create employee independently ---
emp1 = Employee("Ali", "Software Engineer")

# --- Pass existing employee to department ---
it_dept = Department("IT", emp1)

# --- Show info ---
it_dept.show_employee()

# Output:
# 📂 Department: IT
# 👨‍💼 Employee: Ali - Software Engineer
