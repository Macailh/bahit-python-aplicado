def decorator(decorated_function):

    def wrapper():
        return decorated_function()

    return wrapper


@decorator
def function():
    pass


def logger_decorator(func):
    
    def wrapper():
        print(f"The function {func.__name__} was called.")
        return func()
    
    return wrapper


@logger_decorator
def say_hello():
    print("Hello!")

say_hello()
