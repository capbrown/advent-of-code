# Advent of Code: Day 14

import numpy as np
from collections import Counter

input_file_name = r'day14.txt'
with open(input_file_name) as f:
	lines = f.read().splitlines()
	
template = lines[0]
raw_rules = lines[2:]
rules = {}
for rule in raw_rules:
	rule = rule.split(' -> ')
	rules[rule[0]] = rule[1]

pairs = [template[i:i+2] for i in range(len(template)-1)]
time_steps = 10
for i in range(time_steps):
	template = template[0]
	for pair in pairs:
		template += rules[pair] + pair[1]
	pairs = [template[i:i+2] for i in range(len(template)-1)]

_, c = np.unique(list(template), return_counts=True)
print(np.max(c) - np.min(c))
