print("welcome to the Silent Auction Program!")
from art import logo
print(logo)
bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
    winner = ''
    highest_bid = 0
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"the winner is {winner} with highest bid ${highest_bid}")

while not bidding_finished:
    name = input("What is your Name: ")
    price = int(input("what is your bid: "))
    bids[name] = price
    should_continue = input("is there anohter bidder? Yes/Nn: ").lower()
    
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_continue == "yes":
        print("------" * 10 )