#!/usr/bin/env python3


opening = ['[', '{', '(', '<']
closing = [']', '}', ')', '>']
scores = {
        ')' : 1,
        ']' : 2,
        '}' : 3,
        '>' : 4
        }


def read_data_file(fn):
    with open(fn) as data:
        return [line.strip() for line in data]


def solve_line(line: str) -> list[int]:
    stack = []
    iopened = []
    for i, char in enumerate(line):
        if char in opening:
            stack.append(char)
            iopened.append(i)
        elif char in closing and len(stack) > 0:
            prev_opening = stack.pop()
            if opening.index(prev_opening) != closing.index(char):
                # Corrupted line
                return []
            else:
                iopened.pop()
        else:
            raise Exception(f"Unknown char [{char}]")
    return iopened


def mkcompletion(line: str, iopened: list[int]) -> str:
    # Gotta go through backwards
    iopened.reverse()
    complete = ""
    for i in iopened:
        ochar = line[i]
        complete += closing[opening.index(ochar)]
    return complete


def calcscore(completion: str) -> int:
    score = 0
    for c in completion:
        score *= 5
        score += scores[c]
    return score


def solve(data):
    answer = 0
    score = []
    for line in data:
        iopened = solve_line(line)
        if len(iopened) > 0:
            completion = mkcompletion(line, iopened)
            s = calcscore(completion)
            score.append(s)
            # print(f"{line=} {completion=} {s=}")
    score.sort()
    answer = score[int(len(score) / 2)]
    return answer


if __name__ == "__main__":
    answer = solve(read_data_file("input"))
    print(f"{answer = }")
