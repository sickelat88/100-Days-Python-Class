
# TODO: 1. print report of coffee machine resources
# TODO: 2.  check resources sufficient
# TODO: 3. process coins
# TODO: 4. check transaction successful
# TODO: 5. make coffee

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0.00
power = True


def resource_check(coffee_selection):
    """Function to check remaining resources"""
    global check_pass
    for key in MENU[coffee_selection]['ingredients']:
        if resources[key] < MENU[coffee_selection]['ingredients'][key]:
            print(f"Sorry there is not enough {key}.")
            check_pass = False
            return


def intake_coins(coffee_selection):
    """Function to intake coins and check if enough or give back change"""
    global money
    global enough_money
    print("Please insert coins.")
    quarters = float(input("How many quarters?: "))
    dimes = float(input("How many dimes?: "))
    nickles = float(input("How many nickles? "))
    pennies = float(input("How many pennies? "))
    total = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
    change = total - MENU[coffee_selection]['cost']
    if total > MENU[coffee_selection]['cost']:
        print(f"Here is ${change:.2f} in change.")
        money = money + MENU[coffee_selection]['cost']
    elif total < MENU[coffee_selection]['cost']:
        print("Sorry that's not enough money.  Money refunded.")
        enough_money = False
    elif total == MENU[coffee_selection]['cost']:
        money = money + MENU[coffee_selection]['cost']


def make_drink(coffee_selection):
    """Function to deduce the resources required for drink from existing resources"""
    if coffee_selection == "espresso":
        resources['water'] = resources['water'] - MENU[coffee_selection]['ingredients']['water']
        resources['coffee'] = resources['coffee'] - MENU[coffee_selection]['ingredients']['coffee']
    else:
        resources['water'] = resources['water'] - MENU[coffee_selection]['ingredients']['water']
        resources['milk'] = resources['milk'] - MENU[coffee_selection]['ingredients']['milk']
        resources['coffee'] = resources['coffee'] - MENU[coffee_selection]['ingredients']['coffee']
    print(f"Here is your {coffee_selection} ☕. Enjoy!")


while power:
    check_pass = True
    enough_money = True
    user_input = input("What would you like? espresso, latte, or cappuccino? ")

    if user_input == "off":
        power = False
        break
    elif user_input == "report":
        print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${money}")
        continue
    elif user_input != "cappuccino" and user_input != "latte" and user_input != "espresso":
        print("Invalid input.")
        continue

    resource_check(user_input)
    if check_pass:
        intake_coins(user_input)
        if enough_money:
            make_drink(user_input)

