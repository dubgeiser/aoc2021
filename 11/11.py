#!/usr/bin/env python3


def read_data_file(fn):
    octolevels = []
    with open(fn) as data:
        for l in data:
            octolevels.append([int(c) for c in l.strip()])
    return octolevels


def print_octolevels(octolevels):
    for row in octolevels:
        print("".join([str(i) for i in row]))
    print()


IMAX = -1
JMAX = -1
def neighbours(i, j):
    n = []
    # horzon-/vertical
    if i > 0:
        n.append((i - 1, j))
    if i < IMAX:
        n.append((i + 1, j))
    if j > 0:
        n.append((i, j - 1))
    if j < JMAX:
        n.append((i, j + 1))
    # diagonals
    if i > 0 and j > 0:
        n.append((i - 1, j - 1))
    if i > 0 and j < JMAX:
        n.append((i - 1, j + 1))
    if i < IMAX and j > 0:
        n.append((i + 1, j - 1))
    if i < IMAX and j < JMAX:
        n.append((i + 1, j + 1))
    return n


def flash(octolevels, i, j, flashes: set[tuple[int, int]]):
    if octolevels[i][j] > 9 and (i, j) not in flashes:
        flashes.add((i, j))
        for k, l in neighbours(i, j):
            octolevels[k][l] += 1
            if (k, l) not in flashes:
                flash(octolevels, k, l, flashes)


def step(octolevels):
    flashes = set()
    # 1. Increase levels by 1
    for i, row in enumerate(octolevels):
        for j, _ in enumerate(row):
            octolevels[i][j] += 1
    # 2. Check for flashes.
    for i, row in enumerate(octolevels):
        for j, _ in enumerate(row):
            flash(octolevels, i, j, flashes)
    # 3. Reset flashed octolevels
    for i, row in enumerate(octolevels):
        for j, level in enumerate(row):
            if level > 9:
                octolevels[i][j] = 0
    return len(flashes)


def solve(octolevels, iterations=100):
    flashcount = 0
    for _ in range(0, iterations):
        flashcount += step(octolevels)
    return flashcount


def test_neighbours():
    n = neighbours(0, 0)
    n.sort()
    assert [(0,1), (1,0), (1,1)] == n, n
    n = neighbours(0, 4)
    n.sort()
    assert [(0,3), (0,5), (1,3), (1,4), (1,5)] == n, n
    n = neighbours(0, 9)
    n.sort()
    assert [(0, 8), (1,8), (1,9)] == n, n
    n = neighbours(9, 0)
    n.sort()
    assert [(8,0), (8,1), (9,1)] == n, n
    n = neighbours(9, 9)
    n.sort()
    assert [(8,8), (8,9), (9,8)] == n, n
    n = neighbours(4, 0)
    n.sort()
    assert [(3,0), (3,1), (4,1), (5,0), (5,1)] == n, n
    n = neighbours(4, 9)
    n.sort()
    assert [(3,8), (3,9), (4,8), (5,8), (5,9)] == n, n
    n = neighbours(4, 4)
    n.sort()
    assert [(3,3), (3,4), (3,5), (4,3), (4,5), (5,3), (5,4), (5,5)] == n, n


if __name__ == "__main__":
    octolevels = read_data_file("input")
    IMAX = len(octolevels) - 1
    JMAX = len(octolevels[0]) - 1
    test_neighbours()
    answer = solve(octolevels, 100)
    print_octolevels(octolevels)
    print(f"{answer = }")
