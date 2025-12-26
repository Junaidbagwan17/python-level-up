# TODO 1: Import required modules and data
import random
from art_logo import logo, vs
from game_data import data # print(data[0]) # instagram
print("Welcome to Higher Lower Game")
print(logo)
should_play = True

# TODO 2: Create function to get two different persons (A and B)
def get_user():
    user_A = random.choice(data)# choose A
    user_B = random.choice(data)# choose B
    while user_B == user_A:
        user_B = random.choice(data) # while B is same as A → choose again
    return user_A, user_B # return A, B

# TODO 3: Get initial A and B
a, b = get_user()

# TODO 4: Function to get follower count
def get_follower_counts(user):
    return user["follower_count"]

# TODO 5: Function to compare followers
def compare(count_a,count_b):
    if count_a > count_b:
        return "a"
    else:
        return "b"
    
# create a score var to track score
score = 0

# TODO 6: Create game loop
while should_play:
    print(f'\n {a["name"]}, a {a["description"]} from {a["country"]}.')
    print(vs)
    print(f'\n {b["name"]}, a {b["description"]} from {b["country"]}.\n')
    
    # TODO 7: Get follower counts of A and B
    follower_A = get_follower_counts(a) 
    follower_B = get_follower_counts(b) 
    # print("pssst",follower_A, follower_B)
    
    # TODO 8: Compare followers to find winner
    winner = compare(follower_A, follower_B)
      
    # TODO 9: Take guess from user
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    
    # TODO 10: Check guess and update score
    if guess == winner:
        score += 1
        print("----------------" * 4)
        print(f"You are right ✔️! current score is {score} 😍")
        print("----------------" * 4)
        
        # TODO 11: Make B as new A and get a new B
        a = b
        b = random.choice(data)
        while b == a :
            b =  random.choice(data)
            
    # TODO 12: Stop game when guess is wrong
    else:
        print("----------------" * 4)
        print(f"\n Sorry, that's wrong ❌. final score is {score} 😰\n")
        print("----------------" * 4)
        should_play = False
        