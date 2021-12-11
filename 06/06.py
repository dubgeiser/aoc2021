#!/usr/bin/env python3

def read_data_file(fn):
    return [int(i) for i in open(fn).readline().strip().split(",")]


data = read_data_file("input")

total = len(data)
start = 1
end = 80

while start <= end:
    for i, each in enumerate(data.copy()):
        if each == 0:
            data[i] = 6
            data.append(8)
        else:
            data[i] -= 1
    start += 1

print(len(data))
