import aoc.core.utils as acu


def get_diagonal_str(s, i, j):
    res = ""
    for l in range(4):
        try:
            x = s[j + l][i + l]
        except IndexError:
            return res
        else:
            res += x
    return res


def get_other_diagonal_str(s, i, j):
    res = ""
    for l in range(4):
        try:
            x = s[j + l][i - l]
        except IndexError:
            return res
        else:
            res += x
    return res


def get_vertical_str(s, i, j):
    res = ""
    for l in range(4):
        try:
            x = s[j + l][i]
        except IndexError:
            return res
        else:
            res += x
    return res


def solution1(s):
    count = 0
    for j in range(len(s)):
        for i in range(len(s[j])):
            if s[j][i] not in "XS":
                continue
            diag = get_diagonal_str(s, i, j)
            other_diag = get_other_diagonal_str(s, i, j)
            vert = get_vertical_str(s, i, j)
            horiz = s[j][i : min(i + 4, len(s[j]))]

            if diag in ("XMAS", "SAMX"):
                count += 1
            if other_diag in ("XMAS", "SAMX"):
                count += 1
            if vert in ("XMAS", "SAMX"):
                count += 1
            if horiz in ("XMAS", "SAMX"):
                count += 1
    return count


def get3by3(s, i, j):
    r = ""
    for l in range(3):
        for k in range(3):
            try:
                x = s[j + l][i + k]
            except IndexError:
                return r
            else:
                r += x
    return r


def solution2(s):
    count = 0
    for j in range(len(s)):
        for i in range(len(s[j])):
            r = get3by3(s, i, j)
            if len(r) != 9:
                continue
            elif r[::2] in ("MSAMS", "MMASS", "SMASM", "SSAMM"):
                count += 1
    return count
