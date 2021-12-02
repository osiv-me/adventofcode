
def main():
	print(part_one())
	print(part_two())

def part_one():
	lines = open('day_2.txt', 'r').read().split('\n')[:-1]
	x, depth = 0, 0

	for line in lines:
		dirr, value = line.split()[0], int(line.split()[1])
		if dirr == 'forward':
			x += value
		else:
			depth += value if dirr == 'down' else -value

	return x*depth

def part_two():
	lines = open('day_2.txt', 'r').read().split('\n')[:-1]
	x, depth, aim = 0, 0, 0

	for line in lines:
		dirr, value = line.split()[0], int(line.split()[1])
		if dirr == 'forward':
			depth += aim*value
			x += value
		else:
			aim += value if dirr == 'down' else -value

	return x*depth

if __name__ == '__main__':
	main()
