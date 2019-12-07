from math import floor

# part 1
total_fuel = 0
with open("inputs/day1.txt", 'r') as modules:
    for mass in modules:
        total_fuel += floor(int(mass) / 3) - 2

print(total_fuel)

# part 2
total_fuel_2 = 0
with open("inputs/day1.txt", 'r') as modules:
    for mass in modules:
        nm = int(mass)
        while floor(int(nm) / 3) - 2 > 0:
            nm = floor(int(nm) / 3) - 2
            total_fuel_2 += nm


print(total_fuel_2)
