import aoc.core.utils as acu


def read_map(s):
    m = []
    for line in s:
        m.append([*line])
    H = len(m)
    W = len(m[0])
    current_direction = up
    current_position = (-1, -1)
    for i in range(W):
        for j in range(H):
            if m[j][i] == "^":
                current_position = (j, i)
    return m, H, W, current_position


def obstructed(m, pos):
    j, i = pos
    return m[j][i] == "#"


def up(pos):
    j, i = pos
    return (j - 1, i)


def down(pos):
    j, i = pos
    return (j + 1, i)


def right(pos):
    j, i = pos
    return (j, i + 1)


def left(pos):
    j, i = pos
    return (j, i - 1)


def oob(pos, h, w):
    j, i = pos
    return j < 0 or i < 0 or j >= h or i >= w


DIRECTION_ORDER = [up, right, down, left]


def solution1(s):
    m, H, W, current_position = read_map(s)
    visited = {current_position}
    while not oob(current_position, H, W):
        try:
            while obstructed(m, next_position := current_direction(current_position)):
                current_direction = DIRECTION_ORDER[
                    (DIRECTION_ORDER.index(current_direction) + 1)
                    % len(DIRECTION_ORDER)
                ]
                print("Switch direction to", current_direction.__name__)
            print(next_position)
            current_position = next_position
        except IndexError:
            break

        visited.add(current_position)
    else:
        return len(visited) - 1
    return len(visited)


def solution2(s):
    m, H, W, current_position = read_map(s)
