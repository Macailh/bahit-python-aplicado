import math

# Define an angle in radians
angle = math.pi / 6  # 30 degrees in radians

# Sine of the angle
sine = math.sin(angle)
print("Sine:", sine)

# Cosine of the angle
cosine = math.cos(angle)
print("Cosine:", cosine)

# Tangent of the angle
tangent = math.tan(angle)
print("Tangent:", tangent)

# Fundamental trigonometric relationship: sin^2(theta) + cos^2(theta) = 1
result = math.pow(sine, 2) + math.pow(cosine, 2)
print("Fundamental relationship:", result)

# Angle whose sine is 1
angle_sine_1 = math.asin(1)
print("Angle whose sine is 1 (in radians):", angle_sine_1)

# Angle whose cosine is 1
angle_cosine_1 = math.acos(1)
print("Angle whose cosine is 1 (in radians):", angle_cosine_1)

# Angle whose tangent is 1
angle_tangent_1 = math.atan(1)
print("Angle whose tangent is 1 (in radians):", angle_tangent_1)
