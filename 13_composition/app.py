# 13. Composition
# Create a class Engine and a class Car.
# Use composition by passing an Engine object to the Car class during initialization. 
# Access a method of the Engine class via the Car class.

class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

    def start(self):
        print(f"Engine with {self.horsepower} HP is starting... 🔥")


class Car:
    def __init__(self, brand, engine):
        self.brand = brand
        self.engine = engine  # Composition: Car has an Engine

    def start(self):
        print(f"{self.brand} is starting... 🚗")
        self.engine.start()  # Accessing Engine's method

engine1 = Engine(150)  # Creating an Engine object
my_car = Car("Toyota", engine1)  # Creating a Car object with an Engine object

my_car.start()  # Starting the Car, which also starts the Engine

# Output:
# Toyota is starting... 🚗
# Engine with 150 HP is starting... 🔥


