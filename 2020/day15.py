# Advent of Code Day 15

if __name__ == '__main__':
	
	n_spoken = 2020
	spoken = {'2': 1, '0': 2, '1': 3, '9': 4, '5': 5}
	last_spoken = '19'
	
	for i in range(6, n_spoken):
		if last_spoken in spoken:
			turn_spoken = spoken[last_spoken]
			spoken[last_spoken] = i
			last_spoken = str(i - turn_spoken)
		else:
			spoken[last_spoken] = i
			last_spoken = '0'	
	
	print(last_spoken)
