
def intimate_price(item, MENU) :
    cost = MENU[item.lower()]['cost']
    print(f'Excellent choice, you choose {item}, it will cost you £{cost}')
    check_quantity(item)

def collect_money(item) :
    quarters = int(input('How many in Quarter\'s : '))
    tens = int(input('How many in tens : '))
    once = int(input("How many in pence : "))
    total = ((quarters*25) + (tens*10) + once)/100
    cost = MENU[item.lower()]['cost']

    if(cost <= total) :
        remaining = (total - cost)
        rem_content = ''
        if(remaining > 0) :
            rem_content = f', here is your change of £{remaining}'
        
        print('Thanks for the payment'+ rem_content + f'\nENJOY YOUR {item.upper()}')


    else :
        print(f'You dont have enough amount for the {item}, returning all the amount')

def print_report() :
    print('\n\n\n~ ~ ~ ~ ~ ~ ~')
    print(f'Water  : {resources["water"]}')
    print(f'Milk   : {resources["milk"]}')
    print(f'Coffee : {resources['coffee']}')
    print('~ ~ ~ ~ ~ ~ ~\n\n\n')

def load_inventory() : 
    resources['water'] = int(input("How much Water do you want to add .? : "))
    resources['milk'] = int(input("How much milk do you want to add .? : "))
    resources['coffee'] = int(input("How much Coffee do you want to add .? : "))

def check_quantity(item) :
    global machine_working

    ingredients = MENU[item.lower()]['ingredients']

    need_water = ingredients["water"]
    need_milk = ingredients["milk"]
    need_coffee = ingredients["coffee"]

    have_water = resources["water"]
    have_milk = resources["milk"]
    have_coffee = resources["coffee"]

    enough_water = have_water > need_water
    enough_milk = have_milk > need_milk
    enough_coffee = have_coffee > need_coffee

    if( enough_milk and enough_coffee and enough_water ) :
        collect_money(item)
        resources["water"] = resources["water"] - need_water
        resources["milk"] = resources["milk"] - need_milk
        resources["coffee"] = resources["coffee"] - need_coffee
    else :
        print(f'Can\'t prepare the {item}, Stocks are not available')

