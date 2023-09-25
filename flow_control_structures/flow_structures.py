print('-------if------------')
x = 10

if x > 0:
    print("x is positive")
elif x == 0:
    print("x is zero")
else:
    print("x is negative")
print('--------------------')

print('-------for-----------')
# Iterating over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Iterating over a range
for i in range(5):
    print(i)  # Prints numbers from 0 to 4
print('--------------------')

print('-------while---------')
count = 0
while count < 5:
    print(count)
    count += 1
print('--------------------')

print('-------switch--------')
# Simulated switch using a dictionary
def case1():
    print("Case 1")

def case2():
    print("Case 2")

def case_default():
    print("Default case")

switch_cases = {
    1: case1,
    2: case2
}

choice = 2

switch_cases.get(choice, case_default)()
print('--------------------')
