# Advent of Code Day 6

if __name__ == "__main__":
    input_file = 'inputs/input06.txt'
    with open(input_file) as f:
        lines_file = f.read().split('\n\n')

    # Part One
    lines = [line.replace('\n', '') for line in lines_file]
    uniques_in_group = [''.join(set(line)) for line in lines]
    print(sum([len(g) for g in uniques_in_group]))

    # Part Two
    lines = [line.split() for line in lines_file]
    sum_of_counts = 0
    for group in lines:
        n_members = len(group)
        letters = ''.join(group)
        unique_letters = ''.join(set(letters))
        is_in_all = [letters.count(letter) == n_members for letter in unique_letters]
        sum_of_counts += is_in_all.count(True)
    print(sum_of_counts)
