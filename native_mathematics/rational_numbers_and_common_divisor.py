from fractions import Fraction
import math

# Creating a rational number
num1, den1 = 8, 12  # 8/12
rational1 = Fraction(num1, den1)
print(f"Rational number: {rational1}")

# Simplifying the rational number
simplified_rational1 = rational1.numerator, rational1.denominator
print(f"Simplified rational: {simplified_rational1[0]}/{simplified_rational1[1]}")

# Calculating the Greatest Common Divisor (GCD)
gcd = math.gcd(num1, den1)
print(f"GCD of {num1} and {den1}: {gcd}")

# Example with another rational number
num2, den2 = 15, 25  # 15/25
rational2 = Fraction(num2, den2)
print(f"Another rational number: {rational2}")
simplified_rational2 = rational2.numerator, rational2.denominator
print(f"Simplified rational: {simplified_rational2[0]}/{simplified_rational2[1]}")
