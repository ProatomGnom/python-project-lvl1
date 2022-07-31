#!usr/bin/env python3

from brain_games.games import prime
from brain_games import consistency


def main():
    consistency.start(prime)


if __name__ == "__main__":
    main()
