# 19. callable() and __call__()
# Create a class Multiplier with an __init__() to set a factor.
# Define a __call__() method that multiplies an input by the factor.
# Test it with callable() and by calling the object like a function.

class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):
        return value * self.factor



double = Multiplier(2)
triple = Multiplier(3)

# ✅ Use like a function
print(double(5))                # Output: 10
print(triple(4))                # Output: 12

# ✅ Test with callable()
print(callable(double))         # True
print(callable(triple))         # True
print(callable(123))            # False
