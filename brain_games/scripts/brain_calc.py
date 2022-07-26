#!/usr/bin/env python

from brain_games.games import calc
from brain_games import game_logic


def main():
    game_logic.start_game(calc)


if __name__ == "__main__":
    main()
