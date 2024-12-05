import requests
import os
import pathlib as pl
import traceback
import shutil

AOC_SESSION_TOKEN = os.getenv("AOC_TOKEN")

here = pl.Path(__file__).parent
root = here.parents[1]
print(root)


def fetch_input(day, year):
    url = f"https://adventofcode.com/{year}/day/{day}/input"
    return requests.get(url, headers={"Cookie": f"session={AOC_SESSION_TOKEN}"}).text


def get_project_root() -> pl.Path:
    return root


def get_challenge_path(day, year) -> pl.Path:
    return root / "aoc" / "challenges" / f"year{year}" / f"day{day}"


def create_new_challenge(day, year):
    challenge_path = get_challenge_path(day, year)
    if not challenge_path.exists():
        challenge_path.mkdir()
    if not (challenge_path / "input").exists():
        with open(challenge_path / "input", "w+") as f:
            f.write(fetch_input(day, year))
    if not (challenge_path / "solution.py").exists():
        shutil.copy(here / "template.pyt", challenge_path / "solution.py")


def fetch_challenge_input(day, year):
    challenge_path = get_challenge_path(day, year)
    if not (challenge_path / "input").exists():
        with open(challenge_path / "input", "w+") as f:
            f.write(fetch_input(day, year))


def get_challenge_parameters(path=None):
    if path is None:
        state = traceback.extract_stack()
        path = pl.Path(stack[-2].filename)
    if not isinstance(path, pl.Path):
        path = pl.Path(path)
    try:
        day = int(path.parents[0].name)
        year = int(path.parents[1].name)
        print(day, year)
    except e:
        print()
    return day, year
