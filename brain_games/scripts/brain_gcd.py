#!/usr/bin/env python3

from brain_games.games import gcd
from brain_games import game_logic


def main():
    game_logic.start_game(gcd)


if __name__ == "__main__":
    main()
