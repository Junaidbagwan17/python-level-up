#TODO: Implement a program that takes a sentence and a word as  input and checks if the word is present in the sentence.

def is_word_present(sentence, word):
    words = sentence.split()
    if word in words:
        return True
    else:
        return False

if is_word_present("Hello python", "sql"):
    print("Present")
else:
    print("Not Present")
