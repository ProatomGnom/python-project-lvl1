#!usr/bin/env python3
from random import randint
GAME_RULE = "What number is missing in the progression?"


def question_answer():
    difference = randint(1, 5)
    numbers = []
    for number in range(0, 31, difference):
        numbers.append(number)
    answer = numbers[difference]
    numbers[difference] = '..'
    question = str(numbers[0])
    for number in numbers[1:len(numbers)]:
        question = question + ', ' + str(number)

    return question, str(answer)
