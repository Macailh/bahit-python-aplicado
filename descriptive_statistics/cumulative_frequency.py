import numpy as np
from collections import Counter

# Generate a sample dataset
data = np.random.randint(1, 10, 50)  # 50 random integers between 1 and 10

# Calculate absolute frequency using Counter
abs_freq = Counter(data)

# Sort the data to calculate cumulative frequency
sorted_data = sorted(abs_freq.items())

# Calculate cumulative frequency
cum_freq = {}
running_total = 0
for value, freq in sorted_data:
    running_total += freq
    cum_freq[value] = running_total

print("Data:", data)
print("Cumulative Frequency:", cum_freq)
