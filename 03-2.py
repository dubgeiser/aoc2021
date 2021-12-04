#!/usr/bin/env python3

def read_data_file(fn):
    r = []
    with open(fn) as data:
        for line in data:
            r.append(line.strip())
    return r

def transpose(x):
    return list(map(list, zip(*x)))

def most_common_bit(bits):
    return '1' if bits.count('1') >= bits.count('0') else '0'

def least_common_bit(bits):
    return '1' if bits.count('1') < bits.count('0') else '0'

def transpose_reduce(l, bit_decider):
    reduced = l.copy()
    t = transpose(reduced)
    i = 0
    while len(reduced) > 1:
        x = t[i]
        b = bit_decider(x)
        reduced = [n for n in reduced if n[i] == b]
        t = transpose(reduced)
        i += 1
    return reduced[0]


fn = "03.dat"
report = read_data_file(fn)
oxygen_generator_rating = int(transpose_reduce(report, most_common_bit), 2)
co2_scrubber_rating = int(transpose_reduce(report, least_common_bit), 2)
answer = oxygen_generator_rating * co2_scrubber_rating

prefix = ""
if "example" in fn:
    prefix = "EXAMPLE DATA!!!! "

print(f"{prefix}{answer= }")
