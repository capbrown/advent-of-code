import csv


def computer(my_data, noun=None, verb=None, phase=None, input_n=None):
    if noun and verb:
        my_data[1] = noun
        my_data[2] = verb
    n = 0
    output_signal = 0
    auto_input_i = 0
    inputs = [phase, input_n, None]
    while True:
        current = my_data[n]
        instruction = current % 100
        current = str(current).zfill(5)
        mode1 = int(repr(current)[-4])
        mode2 = int(repr(current)[-5])
        mode3 = int(repr(current)[-6])

        if instruction == 1:
            a = my_data[my_data[n + 1]] if mode1 == 0 else my_data[n + 1]
            b = my_data[my_data[n + 2]] if mode2 == 0 else my_data[n + 2]
            if mode3 == 0:
                my_data[my_data[n + 3]] = a + b
            else:
                my_data[n + 3] = a + b
            n += 4

        elif instruction == 2:
            a = my_data[my_data[n + 1]] if mode1 == 0 else my_data[n + 1]
            b = my_data[my_data[n + 2]] if mode2 == 0 else my_data[n + 2]
            if mode3 == 0:
                my_data[my_data[n + 3]] = a * b
            else:
                my_data[n + 3] = a * b
            n += 4

        elif instruction == 3:
            if inputs[auto_input_i] == None:
                my_data[my_data[n + 1]] = int(input("Enter an integer: "))
            else:
                my_data[my_data[n + 1]] = inputs[auto_input_i]
                auto_input_i += 1
            n += 2

        elif instruction == 4:
            output_signal = my_data[my_data[n + 1]]
            n += 2

        elif instruction == 5:
            first_param = my_data[my_data[n + 1]] if mode1 == 0 else my_data[n + 1]
            second_param = my_data[my_data[n + 2]] if mode2 == 0 else my_data[n + 2]

            if first_param:
                n = second_param
            else:
                n += 3

        elif instruction == 6:
            first_param = my_data[my_data[n + 1]] if mode1 == 0 else my_data[n + 1]
            second_param = my_data[my_data[n + 2]] if mode2 == 0 else my_data[n + 2]

            if not first_param:
                n = second_param
            else:
                n += 3

        elif instruction == 7:
            first_param = my_data[my_data[n + 1]] if mode1 == 0 else my_data[n + 1]
            second_param = my_data[my_data[n + 2]] if mode2 == 0 else my_data[n + 2]

            if first_param < second_param:
                my_data[my_data[n + 3]] = 1
            else:
                my_data[my_data[n + 3]] = 0

            n += 4

        elif instruction == 8:
            first_param = my_data[my_data[n + 1]] if mode1 == 0 else my_data[n + 1]
            second_param = my_data[my_data[n + 2]] if mode2 == 0 else my_data[n + 2]

            if first_param == second_param:
                my_data[my_data[n + 3]] = 1
            else:
                my_data[my_data[n + 3]] = 0

            n += 4

        elif instruction == 99:
            break

    return output_signal


if __name__ == "__main__":
    with open('inputs/day5.txt', 'r') as f:
        reader = csv.reader(f)
        my_dat = list(reader)[0]
        my_dat = [int(n) for n in my_dat]

    computer(my_dat)
