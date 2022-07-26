from random import randint, choice
RULE = "What is the result of the expression?"


def create_question_and_answer():
    random_number1 = (randint(1, 101))
    random_number2 = (randint(1, 101))
    operators = ["+", "-", "*"]
    random_operator = choice(operators)
    question = (f"{random_number1} {random_operator} {random_number2}")
    if random_operator == "+":
        answer = (random_number1) + (random_number2)
    if random_operator == "-":
        answer = (random_number1) - (random_number2)
    if random_operator == "*":
        answer = (random_number1) * (random_number2)
    return question, str(answer)
