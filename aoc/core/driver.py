import sys
import importlib
from .challenge import get_challenge_path, fetch_challenge_input, create_new_challenge
import argparse
import time

parser = argparse.ArgumentParser("aocdriver")
parser.add_subparsers()


def run_solutions(day, year, part=None, input_file="input"):
    package = importlib.import_module(f"aoc.challenges.year{year}.day{day}.solution")
    solution1 = package.solution1
    solution2 = package.solution2

    fetch_challenge_input(day, year)
    with open(get_challenge_path(day, year) / input_file, "r") as f:
        input = f.readlines()

    if part is None or part == 1:
        print("#########  Solution Part 1")
        dawn = time.time()
        res = solution1(input)
        dusk = time.time()
        if res is not None:
            print("Result: ", res)
        print("Total runtime: ", dusk - dawn, " seconds")
    if part is None or part == 2:
        print("#########  Solution Part 2")
        dawn = time.time()
        res = solution2(input)
        dusk = time.time()
        if res is not None:
            print("Result: ", res)
        print("Total runtime: ", dusk - dawn, " seconds")


def main():
    action = sys.argv[1]
    year = int(sys.argv[2])
    day = int(sys.argv[3])
    input_file = "input"
    if len(sys.argv) == 5:
        input_file = sys.argv[4]
    if action == "run":
        run_solutions(day, year, input_file=input_file)
    if action == "create":
        create_new_challenge(day, year)
    if action == "submit":
        raise NotImplementedError("Submission is not implemented yet")
