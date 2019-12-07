import csv
import matplotlib.pyplot as plt
import numpy as np


def make_wire_array(wire_list):

    wire = np.array([[0, 0], [0, 0]])

    for instruction in wire_list:

        direction = instruction[0]
        amount = int(instruction[1:])
        last_point_x = wire[-1, 0]
        last_point_y = wire[-1, 1]

        if direction == 'R':
            for i in range(1, amount + 1):
                wire = np.vstack((wire, np.array([last_point_x + i, last_point_y])))
        elif direction == 'L':
            for i in range(1, amount + 1):
                wire = np.vstack((wire, np.array([last_point_x - i, last_point_y])))
        elif direction == 'U':
            for i in range(1, amount + 1):
                wire = np.vstack((wire, np.array([last_point_x, last_point_y + i])))
        elif direction == 'D':
            for i in range(1, amount + 1):
                wire = np.vstack((wire, np.array([last_point_x, last_point_y - i])))

    return wire


with open('inputs/day3.txt', 'r') as f:
    reader = csv.reader(f)
    wire_instructions = list(reader)

wire1_instructions = wire_instructions[0]
wire1_array = make_wire_array(wire1_instructions)

wire2_instructions = wire_instructions[1]
wire2_array = make_wire_array(wire2_instructions)

plt.figure()
plt.plot(wire1_array[:, 0], wire1_array[:, 1], 'b')
plt.plot(wire2_array[:, 0], wire2_array[:, 1], 'r')
plt.show()

# trim those leading zeros
wire1_array = wire1_array[2:]
wire2_array = wire2_array[2:]


nrows, ncols = wire1_array.shape
dtype = {'names': ['f{}'.format(i) for i in range(ncols)],
         'formats': ncols * [wire1_array.dtype]}

C, x_ind, y_ind = np.intersect1d(wire1_array.view(dtype), wire2_array.view(dtype), return_indices=True)

# This last bit is optional if you're okay with "C" being a structured array

ind_sum = x_ind + y_ind
print(np.min(ind_sum) + 2) # part 2
ind_min_ind = np.argmin(ind_sum)

C = C.view(wire1_array.dtype).reshape(-1, ncols)

C = abs(C[:, 0]) + abs(C[:, 1])
#print(C[ind_min_ind])
