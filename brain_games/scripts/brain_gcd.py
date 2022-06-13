#!/usr/bin/env python3

from brain_games.games import game_gcd
from brain_games import game_logic


def main():
    game_logic.start_game(game_gcd)


if __name__ == "__main__":
    main()
