#!/usr/bin/env python

from brain_games.games import calc
from brain_games import consistency


def main():
    consistency.start(calc)


if __name__ == "__main__":
    main()
