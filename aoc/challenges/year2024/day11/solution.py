import aoc.core.utils as acu
import math


def solution1(s):
    numbers = acu.line2ints(s[0])

    for i in range(25):
        new_numbers = []
        for n in numbers:
            s = str(n)
            l = len(s)
            if n == 0:
                new_numbers.append(1)
            elif len(s) % 2 == 0:
                new_numbers.append(int(s[: l // 2]))
                new_numbers.append(int(s[l // 2 :]))
            else:
                new_numbers.append(n * 2024)
        numbers = new_numbers

    return len(numbers)


def solution2(s):
    ...
    numbers = [0]

    for i in range(75):
        new_numbers = []
        for n in numbers:
            if n == 0:
                new_numbers.append(1)
            elif l := math.ceil(math.log10(n)) % 2:
                p = 10 ** (l // 2)
                new_numbers.extend(divmod(n, p))
            else:
                new_numbers.append(n * 2024)
        numbers = new_numbers

    print(numbers)

    return len(numbers)
