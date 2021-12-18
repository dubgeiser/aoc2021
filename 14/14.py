#!/usr/bin/env python3


def read_data_file(fn):
    letters = set()
    insmap = dict()
    template = []
    with open(fn) as data:
        for line in data:
            line = line.strip()
            if len(line) == 0:
                continue
            if ' -> ' in line:
                src, ins = line.split(' -> ')
                insmap[src] = ins
                for l in ins:
                    letters.add(l)
                for l in src:
                    letters.add(l)
            else:
                for l in line:
                    template.append(l)
                    letters.add(l)
    return template, insmap, letters


def step(template: list, insmap: dict):
    pairs = []
    while len(template) > 1:
        c1 = template.pop(0)
        c2 = template.pop(0)
        pairs.append(c1)
        pairs.append(c2)
        spairs = "".join([c1, c2])
        if spairs in insmap.keys():
            template.insert(0, pairs.pop())
            pairs.append(insmap[spairs])
    pairs.append(template.pop(0))
    return pairs


def solve(data, steps):
    template, insmap, letters = data
    for _ in range(steps):
        template = step(template, insmap)
    counts = []
    for l in letters:
        counts.append(template.count(l))
    return max(counts) - min(counts)


if __name__ == "__main__":
    answer = solve(read_data_file("input"), 10)
    print(f"{answer = }")
