# Create a function that returns both the area and circumference of circle given its radius

import math

def Calculate_circle(radius):
    area =  math.pi * radius**2 
    circumference=2*math.pi*radius
    return [area,circumference]

print("the area and circumference of circle is ",(Calculate_circle(3)))
