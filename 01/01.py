#!/usr/bin/env python3

answer = 0
prev = -1
win = []

with open("input") as data:
    for line in data:
        depth = int(line)
        if prev >= 0 and depth > prev:
            answer += 1
        prev = depth

print(f"{answer=}")
