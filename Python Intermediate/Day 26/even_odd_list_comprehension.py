print("Print only even numbers using conditional list comprehension")

numbers = [1, 1 ,2, 4, 6, 9, 13, 21, 34, 35]
result = [n for n in numbers if n % 2 == 0]
print(result)