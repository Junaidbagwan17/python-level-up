# TODO: Create a function that takes a sentence as input and returns the sentence in reverse order

def reverse_the_order(sentence):
    words =sentence.split()
    reversed_sentence = words[::-1]
    return " ".join(reversed_sentence)

print(reverse_the_order(sentence=input("enter the sentence to reverse:")))