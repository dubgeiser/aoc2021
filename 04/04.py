#!/usr/bin/env python3

from typing import List, Tuple


# Diagonals don't count, but if they would; keep track of 2:
# in mark() where rows and cols are checked add a check for diagonals
# tally_diag(i, j):
#   if i == j -> inc(diag.a)
#   if I + j == GRID_SIZE -> inc(diag.b)
class Board:
    MARK = -1
    GRID_SIZE= 5

    def __init__(self) -> None:
        self.grid = []
        self.rows = {}
        self.cols = {}

    def add_row(self, row: str) -> None:
        self.grid.append([int(c) for c in row.split()])

    def mark(self, n: int):
        for i, row in enumerate(self.grid):
            for j, col in enumerate(row):
                if col == n:
                    self.grid[i][j] = self.MARK
                    self.tally_rows(i)
                    self.tally_cols(j)

    def tally_rows(self, i: int):
        if i in self.rows.keys(): self.rows[i] += 1
        else: self.rows[i] = 1

    def tally_cols(self, i: int):
        if i in self.cols.keys(): self.cols[i] += 1
        else: self.cols[i] = 1

    def has_bingo(self) -> bool:
        for k, v in self.rows.items():
            if v >= 5:return True
        for k, v in self.cols.items():
            if v >= 5: return True
        return False

    def get_unmarked_count(self):
        sum = 0
        for row in self.grid:
            for col in row:
                if col > self.MARK:
                    sum += col
        return sum

    def __str__(self) -> str:
        s = ""
        for row in self.grid:
            for col in row:
                if col == self.MARK:
                    s += " X "
                else:
                    s += "{:>2} ".format(col)
            s += "\n"
        return s


def read_data_file(fn: str) -> Tuple[List[int], List[Board]]:
    with open(fn) as data:
        draw = list(map(int, next(data).strip().split(",")))
        boards = []
        curr = None
        for line in data:
            line = line.strip()
            if line == '' or curr is None:
                curr = Board()
                boards.append(curr)
            else:
                curr.add_row(line)
    return (draw, boards)


def print_boards(boards: List[Board]) -> None:
    for b in boards:
        print(b)


def get_winning_board(boards: List[Board], draw: List[int]) -> Tuple[Board, int]:
    for d in draw:
        for b in boards:
            b.mark(d)
            if b.has_bingo():
                return (b, d)
    return (Board(), -1)


def main():
    fn = "04.dat"
    draw, boards = read_data_file(fn)
    print(draw)
    w = get_winning_board(boards, draw)
    if w[1] > -1:
        board, nr = w
        print(f"Winner with [{nr}]:")
        print(board)
        print(f'Score: {board.get_unmarked_count() * nr}')


if __name__ == '__main__':
    main()
