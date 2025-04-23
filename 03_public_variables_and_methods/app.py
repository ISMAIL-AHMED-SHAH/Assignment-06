# 3. Public Variables and Methods
# Create a class Car with a public variable brand and a public method start().
# Instantiate the class and access both from outside the class.

class Car:
    def __init__(self, brand):
        self.brand = brand  # Public variable

    def start(self):  # Public method
        print(f"{self.brand} is starting... 🚗")


# Create an instance of the Car class
my_car = Car("Toyota")

# Access the public variable and method
print(f"My car brand is: {my_car.brand}")  # Accessing public variable
my_car.start()  # Calling public method

# Output:
# My car brand is: Toyota