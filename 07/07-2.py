#!/usr/bin/env python3


def read_data_file(fn):
    return [int(i) for i in open(fn).readline().strip().split(",")]

fn = "07.dat"
positions = read_data_file(fn)
possible_positions = [i for i in range(min(positions), max(positions) + 1)]
answer = 0

for pp in possible_positions:
    fuel = 0
    for p in positions:
        d = abs(p - pp)

        # Programmed the loop first, but that was just way too expensive.
        # Found by staring at the numbers and trying things out until the
        # sequence function was correct for this small sample:
        # fuelconsumption   1, 3, 6, 10, 15, 21, 28, 36, 45, 55,... (n*n + n)/2
        # distance           2  3  4   5   6   7   8   9   10     n
        fuel += (d**2 + d) / 2

    if fuel < answer or answer == 0:
        answer = fuel

print(f"{int(answer)=}")
