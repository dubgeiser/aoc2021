#!/usr/bin/env python3

# map <Leader>t :wall!\|!./%<cr>

answer = 0

with open("01.dat") as data:
    try:
        a = int(next(data))
        b = int(next(data))
        c = int(next(data))
        while True:
            d = int(next(data))
            if b + c + d > a + b + c:
                answer += 1
            a, b, c = b, c, d
    except StopIteration:
        pass

print(f"{answer=}")
