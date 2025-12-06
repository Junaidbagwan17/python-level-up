import random
word_list = ["advark", "baboon", "camel"]
chosen_word = random.choice(word_list)
print("pssst:",chosen_word)

# genrate as many as blanks in chosen word
display = []
word_len = len(chosen_word)
for _ in range(word_len):
    display += "_"
print( display)

guess = input("guess the word:").lower()
# fill the blanks with guessed letter if it is right only!
# and display that right letter at that position

for n in range(word_len):
    if chosen_word[n] == guess:
        display[n] += guess

#print the display
print(display)


