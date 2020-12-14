# Advent of Code Day 12

import numpy as np


if __name__ == "__main__":
    with open("input12.txt") as f:
        lines = f.read().splitlines()

    # Part One
    directions = []
    x = 0
    y = 0
    for line in lines:
        direction = line[0]
        amount = int(line[1:])
        if direction == 'N':
            y += amount
        elif direction == 'S':
            y -= amount
        elif direction == 'E':
            x += amount
        elif direction == 'W':
            x -= amount
        else:
            directions.append((direction, amount))

    point = 90
    for dir in directions:
        movement = dir[0]
        amount = dir[1]
        if movement == 'R':
            point = (point + amount) % 360
        elif movement == 'L':
            point = (point - amount) % 360
        elif movement == 'F':
            if point == 0:
                y += amount
            elif point == 180:
                y -= amount
            elif point == 90:
                x += amount
            elif point == 270:
                x -= amount

    print(abs(x) + abs(y))

    # Part Two
    x = 0
    y = 0
    wx = 10
    wy = 1

    directions = []
    for line in lines:
        direction = line[0]
        amount = int(line[1:])
        directions.append((direction, amount))

    for dir in directions:
        movement = dir[0]
        amount = dir[1]
        print(dir)
        if movement == 'N':
            wy += amount
        elif movement == 'S':
            wy -= amount
        elif movement == 'E':
            wx += amount
        elif movement == 'W':
            wx -= amount
        elif movement == 'R':
            if amount == 90:
                wx, wy = wy, -wx
            elif amount == 180:
                wx, wy = -wx, -wy
            if amount == 270:
                wx, wy = -wy, wx
        elif movement == 'L':
            if amount == 90:
                wx, wy = -wy, wx
            elif amount == 180:
                wx, wy = -wy, -wx
            if amount == 270:
                wx, wy = wy, -wx
        elif movement == 'F':
            y += amount*wy
            x += amount*wx
        print(x, y)
        print(wx, wy)

    print(abs(x) + abs(y))
