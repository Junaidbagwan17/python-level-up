#todo: Use function to Create a program that checks if a given string is a palindrome.

user_text = input("enter word:")

def check_palindrome(text):
    if text == text[::-1]:
        print("Its Palindrome")
    else:
        print("Its not a Palindrome")

check_palindrome(text=user_text)
