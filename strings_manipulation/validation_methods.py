print("==================================")
print("Search using startswith() and endswith()")
string = "Welcome to my application"
print(string.startswith("Welcome"))   # True
print(string.endswith("application")) # True

print("==================================")
print("Check if a string is alphanumeric")
alphanumeric_string = "Welcome123"
print(alphanumeric_string.isalnum())  # True

print("==================================")
print("Check if a string is alphabetic")
alphabetic_string = "Welcome"
print(alphabetic_string.isalpha())    # True

print("==================================")
print("Check if a string is numeric")
numeric_string = "12345"
print(numeric_string.isdigit())       # True

print("==================================")
print("Check if a string contains only lowercase characters")
lowercase_string = "welcome"
print(lowercase_string.islower())     # True

print("==================================")
print("Check if a string contains only uppercase characters")
uppercase_string = "WELCOME"
print(uppercase_string.isupper())     # True

print("==================================")
print("Check if a string contains only whitespace characters")
whitespace_string = "     "
print(whitespace_string.isspace())    # True

print("==================================")
print("Check if a string is in title format")
title_string = "Welcome To My Application"
print(title_string.istitle())         # True
