n = int(input("Enter a number to check: "))

# a prime number is the number whihc is only can cleanly divisible 1 and itself
# for eg. we we want to check 7 as number:
# do iteration chk by exluding 1 and 7 and if (7 / 23456) = 0 --> not a prime!

# def the funtion
def prime_checker(number):
    is_prime = True
    for i in range(2, number-1):
        if number % i == 0:
            is_prime =False
    if is_prime:  #is_prime == True
        print(number, "is prime number")
    else:
        print(number, "is not a prime number")
        
# call the function
prime_checker(number=n)