from main import MENU, resources, coffee

money = 0
def get_report(report):
    print(f'Water:{report["water"]} ml.')          
    print(f'Milk: {report["milk"]} ml.')
    print(f'Coffee:{report["coffee"]} gm.')
    print(f'Money: ${money}')

def get_drink(drink):
    print(MENU[drink])

def check_resources(drink_name, resources):
    requirnment = MENU[drink_name]["ingredients"]
    for i in requirnment:
        if requirnment[i] > resources[i]:
            print(f"Sorry there is not enough {i}")
            return False 
    return True

def take_money():
    
    quarter  = int(input("How many Quraters :")) * 0.25
    dimes = int(input("How many Dimes: ")) * 0.10
    nickels = int(input("How many nickels: "))*0.05
    pennies = int(input("How many Pennies"))* 0.01
    
    total_coins = quarter + dimes + nickels + pennies
    return total_coins

def make_coffee(drink_name, resources):
    get_ingrediants = MENU[drink_name]["ingredients"]
    for i in get_ingrediants:
        resources[i] -= get_ingrediants[i]
    
turn_off = False
while not turn_off:
    drink = input("What would you like? (espresso/latte/cappuccino):").lower()
    
    if drink == 'off':
        turn_off = True
    elif drink  == "report":
        get_report(resources)
    
    elif drink in MENU:
      has_resources = check_resources(drink_name=drink, resources=resources)
      if  has_resources:
        money_recived = take_money()
        drink_cost = MENU[drink]["cost"]
        if money_recived < drink_cost:
           print("Sorry that's not enough money. Money refunded.")
        else:
           change =  money_recived - drink_cost
           if change > 0:
               print(f"Here is your ${round(change, 2)}, in change.")
           money += drink_cost
           make_coffee(drink_name=drink, resources=resources)
           print(f"here is your {drink} ☕. Enjoy!")
           print(f" \n {coffee}")
            
               