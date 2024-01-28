import random

# Function to simulate rolling a die
def roll_die():
    return random.randint(1, 6)

# Simulate rolling a die 10 times
results = [roll_die() for _ in range(10)]

print("Results of rolling a die 10 times:", results)
