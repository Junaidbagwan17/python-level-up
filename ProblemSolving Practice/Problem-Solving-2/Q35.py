#TODO Implement a function that returns the factorial of a given number using recursion
# Multiply that number by all positive numbers below it till 1

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)

print(factorial(6))
