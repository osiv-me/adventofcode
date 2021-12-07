def main():
	print(part_one())
	print(part_two())

def part_one():
	data = open('day_5.txt', 'r').read().split('\n')[:-1]
	grid = [ [0]*1000 for i in range(1000) ]

	for line in data:
		vec = line.split(' -> ')
		v1, v2 = vec[0].split(','), vec[1].split(',')
		if (not(v1[0] == v2[0] or v1[1] == v2[1])): # not horizontal or vertical
			continue
		v1 = [int(x) for x in v1]
		v2 = [int(x) for x in v2]

		if v1[0] == v2[0]: # vertical line
			len = v2[1] - v1[1]
			mult = -1 if len < 1 else 1
			for i in range(abs(len) + 1):
				grid[v1[0]][v1[1] + i*mult] += 1
		else: # horizontal line
			len = v2[0] - v1[0]
			mult = -1 if len < 1 else 1
			for i in range(abs(len) + 1):
				grid[v1[0] + i*mult][v1[1]] += 1

	# grid = map(list, zip(*grid)) # transpose for visuals
	return sum([1 for row in grid for col in row if col > 1])

def part_two():
	data = open('day_5.txt', 'r').read().split('\n')[:-1]
	grid = [ [0]*1000 for i in range(1000) ]

	for line in data:
		vec = line.split(' -> ')
		v1, v2 = vec[0].split(','), vec[1].split(',')
		v1 = [int(x) for x in v1]
		v2 = [int(x) for x in v2]
		# skip non horizontal, vertical or diagonal lines
		if not(v1[0] == v2[0] or v1[1] == v2[1] or (v1[0] == v2[1] and v1[1] == v2[0]) or (v1[0] == v1[1] and v2[1] == v2[0]) or (v2[0]-v1[1] == v2[0]-v1[1])):
			continue

		if v1[0] == v2[0]: # vertical line
			length = v2[1] - v1[1]
			mult = -1 if length < 1 else 1
			for i in range(abs(length) + 1):
				grid[v1[0]][v1[1] + i*mult] += 1
		elif v1[1] == v2[1]: # horizontal line
			length = v2[0] - v1[0]
			mult = -1 if length < 1 else 1
			for i in range(abs(length) + 1):
				grid[v1[0] + i*mult][v1[1]] += 1
		else: # diagonal line
			xlen = v2[0] - v1[0]
			ylen = v2[1] - v1[1]
			xmult = -1 if xlen < 1 else 1
			ymult = -1 if ylen < 1 else 1
			# print(v1, v2, xlen, ylen, xmult, ymult)
			for i in range(abs(xlen) + 1):
				# print(v1[0] + i*xmult, v1[1] + i*ymult)
				grid[v1[0] + i*xmult][v1[1] + i*ymult] += 1

	return sum([1 for row in grid for col in row if col > 1])


if __name__ == '__main__':
	main()
