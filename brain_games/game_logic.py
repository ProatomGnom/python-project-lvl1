import prompt
NUMBER_OF_ROUNDS = 3


def start_game(game):
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have yuor name? ')
    print(f'Hello, {name}!')
    print(game.RULE)
    for _ in range(0, NUMBER_OF_ROUNDS):
        (expression, correct_answer) = game.create_question_and_answer()
        print(f"Question: {expression}")
        answer_user = prompt.string("Your answer: ")
        if answer_user == correct_answer:
            print("Correct!")
        else:
            print(f"'{answer_user}' is wrong answer ;(."
                  f" Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            break
    else:
        print(f"Congratulations, {name}!")
