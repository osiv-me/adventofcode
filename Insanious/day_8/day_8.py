digits = ['abcefg', 'cf', 'acdeg', 'acdfg', 'bcdf', 'abdfg', 'abdefg', 'acf', 'abcdefg', 'abcdfg']

def main():
	print(part_one())
	print(part_two())

def part_one():
	data = open('day_8.txt', 'r').read().split('\n')[:-1]
	inputs = []
	outputs = []
	for line in data:
		splitted = line.split('|')
		inputs.append(splitted[0].split(' '))
		outputs.append(splitted[1].split(' '))

	unique_lengths = [len(digits[1]), len(digits[4]), len(digits[7]), len(digits[8])]
	return sum([1 for output in outputs for word in output if len(word) in unique_lengths])

def shared_segments(first, second):
	return sum([1 for c in first if c in second])


def part_two():
	data = open('day_8.txt', 'r').read().split('\n')[:-1]
	sum_of_outputs = 0

	for line in data:
		buckets = {}
		for x in digits:
			if len(x) not in buckets:
				buckets[len(x)] = []

		known = {}
		for i in range(10):
			known[i] = ''
		splitted = line.split('|')
		input, output = splitted[0].split(' ')[:-1], splitted[1].split(' ')[1:]
		for word in input:
			buckets[len(word)].append(''.join(sorted(word)))

		known[1] = buckets[2][0]
		known[4] = buckets[4][0]
		known[7] = buckets[3][0]
		known[8] = buckets[7][0]

		for word in buckets[6]:
			if shared_segments(word, known[1]) == 1:
				known[6] = word
			elif shared_segments(word, known[4]) == 3:
				known[0] = word
			else:
				known[9] = word

		for word in buckets[5]:
			if shared_segments(word, known[1]) == 2:
				known[3] = word
			elif shared_segments(word, known[9]) == 5:
				known[5] = word
			else:
				known[2] = word

		new = [''.join(sorted(value)) for key,value in known.items()]
		out = ''
		for number in output:
			translated = ''.join(sorted(number))
			out += [str(i) for i in range(len(new)) if new[i] == translated][0]
		sum_of_outputs += int(out)

	return sum_of_outputs

if __name__ == '__main__':
	main()
