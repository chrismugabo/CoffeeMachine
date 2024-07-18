from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
coffee_continue=True
menu=Menu()
money_machine=MoneyMachine()
coffee_maker=CoffeeMaker()
while coffee_continue:
    choice=input(f"What would you like? ({menu.get_items()}) :").lower()
    #menu.find_drink(choice)
    if choice == "off":
        coffee_continue=False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink=menu.find_drink(choice)
        print(drink)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)


