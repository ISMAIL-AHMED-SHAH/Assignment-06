# 15. Method Resolution Order (MRO) and Diamond Inheritance
# Create four classes:
# A with a method show(),
# B and C that inherit from A and override show(),
# D that inherits from both B and C.
# Create an object of D and call show() to observe MRO.


class A:
    def show(self):
        print("Show from class A")

class B(A):
    def show(self):
        print("Show from class B")
        super().show()  # Call to A (next in MRO)
        # super().show() can be used to call the method of the parent class

class C(A):
    def show(self):
        print("Show from class C")
        super().show() # Call to A (next in MRO)

class D(B, C):  # D inherits from B and C
    def show(self):
        print("Show from class D")
        print("D")
        super().show() # call B, and then continues through MRO to C and A

# Creating object of class D
obj = D()
obj.show()

# Let's also print MRO
print("\nMRO:", D.__mro__)




    #   A
    #  / \
    # B   C
    #  \ /
    #   D
