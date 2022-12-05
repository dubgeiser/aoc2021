#!/usr/bin/env python3


from collections import defaultdict
import heapq


def read_data_file(fn):
    with open(fn) as data:
        grid = [[int(c) for c in l.strip()] for l in data]
    return grid


def solve(grid: list[list[int]]):
    max_row = len(grid) - 1
    max_col = len(grid[0]) - 1
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
        if row == max_row and col == max_col: break # Reached the end point.
        for row_move, col_move in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            next_row = row + row_move
            next_col = col + col_move
            if next_row > max_row or next_row < 0 or next_col > max_col or next_col < 0:
                continue
            heapq.heappush(pq, (risk + grid[next_row][next_col], next_row, next_col))
    return total_risk[(max_row, max_col)]


if __name__ == "__main__":
    answer = solve(read_data_file("input"))
    print(f"{answer = }")
