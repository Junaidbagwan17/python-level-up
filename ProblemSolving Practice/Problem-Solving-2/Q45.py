# TODO: Write a function to count the number of vowels in given string.

vowels = "a e i o u".split(" ") # now it is list

def count_vowels(text):
    result = [i for i in text if i.lower() in vowels]
    print(len(result))
count_vowels("India is my country.")