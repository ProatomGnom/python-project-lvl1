from random import randint, choice
RULE = "What number is missing in the progression?"


def create_question_and_answer():
    start_number = randint(0, 10)
    step = randint(1, 10)
    progression = []
    for num in range(10):
        next_number = start_number + step * num
        progression.append(str(next_number))
    random_index = choice(range(len(progression) - 1))
    answer = (progression[random_index])
    progression[random_index] = '..'
    question = " ".join(progression)
    return question, answer
