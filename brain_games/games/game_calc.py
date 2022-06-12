#!/usr/bin/env python3


from random import randint, choice
GAME_RULE = "What is the result of the expression?"


def question_answer():
    random_number1 = str(randint(1, 101))
    random_number2 = str(randint(1, 101))
    operators = ["+", "-", "*"]
    random_operator = choice(operators)

    question = (random_number1 + " " + random_operator + " " + random_number2)
    if random_operator == "+":
        answer = int(random_number1) + int(random_number2)
    elif random_operator == "-":
        answer = int(random_number1) - int(random_number2)
    else:
        answer = int(random_number1) * int(random_number2)
    return question, str(answer)
