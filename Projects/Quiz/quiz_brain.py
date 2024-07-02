import random
from question_model import Question
from data import question_data

class Brain:
    def __init__(self):
        self.score = 0

    def generate_question(self):
        one = random.choice(question_data)
        return Question(one['text'], one['answer'])
    
    def validate_question(self, question, user_answer):
        if (question.answer).lower() == user_answer.lower() :
            return True
        else :
            return False
        
    def ask_question(self, question):
        user_answer = input(f'{question.text} is it true/false : ')
        validate_answer = self.validate_question(question, user_answer)

        if(validate_answer) :
            self.score = self.score + 1
            print(f"Congratulations you are correct, your score is {self.score}")
        else :
            print(f'Correct answer is {question.answer}')
            print('Your answer is wrong, apologies, you can\'t continue')
