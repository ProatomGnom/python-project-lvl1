#!usr/bin/env python3
from brain_games.games import prime
from brain_games import game_logic


def main():
    game_logic.start_game(prime)


if __name__ == "__main__":
    main()
