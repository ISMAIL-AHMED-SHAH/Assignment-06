# 7. Access Modifiers: Public, Private, and Protected
# Create a class Employee with:
# a public variable name,
# a protected variable _salary, and
# a private variable __ssn.
# Try accessing all three variables from an object of the class and document what happens.


class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name            # Public
        self._salary = salary       # Protected
        self.__ssn = ssn            # Private

    def show_info(self):
        print("Inside class:")
        print("Name:", self.name)
        print("Salary:", self._salary)
        print("SSN:", self.__ssn)


emp = Employee("Ali", 50000, "123-45-6789")

# Accessing variables
print("\nOutside class:")
print("Name:", emp.name)                # ✅ Accessible
print("Salary:", emp._salary)           # ⚠️ Accessible, but not recommended
# print("SSN:", emp.__ssn)              # ❌ Error: AttributeError

# Accessing private via name mangling

print("SSN (via mangling):", emp._Employee__ssn)  # ✅ Hacky Access
