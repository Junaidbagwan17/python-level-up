def deal_card():
    """return the random card from cards list"""
    import random
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card

def caluculated_score(cards):

    if sum(cards) == 21 and len(cards) == 2:
        return 0
    # also check 11 and if score is over 21 then remove the 11 and replace it with 1
    if 11 in cards and sum(cards)> 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        return "You went over. You lose "

    if user_score == computer_score:
        return "Draw ! " 
    elif computer_score == 0:
        return "Delaer has blackJack"
    elif user_score == 0:
        return "Win with the BlackJack"
    elif user_score > 21:
        return "you went over opponent has a blackjack"
    elif computer_score > 21:
        return "Delaer went over , You win"
    elif user_score > computer_score:
        return "You win"
    else:
        return "you lose"
def play_game():

    user_cards = []
    computer_cards = []

    is_game_over = False

    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
        
    while not is_game_over:
        user_score = caluculated_score(user_cards)
        computer_score = caluculated_score(computer_cards)
        print(f"  your cards : {user_cards}, current score: {user_score}\n")
        print(f"  dealer cards : {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over =True
        else:
            user_should_deal = input("type y to get another card type n to pass:")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = caluculated_score(computer_cards)
   
   
    print(f"   Your final hand: {user_cards}, final score: {user_score}")
    print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))     

    
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  print("-----------------------Clear--------------------------------\n" * 2)
  play_game()
  
  
  
