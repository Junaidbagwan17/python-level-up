# def function with return for operations 
def add(n1 , n2):
    return n1 + n2

def subtract(n1, n2):
    return n1-n2

def multiply(n1, n2):
    return(n1 * n2)

def divide(n1 , n2):
    return n1 / n2


# Create a dictonary named operation keys

operations = {
   "+" : add,
   "-" :subtract,
   "*" : multiply,
   "/" :divide, 
}

def calculator():
    print('''_____________________
|  _________________  |
| | JO           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|''')

    num1 = int(input("enter the fisrst number:"))
    
    for symbols in operations:
        print(symbols)

    want_continue = True
    while want_continue:
        operation_symbol= input("Pick an operation: ")
        num2 = int(input("Enter the next number:"))
        calculation_function = operations[operation_symbol]
        print("calcfunction",calculation_function)
        answer = calculation_function(num1 , num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        again = input("do want to continue (y/n):")
        if again == 'y':
            num1 = answer
        else:
            want_continue = False
            calculator()

calculator()