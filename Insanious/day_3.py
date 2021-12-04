import numpy as np

def main():
	print(part_one())
	print(part_two())

def part_one():
	data = open('day_3.txt', 'r').read().split('\n')[:-1]
	sum_of_bits = [0] * len(data[0])

	for bits in data:
		for i in range(len(sum_of_bits)):
			sum_of_bits[i] += int(bits[i])

	result = ['0'] * len(data[0])
	negation = ['1'] * len(data[0])
	half_length = len(data) / 2
	for i in range(len(result)):
		if sum_of_bits[i] > half_length:
			result[i] = '1'
			negation[i] = '0'

	return int(''.join(result), 2) * int(''.join(negation), 2)


def part_two():
	data = open('day_3.txt', 'r').read().split('\n')[:-1]
	nr_of_bits = len(data[0])

	half_length = len(data) / 2
	oxygen, new = data, []
	for i in range(nr_of_bits):
		if len(oxygen) == 1:
			break
		chosen_bit = most_frequent(oxygen, i)
		new = [bits for bits in oxygen if bits[i] == chosen_bit]
		half_length = int(len(new) / 2)

		oxygen = new

	half_length = len(data) / 2
	co2, new = data, []
	for i in range(nr_of_bits):
		if len(co2) == 1:
			break
		chosen_bit = most_infrequent(co2, i)
		new = [bits for bits in co2 if bits[i] == chosen_bit]
		half_length = int(len(new) / 2)

		co2 = new

	return int(''.join(oxygen), 2) * int(''.join(co2), 2)

def most_frequent(data, index):
	result = 0
	for bits in data:
		result += int(bits[index])

	return '1' if result >= len(data) / 2 else '0'

def most_infrequent(data, index):
	return '1' if most_frequent(data, index) == '0' else '0'


if __name__ == '__main__':
	main()
