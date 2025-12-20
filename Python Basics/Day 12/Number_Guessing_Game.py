import random
print("welcome to the python Number Guessing Game!")
print("""                                                                                                                 
   ▄▄▄                                    ▄▄▄▄▄▄▄ █                    ▄▄   ▄               █                   
 ▄▀   ▀ ▄   ▄   ▄▄▄    ▄▄▄    ▄▄▄            █    █ ▄▄    ▄▄▄          █▀▄  █ ▄   ▄  ▄▄▄▄▄  █▄▄▄    ▄▄▄    ▄ ▄▄ 
 █   ▄▄ █   █  █▀  █  █   ▀  █   ▀           █    █▀  █  █▀  █         █ █▄ █ █   █  █ █ █  █▀ ▀█  █▀  █   █▀  ▀
 █    █ █   █  █▀▀▀▀   ▀▀▀▄   ▀▀▀▄           █    █   █  █▀▀▀▀         █  █ █ █   █  █ █ █  █   █  █▀▀▀▀   █    
  ▀▄▄▄▀ ▀▄▄▀█  ▀█▄▄▀  ▀▄▄▄▀  ▀▄▄▄▀           █    █   █  ▀█▄▄▀         █   ██ ▀▄▄▀█  █ █ █  ██▄█▀  ▀█▄▄▀   █    
                                                                                                                
                                                                                                                """)
# 1 - get a random number
number = random.randint(1,100)
print("I am thinking number between 1 to 100")
print(f"number pssst: {number} ")

game_level =input("select level for the game easy or hard: ")

if game_level == 'hard':
    attempts = 5 
else:
    attempts = 10

while attempts > 0:  # guess != number:
    
    guess = int(input("Guess the number: "))
    if attempts == 0:
        print("you lose you have no attempts left")
    else:
        print(f"you have {attempts} attempts left")

    if guess != number:
            attempts -= 1
            
    if guess == number:
        print("You win")
        break
    elif guess > number:
        print("Too High")
    elif guess < number:
        print("Too Low")
        
