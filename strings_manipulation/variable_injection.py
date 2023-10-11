name = "Alice"
print("Hello, %s!" % name)

name = "Bob"
age = 30
print("Hello, {}. You are {} years old.".format(name, age))

print("Hello, {1}. You are {0} years old.".format(age, name))
print("Hello, {name}. You are {age} years old.".format(name=name, age=age))

name = "Charlie"
age = 40
print(f"Hello, {name}. You are {age} years old.")

print(f"{name} will be {age + 5} years old in 5 years.")

name = "David"
print("Hello, " + name + "!")
