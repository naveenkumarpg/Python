

# data types



# int - represents integer
    # can convert any other data into int by int()
my_int = '10';
to_int = int(my_int);
print(to_int); # 10
    

# float - represents number with decimal values
    # can convert different data type into float by float()
my_fl = 10;
to_float = float(my_fl);
print(to_float) #10.0
# float could give you the big decimals always
print(100/3); #33.333333333333336
# if you want to to shrink the number to specific digits, you can do that by round()

print(round(100/3)) #33 - will remove the decimals if <5, +1 if >6
print(round(100/3,1)) #33.3 (1 - is number of digits to be considered)
print(round(100/3,2)) #33.33 (2 - is number of digits to be considered)
# Flow division

print("//")
print(100//3); #33 - number will be rounded automatically
print(8//5); #1 - it suppose to be 1.6 as we used // will be rounded to 1


# string - represents string
    # can convert any other data type into string by str()
my_str = 10;
to_string = str(my_str);
print(to_string)


# boolean - represents boolean
    # can convert any other data type into boolean by bool()
    # True and False  (capitals not like js)

my_number = 1;
is_true = bool(my_number);
print(is_true); # True


# data types can be checked using type()
my_number_one = 1;
print(type(my_number_one)) #<class 'int'>
