import numpy as np
from scipy.stats import itemfreq

# Generate a sample dataset
data = np.random.randint(1, 10, 50)  # 50 random integers between 1 and 10

# Calculate absolute frequency
abs_freq = itemfreq(data)

# Calculate relative frequency
rel_freq = abs_freq.copy()  # Create a copy for relative frequency
rel_freq[:, 1] = rel_freq[:, 1] / len(data)

print("Data:", data)
print("Absolute Frequency:\n", abs_freq)
print("Relative Frequency:\n", rel_freq)
