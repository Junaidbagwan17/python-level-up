#TODO: Calculate the sum of digits of a given number.
from math import remainder

number = int(input("Enter a number: "))
total = 0

while number > 0:
    digit = number % 10
    total += digit
    number = number // 10
print("the sum of digits of a given number is:",total)

