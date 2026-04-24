#TODO: Create a function that takes a number as input and prints its multiplication table.

def multiplication_table(number):
    for i in range(1, 11):
        # print(number * i)
        print(n, "x", i, "=", n * i)

n = int(input("enter number to print its table:"))
multiplication_table(number=n) #when you use print() here it will return NONE


# method 2
def table_of_number(number):
    count = 0
    for i in range(number, (number*10)+1, number):
        # print(i)
        print(number, "x", count, "=", i)
        count += 1
table_of_number(5)
