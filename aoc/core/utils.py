def line2ints(l):
    return list(map(int, l.split()))


def clamp(x, lo=0, hi=1):
    return max(min(x, hi), lo)
