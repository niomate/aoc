from aoc.core.utils import line2ints


def is_safe(levels):
    # Safe if levels all decreasing or all increasing
    # and levels difference between 1 and 3
    diffs = [levels[i - 1] - levels[i] for i in range(1, len(levels))]

    inc = []
    dec = []
    diff_outlier = []

    for i, d in enumerate(diffs):
        if not (1 <= abs(d) <= 3):
            diff_outlier.append(i)

        if d < 0:
            dec.append(i)
        elif d > 0:
            inc.append(i)

    return (len(inc) < 1 or len(dec) < 1) and len(diff_outlier) == 0


def solution1(s):
    result = 0
    for line in s:
        if is_safe(line2ints(line)):
            result += 1

    print("Solution (Part 1): ", result)


def solution2(s):
    result = 0
    for line in s:
        line = line2ints(line)
        if is_safe(line):
            result += 1
            continue
        for i in range(len(line)):
            if is_safe(line[:i] + line[i + 1 :]):
                result += 1
                break

    print("Solution (Part 2): ", result)
