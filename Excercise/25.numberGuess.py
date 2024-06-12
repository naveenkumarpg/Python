import random

total_count = 5
guessed = True
random_number = 0
print('''
  ___  __  __  ____  ___  ___    ____  _   _  ____    _  _  __  __  __  __  ____  ____  ____ 
 / __)(  )(  )( ___)/ __)/ __)  (_  _)( )_( )( ___)  ( \( )(  )(  )(  \/  )(  _ \( ___)(  _ \/
( (_-. )(__)(  )__) \__ \\__ \    )(   ) _ (  )__)    )  (  )(__)(  )    (  ) _ < )__)  )   /
 \___/(______)(____)(___/(___/   (__) (_) (_)(____)  (_)\_)(______)(_/\/\_)(____/(____)(_)\_)
''')
level = input('What level do you want to play .?\nPlease type "Easy" and "Hard" : ')
print("Guess the number from 1 to 100")

if (level.lower() != 'hard' ) :
    total_count = 10
    random_number = random.randint(1,100)
else :
    random_number = random.randint(1,50)



while guessed == True :
    print('----------------------------------------------------------------')
    print(f'You have {total_count} attempts to guess the number')
    guess = int(input('Please guess the number : '))
    total_count = total_count - 1

    if(guess < random_number) :
        print('Bigger than this')
    elif(guess == random_number):
        guessed = False
        print(f'*****************************\nYou have guessed the number : {random_number} :)\n*****************************')

    else :
        print('Smaller than this')

    if(total_count < 1) :
        print("You have lost the game, as you dont have any attempts left :(")
        guessed = False

