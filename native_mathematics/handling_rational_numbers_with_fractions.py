from fractions import Fraction
import decimal

# Create a Fraction from a floating-point number
fraction_float = Fraction(0.5)
print("Fraction from floating-point number 0.5:", fraction_float)

# Create a Fraction from a string
fraction_str = Fraction("3/4")
print("Fraction from string '3/4':", fraction_str)

# Perform arithmetic operations with Fractions
fraction_sum = fraction_float + fraction_str
print("Sum of fractions:", fraction_sum)

fraction_product = fraction_float * fraction_str
print("Product of fractions:", fraction_product)

# Convert Fraction to float
fraction_to_float = float(fraction_sum)
print("Convert fraction to float:", fraction_to_float)

# Convert Fraction to a string
fraction_to_str = str(fraction_sum)
print("Convert fraction to string:", fraction_to_str)

# Get numerator and denominator of a Fraction
numerator = fraction_sum.numerator
denominator = fraction_sum.denominator
print("Numerator:", numerator)
print("Denominator:", denominator)
