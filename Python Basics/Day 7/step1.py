import random
# randomly chose the word from list and assign it to a var
word_list = ["advark", "baboon", "camel"]
chosen_word = random.choice(word_list)
print(chosen_word)


# ask the user to guess the letter and assign to var guess
guess = input("guess the word:").lower()

# check the guess is right or wrong and print right if right, otherwise print wrong
# loop through chosen word and then guess

for letter in chosen_word:
    if letter == guess:
        print("Right") 
    else:
        print("Wrong")
