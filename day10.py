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
max_i = None
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
            if angle_to_asteroid[0] == 0:
                new_y = angle_to_asteroid[0]
                new_x = angle_to_asteroid[1] // np.abs(angle_to_asteroid[1])
            else:
                new_y = angle_to_asteroid[0] // np.abs(angle_to_asteroid[0])
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
        max_i = asteroid

print('Part 1:', max_asteroids)

# part 2
alla = all_asteroids[:]
asteroid = max_i
removed = []
while True:
    other_asteroids = all_asteroids[:]
    other_asteroids.remove(asteroid)
    visible_asteroids = []

    for current_asteroid in other_asteroids:

        angle_to_asteroid = tuple(np.subtract(current_asteroid, asteroid))
        # simplify angle 'fraction'
        if 0 in angle_to_asteroid:
            if angle_to_asteroid[0] == 0:
                new_y = angle_to_asteroid[0]
                new_x = angle_to_asteroid[1] // np.abs(angle_to_asteroid[1])
                ang_sort = 90 if new_x > 0 else 270
            else:
                new_y = angle_to_asteroid[0] // np.abs(angle_to_asteroid[0])
                new_x = angle_to_asteroid[1]
                ang_sort = 0 if new_y < 0 else 180
        else:
            f = Fraction(angle_to_asteroid[0], angle_to_asteroid[1])
            new_y = np.abs(f.numerator) * angle_to_asteroid[0] / np.abs(angle_to_asteroid[0])
            new_x = np.abs(f.denominator) * angle_to_asteroid[1] / np.abs(angle_to_asteroid[1])
            if new_y > 0 and new_x > 0:
                ang_sort = 90 + np.abs(np.degrees((np.arctan((-1 * new_y / new_x)))))
            elif new_y > 0 and new_x < 0:
                ang_sort = 270 - np.degrees((np.arctan((-1 * new_y / new_x))))
            elif new_y < 0 and new_x > 0:
                ang_sort = 90 - np.degrees((np.arctan((-1 * new_y / new_x))))
            elif new_y < 0 and new_x < 0:
                ang_sort = 270 + np.abs(np.degrees((np.arctan((-1 * new_y / new_x)))))

        # See if any multiples of this base fraction exist that would block visibility
        blocked = False
        current_check = tuple(np.add(asteroid, (new_y, new_x)))

        while current_check != current_asteroid:
            if current_check in other_asteroids:
                blocked = True
            current_check = tuple(np.add(current_check, (new_y, new_x)))

        if not blocked:
            visible_asteroids.append((current_asteroid, ang_sort))

    # sort visible asteroids based on their angle relative to the vertical
    sort_a = sorted(visible_asteroids, key=lambda asa: asa[1])
    removed.extend([a[0] for a in sort_a])

    if len(removed) >= 200:
        break

print('Part 2:', removed[199][1] * 100 + removed[199][0])
