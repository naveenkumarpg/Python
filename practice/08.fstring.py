# it is difficult to print multiple data types values you may need to convert them into the sting before concatenating them 
# f string allows to print multiple data types into simple string format


name = 'Naveen';
age = 20;
isMale = True

print('My name is' + name + 'My age is '+ age + 'and i am ' + isMale); #TypeError: can only concatenate str (not "int") to str
