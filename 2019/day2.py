import csv

with open('inputs/day2.txt', 'r') as f:
    reader = csv.reader(f)
    your_list = list(reader)

your_list = your_list[0]
save_list = [int(item) for item in your_list]

for noun in range(100):
    for verb in range(100):
        insts = save_list[:]

        insts[1] = noun
        insts[2] = verb
        i = 0
        num = insts[i]
        while num != 99:

            if num == 1:
                insts[insts[i + 3]] = insts[insts[i + 1]] + insts[insts[i + 2]]

            elif num == 2:
                insts[insts[i + 3]] = insts[insts[i + 1]] * insts[insts[i + 2]]

            i += 4
            num = insts[i]

        if insts[0] == 19690720:
            print(100 * noun + verb)
            break
