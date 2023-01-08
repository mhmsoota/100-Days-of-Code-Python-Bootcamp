from data import MENU, resources

# TODO 1: Prompt User


def prompt_user(coffee="ask"):
    '''
        One Input: Name of the Coffee. Gives a prompt, saying
        enjpoy your coffee to the user.
        No Input: Asks the user what coffee they would like to drink and return the name of the coffee
    '''
    if coffee == "ask":
        what_to_do = input(
            "What would you like? (espresso/latte/cappuccino) ").lower()
        return what_to_do
    else:
        print(f"Here's your {coffee}. Have a great day!")

# TODO 2: Turn off the coffee machine


def turn_me_off():
    '''Turns off the machine after a prompt'''
    print("Thank you for helping me serve you! Good Bye!!")

# TODO 3: Print Report


def print_report():
    '''Showns the details of inventory. No Input or Output'''
    print(
        f'Inventory Contains:\nWater: {resources["water"]}\nMilk: {resources["milk"]}\nCoffee: {resources["coffee"]}\nMoney: ${resources["money"]} ')

# TODO 4: check sufficient resources


def check_sufficient_resources(coffee_choice):
    '''
        Checks the inventory based on input of the choice of coffee. Compares them with
        stuff in inventory and return True or False based on whether the material is sufficient
    '''
    for key in MENU:
        if key == coffee_choice:
            water_needed = MENU[key]["ingredients"]["water"]
            coffee_needed = MENU[key]["ingredients"]["coffee"]
            milk_needed = MENU[key]["ingredients"]["milk"]
            break

    if water_needed > resources["water"]:
        print("Sorry, there is not enough Water")
        return False
    elif milk_needed > resources["milk"]:
        print("Sorry, there is not enough Milk")
        return False
    elif coffee_needed > resources["coffee"]:
        print("Sorry, there is not enough Coffee")
        return False
    else:
        return True


# TODO 5: Process Coins


def process_coins(coffee_choice):
    '''
        Based on the Input Choice of Coffee, the function will find out, the cost and ask the user for
        the money, if the amount is insufficient, the function returns False, and if the transaction is successful
        it returns True
    '''

    for key in MENU:
        if key == coffee_choice:
            cost_of_coffee = MENU[key]["cost"]
            print(f'{coffee_choice.capitalize()} will be ${cost_of_coffee}')
            break
    print("You will be expected to pay in Quarters($0.25), Dimes($0.10), Nickles($0.05) and Pennies($0.01).")
    quarters = int(input("How many Quarters? ")) * 0.25
    dimes = int(input("How many Dimes? ")) * 0.10
    nickles = int(input("How many Nickles? "))*0.05
    pennies = int(input("How many Pennies? ")) * 0.01
    total_money_user_gave = quarters + dimes + nickles + pennies

    if total_money_user_gave < cost_of_coffee:
        print(
            f"The amount is insufficient! Please find the refunded amount of ${total_money_user_gave}")
        return False
    else:
        print(
            f"Amount of ${total_money_user_gave} has been received.\tRefunded Amount: ${total_money_user_gave-cost_of_coffee}")
        resources["money"] += cost_of_coffee
        return True

# TODO 7: Make Coffee


def make_the_coffee(coffee_choice):
    ''' Makes the coffee based on the input Coffee_choice'''
    if check_sufficient_resources(coffee_choice) == True:
        if process_coins(coffee_choice) == True:
            for key in MENU:
                if key == coffee_choice:
                    resources["water"] -= MENU[key]["ingredients"]["water"]
                    resources["coffee"] -= MENU[key]["ingredients"]["coffee"]
                    resources["milk"] -= MENU[key]["ingredients"]["milk"]
                    break
            prompt_user(coffee_choice)


prompt = "something but not off yet"
while prompt != "off":
    prompt = prompt_user()
    if prompt in ["espresso", "latte", "cappuccino"]:
        make_the_coffee(prompt)
    elif prompt == "report":
        print_report()
    elif prompt == "off":
        turn_me_off()
    else:
        print("Wrong input! Let's Try this Again...")
