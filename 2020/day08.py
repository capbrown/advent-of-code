

def run(program):
	accumulator = 0
	i = 0=
	ended_naturally = False
	while True:
		if i > len(program) - 1:
			ended_naturally = True
			break
		current_instruction = program[i]
		instruction = current_instruction[0]
		operand = current_instruction[1]
		has_run = current_instruction[2]
		program[i] = (instruction, operand, True)
		if has_run:
			# found infinite loop so terminate
			break
		else:
			if instruction == 'nop':
				i += 1
			elif instruction == 'acc':
				accumulator += operand
				i += 1
			elif instruction == 'jmp':
				i += operand
	return accumulator, ended_naturally

	
if __name__ == "__main__":
	with open("input08.txt") as f:
		lines = f.read().splitlines()
	program = []
	for line in lines:
		instruction, operand = line.split()
		program.append((instruction, int(operand), False))
	
	# Part One
	#print(run(program)) 
	# need to fix program to make fn non stateful
	
	# Part Two
	for i in range(len(program)):
		current_instruction = program[i]
		instruction = current_instruction[0]
		operand = current_instruction[1]
		print(i)
		if instruction == 'nop':
			program[i] = ('jmp', operand, False)
			a = run(program)
			program[i] = ('nop', operand, False)
		elif instruction == 'jmp':
			program[i] = ('nop', operand, False)
			a = run(program)
			program[i] = ('jmp', operand, False)
		if a[1]:
			print(a[0])
			break
