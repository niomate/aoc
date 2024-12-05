def solution1(s):
    result1 = 0
    for line in s:
        # Safe if levels all decreasing or all increasing
        # and levels difference between 1 and 3
        levels = [int(x) for x in line.split()]
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

        if (len(inc) < 1 or len(dec) < 1) and len(diff_outlier) == 0:
            result1 += 1

    print("Solution (Part 1): ", result1)

def solution2(s):
    ...
