import sys
from collections import Counter

def shared(s)
    left = []
    right = []
    for line in s:
        l, r = line.split()
        left.append(int(l))
        right.append(int(r))
    return left, right


def solution1(s):
    left, right = shared
    # Solution Part 1:
    print(
        "Solution (Part 1): ",
        sum(abs(x - y) for x, y in zip(sorted(left), sorted(right))),
    )


def solution2(s):
    left, right = shared
    nums = set(left)
    right = Counter(right)

    print("Solution (Part 2): ", sum(right[n] * n for n in nums))
