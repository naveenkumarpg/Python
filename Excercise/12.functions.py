
# function definition
def my_function() :
    print('This is inside function')
    print('Function is ended')

# Function invocation
my_function()


#function with parameter
def my_one_function(name) :
    print(f'Hello {name}')
    print('How are you doing today .?')

my_one_function('naveen')


# Function with multiple parameters
def my_two_function(name, place) :
    print(f'Hello {name}')
    print(f'What is it like to be in {place}')
    
my_two_function('Naveen', 'London')


# function with named parameters
# advantage is even positions are changed, we can sill get the keys mapped properly

def my_three_function(place, name) :
    print(f'Hello {name}')
    
    if place :
        print(f'What is it like to be in {place} .?')
    
my_three_function(place='London', name='Naveen')



# functions with return types
def add(a,b) :
    return a + b

total = add(2,4)
print(total)
