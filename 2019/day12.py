import re
import math


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
time_steps = 1000
for t in range(time_steps):
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

energy = 0
for moon in positions:
    m = positions.index(moon)
    tabs = lambda a: abs(a)
    energy += sum(tuple(map(tabs, moon))) * sum(tuple(map(tabs, velocities[m])))
print("Total energy =", energy)


# part 2
def find_n_steps(positions, velocities, i):

    init = positions[:]
    initV = velocities[:]
    n = 0
    while True:
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

        # check whether we have returned to the initial values
        n += 1
        original_positions = [a[i] for a in init]
        original_velocities = [a[i] for a in initV]
        current_positions = [a[i] for a in positions[:]]
        current_velocities = [a[i] for a in velocities[:]]
        if original_positions == current_positions and original_velocities == current_velocities:
            break

    return n


lineList = [line.rstrip('\n') for line in open('inputs/day12.txt')]
positions = []
for string in lineList:
    positions.append(tuple([int(c) for c in re.sub('[xyz<=,>]', '', string).split(' ')]))
velocities = [(0, 0, 0) for p in positions]
n_steps_x = find_n_steps(positions, velocities, 0)
n_steps_y = find_n_steps(positions, velocities, 1)
n_steps_z = find_n_steps(positions, velocities, 2)
lcm_x_y = abs(n_steps_x * n_steps_y) // math.gcd(n_steps_x, n_steps_y)
lcm = abs(lcm_x_y * n_steps_z) // math.gcd(lcm_x_y, n_steps_z)

print('# steps to return to initial state =', lcm)
