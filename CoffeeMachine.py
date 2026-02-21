MENU = {
    "espresso" : {
        "ingredients": {
            "water" : 50,
            "coffee" : 18,
            "milk" : 0
        },
        "cost" : 1.5
    },
    "latte" : {
        "ingredients": {
            "water" : 200,
            "milk" : 150,
            "coffee" : 24
        },
        "cost" : 2.5
    },
    "cappuccino" : {
        "ingredients": {
            "water" : 250,
            "milk" : 100,
            "coffee" : 24
        },
        "cost" : 3
    }
}
is_machine = "on"
resources  = {
    "money" : 0.00,
    "water" : 500,
    "milk" : 500,
    "coffee" : 500
}
def transaction(choice):
    print(f"Please enter ${MENU[choice]['cost']}")
    quarter_coins = int(input("How many quarter coins?"))
    dimes_coins = int(input("How many dimes coins?"))
    nickles_coins = int(input("How many nickles coins?"))
    pennies_coins = int(input("How many pennies coins?"))
    total = round(quarter_coins * 0.25 + dimes_coins * 0.10 + nickles_coins * 0.05 + pennies_coins * 0.01, 2)
    if total < MENU[choice]["cost"]:
        print("Sorry! That's not enough money. Money refunded")
    elif total == MENU[choice]["cost"]:
        resources["water"] -= MENU[choice]["ingredients"]["water"]
        resources["milk"] -= MENU[choice]["ingredients"]["milk"]
        resources["coffee"] -= MENU[choice]["ingredients"]["coffee"]
        resources["money"] += total
        print(f"Here is your {choice}.Enjoy!")
    else:
        if resources["money"] == 0.00:
            print("Please tend exact change! Money refunded")
        else:
            remaining = round(total - MENU[choice]["cost"], 2)
            if  resources["money"] < remaining:
                print("Please tend exact change! Money refunded")
            else:
                resources["money"] += MENU[choice]["cost"]
                resources["money"] -= remaining
                print(f"${total - MENU[choice]["cost"]} returned. Enjoy!")
def drink(choice):
    total = 0
    if choice == "report":
        print(f"Available Resources:\nWater: {resources['water']} ml\nMilk: {resources['milk']} ml\nCoffee: {resources['coffee']} g\nMoney: ${resources['money']}")
    elif resources["water"] >= MENU[choice]["ingredients"]["water"] and resources["milk"] >= MENU[choice]["ingredients"]["milk"] and resources["coffee"] >= MENU[choice]["ingredients"]["coffee"]:
        transaction(choice)
    else:
        print("There are not enough resources for this drink.")
while is_machine == "on":
    user_choice = input("What would you like? (espresso, latte, cappuccino)\n")
    drink(user_choice)
    is_machine  = input("Do you want to switch off the machine or do you want it keep it on?('off' / 'on')\n")









