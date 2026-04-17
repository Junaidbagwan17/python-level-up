#TODO: Create a program that generates the Fibonacci sequence up to a given number of terms
terms = 5
a = 0
b = 1

for i in range(terms):
    print(a)
    temp = b
    b = a + b
    a = temp
    # a, b = b, a + b