from statistics import (
    variance,
    pvariance,
    stdev,
    pstdev,
    mean,
    median,
    mode,
    median_low,
    median_high,
)

data = [5, 7, 8, 10, 12, 15, 18, 20]

print("Data:", data)

# Variance: Measure of the spread of data points around the mean
print("Variance:", variance(data))

# Population Variance: Variance of the entire population (uses N as divisor)
print("Population Variance:", pvariance(data))

# Standard Deviation: Measure of the amount of variation or dispersion
print("Standard Deviation:", stdev(data))

# Population Standard Deviation: Standard deviation of the entire population (uses N as divisor)
print("Population Standard Deviation:", pstdev(data))

# Mean: Average value of the data
print("Mean:", mean(data))

# Median: Middle value of the data when it is sorted
print("Median:", median(data))

# Mode: Value that appears most frequently in the data
print("Mode:", mode(data))

# Low Median: Middle value of the lower half of the data
print("Low Median:", median_low(data))

# High Median: Middle value of the upper half of the data
print("High Median:", median_high(data))
