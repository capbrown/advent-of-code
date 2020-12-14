# Advent of Code Day 14


with open('input14.txt') as f:
	lines = f.read().splitlines()

# Part One
instructions = []
for line in lines:
	if 'mask' in line:
		mask = line.split(' ')[2]
		indices = [i for i, x in enumerate(list(mask)) if x == '1' or x == '0']
	else:
		address = int(line.split(' ')[0].strip('mem[]'))
		val = bin(int(line.split(' ')[2]))[2:].zfill(36)

		# apply mask
		for i in indices:
			val = val[:i] + mask[i] + val[i + 1:]
		
		# overwrite if address has been written to
		addresses_written_to = [ad[0] for ad in instructions]
		if address in addresses_written_to:
			instructions.pop(addresses_written_to.index(address))
		
		instructions.append((address, int(val, 2)))

print(sum([val[1] for val in instructions]))