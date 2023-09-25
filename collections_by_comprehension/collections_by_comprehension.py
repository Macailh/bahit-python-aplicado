print('----List Comprehension----')
# Creating a list using list comprehension
numbers = [x for x in range(10) if x % 2 == 0]
print(numbers)  # Output: [0, 2, 4, 6, 8]
print('--------------------------')

print('---Dictionary Comprehension---')
# Creating a dictionary using dictionary comprehension
square_numbers = {x: x*x for x in range(1, 6)}
print(square_numbers)  # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
print('-------------------------------')

print('-----Set Comprehension-----')
# Creating a set using set comprehension
unique_chars = {char for char in 'hello'}
print(unique_chars)  # Output: {'h', 'o', 'l', 'e'}
print('---------------------------')
