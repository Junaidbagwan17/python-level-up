#TODO: Write a function to check if a number is even or odd and return "Even" or "Odd" accordingly

def check_even_odd(number):
    if number % 2 == 0:
        return 'Even'
    else:
        return 'Odd'
print(check_even_odd(4))