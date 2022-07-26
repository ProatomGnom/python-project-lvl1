from random import randint
RULE = 'Answer "yes" if the number is even, ' \
       'otherwise answer "no".'


def create_question_and_answer():
    question = randint(1, 100)
    if question % 2 == 0:
        answer = 'yes'
    else:
        answer = 'no'
    return question, answer
