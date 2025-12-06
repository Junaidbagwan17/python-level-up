#step 3

import random
word_list = ["advark", "baboon", "camel"]
chosen_word = random.choice(word_list)
print("pssst:",chosen_word)


display = []
word_len = len(chosen_word)
for _ in range(word_len):
    display += "_"
print( display)

# ask user to guess until blanks got filled

end_of_game = False 
while not end_of_game:
    guess = input("guess the word:").lower()

    for position in range(word_len):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    print(display)

    if "_" not in display:
        end_of_game = True
        print("you win")
        
        
        
        
