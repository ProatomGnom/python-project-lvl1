#!/usr/bin/env python3


import prompt
from brain_games.games import game_even
NUMBER_CYCLES = 3


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have yuor name? ')
    welcome = (f"Hello, {name}!")
    return welcome, name


def printing_rules(rules):
    if rules == game_even.GAME_RULES_EVEN:
        return game_even.GAME_RULES_EVEN


def start_game(game):
    (welcome, name_user) = welcome_user()
    print(welcome)
    print(printing_rules(game.GAME_RULES_EVEN))
    for _ in range(0, NUMBER_CYCLES):
        (number_question, answer) = game.question_answer()
        print(f"Question: {number_question}")
        answer_user = prompt.string("Your answer: ")
        if answer_user == answer:
            print("Correct!")
        else:
            print(f"'{answer_user}' is wrong answer ;(."
                    f" Correct answer was '{answer}'.")
            print(f"Let's try again, {name_user}!")
            break
    else:
        print(f"Congratulions, {name_user}!")
