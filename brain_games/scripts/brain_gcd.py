#!/usr/bin/env python3

from brain_games.games import gcd
from brain_games import consistency


def main():
    consistency.start(gcd)


if __name__ == "__main__":
    main()
