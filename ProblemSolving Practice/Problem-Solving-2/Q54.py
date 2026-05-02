#TODO: Write a Python program to find the length of the longest word in a sentence

def find_longest_word(text):
    maximum = 0
    words = text.split(" ")
    for i in words:
        if len(i) > maximum:
            maximum =len (i)
    return maximum
print(find_longest_word("Hello i am JunaidBagwan"))

# or

def find_longest_word_again(text):
    words = text.split(" ")
    result =  max(words, key=len)
    return len(result)
print(find_longest_word_again("Hello i am JunaidBagwan"))