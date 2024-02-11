import numpy as np

# Generate a sample dataset
data = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

# Calculate standard deviation
std_dev = np.std(data)

# Calculate variance
variance = np.var(data)

# Calculate range (difference between max and min)
data_range = np.max(data) - np.min(data)

# Calculate interquartile range
Q1 = np.percentile(data, 25)  # First quartile
Q3 = np.percentile(data, 75)  # Third quartile
IQR = Q3 - Q1

print(f"Standard Deviation: {std_dev}")
print(f"Variance: {variance}")
print(f"Range: {data_range}")
print(f"Interquartile Range: {IQR}")
