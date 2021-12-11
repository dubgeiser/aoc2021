#!/usr/bin/env python3

class HeightMap:
    def __init__(self, heightmap : list[list[int]]) -> None:
        self.heightmap = heightmap
        self.IMIN = self.JMIN = 0
        self.IMAX = len(self.heightmap) - 1
        self.JMAX = len(self.heightmap[0]) - 1

    def neighbours(self, p : tuple[int, int]) -> list[tuple[int, int]]:
        i, j = p
        up = (i - 1, j)
        down = (i + 1, j)
        left = (i, j - 1)
        right = (i, j + 1)
        neighbours = [up, right, down, left]
        if i - 1 < self.IMIN: neighbours.remove(up)
        if i + 1 > self.IMAX: neighbours.remove(down)
        if j - 1 < self.IMIN: neighbours.remove(left)
        if j + 1 > self.JMAX: neighbours.remove(right)
        return neighbours

    def height(self, p : tuple[int, int]):
        i, j = p
        return self.heightmap[i][j]

    def islowpoint(self, p : tuple[int, int]):
        height = self.height(p)
        if height == 9:
            return False
        neighbours = self.neighbours(p)
        for pn in neighbours:
            if self.height(pn) < height:
                return False
        return True


    def basin(self, p : tuple[int, int], basin : set[tuple[int, int]] = None):
        """ Return the basin defined by a given lowpoint """
        if basin is None:
            basin = set()
        basin.add(p)
        height = self.height(p)
        neighbours = self.neighbours(p)
        for n in neighbours:
            height_n = self.height(n)
            if height_n > height and height_n < 9:
                self.basin(n, basin)
        return basin

    def all_basins(self) -> list[set[tuple[int, int]]]:
        basins = []
        for i, row in enumerate(self.heightmap):
            for j, _ in enumerate(row):
                p = (i, j)
                if self.islowpoint(p):
                    basins.append(self.basin(p))
        return basins

    def largest_basin_counts(self):
        lengths = [len(basin) for basin in self.all_basins()]
        lengths.sort()
        lengths.reverse()
        return lengths[0] * lengths[1] * lengths[2]


def read_data_file(fn):
    with open(fn) as data:
        return [[int(i) for i in list(row.strip())] for row in data]


if __name__  == "__main__":
    hm = HeightMap(read_data_file("input"))
    answer = hm.largest_basin_counts()
    print(f"{answer= }")
