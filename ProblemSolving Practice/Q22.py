#TODO Write a program to check if a number is prime.

number = int(input("enter number:"))

is_prime = True
for n in range(2, number-1):
    if n % 2 == 0:
        is_prime = False
    else:
        is_prime= True

if is_prime:
    print("Its prime number.")
else:
    print("Its not a prime number.")