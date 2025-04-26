# 12. Static Methods
# Create a class TemperatureConverter with a static method
# celsius_to_fahrenheit(c) that returns the Fahrenheit value.

class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32
    
celcius = 36.7

fahrenheit = TemperatureConverter.celsius_to_fahrenheit(celcius)
print(f"{celcius}°C is equal to {fahrenheit}°F")

# Output: 36.7°C is equal to 98.06°F