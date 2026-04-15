#TODO: Calculate the area and circumference of a circle given its radius

r = float(input("enter radius:"))

pi = 3.14

area_of_circle = round(pi * r**2, 2)
circumference = round(2 * pi * r, 2)

print(f"The area of the circle is {area_of_circle}")
print(f"The circumference of the circle is {circumference}")