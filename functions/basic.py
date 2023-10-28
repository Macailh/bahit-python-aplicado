def my_function():
    return "First function"

def my_second_function(string):
    return string

def my_third_function():
    print("Third function")

def fun_in_var():
    return "function in var"

phrase = fun_in_var()
print(phrase)


def calculate_net(gross, aliquot):
    iva = gross * float(aliquot) / 100
    net = gross + iva
    return net

print(calculate_net(100, 12))


def calculate_net_2(gross, aliquot=16):
    iva = gross * float(aliquot) / 100
    net = gross + iva
    return net

print(calculate_net_2(1000))


def example_fun(*elements):
    for element in elements:
        print(element)

list = [1, 2, 3, 4, 5 , 6]
example_fun(list)


def example_fun_2(**elements):
    for value in elements.values():
        print(value)

values = {"a": 1, "b": 2, "c": 3}
example_fun_2(**values)