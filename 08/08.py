#!/usr/bin/env python3


def read_data_file(fn):
    dashboard = []
    with open(fn) as data:
        for row in data:
            parts = row.strip().split('|')
            dashboard.append((parts[0].strip(), parts[1].strip()))
    return dashboard


fn = '08.dat'
data = [i[1] for i in read_data_file(fn)]
unique_segment_lengths = [2, 3, 4, 7]
answer = 0

for display in data:
    digits = display.split()
    for n in digits:
        if len(n) in unique_segment_lengths:
            answer += 1

print(answer)
