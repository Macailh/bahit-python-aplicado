# Capitalize the first letter:
text = "hello world"
capitalized_text = text.capitalize()
print(capitalized_text)  # Output: "Hello world"

# Convert string to lowercase:
text = "HELLO WORLD"
lowercase_text = text.lower()
print(lowercase_text)  # Output: "hello world"

# Convert string to uppercase:
text = "hello world"
uppercase_text = text.upper()
print(uppercase_text)  # Output: "HELLO WORLD"

# Swap uppercase to lowercase and vice versa:
text = "HeLLo WoRLD"
swapped_text = text.swapcase()
print(swapped_text)  # Output: "hEllO wOrld"

# Convert string to title format:
text = "hello world"
title_text = text.title()
print(title_text)  # Output: "Hello World"

# Center the text:
text = "hello"
centered_text = text.center(20)  # Width of 20 characters
print(centered_text)  # Output: "       hello        "

# Align text to the left:
text = "hello"
left_aligned_text = text.ljust(20)  # Width of 20 characters
print(left_aligned_text)  # Output: "hello               "

# Align text to the right:
text = "hello"
right_aligned_text = text.rjust(20)  # Width of 20 characters
print(right_aligned_text)  # Output: "               hello"

# Pad text with leading zeros:
text = "42"
zero_padded_text = text.zfill(5)  # Width of 5 characters
print(zero_padded_text)  # Output: "00042"
