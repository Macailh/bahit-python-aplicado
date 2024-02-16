import math

# Function to calculate the area of a circle
def calculate_circle_area(radius):
    return math.pi * math.pow(radius, 2)

# Function to calculate the hypotenuse of a right-angled triangle
def calculate_hypotenuse(side_a, side_b):
    return math.sqrt(math.pow(side_a, 2) + math.pow(side_b, 2))

# Function to calculate the base-10 logarithm of a number
def calculate_log10(number):
    return math.log10(number)

# Function to round a number to its nearest integer
def round_number(number):
    return round(number)

# Function to calculate the exponential of a number
def calculate_exponential(number):
    return math.exp(number)

# Example usage
radius = 5
side_a = 3
side_b = 4
number = 10

print("Area of circle:", calculate_circle_area(radius))
print("Hypotenuse of triangle:", calculate_hypotenuse(side_a, side_b))
print("Logarithm base 10 of number:", calculate_log10(number))
print("Number rounded to nearest integer:", round_number(2.7))
print("Exponential of number:", calculate_exponential(number))
