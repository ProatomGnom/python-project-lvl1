from random import randint
RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def create_question_and_answer():
    question = randint(1, 1000)
    number = 2
    for i in range(2, question):
        if question % i != 0:
            number += 1
    if number == question:
        answer = 'yes'
    else:
        answer = 'no'
    return question, answer
