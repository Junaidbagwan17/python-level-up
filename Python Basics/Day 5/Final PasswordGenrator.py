#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

password = ''
for letter in range(nr_letters):
    random_letter = random.randint(0, nr_letters-1)
    password += letters[random_letter]
# print(password)

for sym in range(nr_symbols):
    random_sym = random.choice(symbols)
    password += random_sym

for num in range(nr_numbers):
    password += random.choice(numbers)
# easy level
print(f"your easy password is {password}")


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P


password_list = list(password) #cant shuffle string it must be data structure
random.shuffle(password_list) # converted into list 
# print(password_list) #['0', '0', 'b', '*', 'c', 'a', '#'] #need to conv this as plain text

strong_password = ''.join(password_list)
print(f"your strong password is {strong_password}")

# OUTPUT:
# your easy password is baaa$%29
# your strong password is $a9b%aa2