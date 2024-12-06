import aoc.core.utils as acu
import re

mulre = re.compile("mul\(([0-9]+),([0-9]+)\)")

domulre = re.compile("mul\(([0-9]+),([0-9]+)\)|do\(\)|don't\(\)")

do = "do()"
dont = "don't()"


def solution1(s):
    result = 0
    complete_input = "".join(s)
    for match in re.finditer(mulre, complete_input):
        result += int(match.group(1)) * int(match.group(2))
    return result


def solution2(s):
    result = 0
    complete_input = "".join(s)
    ignore_next = False
    for match in re.finditer(domulre, complete_input):
        if match.group(0) == do:
            ignore_next = False
        elif match.group(0) == dont:
            ignore_next = True
        elif not ignore_next:
            result += int(match.group(1)) * int(match.group(2))
    return result
