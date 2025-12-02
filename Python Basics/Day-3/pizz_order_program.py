print("welcm to pizza shop")

size =  input("what size pizza do you want: SML:")
add_pepperoni = input("do want pepporoni? Y/N: ")
extra_cheese = input("do you want extra Y/N : ")
bill = 0

if size == "S":
    bill += 10
elif size == "M":
    bill += 15
elif size == "L":
    bill += 20

if add_pepperoni == "Y":
    if size =="S":
        bill += 2
    else:
        bill += 3

if extra_cheese =="Y":
    bill += 3


print(f"toatl bill is {bill}")     