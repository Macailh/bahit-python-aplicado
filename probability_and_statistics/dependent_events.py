import random

# Create a standard deck of 52 cards
deck = ["Ace", "King", "Queen", "Jack"] + ["10", "9", "8", "7", "6", "5", "4", "3", "2"]*4
# Each of the above ranks appears in four suits, so we have 52 cards

# Function to draw a card from the deck
def draw_card(deck):
    card = random.choice(deck)
    deck.remove(card)
    return card

# Draw the first card
first_card = draw_card(deck)
# Check if the first card is an Ace
is_ace = first_card == "Ace"

# Draw the second card
second_card = draw_card(deck)
# Check if the second card is a King
is_king = second_card == "King"

# Display the results
print("First card drawn:", first_card)
print("Second card drawn:", second_card)
print("First card is Ace and second card is King:", is_ace and is_king)
