import numpy as np
from scipy import stats

# Generar un conjunto de datos de ejemplo
data = np.array([10, 20, 20, 20, 30, 40, 50, 60, 70, 80])

# Calcular la media
mean = np.mean(data)

# Calcular la mediana
median = np.median(data)

# Calcular la moda
mode = stats.mode(data)

print(f"Mean (Media): {mean}")
print(f"Median (Mediana): {median}")
print(f"Mode (Moda): {mode.mode[0]} (Count: {mode.count[0]})")
