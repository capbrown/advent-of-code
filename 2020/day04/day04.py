# Advent of Code Day 4
import re
import string


def day04_1(passports):
	n_valid = 0
	for passport in passports:
		if n_fields_valid(passport):
			n_valid += 1
	return n_valid

	
def day04_2(passports):
	n_valid = 0
	for passport in passports:
		if n_fields_valid(passport) and fields_valid(passport):
			n_valid += 1
	return n_valid

	
def n_fields_valid(passport):
	n_fields = len(passport)
	if n_fields == 8:
		return True
	elif n_fields == 7 and 'cid' not in passport:
		return True
	return False
	
	
def fields_valid(passport):
	
	byr_valid = int(passport['byr']) in range(1920, 2003)
	iyr_valid = int(passport['iyr']) in range(2010, 2021)
	eyr_valid = int(passport['eyr']) in range(2020, 2031)

	height = passport['hgt']
	cm_valid = len(height) == 5 and 'cm' in height and int(height[0:3]) in range(150, 194)
	in_valid = len(height) == 4 and 'in' in height and int(height[0:2]) in range(59, 77)
	hgt_valid = cm_valid or in_valid
	
	hcl = passport['hcl']
	hcl_valid = hcl[0] == '#' and len(hcl) == 7 and all(c in string.hexdigits for c in hcl[1:])
	
	ecl_valid = passport['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
	pid_valid = passport['pid'].isdigit() and len(passport['pid']) == 9
	
	if all([byr_valid, iyr_valid, eyr_valid, hgt_valid, hcl_valid, ecl_valid, pid_valid]):
		return True
	return False
	
	
if __name__ == "__main__":
	input_file = 'input04.txt'
	with open(input_file) as f:
		lines = f.read().split('\n\n')
		lines = [line.replace('\n', ' ') for line in lines]
	
	passports = []
	for line in lines:
		entry = {}
		for field in line.split():
			field_name, val = field.split(':')
			entry[field_name] = val
		passports.append(entry)

	# Part One
	print(day04_1(passports))
	
	# Part Two
	print(day04_2(passports))
