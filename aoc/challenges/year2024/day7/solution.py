import aoc.core.utils as acu
from operator import add, mul
import itertools as it
import functools
import math

pow_memo = [
    1,
    10,
    100,
    1000,
    10000,
    100000,
    1000000,
    10000000,
    100000000,
    1000000000,
    10000000000,
    100000000000,
    1000000000000,
    10000000000000,
    100000000000000,
]
log_memo = {}

memo = {}


def solution1(s):
    result = 0

    for line in s:
        test_value, operands = line.strip().split(":")
        test_value = int(test_value)
        operands = acu.line2ints(operands)

        @functools.lru_cache(maxsize=None)
        def recurse(acc, idx):
            if idx == len(operands):
                return acc == test_value

            operand = operands[idx]

            t = acc + operand
            if t > test_value:
                return False
            elif t == test_value:
                return True
            elif recurse(t, idx + 1):
                return True

            t = acc * operand
            if t > test_value:
                return False
            elif t == test_value:
                return True
            elif recurse(t, idx + 1):
                return True

        if recurse(0, 0):
            result += test_value

    return result


def solution2(s):
    result = 0

    for line in s:
        test_value, operands = line.strip().split(":")
        test_value = int(test_value)
        operands = acu.line2ints(operands)

        @functools.lru_cache(maxsize=None)
        def recurse(acc, idx):
            if idx == len(operands):
                return acc == test_value

            operand = operands[idx]

            t = acc + operand
            if t > test_value:
                return False
            elif t == test_value:
                return True
            elif recurse(t, idx + 1):
                return True

            t = acc * operand
            if t > test_value:
                return False
            elif t == test_value:
                return True
            elif recurse(t, idx + 1):
                return True

            if operand not in log_memo:
                log_memo[operand] = pow_memo[math.ceil(math.log10(operand))]

            t = acc * log_memo[operand] + operand

            if t > test_value:
                return False
            elif t == test_value:
                return True
            elif recurse(t, idx + 1):
                return True

        if recurse(0, 0):
            result += test_value

    return result
