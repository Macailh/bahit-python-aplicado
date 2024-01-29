import random

# Possible outcomes of a coin toss
coin_outcomes = ["Heads", "Tails"]

# Function to simulate a coin toss
def toss_coin():
    return random.choice(coin_outcomes)

# Simulate the coin toss
result = toss_coin()
print("Coin toss result:", result)

# Check if the events are mutually exclusive
is_heads = result == "Heads"
is_tails = result == "Tails"
print("Is it Heads:", is_heads)
print("Is it Tails:", is_tails)
