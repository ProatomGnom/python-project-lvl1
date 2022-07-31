#!/usr/bin/env python3


from brain_games.games import even
from brain_games import consistency


def main():
    consistency.start(even)


if __name__ == "__main__":
    main()
