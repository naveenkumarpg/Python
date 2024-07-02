from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

bh_money_machine = MoneyMachine()
bh_menu = Menu()
bh_coffee_maker = CoffeeMaker()

print('~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~')
print("~ ~ ~ ~ ~ Welcome to Bluehawk's Coffee shop ~ ~ ~ ~ ~ ~")
print('~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~')

task = input(f'What would you like to have today {bh_menu.get_items()} .? :')
item_details = bh_menu.find_drink(task)

if item_details:
    can_make = bh_coffee_maker.is_resource_sufficient(item_details)

    if can_make:
        is_paid = bh_money_machine.make_payment(item_details.cost)

        if is_paid:
            bh_coffee_maker.make_coffee(item_details)

