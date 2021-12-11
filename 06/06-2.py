#!/usr/bin/env python3


def read_data_file(fn):
    return [int(i) for i in open(fn).readline().strip().split(",")]


data = read_data_file("input")
total = len(data)
start = 1
end = 256

# fishcounter by timer
# index = timer
# value = number of fish
timers = [0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in data:
    timers[i] += 1

while start <= end:
    no_fish_delivering = timers[0]
    timers[0] = timers[1]
    timers[1] = timers[2]
    timers[2] = timers[3]
    timers[3] = timers[4]
    timers[4] = timers[5]
    timers[5] = timers[6]
    timers[6] = timers[7] + no_fish_delivering
    timers[7] = timers[8]
    timers[8] = no_fish_delivering
    start += 1

print(sum(timers))
