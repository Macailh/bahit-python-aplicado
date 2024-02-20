from random import (
    randint,
    randrange,
    getrandbits,
    choice,
    choices,
    sample,
    shuffle,
    gauss,
    gammavariate,
)

print("Return an integer between a and b (inclusive)")
print(randint(1, 10))

print("Return an integer between a and b, x how step (exclusive)")
print(randrange(1, 10, 2))

print("Return an integer with k random bits")
print(getrandbits(4))

print("Return a random element from a sequence")
print(choice([1, 2, 3, 4, 5]))

print("Generar random sequences")
sequence = ["foo", 134123, 123.123, "bar", True, (1, 2, 3)]
print(choice(sequence))
print(choices(sequence, k=3))
print(sample(sequence, 2))
shuffle(sequence)
print(sequence)

print("Randomly distibuted values")
# gauss(mu=average, sigma=deviation)
print(gauss(250, 2))
# gammavariable(alfa=shape, beta=scope)
print(gammavariate(250, 2))
