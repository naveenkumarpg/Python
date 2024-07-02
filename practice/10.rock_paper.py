import random
user_option = str(input('What are you choosing Rock, Paper and Scissor- Press 0 1 2 : '))
comp_option = str(random.randint(0,2))

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print('User has choice : ', user_option)

if user_option == '0' :
    print(rock)
elif user_option == '1' :
    print(paper)
else:
    print(scissor)
    
print('Computer Choice : ', comp_option)
if comp_option == '0' :
    print(rock)
elif comp_option == '1' :
    print(paper)
else:
    print(scissor)

if user_option == comp_option :
    print('Match is DRAW')
elif user_option == '0' and  comp_option == '1' :
    print('User Wins')
elif user_option == '1 'and comp_option == '2' :
    print("Computer Wins")
elif user_option == '2' and  comp_option == '0' :
    print('Computer Wins')
else :
    print('Something went wrong ..!')
