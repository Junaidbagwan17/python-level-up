#TODO: Create a function that takes a list of strings and returns the list sorted by the length of the strings

def sorting(words):
    words.sort(key=len)
    return words

words_list = ["apple","hi","world"]

print(sorting(words_list))