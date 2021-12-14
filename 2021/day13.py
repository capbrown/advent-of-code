# Advent of Code: Day 13

input_file_name = r'day13.txt'
with open(input_file_name) as f:
	lines = f.read().splitlines()

blank_line = lines.index('')
dots = lines[:blank_line]
folds = lines[blank_line+1:]

paper_y, paper_x = max([int(dot.split(',')[1]) for dot in dots])+1, max([int(dot.split(',')[0]) for dot in dots])+1
paper = np.zeros((paper_y,paper_x))
for dot in dots:
	dot = dot.split(',')
	j = int(dot[1])
	i = int(dot[0])
	paper[j, i] = 1

for fold in folds:
	fold = fold.split(' ')[-1]
	fold_dir, fold_pos = fold.split('=')
	fold_pos = int(fold_pos)
	
	if fold_dir == 'x':
		keep_part = paper[:,:fold_pos]
		fold_part = paper[:,fold_pos+1:]
		fold_part = np.fliplr(fold_part)
		paper = keep_part
		paper += np.pad( fold_part, ((0,0),(paper.shape[1]-fold_part.shape[1],0)), 'constant', constant_values = ((0, 0),(0, 0)))
	elif fold_dir == 'y':
		keep_part = paper[:fold_pos,:]
		fold_part = paper[fold_pos+1:,:]
		fold_part = np.flipud(fold_part)
		paper = keep_part
		paper += np.pad( fold_part, ((paper.shape[1]-fold_part.shape[1],0),(0,0)), 'constant', constant_values = ((0, 0),(0, 0)))
	print(np.count_nonzero(paper > 0))

for line in paper:
	for c in line:
		if c > 0:
			print('|', end='')
		else:
			print(' ', end='')
	print()
