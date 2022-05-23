#!/usr/bin/env python3

from random import randint
GAME_RULES_EVEN = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    return number % 2 == 0


def question_answer():
    random_number = randint(1, 100)
    if is_even(random_number):
        answer = 'yes'
    else:
        answer = 'no'
    return random_number, answer
