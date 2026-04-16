# TODO Implement a program that finds the largest number in a list.

numbers = [12,100,78,88,89,155,102]
largest_number = 0
for num in numbers:
    if num > largest_number:
        largest_number = num
print(f"The largest number in the list is: {largest_number}")