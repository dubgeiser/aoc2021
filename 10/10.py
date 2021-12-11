#!/usr/bin/env python3


def read_data_file(fn):
    with open(fn) as data:
        return [line.strip() for line in data]


def solve(data):
    opening = ['[', '{', '(', '<']
    closing = [']', '}', ')', '>']
    score = {
            ')' : 3,
            ']' : 57,
            '}' : 1197,
            '>' : 25137
            }
    stack = []
    answer = 0
    for line in data:
        for char in line:
            if char in opening:
                stack.append(char)
            elif char in closing and len(stack) > 0:
                prev_opening = stack.pop()
                if opening.index(prev_opening) != closing.index(char):
                    # Corrupted
                    expected = closing[opening.index(prev_opening)]
                    answer += score[char]
                    print(f"Corrupted, expected {expected}, but found {char}")
                    break # next line
            else:
                raise Exception(f"Unknown char [{char}]")
    return answer


if __name__ == "__main__":
    answer = solve(read_data_file("input"))
    print(f"{answer = }")
