import sys
import importlib
from aoc.core.challenge import get_challenge_path, fetch_challenge_input, create_new_challenge


def get_solutions(day, year, part=None):
    package = importlib.import_module(f"aoc.challenges.year{year}.day{day}.solution")
    solution1 = package.solution1
    solution2 = package.solution2

    fetch_challenge_input(day, year)
    with open(get_challenge_path(day, year) / "input", "r") as f:
        input = f.readlines()

    if part is None or part == 1:
        print("#########  Solution Part 1")
        solution1(input)
    if part is None or part == 2:
        print("#########  Solution Part 2")
        solution2(input)


if __name__ == "__main__":
    action = sys.argv[1]
    year = int(sys.argv[2])
    day = int(sys.argv[3])
    if action == "run":
        get_solutions(day, year)
    if action == "create":
        create_new_challenge(day, year)
