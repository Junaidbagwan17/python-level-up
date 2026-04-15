#TODO Create a function to count the number of vowels in a given string

vowels = ["a", "e", "i", "o", "u"]

def count_vowels(text):
    count = 0
    for letter in text.lower():
        if  letter in vowels:
            count += 1
    print("total vowels in sentence is",count)
count_vowels("this Is a Pen")