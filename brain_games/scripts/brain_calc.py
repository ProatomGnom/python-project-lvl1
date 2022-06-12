#!/usr/bin/env python

from brain_games.games import game_calc
from brain_games import game_logic


def main():
    game_logic.start_game(game_calc)


if __name__ == "__main__":
    main()
