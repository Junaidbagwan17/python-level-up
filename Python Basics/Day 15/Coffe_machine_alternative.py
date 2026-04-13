from functools import total_ordering

from main import MENU, resources, coffee
money = 0

def get_report():
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    return (f"\n Water: {water}ml \n Milk: {milk}ml \n Coffee: {coffee}gm \n Money: ${money}\n ")

def check_resources(coffee):
    for i in MENU[coffee]['ingredients']:
        if MENU[coffee]['ingredients'][i] > resources[i]:
            print(f"Sorry there is not enough {i}.")
            return False
    return True

def process_coins():
    quarter = int(input("How many Quarters do you have:")) * 0.25
    nickel = int(input("How many Nickels do you have:")) * 0.05
    dime = int(input("How many Dimes do you have:"))*0.10
    penny = int(input("How many Penny do you have:"))*0.01
    total = quarter + nickel + dime + penny
    return total

def is_transaction_completed(total , coffee):
    global  money
    if total < MENU[coffee]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        change_returned = round(total - MENU[coffee]['cost'],2)
        print(f"Here is your ${change_returned} in change")
        money += MENU[coffee]['cost']
        return True

def make_coffee(coffee):
    for i in MENU[coffee]['ingredients']:
        resources[i] -= MENU[coffee]['ingredients'][i]
    print(f"Here is Your ☕ {coffee} Enjoy! ")


should_continue  = True
while should_continue:
    order = input("What would you like? (espresso/latte/cappuccino)")
    if order == "off":
        should_continue = False
    elif order == "report":
        print(get_report())
    elif order in MENU:
        if check_resources(order):
            total_amt = process_coins()
            if is_transaction_completed(total_amt, order):
                make_coffee(order)
