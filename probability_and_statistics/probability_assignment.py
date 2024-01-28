import random

# Representation of a die with 6 faces
faces_of_die = [1, 2, 3, 4, 5, 6]

# Assigning probabilities (each face has the same probability)
probability_per_face = 1/6

# Function to calculate the probability of rolling an odd number
def probability_of_odd_number(faces, probability):
    odd_numbers = [face for face in faces if face % 2 != 0]
    return len(odd_numbers) * probability

# Calculate the probability of rolling an odd number
probability_odd = probability_of_odd_number(faces_of_die, probability_per_face)
print(probability_odd)
