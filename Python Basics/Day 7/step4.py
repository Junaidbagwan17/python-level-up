from hangman_art import stages
#step 4
import random
word_list = ["advark", "baboon", "camel"]
chosen_word = random.choice(word_list)
# creae a lives tracker
lives = 6
print("pssst:",chosen_word)

display = []
word_len = len(chosen_word)
for _ in range(word_len):
    display += "_"
print( display)

end_of_game = False 
while not end_of_game:
    guess = input("guess the word:").lower()

    for position in range(word_len):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
            
    #if guess is not letter in chosenword then reduce lives by -1 and if 
    # if there lives = 0 end game and say lose
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            print("you lose")
            end_of_game = True
            

    print(f"{''.join(display)}")

    if "_" not in display:
        print("you win")
        end_of_game = True
        
    # print the stages 
    print(stages[lives])
        
        
        
