print("welcome to the bidding app, you are bidding for Kohinoor Diamond...! \nBig starting price is $100")


should_stop = True
data = []


while should_stop :
    
    name = str(input("What is your name .? : "))
    amount = float(input("What is your bid amount .? $"))
    anyone = str(input('Is there any one in the room .? Type Yes or No : ').lower())

    new_bidder = {}
    new_bidder['name'] = name
    new_bidder['amount'] = amount
    data.append(new_bidder)
    
    if anyone == 'no' :
        should_stop = False

high_amount = 0
high_index = None

for item in data :
    if high_amount < float(item['amount']) :
        high_amount = item['amount']
        high_index = item

print(f"{high_index['name']} has won the bid, with amount of {high_index['amount']}")
print('Bidding is closed now.\nThank you for participating')
