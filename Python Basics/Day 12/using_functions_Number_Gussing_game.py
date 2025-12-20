
from random import randint

EASY_LEVEL = 10
HARD_LEVEL = 5

def check_answer(guess, answer, turns):
    if guess > answer:
        print("Too High")
        return turns -1
    elif guess < answer:
        print("Too Low")
        return turns   -1

    else:
        print(f"you got it! and answer was {answer}")

def set_difficulty():
    level = input("Hard or Easy level : ")
    if level == "easy":
        return EASY_LEVEL
    else:
        return HARD_LEVEL

def game(): 
    # choose a random number between 1 to 100
    print("welcome to number guessing game")
    print("I am thinking a number between 1 and 100.")
    answer = randint(1,100)
    print("pssssst answer:", answer)

    turns = set_difficulty()

    guess = 0
    while guess != answer: 
        print(f"You have {turns} attempts remaining to guess the number! ")
        guess = int(input("Guess the number: "))
        turns = check_answer(guess , answer, turns)
        if turns == 0:
            print("You run out of guesses, you lose.")
            return 
        elif guess != answer:
           print("Guess again!") 
          
game() 