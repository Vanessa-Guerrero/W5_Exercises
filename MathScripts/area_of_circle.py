# Importing math module to use the math.pi constant for pi
import math

# Define known values
radius = 3
pi = math.pi

# Calculate the unknown
area_of_circle = pi * radius ** 2

# Display the results
print("The area of a circle with radius " + str(radius) + " is " + format(area_of_circle, ".2f"))