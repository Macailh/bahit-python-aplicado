print("==================================")
print("Formatting a string by dynamically substituting text")
template = "Hello, my name is {} and I am {} years old."
formatted_string = template.format("Alice", 30)
print(formatted_string)  # Output: Hello, my name is Alice and I am 30 years old.

print("==================================")
print("Replace text in a string")
original_string = "I love apples, apples are my favorite fruit."
replaced_string = original_string.replace("apples", "oranges")
print(replaced_string)  # Output: I love oranges, oranges are my favorite fruit.

print("==================================")
print("Remove characters from the left and right of a string")
string_with_spaces = "   This is a test string.   "
trimmed_string = string_with_spaces.strip()
print(trimmed_string)  # Output: This is a test string.

print("==================================")
print("Remove characters from the left of a string")
left_spaced_string = "   Remove spaces to the left."
left_trimmed_string = left_spaced_string.lstrip()
print(left_trimmed_string)  # Output: Remove spaces to the left.

print("==================================")
print("Remove characters from the right of a string")
right_spaced_string = "Remove spaces to the right.   "
right_trimmed_string = right_spaced_string.rstrip()
print(right_trimmed_string)  # Output: Remove spaces to the right.
