import aoc.core.utils as acu
from collections import defaultdict


def shared(s):
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
    for pages in orders:
        printed = []
        for page in pages:
            for dependency in dependencies[page]:
                if dependency in pages and dependency not in printed:
                    break
            else:
                printed.append(page)
        if printed == pages:
            correctly_ordered.append(pages)

    return dependencies, orders, correctly_ordered


def solution1(s):
    _, _, correctly_ordered = shared(s)
    r = 0
    for o in correctly_ordered:
        r += o[len(o) // 2]
    return r


def solution2(s):
    dependencies, orders, correctly_ordered = shared(s)

    print(dependencies)
    for pages in orders:
         if pages in correctly_ordered:
            continue
         new_order = []
         for page in pages:
             if all(x in new_order for x in dependencies if x in pages):
                 new_order.append(page)




