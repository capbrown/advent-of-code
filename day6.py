with open('inputs/day6.txt', 'r') as f:
    orbits = f.readlines()

orbits = [o.strip() for o in orbits]

orbits2 = [[] for i in range(len(orbits))]
for i, o in enumerate(orbits):
    bodies = o.split(')')
    orbits2[i] = bodies

print(orbits2)
