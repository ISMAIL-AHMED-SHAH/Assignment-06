# 10. Instance Methods
# Create a class Dog with instance variables name and breed.
# Add an instance method bark() that prints a message including the dog's name.

class Dog:
    def __init__(self, name, breed):
        self.name = name            # Instance variable
        self.breed = breed          # Instance variable

    def bark(self):                 # Instance method
        print(f"{self.name} says Woof! 🐶")

dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Max", "Bulldog")
dog3 = Dog("Bella", "Beagle")
dog4 = Dog("Lucy", "Poodle")
dog5 = Dog("Charlie", "Labrador")
dog6 = Dog("Rocky", "German Shepherd")
dog7 = Dog("Daisy", "Siberian Husky")

dog1.bark()  # Output: Buddy says Woof! 🐶
dog2.bark()  # Output: Max says Woof! 🐶
dog3.bark()  # Output: Bella says Woof! 🐶
dog4.bark()  # Output: Lucy says Woof! 🐶
dog5.bark()  # Output: Charlie says Woof! 🐶
dog6.bark()  # Output: Rocky says Woof! 🐶
dog7.bark()  # Output: Daisy says Woof! 🐶



