from coffee_maker import CoffeeMaker
from menu import Menu, MenuItem
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()

is_off = False
while not is_off:
    options = menu.get_items()
    drink = input(f"Would you like to drink? {options}: ")

    if drink == "off":
        is_off = True
    elif drink == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        coffee = menu.find_drink(drink)
        enough_resources = coffee_maker.is_resource_sufficient(coffee)
        enough_money = money_machine.make_payment(coffee.cost)
        if enough_resources  and  enough_money:
            coffee_maker.make_coffee(coffee)
