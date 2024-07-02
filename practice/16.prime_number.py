# Write your code below this line 👇
def prime_checker(number) :
    not_prime = True
    for i in range(2,number) :
        if number % i == 0 :
             not_prime = False
    if(not_prime):
        print("Prime number")
    else :
        print("Not a prime number");

# Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input()) # Check this number
prime_checker(number=n)
