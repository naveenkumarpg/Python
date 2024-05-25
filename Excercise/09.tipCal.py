bill = input("What is your total bill .? $")
tip = input("Do you want to tip the service ? $")
splitWith = input('Do you want to split the bill .? with how many .?')


totalBill = float(bill)+ float(tip);
split =totalBill/int(splitWith)

print(f'Your total bill is ${totalBill} and split amount is ${split}')
