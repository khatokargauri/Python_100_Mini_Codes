from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
is_on = True
while is_on:
    choice = input(f"What would you like to order?\n{menu.get_items()}")
    if choice == "off":
        is_on = False
        break
    elif choice == "report":
        money_machine.report()
        coffee_maker.report()
    else:
        drink = menu.find_drink(choice)
        is_available = coffee_maker.is_resource_sufficient(drink)
        if is_available:
            transaction = money_machine.make_payment(drink.cost)
            if transaction:
                coffee_maker.make_coffee(drink)
