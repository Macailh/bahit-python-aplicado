import numpy as np
from collections import Counter

# Generate a sample dataset
data = np.random.randint(1, 10, 50)  # 50 random integers between 1 and 10

# Calculate absolute frequency using Counter
abs_freq = Counter(data)

# Calculate total number of data points
total_data_points = len(data)

# Calculate relative frequency
rel_freq = {key: value / total_data_points for key, value in abs_freq.items()}

print("Data:", data)
print("Relative Frequency:", rel_freq)
