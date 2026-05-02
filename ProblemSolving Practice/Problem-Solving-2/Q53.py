#TODO: Given a list of names, count the number of names that start with a vowel
from tkinter.font import names

name_list = ["Ashish", "Adam", "Jarvo", "Archer", "Imran", "Bumrah", "Josh"]

def count_vowles(names):
    vowels = "AEIOU"
    count = 0

    for name in names:
        if name[0].upper() in vowels:
            count += 1
    return f"there are total {count}  names in the list which start with vowels"
print(count_vowles(name_list))
