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

num1 = int(input("enter the fisrst number:"))
num2 = int(input("Enter the second number:"))

#Loop throgh opearations and print the symbols

for symbols in operations:
    print(symbols)
operation_symbol= input("Pick an operation from Above ")

calculation_function = operations[operation_symbol]
answer = calculation_function(num1 , num2)


print(f"{num1} {operation_symbol} {num2} = {answer}")