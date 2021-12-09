#!/usr/bin/env python3

from typing import List


def generate_all_intersect_lengths():
    """ List the lengts of the intersections of an unknown segment combination
    with a known segment combination.  Group by the only remaining segment
    combination.
    Was used to find de intersections to make in solve().

    Produces for instance for intersecting of 2, 3, 5 respectively:
    seglen=5 -> Length of unknown_seg='acdeg' intersect known_seg='cf' 1
    seglen=5 -> Length of unknown_seg='acdfg' intersect known_seg='cf' 2
    seglen=5 -> Length of unknown_seg='abdfg' intersect known_seg='cf' 1
    ...

    This way you can always find (at least here) 1 unique length, so you can
    use that to produce the corresponding number.
    """
    digits = ['abcefg', 'cf', 'acdeg', 'acdfg', 'bcdf', 'abdfg', 'abdefg', 'acf', 'abcdefg', 'abcdfg']
    known_digits =['cf', 'bcdf', 'acf', 'abcdefg']
    unknown_digits = [seg for seg in digits if seg not in known_digits]
    for seglen in (5, 6):
        for known_seg in known_digits:
            sknown_seg = set(known_seg)
            for unknown_seg in unknown_digits:
                if len(unknown_seg) != seglen: continue
                sunknown_seg = set(unknown_seg)
                print(f"{seglen=} -> Length of {unknown_seg=} intersect {known_seg=}", len(sunknown_seg & sknown_seg))


def read_data_file(fn):
    displays = []
    with open(fn) as data:
        for row in data:
            parts = row.strip().split('|')
            ins = ["".join(sorted(seg)) for seg in parts[0].strip().split()]
            outs = ["".join(sorted(seg)) for seg in parts[1].strip().split()]
            assert len(ins) == 10
            assert len(outs) == 4
            displays.append((ins, outs))
    return displays


def solve(ins: List, outs: List):
    # known by unique segment length
    one = [i for i in ins if len(i) == 2].pop()
    four = [i for i in ins if len(i) == 4].pop()
    seven = [i for i in ins if len(i) == 3].pop()
    eight = [i for i in ins if len(i) == 7].pop()

    # find 2, 3, 5 (segment length 5)
    two = [i for i in ins if len(i) == 5 and len(set(i) & set(four)) == 2].pop()
    three = [i for i in ins if len(i) == 5 and len(set(i) & set(one)) == 2].pop()
    five = [i for i in ins if len(i) == 5 and i != two and i != three].pop()

    # find 0, 6, 9 (segment length 6)
    six = [i for i in ins if len(i) == 6 and len(set(i) & set(one)) == 1].pop()
    nine = [i for i in ins if len(i) == 6 and len(set(i) & set(four)) == 4].pop()
    zero = [i for i in ins if len(i) == 6 and i != six and i != nine].pop()

    output2digit = {
            zero: 0,
            one: 1,
            two: 2,
            three: 3,
            four: 4,
            five: 5,
            six: 6,
            seven: 7,
            eight: 8,
            nine: 9
            }
    solution = [-1, -1, -1, -1]
    for i, out in enumerate(outs):
        solution[i] = output2digit[out]
    return int("".join([str(i) for i in solution]))


fn = '08.dat'
displays = read_data_file(fn)
answer = 0
for inputs, outputs in displays:
    answer += solve(inputs, outputs)

print(f"{answer= }")
