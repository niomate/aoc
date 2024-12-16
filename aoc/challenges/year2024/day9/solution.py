import aoc.core.utils as acu


def checksum(s):
    return sum(i * x for i, x in enumerate(s))


def swap(s, x, y):
    s[x], s[y] = s[y], s[x]


def solution1(s):
    s = [int(x) for x in s[0].strip()]
    exploded = []
    counter = 1
    for i, x in enumerate(s):
        value = 0
        if i % 2 == 0:
            value = counter
            counter += 1

        if x > 0:
            exploded.extend([value for _ in range(x)])

    front = 0
    back = len(exploded) - 1

    while True:
        while exploded[front] > 0:
            front += 1
        while exploded[back] == 0:
            back -= 1

        if front >= back:
            break

        exploded[front], exploded[back] = exploded[back], exploded[front]
    exploded = [max(x - 1, 0) for x in exploded]
    return checksum(exploded)


def solution2(s):
    s = [int(x) for x in s[0].strip()]
    exploded = []
    counter = 1

    def count_empty(l):
        return sum(1 for x in l if x == 0)

    for i, x in enumerate(s):
        value = 0

        if i % 2 == 0:
            value = counter
            counter += 1

        if x > 0:
            exploded.append([value for _ in range(x)])

    for current in range(counter - 1, 1, -1):
        file_id = next(
            i for i, x in reversed(list(enumerate(exploded))) if x[0] == current
        )
        try:
            slot_id = next(
                i
                for i, x in enumerate(exploded)
                if count_empty(x) >= len(exploded[file_id])
            )
        except StopIteration:
            continue

        if file_id <= slot_id:
            continue

        start_id = next(i for i, x in enumerate(exploded[slot_id]) if x == 0)

        for i in range(len(exploded[file_id])):
            exploded[file_id][i], exploded[slot_id][start_id + i] = (
                exploded[slot_id][start_id + i],
                exploded[file_id][i],
            )

    exploded = [max(y - 1, 0) for x in exploded for y in x]
    return checksum(exploded)
