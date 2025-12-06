from hangman_art import stages, logo
from hangman_words import word_list
#step 5
import random

# update the word list
chosen_word = random.choice(word_list)
# import hangman logo
print(logo)
lives = 6

display = []
word_len = len(chosen_word)
for _ in range(word_len):
    display += "_"
print( display)

end_of_game = False 
while not end_of_game:
    guess = input("guess the word:").lower()
    
    # if user gussed the already gussed letter alert them
    if guess in display:
        print("you have already gussed the letter!")
    for position in range(word_len):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        # alert them when they lose a life
        print("You guessed a wrong letter, you lose a life.")
        lives -= 1
        if lives == 0:
            print("You lose")
            # print the word which user failed to guess
            print("the word that you are trying to guess was: ",chosen_word)
            end_of_game = True
            
    print(f"{''.join(display)}")

    if "_" not in display:
        print("You Win")
        print("the word that you were trying to guess is:",chosen_word)
        end_of_game = True
        
    # print the stages 
    print(stages[lives])
        
        
