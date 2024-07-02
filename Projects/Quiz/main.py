from quiz_brain import Brain

is_on = True
print('~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~')
print("~ ~ ~ ~ ~Welcome to Bluehawk's Question bank~ ~ ~ ~ ~ ~")
print('~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~')


brain = Brain()

while is_on == True:
    question = brain.generate_question()
    brain.ask_question(question)
