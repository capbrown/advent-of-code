import numpy as np
import re


def compare(a, b):
    comparison = None
    if a > b:
        comparison = -1
    elif a < b:
        comparison = 1
    elif a == b:
        comparison = 0
    return comparison


lineList = [line.rstrip('\n') for line in open('inputs/day12.txt')]
positions = []
for string in lineList:
    positions.append(tuple([int(c) for c in re.sub('[xyz<=,>]', '', string).split(' ')]))
velocities = [(0, 0, 0) for p in positions]
print(positions)
print(velocities)
print()
time_steps = 1000
for t in range(time_steps):

    print("Time step =", t + 1)

    # apply gravity
    for moon in positions:
        other_moons = positions[:]
        other_moons.remove(moon)
        m = positions.index(moon)
        for o in other_moons:
            dx = compare(positions[m][0], o[0])
            dy = compare(positions[m][1], o[1])
            dz = compare(positions[m][2], o[2])
            new_vx = velocities[m][0] + dx
            new_vy = velocities[m][1] + dy
            new_vz = velocities[m][2] + dz
            velocities[m] = (new_vx, new_vy, new_vz)

    # apply velocity
    for moon in positions:
        m = positions.index(moon)
        v = velocities[m]
        positions[m] = (moon[0] + v[0], moon[1] + v[1], moon[2] + v[2])

    print(positions)
    print(velocities)
    print()

energy = 0
for moon in positions:
    m = positions.index(moon)
    energy += sum(tuple(map(lambda a: abs(a), moon))) * sum(tuple(map(lambda a: abs(a), velocities[m])))
print(energy)
