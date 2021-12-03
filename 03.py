#!/usr/bin/env python3

def gamma_bit(bits):
    return '1' if bits.count('1') >= len(bits) / 2 else '0'

def epsilon_bit(bits):
    return '1' if bits.count('1') <= len(bits) / 2 else '0'

def read_data_file(fn):
    r = []
    with open(fn) as data:
        for line in data:
            r.append(line.strip())
    return r

def transform(x):
    return list(zip(*x))

def test():
    assert '1' == gamma_bit(list('011110011100'))
    assert '0' == gamma_bit(list('010001010101'))
    assert '1' == gamma_bit(list('111111110000'))
    assert '1' == gamma_bit(list('011101100011'))
    assert '0' == gamma_bit(list('000111100100'))

    assert '0' == epsilon_bit(list('011110011100'))
    assert '1' == epsilon_bit(list('010001010101'))
    assert '0' == epsilon_bit(list('111111110000'))
    assert '0' == epsilon_bit(list('011101100011'))
    assert '1' == epsilon_bit(list('000111100100'))


    assert transform(read_data_file("03-example.dat")) == [
            tuple('011110011100'),
            tuple('010001010101'),
            tuple('111111110000'),
            tuple('011101100011'),
            tuple('000111100100'),
            ]

fn = "03.dat"
test()
report = read_data_file(fn)
t = transform(report)
gamma_rate = ''
epsilon_rate = ''
for x in t:
    gamma_rate += gamma_bit(x)
    epsilon_rate += epsilon_bit(x)
answer = int(gamma_rate, 2) * int(epsilon_rate, 2)

prefix = ""
if "example" in fn:
    prefix = "EXAMPLE DATA!!!! "

print(f"{prefix}{answer= }")
