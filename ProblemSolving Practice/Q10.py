# TODO Create a program that takes a sentence as input and counts the number of words in it

sentence = "I love INDIA."

# 1. Very Short way to count
count = (sentence.count(" "))
print(count+1)

#using Functions
sentence_list = sentence.split()
print(len(sentence_list))
