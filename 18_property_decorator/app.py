# 18. Property Decorators: @property, @setter, and @deleter
# Create a class Product with a private attribute _price.
# Use @property to get the price, @price.setter to update it, and @price.deleter to delete it.

class Product:
    def __init__(self, price):
        self.price = price 

    @property
    def price(self):
        print("Getting price...")
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            print("\n❌ Price cannot be negative!")
        else:
            print("\nSetting price...")
            self._price = value

    @price.deleter
    def price(self):
        print("Deleting price...")
        del self._price


item = Product(100)     #      Setting price...

print(item.price)       #      Getting price... 100
item.price = 150        #      Setting price...
print(item.price)       #      Getting price... 150

item.price = -50        #      ❌ Price cannot be negative!
del item.price          #      Deleting price...

