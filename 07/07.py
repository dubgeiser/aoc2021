#!/usr/bin/env python3

def read_data_file(fn):
    return [int(i) for i in open(fn).readline().strip().split(",")]


positions = read_data_file("input")
pos_min = min(positions)
pos_max = max(positions) + 1
possible_positions = [i for i in range(pos_min, pos_max)]
fuel_usage = []
fuel_max_usage = pos_max * len(positions)

for pp in possible_positions:
    fuel = 0
    for p in positions:
        fuel += abs(p - pp)
    if fuel < fuel_max_usage:
        fuel_usage.append(fuel)
        fuel_max_usage = fuel

print(min(fuel_usage))
