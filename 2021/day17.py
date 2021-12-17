# Advent of Code: Day 17

from itertools import product

x = (265,287)
y = (-103,-58)

max_y = 0
hits = 0

# Brute force time
vs = product(list(range(x[1]+1)), list(range(-500,500)))
for v in vs:
	p = (0,0)
	max_y_i = 0
	while True:
		p = (p[0] + v[0], p[1] + v[1])
		v = (max([v[0] - 1, 0]), v[1] - 1)
		if p[1] > max_y_i:
			max_y_i = p[1]
		if p[0] >= x[0] and p[0] <= x[1] and p[1] >= y[0] and p[1] <= y[1]:
			hits += 1
			if max_y_i > max_y:
				max_y = max_y_i
			break
		if p[0] > x[1] or p[1] < min(y):
			break

print(max_y)
print(hits)
