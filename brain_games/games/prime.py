from random import randint
RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    devider = 2
    while number % devider != 0:
        devider += 1
    return devider == number


def create_question_and_answer():
    question = randint(1, 1000)
    if is_prime(question):
        answer = 'yes'
    else:
        answer = 'no'
    return question, answer
