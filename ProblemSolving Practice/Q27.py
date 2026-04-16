#TODO: Given a list of integers, find all the even numbers and store them in a new list
numbers = [41,20, 8, 55, 14, 6, 88,30,56]

even_numbers = []
for n in numbers:
    if n % 2 == 0:
        even_numbers.append(n)

even_numbers.sort()
print(even_numbers)