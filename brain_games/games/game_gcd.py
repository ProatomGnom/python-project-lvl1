#!/usr/bin/env python3
from random import randint
GAME_RULE = "Find the greatest common divisor of given numbers."


def gcd_fun(random_number1, random_number2):
    if random_number2 == 0:
        return random_number1
    else:
        return gcd_fun(random_number2, random_number1 % random_number2)


def question_answer():
    number1 = randint(1, 101)
    number2 = randint(1, 101)
    question = str(number1) + " " + str(number2)
    answer = str(gcd_fun(number1, number2))
    return question, answer
