# TODO 6: Create a Python function to check if a given string is a palindrome

def palindrome(text):
    if text[::-1] == text:
        return True
    else:
        return False
    
name = input("enter name:").lower()
if palindrome(name):
    print("Palindrome")
else:
    print("not Palindrome")