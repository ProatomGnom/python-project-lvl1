from random import randint
RULE = 'Answer "yes" if the number is even, ' \
       'otherwise answer "no".'


def create_question_and_answer():
    random_number = randint(1, 100)
    if random_number % 2 == 0:
        answer = 'yes'
    else:
        answer = 'no'
    return random_number, answer
