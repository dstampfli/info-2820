"""
Program: sphere.py
Author: David Stampfli  
Date: 1/28/2024
This program calculates the diameter,circumference, surface area, and volume of a sphere.
Input: The radius of the sphere as an int or floating-point number.
Output: The diameter, circumference, surface area, and volume of the sphere using the supplied radius.
"""

radius = int(input("Enter the radius of the sphere: "))

diameter = radius * 2
circumference = 2 * 3.14 * radius
surface_area = 4 * 3.14 * radius ** 2
volume = 4 / 3 * 3.14 * radius ** 3

print("The diameter of the sphere is", diameter)
print("The circumference of the sphere is", circumference)
print("The surface area of the sphere is", surface_area)
print("The volume of the sphere is", volume)

# Output:
# Enter the radius of the sphere: 5
# The diameter of the sphere is 10
# The circumference of the sphere is 31.41592653589793
# The surface area of the sphere is 314.1592653589793
# The volume of the sphere is 523.5987755982989