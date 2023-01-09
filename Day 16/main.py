from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

what_to_do = "go on"

CoffeeMenu = Menu()
GetCoffee = CoffeeMaker()
Finance = MoneyMachine()

while what_to_do != "off":
    what_to_do = input(f"What would you like to have today? {CoffeeMenu.get_items()}")
    if what_to_do == "report":
        GetCoffee.report()
        Finance.report()
    elif what_to_do == "off":
        print("Thankyou for helping me serve you")
    else:
        Selected_Coffee = CoffeeMenu.find_drink(what_to_do)
        if Selected_Coffee != None:
            if GetCoffee.is_resource_sufficient(Selected_Coffee):
                print(f"Please pay ${Selected_Coffee.cost}")
                if Finance.make_payment(Selected_Coffee.cost):
                    GetCoffee.make_coffee(Selected_Coffee)
