class Node(object):
    def __init__(self, value):
        self.value = value
        self.children = []
        self.n = 0

    def n_children(self):
        if self.children:
            for c in self.children:
                c.n += 1
                c.n_children()
        else:
            return

    def add_child(self, obj):
        self.children.append(obj)


with open('inputs/day6.txt', 'r') as f:
    orbits = f.readlines()

orbits = [o.strip() for o in orbits]

orbits2 = [[] for i in range(len(orbits))]
for i, o in enumerate(orbits):
    bodies = o.split(')')
    orbits2[i] = bodies

unique_planets = list(set([item for sublist in orbits2 for item in sublist]))

nodes = []
for p in unique_planets:
    nodes.append(Node(p))

for i in orbits2:
    nodes[unique_planets.index(i[0])].add_child(nodes[unique_planets.index(i[1])])

# calculate distance to root for each
for n in nodes:
    n.n_children()

# add up all the distances from root
norbits = 0
for n in nodes:
    norbits += n.n

print(norbits)
