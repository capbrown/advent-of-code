import numpy as np
from fractions import Fraction

input_file = 'inputs/day10.txt'
lineList = [line.rstrip('\n') for line in open(input_file)]
fixed_list = []
for string in lineList:
    fixed_list.append(string.replace('.', '0').replace('#', '1'))

arr = np.zeros((len(fixed_list), len(fixed_list[0])), dtype=int)

for i in range(len(fixed_list)):
    arr[i, :] = [int(c) for c in list(fixed_list[i])]

a = np.transpose(np.nonzero(arr))
all_asteroids = list(map(tuple, a))

max_asteroids = 0
for asteroid in all_asteroids:

    # print("asteroid =", asteroid)

    other_asteroids = all_asteroids[:]
    other_asteroids.remove(asteroid)
    visible_asteroids = []

    for current_asteroid in other_asteroids:

        # print("  current asteroid =", current_asteroid)

        angle_to_asteroid = tuple(np.subtract(current_asteroid, asteroid))

        # print("  relation to main =", angle_to_asteroid)

        # simplify angle 'fraction'
        if 0 in angle_to_asteroid:
            new_y = angle_to_asteroid[0]
            new_x = angle_to_asteroid[1]
        else:
            f = Fraction(angle_to_asteroid[0], angle_to_asteroid[1])
            new_y = np.abs(f.numerator) * angle_to_asteroid[0] / np.abs(angle_to_asteroid[0])
            new_x = np.abs(f.denominator) * angle_to_asteroid[1] / np.abs(angle_to_asteroid[1])

        # See if any multiples of this base fraction exist that would block visibility
        blocked = False
        current_check = tuple(np.add(asteroid, (new_y, new_x)))
        # print(current_check)
        while current_check != current_asteroid:
            if current_check in other_asteroids:
                blocked = True
            current_check = tuple(np.add(current_check, (new_y, new_x)))
            # print(current_check)

        if not blocked:
            visible_asteroids.append(current_asteroid)

    if len(visible_asteroids) > max_asteroids:
        max_asteroids = len(visible_asteroids)

print(max_asteroids)
