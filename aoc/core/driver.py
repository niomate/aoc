import sys
import importlib
from .challenge import get_challenge_path, fetch_challenge_input, create_new_challenge
import argparse
import time
import datetime


def run_solutions(day, year, part=None, input_file="input"):
    print("Running solutions")
    try:
        package = importlib.import_module(
            f"aoc.challenges.year{year}.day{day}.solution"
        )
        solution1 = package.solution1
        solution2 = package.solution2
    except ModuleNotFoundError:
        print(f"You didn't do challenge {day}-{year} yet.")
        return

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


parser = argparse.ArgumentParser("aocdriver")

subparsers = parser.add_subparsers(dest="command")

parent_parser = argparse.ArgumentParser(add_help=False)
parent_parser.add_argument("-d", "--day", type=int)
parent_parser.add_argument("-y", "--year", type=int)

parser_run = subparsers.add_parser("run", parents=[parent_parser])
parser_run.add_argument("input_file", default="input", nargs="?")
parser_create = subparsers.add_parser("create", parents=[parent_parser])
parser_submit = subparsers.add_parser("submit", parents=[parent_parser])


def main():
    args = parser.parse_args()
    today = datetime.datetime.now()

    if args.day is None:
        args.day = today.day
    if args.year is None:
        args.year = today.year

    if args.command == "run":
        run_solutions(args.day, args.year, input_file=args.input_file)
    if args.command == "create":
        create_new_challenge(args.day, args.year)
    if args.command == "submit":
        raise NotImplementedError("Submission is not implemented yet")
