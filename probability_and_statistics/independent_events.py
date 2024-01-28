import random

# Function to simulate rolling a six-sided die
def roll_die():
    return random.randint(1, 6)

# Function to simulate flipping a coin
def flip_coin():
    return random.choice(["Heads", "Tails"])

# Simulate rolling a die and flipping a coin
die_roll = roll_die()
coin_flip = flip_coin()

# Display the results
print("Die roll result:", die_roll)
print("Coin flip result:", coin_flip)

# Check if the two events are independent
# In theory, since one does not affect the other, they are independent
