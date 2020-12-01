import csv
from day5 import computer
from itertools import permutations

with open('inputs/day7.txt', 'r') as f:
    reader = csv.reader(f)
    my_dat = list(reader)[0]
    my_dat = [int(n) for n in my_dat]
max_thrust = 0

for perm in permutations([5, 6, 7, 8, 9]):
    phase_a, phase_b, phase_c, phase_d, phase_e = perm
    init = True
    list_a = list_b = list_c = list_d = list_e = list(my_dat)
    thrust = 0
    n_a = n_b = n_c = n_d = n_e = 0
    while True:
        a, list_a, n_a, _ = computer(list_a, phase=phase_a, input_n=thrust, n=n_a, init=init)
        b, list_b, n_b, _ = computer(list_b, phase=phase_b, input_n=a, n=n_b, init=init)
        c, list_c, n_c, _ = computer(list_c, phase=phase_c, input_n=b, n=n_c, init=init)
        d, list_d, n_d, _ = computer(list_d, phase=phase_d, input_n=c, n=n_d, init=init)
        thrust, list_e, n_e, done = computer(list_e, phase=phase_e, input_n=d, n=n_e, init=init)
        if thrust > max_thrust:
            max_thrust = thrust
        init = False
        if done:
            break

print(max_thrust)
