import aoc.core.utils as acu
from collections import defaultdict
from itertools import permutations


def parse_input(s):
    dependencies = defaultdict(list)
    orders = []
    parse_dependencies = True
    for line in s:
        line = line.strip()
        if not line:
            parse_dependencies = False
            continue
        if parse_dependencies:
            l, r = line.split("|")
            dependencies[int(r)].append(int(l))
        else:
            orders.append([int(x) for x in line.split(",")])

    correctly_ordered = []
    for order in orders:
        if order := is_ordered_correctly(order, dependencies):
            correctly_ordered.append(order)
    return dependencies, orders, correctly_ordered


def is_ordered_correctly(order, dependencies):
    printed = []
    order = [*order]
    for page in order:
        for dependency in dependencies[page]:
            if dependency in order and dependency not in printed:
                break
        else:
            printed.append(page)

    if printed == order:
        return order
    return None


def solution1(s):
    _, _, correctly_ordered = parse_input(s)
    r = 0
    for o in correctly_ordered:
        r += o[len(o) // 2]
    return r


def solution2(s):
    dependencies, orders, correctly_ordered = parse_input(s)

    order_restored = []

    for order in orders:
        if order in correctly_ordered:
            continue

        new_order = order
        while True:
            expanded = []
            for page in new_order:
                expanded.append([x for x in dependencies[page] if x in order] + [page])
            collapsed = []
            for deps in expanded:
                collapsed.extend([d for d in deps if d not in collapsed])
            if new_order == collapsed:
                break
            new_order = collapsed

        order_restored.append(new_order)

    r = 0
    for o in order_restored:
        r += o[len(o) // 2]
    return r
