#!/usr/bin/env python3

# AOC2021 - Day 2, part 2

def forward(d, pos):
    x, y, aim = pos
    x += d
    y += aim * d
    return (x, y, aim)

def down(d, pos):
    x, y, aim = pos
    aim += d
    return (x, y, aim)

def up(d, pos):
    x, y, aim = pos
    aim -= d
    return (x, y, aim)

def answer(pos):
    return pos[0] * pos[1]


def test_movement():
    pos = (0, 0, 0)

    pos = forward(5, pos)
    assert pos == (5, 0, 0)

    pos = down(5, pos)
    assert pos == (5, 0, 5)

    pos = forward(8, pos)
    assert pos == (13, 40, 5)

    pos = up(3, pos)
    assert pos == (13, 40, 2)

    pos = down(8, pos)
    assert pos == (13, 40, 10)

    pos = forward(2, pos)
    assert pos == (15, 60, 10)

    assert answer(pos) == 900


test_movement()

pos = (0, 0, 0)
with open("input") as data:
    for movement in data:
        op, delta = movement.split()
        delta = int(delta)
        op = globals()[op]
        pos = op(delta, pos)

print(f"{answer(pos)= }")
