import csv
from day5 import computer
from itertools import permutations


def amp_a(int_codes, phase=0, input_signal=0):
    return computer(int_codes, input_n=input_signal, phase=phase)


def amp_b(int_codes, phase=0, input_signal=0):
    return computer(int_codes, phase=phase, input_n=input_signal)


def amp_c(int_codes, phase=0, input_signal=0):
    return computer(int_codes, phase=phase, input_n=input_signal)


def amp_d(int_codes, phase=0, input_signal=0):
    return computer(int_codes, phase=phase, input_n=input_signal)


def amp_e(int_codes, phase=0, input_signal=0):
    return computer(int_codes, phase=phase, input_n=input_signal)


with open('inputs/day7.txt', 'r') as f:
    reader = csv.reader(f)
    my_dat = list(reader)[0]
    my_dat = [int(n) for n in my_dat]
max_thrust = 0

for perm in permutations([0, 1, 2, 3, 4]):
    phase_a, phase_b, phase_c, phase_d, phase_e = perm
    a = amp_a(list(my_dat), phase_a, 0)
    b = amp_b(list(my_dat), phase_b, a)
    c = amp_c(list(my_dat), phase_c, b)
    d = amp_d(list(my_dat), phase_d, c)
    thrust = amp_e(list(my_dat), phase_e, d)
    if thrust > max_thrust:
        max_thrust = thrust

print(max_thrust)
