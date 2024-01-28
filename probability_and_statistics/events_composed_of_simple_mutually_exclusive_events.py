import random

# Function to simulate rolling a six-sided die
def roll_die():
    return random.randint(1, 6)

# Function to simulate flipping a coin
def flip_coin():
    return random.choice(["Heads", "Tails"])

# Simulate rolling a die and flipping a coin
die_result = roll_die()
coin_result = flip_coin()

# Display the results
print("Die roll result:", die_result)
print("Coin flip result:", coin_result)

# Check for a specific compound event, e.g., rolling a 4 and getting Heads
is_specific_event = die_result == 4 and coin_result == "Heads"
print("Rolled a 4 and got Heads:", is_specific_event)
