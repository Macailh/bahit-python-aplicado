import numpy as np
from collections import Counter

# Generate a sample dataset
data = np.random.randint(1, 10, 50)  # 50 random integers between 1 and 10

# Calculate absolute frequency using Counter
abs_freq = Counter(data)

print("Data:", data)
print("Absolute Frequency:", abs_freq)
