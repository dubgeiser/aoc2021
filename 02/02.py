#!/usr/bin/env python3

# AOC2021 - Day 2, part 1

def forward(d, pos): return (pos[0] + d, pos[1])
def down(d, pos): return (pos[0], pos[1] + d)
def up(d, pos): return (pos[0], pos[1] - d)
def answer(pos): return pos[0] * pos[1]


def test_movement():
    pos = (0, 0)

    pos = forward(5, pos)
    assert pos == (5, 0)

    pos = down(5, pos)
    assert pos == (5, 5)

    pos = forward(8, pos)
    assert pos == (13, 5)

    pos = up(3, pos)
    assert pos == (13, 2)

    pos = down(8, pos)
    assert pos == (13, 10)

    pos = forward(2, pos)
    assert pos == (15, 10)

    assert answer(pos) == 150


test_movement()

pos = (0, 0)
with open("input") as data:
    for movement in data:
        op, delta = movement.split()
        delta = int(delta)
        op = globals()[op]
        pos = op(delta, pos)

print(f'{answer(pos)=}')
