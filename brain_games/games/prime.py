from random import randint
from math import sqrt
RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number <= 1:
        return False
    for divisor in range(2, int(sqrt(number)) + 1):
        if number % divisor == 0:
            return False
    return True


def create_question_and_answer():
    question = randint(1, 100)
    answer = 'yes' if is_prime(question) else 'no'
    return question, answer
