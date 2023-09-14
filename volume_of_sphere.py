import math

def calculate_volume_of_sphere(radius):
    volume = (4/3) * math.pi * radius**3
    return volume

radius1 = 30
radius2 = 40

volume1 = calculate_volume_of_sphere(radius1)
volume2 = calculate_volume_of_sphere(radius2)

print(f"The volume of a sphere with radius {radius1} is: {volume1:.2f}")
print(f"THe volume of a sphere with radius {radius2} is: {volume2:.2f}")
