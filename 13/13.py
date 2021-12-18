#!/usr/bin/env python3

AXIS_X = 0
AXIS_Y = 1

def read_data_file(fn) -> tuple[list[tuple], list[tuple]]:
    """ Return tuple (dots, instructions):
        - dots: list: the positions (x, y) of all the dots
        - instructions: list: the instructions (axis, value) for folding
    """
    def parse_instruction(line) -> tuple[int, int]:
        instruction, value = line.split('=')
        i = AXIS_X if 'x' in instruction else AXIS_Y
        return (int(i), int(value))

    with open(fn) as data:
        dots = []
        instructions = []
        for line in data:
            line = line.strip()
            if len(line) == 0: continue
            if line.startswith('fold'):
                instructions.append(parse_instruction(line))
            else:
                x, y = map(int, line.split(','))
                dots.append((x, y))
    return (dots, instructions)


def mkmirror(pos: tuple[int,int],
             axis: int,
             i_fold: int) -> tuple[int, int]:
    if axis == AXIS_X:
        mirror = (i_fold - (pos[0] - i_fold), pos[1])
    else:
        mirror = (pos[0], i_fold - (pos[1] - i_fold))
    return mirror


def fold(dots: list[tuple[int, int]], instruction: tuple[int, int]) -> list[tuple[int, int]]:
    folded_dots = []
    axis, i_fold = instruction
    for pos in dots:
        if pos[axis] < i_fold:
            folded_dots.append(pos)
        else:
            mirror = mkmirror(pos, axis, i_fold)
            if mirror not in dots:
                folded_dots.append(mirror)
    return folded_dots


def solve(data: tuple):
    dots, instructions = data
    dots = fold(dots, instructions[0])
    return len(dots)


if __name__ == "__main__":
    data = read_data_file("input")
    answer = solve(data)
    print(f"{answer = }")
