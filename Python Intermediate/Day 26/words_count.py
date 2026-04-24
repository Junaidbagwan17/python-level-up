sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

# convert it into list of words
sentence_list = sentence.split(" ")
# print(sentence_list)

# make list as dict from list and count the len of each word
result = {word:len(word) for word in sentence_list}
print(result)
