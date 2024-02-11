import numpy as np

# Generate a simulated population
np.random.seed(0)  # For reproducibility
population_mean = 170  # mean height in cm
population_std_dev = 10  # standard deviation in cm
population_size = 1000000  # number of people in the population
population_heights = np.random.normal(population_mean, population_std_dev, population_size)

# Take a sample from the population
sample_size = 1000  # size of the sample
sample_heights = np.random.choice(population_heights, sample_size, replace=False)

# Calculate population and sample statistics
mean_of_population = np.mean(population_heights)
mean_of_sample = np.mean(sample_heights)
std_dev_of_population = np.std(population_heights)
std_dev_of_sample = np.std(sample_heights)
