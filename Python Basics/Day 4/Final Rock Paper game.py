import random

rock = '🪨'
paper = '📄'
scissor = '✂️'

emoji = [rock, paper, scissor]
user_choice = int(input("enter 0 for rock , 1 for Paper, 2 for scissor: "))
print('Your choice :' ,emoji[user_choice])

computer_choice = random.randint(0, 2)
print('Opponent choice:', emoji[computer_choice])

if user_choice >= 3 or user_choice < 0:
    print("U chose an invalid Number try again!")
elif user_choice == computer_choice:
    print("Draw !😲")
    
elif user_choice == 0 and computer_choice == 2:
    print("You win")
elif user_choice == 1 and computer_choice == 0:
    print("you win")
elif user_choice == 2 and computer_choice == 1:
    print("you win")     

else:
    print('you lose')
