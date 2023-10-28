def closure():
    def intern_function():
        return 1
    
    return intern_function

variable = closure()

print(variable)
print(variable())


def closure_2(param):
    def function():
        return param + 1
    
    return function


variable_2 = closure_2(param=1)
print(variable_2)
print(variable_2())


def outer(x):
    # This outer function takes an argument x

    def inner(y):
        # This inner function takes an argument y
        return x + y  # Here, x is a variable "closed" within the closure

    return inner  # We return the inner function as a result

# Now, we create two closures with different values of x
closure1 = outer(10)
closure2 = outer(20)

# We can use these closures like regular functions
result1 = closure1(5)  # result1 is equal to 15 (10 + 5)
result2 = closure2(5)  # result2 is equal to 25 (20 + 5)

print(result1)
print(result2)