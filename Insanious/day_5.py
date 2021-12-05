def main():
	print(part_one())
	print(part_two())

def part_one():
	data = open('day_5.txt', 'r').read().split('\n')[:-1]
	grid = [ [0]*1000 for i in range(1000) ]

	for line in data:
		vec = line.split(' -> ')
		v1, v2 = vec[0].split(','), vec[1].split(',')
		v1 = [int(x) for x in v1]
		v2 = [int(x) for x in v2]
		if (not(v1[0] == v2[0] or v1[1] == v2[1])): # not horizontal or vertical
			continue

		if v1[0] == v2[0]: # vertical line
			len = v2[1] - v1[1]
			for i in range(abs(len) + 1): # magic number(?)
				if len < 1:		grid[v1[0]][v1[1] - i] += 1
				else:			grid[v1[0]][v1[1] + i] += 1
		else: # horizontal line
			len = v2[0] - v1[0]
			for i in range(abs(len) + 1): # magic number(?)
				if len < 1:		grid[v1[0] - i][v1[1]] += 1
				else:			grid[v1[0] + i][v1[1]] += 1

	# grid = map(list, zip(*grid)) # transpose for visuals
	return sum([1 for row in grid for col in row if col > 1])

def part_two():
	data = open('day_5.txt', 'r').read()


if __name__ == '__main__':
	main()
