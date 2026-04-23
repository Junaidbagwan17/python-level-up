#TODO; Write a function to calculate the area of a circle given its radius.

PI = 3.14
r = int(input("enter radius:"))

def area_of_circle(radius):
    area = PI * radius**2
    print(f"area of circle for a given radius is: {area}")
area_of_circle(radius=r)

