# Advent of Code Day 13

import numpy as np


if __name__ == "__main__":
    with open("inputs/input13.txt") as f:
        lines = f.read().splitlines()

    earliest_timestamp = int(lines[0])
    bus_ids = [int(n) for n in lines[1].split(',') if n != 'x']

    # Part One
    current = earliest_timestamp
    while True:
        all_mods = [current % bus_id for bus_id in bus_ids]
        if not all(all_mods):
            break
        current += 1

    print(bus_ids[[current % bus_id for bus_id in bus_ids].index(0)]*(current-earliest_timestamp))

