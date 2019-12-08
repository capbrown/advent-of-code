import csv
from day5 import computer
from itertools import permutations


def amp_a(int_codes, phase=0, input_signal=0, n=0, init=True):
    return computer(int_codes, input_n=input_signal, phase=phase, n=n, init=init)


def amp_b(int_codes, phase=0, input_signal=0, n=0, init=True):
    return computer(int_codes, phase=phase, input_n=input_signal, n=n, init=init)


def amp_c(int_codes, phase=0, input_signal=0, n=0, init=True):
    return computer(int_codes, phase=phase, input_n=input_signal, n=n, init=init)


def amp_d(int_codes, phase=0, input_signal=0, n=0, init=True):
    return computer(int_codes, phase=phase, input_n=input_signal, n=n, init=init)


def amp_e(int_codes, phase=0, input_signal=0, n=0, init=True):
    return computer(int_codes, phase=phase, input_n=input_signal, n=n, init=init)


with open('inputs/day7.txt', 'r') as f:
    reader = csv.reader(f)
    my_dat = list(reader)[0]
    my_dat = [int(n) for n in my_dat]
max_thrust = 0

for perm in permutations([5, 6, 7, 8, 9]):
    phase_a, phase_b, phase_c, phase_d, phase_e = perm
    init = True
    list_a = list(my_dat)
    list_b = list(my_dat)
    list_c = list(my_dat)
    list_d = list(my_dat)
    list_e = list(my_dat)
    thrust = 0
    n_a = 0
    n_b = 0
    n_c = 0
    n_d = 0
    n_e = 0
    while True:
        a, list_a, n_a, _ = amp_a(list_a, phase_a, thrust, n_a, init)
        b, list_b, n_b, _ = amp_b(list_b, phase_b, a, n_b, init)
        c, list_c, n_c, _ = amp_c(list_c, phase_c, b, n_c, init)
        d, list_d, n_d, _ = amp_d(list_d, phase_d, c, n_d, init)
        thrust, list_e, n_e, done = amp_e(list_e, phase_e, d, n_e, init)
        if thrust > max_thrust:
            max_thrust = thrust
        init = False
        if done:
            break

print(max_thrust)
