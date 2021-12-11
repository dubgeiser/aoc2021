#!/usr/bin/env python3


def read_data_file(fn):
    with open(fn) as data:
        return [[int(i) for i in list(row.strip())] for row in data]


def islowpoint(heightmap, i, j):
    height = heightmap[i][j]
    if height == 9:
        return False
    up = (i - 1, j)
    down = (i + 1, j)
    left = (i, j - 1)
    right = (i, j + 1)
    neighbours = [up, right, down, left]
    if i - 1 < IMIN: neighbours.remove(up)
    if i + 1 > IMAX: neighbours.remove(down)
    if j - 1 < IMIN: neighbours.remove(left)
    if j + 1 > JMAX: neighbours.remove(right)
    for n in neighbours:
        if heightmap[n[0]][n[1]] < height:
            return False
    return True


fn = '09.dat'
heightmap = read_data_file(fn)
IMIN = JMIN = 0
IMAX = len(heightmap) - 1
JMAX = len(heightmap[0]) - 1

answer = 0
lowpoints = []
for i, row in enumerate(heightmap):
    for j, height in enumerate(row):
        if islowpoint(heightmap, i, j):
            lowpoints.append(height)
risk_levels = [i + 1 for i in lowpoints]
answer = sum(risk_levels)
print(f"{answer= }")
