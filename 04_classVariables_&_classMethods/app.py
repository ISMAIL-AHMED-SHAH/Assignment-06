# 4. Class Variables and Class Methods
# Create a class Bank with a class variable bank_name. Add a class method change_bank_name(cls, name)
# that allows changing the bank name. Show that it affects all instances.

class Bank:
    bank_name = "Older Bank"  # Class variable

    def __init__(self, account_holder):
        self.account_holder = account_holder

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name  # Change the class variable

    def display(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Bank Name: {Bank.bank_name}")


# Create objects
account1 = Bank("Ali")
account2 = Bank("Sara")

# 🔍 Display BEFORE bank name change
print("📍 Before Bank Name Change:")
account1.display()
account2.display()

# 🎯 Change bank name
print("\n🎯 Changing bank name...\n")
Bank.change_bank_name("GIAIC National Bank")

# 🔍 Display AFTER change
print("📍 After Bank Name Change:")
account1.display()
account2.display()
