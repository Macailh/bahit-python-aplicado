# Define two sets
prime_numbers = {2, 3, 5, 7}
odd_numbers = {1, 3, 5, 7, 9}

# Union: all elements that are in either set
union_set = prime_numbers.union(odd_numbers)

# Intersection: elements that are common to both sets
intersection_set = prime_numbers.intersection(odd_numbers)

# Difference: elements that are in the first set but not in the second
difference_set = prime_numbers.difference(odd_numbers)

# Symmetric Difference: elements in either of the sets, but not in both
symmetric_difference_set = prime_numbers.symmetric_difference(odd_numbers)

# Display the results
print("Prime Numbers:", prime_numbers)
print("Odd Numbers:", odd_numbers)
print("Union:", union_set)
print("Intersection:", intersection_set)
print("Difference (Prime - Odd):", difference_set)
print("Symmetric Difference:", symmetric_difference_set)
