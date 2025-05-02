# 16. Function Decorators
# Write a decorator function log_function_call that prints
# "Function is being called" before a function executes.
# Apply it to a function say_hello().

# Decorator Function
def log_function_call(func):
    def wrapper():
        print("Function is being called")
        func()
    return wrapper

@log_function_call
def say_hello():
    print("Hello!")

say_hello()


# Output:    Function is being called
#            Hello!


