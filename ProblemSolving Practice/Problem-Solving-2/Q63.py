#TODO: Given a list of words, find the word with the maximum length and its length

words = ["Mobile", "Laptop", "Computer", "Tab", "Software", "Hardware", "Data Science"]

max_length = 0
max_word = ""

for word in words:
    if len(word) > max_length:
        max_length = len(word)
        max_word = word
print(f"Maximum word len is {max_length} and that word is {max_word}")


# or Just:
print(max(words, key=len))