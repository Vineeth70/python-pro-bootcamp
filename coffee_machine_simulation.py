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

def report_format(resource,mon):
    water_level = resource["water"]
    milk_remaining = resource["milk"]
    coffee_remaining = resource["coffee"]
    return f"Water: {water_level}ml \nMilk: {milk_remaining}ml\nCoffee: {coffee_remaining}g\nMoney: ${mon}"

def machine_status(user):
    if user == "off":
        return False
    else:
        return True

def check_sufficiency(usr):
    for items in MENU[usr]["ingredients"]:
        if MENU[usr]["ingredients"][items] > resources[items]:
            print("Sorry there is not enough resources.")
            return False
    return True

def enter_money():
    print("Please insert coins.")
    quarters = float(input("how many quarters?:"))
    dimes = float(input("how many dimes?:"))
    nickles = float(input("how many nickles?"))
    pennies = float(input("how many pennies?:"))
    total_money = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
    return total_money

def check_money_sufficiency(u_money,u_choice):
    if u_money < MENU[u_choice]["cost"] :
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        return True

def coffee_machine():
    is_on = True
    machine_money = 0
    while is_on:
        user_choice = input("What would you like? (espresso/latte/cappuccino):").lower()
        check_status = machine_status(user_choice)
        if not check_status:
            is_on = False
        else:
            if user_choice == "report":
                print(report_format(resources, machine_money))
            elif user_choice in MENU:
                if check_sufficiency(user_choice):
                    user_money = enter_money()
                    if check_money_sufficiency(user_money, user_choice):
                        remain = user_money - MENU[user_choice]["cost"]
                        print(f"Here is ${remain} in change.")
                        print(f"Here is your {user_choice} ☕️. Enjoy!")
                        machine_money += MENU[user_choice]["cost"]
                        for item in MENU[user_choice]["ingredients"]:
                            resources[item] -= MENU[user_choice]["ingredients"][item]

coffee_machine()
