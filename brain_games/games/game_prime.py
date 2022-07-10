#!usr/bin/env python3
from random import randint
GAME_RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'

def question_answer():
    question = randint(1, 1000)
    numbers = []
    for number in range(1, question):
        if (question % number) == 0:
            numbers.append(number)

    if len(numbers) < 3:
        answer = 'yes'
        return question, answer
    else:
        answer = 'no'
        return question, answer
