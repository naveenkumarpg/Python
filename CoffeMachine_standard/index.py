MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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

profit = 0
machine_working = True
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def intimate_price(item) :
    cost = MENU[item.lower()]['cost']
    print(f'Excellent choice, you choose {item}, it will cost you £{cost}')
    check_quantity(item)

def collect_money(item) :
    global profit
    quarters = int(input('How many in Quarter\'s : '))
    tens = int(input('How many in tens : '))
    once = int(input("How many in pence : "))
    total = ((quarters*25) + (tens*10) + once)/100
    cost = MENU[item.lower()]['cost']

    if(cost <= total) :
        remaining = round((total - cost), 2)
        rem_content = ''
        if(remaining > 0) :
            rem_content = f', here is your change of £{remaining}'
        
        print('Thanks for the payment'+ rem_content + f'\nENJOY YOUR {item.upper()}')
        profit = profit + cost


    else :
        print(f'You dont have enough amount for the {item}, returning all the amount')

def print_report() :
    print('\n\n\n~ ~ ~ ~ ~ ~ ~')
    print(f'Water  : {resources["water"]}')
    print(f'Milk   : {resources["milk"]}')
    print(f'Coffee : {resources['coffee']}')
    print(f'Profit : {profit}')
    print('~ ~ ~ ~ ~ ~ ~\n\n\n')

def load_inventory() : 
    resources['water'] = resources['water'] + int(input("How much Water do you want to add .? : "))
    resources['milk'] = resources['milk'] + int(input("How much milk do you want to add .? : "))
    resources['coffee'] = resources['coffee'] + int(input("How much Coffee do you want to add .? : "))

def check_quantity(item) :
    global machine_working

    ingredients = MENU[item.lower()]['ingredients']

    need_water = ingredients["water"]
    need_milk = ingredients["milk"]
    need_coffee = ingredients["coffee"]

    have_water = resources["water"]
    have_milk = resources["milk"]
    have_coffee = resources["coffee"]

    enough_water = need_water < have_water
    enough_milk = need_milk < have_milk
    enough_coffee = need_coffee < have_coffee

    if( enough_milk and enough_coffee and enough_water ) :
        collect_money(item)
        resources["water"] = resources["water"] - need_water
        resources["milk"] = resources["milk"] - need_milk
        resources["coffee"] = resources["coffee"] - need_coffee
    else :
        print(f'Can\'t prepare the {item}, Stocks are not available')



print('~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~')
print("~ ~ ~ ~ ~ Welcome to Bluehawk's Coffee shop ~ ~ ~ ~ ~ ~")
print('~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~')


def switch(task):
    global machine_working

    if(task == '1') :
        item = 'Espresso'
        intimate_price(item)
    elif(task == '2') :
        intimate_price('Latte')
    elif (task == '3') :
        intimate_price('Cappuccino')
    elif (task == 'off') :
        machine_working = False
    elif (task == 'report') :
        print_report()
    elif (task == 'load') :
        load_inventory()
    else :
        print("Task not matching")

while machine_working == True :
    task = input('What would you like to have today .? \n1. Espresso \n2. Latte \n3. Cappuccino\nType the number : ').lower()
    switch(task)
