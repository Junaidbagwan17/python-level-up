#TODO: Write a Python program to check if a given string is a  pangram (contains all letters of the alphabet)

text = input("Enter a sentence: ")
text = text.lower()
letters = "abcdefghijklmnopqrstuvwxz"
is_pangram = True

for letter in letters:
    if letter not in text:
        is_pangram = False
    else:
        is_pangram = True
if is_pangram:
    print("Its a Pangram.")
else:
    print("Its Not a Pangram.")