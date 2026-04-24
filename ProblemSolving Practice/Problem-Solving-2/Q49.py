#todo: Implement a function that checks if a given string is a  pangram (contains all letters of the alphabet)


alphabets = 'abcdefghijklmnopqrstuvwxyz'

def is_pangram(text):
    for i in alphabets:
        if i not in text:
            return False # Exit early if a single letter is missing
    return True  # If the loop finishes, all letters are present

if is_pangram("The quick brown fox jumps over the lazy dog"):
    print("It's a pangram!")
else:
    print("Not a pangram.")