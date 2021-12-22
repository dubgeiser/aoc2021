#!/usr/bin/env python3


def read_data_file(fn):
    letters = set()
    insmap = dict()
    template = ""
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
                    template = template + l
                    letters.add(l)
    return template, insmap, letters


def nextpairs(p: str, insmap: dict) -> list:
    return [f"{p[0]}{insmap[p]}", f"{insmap[p]}{p[1]}"]


def mkpairs(tpl: str) -> list:
    return [tpl[i - 1] + tpl[i] for i in range(1, len(tpl))]


def countpairs(pfreq, insmap):
    temp_pfreq = dict()
    for p in pfreq.keys():
        n = pfreq.get(p)
        p1, p2 = nextpairs(p, insmap)
        temp_pfreq[p1] = temp_pfreq.get(p1, 0) + n
        temp_pfreq[p2] = temp_pfreq.get(p2, 0) + n
    return temp_pfreq.copy()


def solve(data, steps=40):
    tpl, insmap, letters = data
    freq = dict.fromkeys(letters, 0)
    pfreq = dict()
    for p in mkpairs(tpl):
        pfreq[p] = pfreq.get(p, 0) + 1

    for n in range(0, steps):
        pfreq = countpairs(pfreq, insmap)

    for p in pfreq.keys():
        freq[p[0]] += pfreq[p]

    # Last char of template will always be present in the end result
    freq[tpl[-1]] = freq[tpl[-1]] + 1

    return max(freq.values()) - min(freq.values())

if __name__ == "__main__":
    answer = solve(read_data_file("input"))
    print(f"{answer = }")
