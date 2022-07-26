from random import randint, choice
RULE = "What number is missing in the progression?"


def create_question_and_answer():
    number = randint(0, 10)
    step = randint(1, 10)
    progression = []
    for num in range(10):
        next_number = number + step * num
        progression.append(str(next_number))
    index = choice(range(len(progression) - 1))
    answer = int(progression[index])
    progression[index] = '..'
    question = " ".join(progression)
    return question, str(answer)
