#!/usr/bin/env python3


from collections import defaultdict
import heapq


def read_data_file(fn):
    with open(fn) as data:
        grid = [[int(c) for c in l.strip()] for l in data]
    return grid


def increment(x: int) -> int:
    y = x + 1
    if y > 9: y = 1
    return y


def get_risk(grid: list[list[int]], row: int, col: int, size_r: int, size_c: int) -> int:
    if row < size_r and col < size_c:
        return grid[row][col]
    original_row = row % size_r
    original_col = col % size_c
    v = grid[original_row][original_col]
    for _ in range(original_col, col - size_c + 1):
        v = increment(v)
    if row < size_r: return v
    for _ in range(original_row, row - size_r + 1):
        v = increment(v)
    return v


def solve(grid: list[list[int]]):
    size_r = len(grid)
    size_c = len(grid[0])
    virtual_max_row = size_r * 5 - 1
    virtual_max_col = size_c * 5 - 1
    visited = set()
    total_risk = defaultdict(int)

    # priority queue; (weigth, row, col)
    # First cell has no risk.
    pq = [(0, 0, 0)]
    heapq.heapify(pq)

    while len(pq) > 0:
        risk, row, col = heapq.heappop(pq)
        if (row, col) in visited:
            continue
        visited.add((row, col))
        total_risk[(row, col)] = risk
        if row == virtual_max_row and col == virtual_max_col: break # Reached the end point.
        for row_move, col_move in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            next_row = row + row_move
            next_col = col + col_move
            if next_row > virtual_max_row or next_row < 0 or next_col > virtual_max_col or next_col < 0:
                continue
            heapq.heappush(pq, (risk + get_risk(grid, next_row, next_col, size_r, size_c), next_row, next_col))
    return total_risk[(virtual_max_row, virtual_max_col)]


if __name__ == "__main__":
    answer = solve(read_data_file("input"))
    print(f"{answer = }")
