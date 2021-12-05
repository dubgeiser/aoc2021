#!/usr/bin/env python3

import re


class Line:
    def __init__(self, x1:int, y1:int, x2:int, y2:int):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def is_horizontal(self):
        return self.y1 == self.y2

    def is_vertical(self):
        return self.x1 == self.x2

    def is_diagonal(self):
        return self.x1 != self.x2 and self.y1 != self.y2

    def __str__(self) -> str:
        return f"({self.x1}, {self.y1}) -> ({self.x2}, {self.y2}))"


class Grid:
    def __init__(self, x1, y1, x2, y2) -> None:
        self.grid = [ [0 for _ in range(x1, x2 + 1)] for _ in range(y1, y2 + 1)]

    def mark_line(self, line: Line):
        if line.is_horizontal():
            y = line.y1
            x1, x2 = min(line.x1, line.x2), max(line.x1, line.x2)
            for x in range(x1, x2 + 1):
                self.mark(x, y)
        elif line.is_vertical():
            x = line.x1
            y1, y2 = min(line.y1, line.y2), max(line.y1, line.y2)
            for y in range(y1, y2 + 1):
                self.mark(x, y)
        elif line.is_diagonal():
            stepx = -1 if line.x1 > line.x2 else 1
            addx = 1 if line.x2 > line.x1 else -1
            stepy = -1 if line.y1 > line.y2 else 1
            addy = 1 if line.y2 > line.y1 else -1
            xs = range(line.x1, line.x2 + addx, stepx)
            ys = range(line.y1, line.y2 + addy, stepy)
            points = zip(xs, ys)
            for x, y in points:
                self.mark(x, y)
        else:
            assert False, "BOOBOO SHOULD NOT BE REACHED!"

    def mark(self, x, y):
        self.grid[x][y] += 1

    def get_overlap_count(self):
        counter = 0
        for x in self.grid:
            for y in x:
                if y > 1:
                    counter += 1
        return counter

    def __str__(self) -> str:
        s = ''
        for x in self.grid:
            s += str(x)
            s += '\n'
        return s


r_line = re.compile('([0-9]+),([0-9]+) -> ([0-9]+),([0-9]+)')
def read_data_file(fn):
    def parse_row(line):
        x1, y1, x2, y2 = map(int, r_line.findall(line)[0])
        return Line(int(x1), int(y1), int(x2), int(y2))

    with open(fn) as data:
        lines = []
        minx = maxx = miny = maxy = 0
        for row in data:
            line = parse_row(row)
            lines.append(line)
            if line.x1 < minx:
                minx = line.x1
            if line.x2 < minx:
                minx = line.x2
            if line.y1 < miny:
                miny = line.y1
            if line.y2 < miny:
                miny = line.y2
            if line.x1 > maxx:
                maxx = line.x1
            if line.x2 > maxx:
                maxx = line.x2
            if line.y1 > maxy:
                maxy = line.y1
            if line.y2 > maxy:
                maxy = line.y2
        return lines, Grid(minx, miny, maxx, maxy)


fn = "05.dat"
vents, grid = read_data_file(fn)
for line in vents:
    grid.mark_line(line)
print(f"{grid.get_overlap_count()= }")
