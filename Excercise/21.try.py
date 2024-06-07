try:
    age = int(input('What is your age : '))
    income = int(input('What is your income  : '))
    risk = income/age;
    print(risk)
except ValueError:
    print("Please enter valid number")
except ZeroDivisionError:
    print("You cannot pass zero")
except Exception:
    print('Some Exception')
finally:
    print("The 'try except' is finished")
else:
    print('Program did not run')
