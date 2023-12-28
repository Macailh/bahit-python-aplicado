from os import environ

for var, value in environ.items():
    print(var, value)

PWD = environ.get("PWD")
print("------------------PWD---------------")
print("PWD", PWD)

SHELL = environ.get("SHELL")
print("------------------SHELL---------------")
print("SHELL", SHELL)

HOSTTYPE = environ.get("HOSTTYPE")
print("------------------HOSTTYPE---------------")
print("HOSTTYPE", HOSTTYPE)