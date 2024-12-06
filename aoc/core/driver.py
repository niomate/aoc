import sys
import importlib
from .challenge import get_challenge_path, fetch_challenge_input, create_new_challenge
import argparse


def get_solutions(day, year, part=None, input_file='input'):
    package = importlib.import_module(f"aoc.challenges.year{year}.day{day}.solution")
    solution1 = package.solution1
    solution2 = package.solution2

    fetch_challenge_input(day, year)
    with open(get_challenge_path(day, year) / input_file, "r") as f:
        input = f.readlines()

    if part is None or part == 1:
        print("#########  Solution Part 1")
        res = solution1(input)
        if res is not None:
            print("Result: ", res)
    if part is None or part == 2:
        print("#########  Solution Part 2")
        res = solution2(input)
        if res is not None:
            print("Result: ", res)


def main():
    action = sys.argv[1]
    year = int(sys.argv[2])
    day = int(sys.argv[3])
    input_file = "input"
    if len(sys.argv) == 5:
        input_file = sys.argv[4]
    if action == "run":
        get_solutions(day, year, input_file=input_file)
    if action == "create":
        create_new_challenge(day, year)
    if action == "submit":
        raise NotImplementedError("Submission is not implemented yet")
