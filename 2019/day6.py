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

    def is_you_child(self):
        if self.value == "YOU":
            return True
        elif not self.children:
            return False
        for sc in self.children:
            if sc.is_you_child():
                return True

    def is_san_child(self):
        if self.value == "SAN":
            return True
        elif not self.children:
            return False
        for sc in self.children:
            if sc.is_san_child():
                return True

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

i_you = 0
i_san = 0
for i, n in enumerate(nodes):
    if n.value == "YOU": i_you = n.n
    if n.value == "SAN": i_san = n.n


def find_shared_parent(i_min):
    while True:
        for i, ni in enumerate(nodes):
            if ni.n == i_min:
                for c in ni.children:
                    if c.is_you_child() and c.is_san_child():
                        return c
        i_min -= 1
        if not i_min:
            break


shared_parent = find_shared_parent(min([i_you, i_san]) - 1)
print(((i_you - 1) - shared_parent.n) + ((i_san - 1) - shared_parent.n))
