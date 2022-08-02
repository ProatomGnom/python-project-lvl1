from random import randint
RULE = "Find the greatest common divisor of given numbers."


def gcd(random_number1, random_number2):
    if random_number2 == 0:
        return random_number1
    else:
        return gcd(random_number2, random_number1 % random_number2)


def create_question_and_answer():
    number1 = randint(1, 101)
    number2 = randint(1, 101)
    question = f"{number1} {number2}"
    answer = str(gcd(number1, number2))
    return question, answer
