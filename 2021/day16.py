# Advent of Code: Day 16

def literal(binary_string):
	literal = ''
	while True:
		g = binary_string[:5]
		literal += g[1:]
		if g[0] == '0':
			binary_string = binary_string[5:]
			break
		binary_string = binary_string[5:]
	literal = int(literal, 2)
	return binary_string, literal
	
def other(binary_string):
	return

def process(binary_string, packet_version_sum = 0, value = 0, operation = None):

	if len(binary_string.strip('0')) == 0 :
		return binary_string, packet_version_sum, value

	packet_version = int(binary_string[:3].zfill(4), 2)
	packet_version_sum += packet_version
	type_ID = int(binary_string[3:6].zfill(4), 2)
	binary_string = binary_string[6:]
	
	if type_ID == 4:
		binary_string, literal_n = literal(binary_string)
		
		if value:
			if operation == 'sum':
				literal_n += value
			elif operation == 'product':
				literal_n *= value
			elif operation == 'minimum':
				literal_n = min([value, literal_n])
			elif operation == 'maximum':
				literal_n = max([value, literal_n])
			elif operation == 'greater than':
				if value > literal_n:
					literal_n = 1
				else:
					literal_n = 0
			elif operation == 'less than':
				if value < literal_n:
					literal_n = 1
				else:
					literal_n = 0
			elif operation == 'equal to':
				if value == literal_n:
					literal_n = 1
				else:
					literal_n = 0
		
		return process(binary_string, packet_version_sum, literal_n, operation)
	else:
		operations = ['sum', 'product', 'minimum', 'maximum', '',  'greater than', 'less than', 'equal to']
		operation = operations[type_ID]
	
		length_type_ID = int(binary_string[0])
		binary_string = binary_string[1:]
		
		if length_type_ID == 0:
			total_length = int(binary_string[:15], 2)
			binary_string = binary_string[15:]
			substring = binary_string[:total_length]
			_, packet_version_sum, value = process(binary_string[:total_length], packet_version_sum, value, operation)
			binary_string, packet_version_sum, value = process(binary_string[total_length:], packet_version_sum, value, operation)
		
		elif length_type_ID == 1:
			
			n_subpackets = int(binary_string[:11], 2)
			binary_string = binary_string[11:]
			for n in range(n_subpackets):
				binary_string, packet_version_sum, value = process(binary_string, packet_version_sum, value, operation)

	return binary_string, packet_version_sum, value
	
# need to fix for final case where things are calculated as groups before a comparison
input_string = '9C0141080250320F1802104A08'
binary_string = bin(int(input_string, 16))[2:].zfill(len(input_string*4))
print(process(binary_string))
