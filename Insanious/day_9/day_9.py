def main():
	print(part_one())
	print(part_two())


def low_point(data, y, x):
	if y-1 >= 0 and not(data[y][x] < data[y-1][x]):	return False
	if y+1 < len(data) and not(data[y][x] < data[y+1][x]):	return False
	if x-1 >= 0 and not(data[y][x] < data[y][x-1]):	return False
	if x+1 < len(data[0]) and not(data[y][x] < data[y][x+1]):	return False
	return True

def part_one():
	data = open('day_9.txt', 'r').read().split('\n')[:-1]
	lows = []
	for y in range(len(data)):
		for x in range(len(data[y])):
			if low_point(data, y, x):
				lows.append(int(data[y][x]))

	return sum(lows) + len(lows)

def get_high_points(data, y, x):
	points = []
	if y-1 >= 0 and data[y][x] < data[y-1][x]:			points.append([y-1, x])
	if y+1 < len(data) and data[y][x] < data[y+1][x]:	points.append([y+1, x])
	if x-1 >= 0 and data[y][x] < data[y][x-1]:			points.append([y, x-1])
	if x+1 < len(data[0]) and data[y][x] < data[y][x+1]:points.append([y, x+1])
	return points

def explore_basin(data, low):
	already_visited = []
	not_visited = [low]

	while len(not_visited):
		point = not_visited.pop()
		already_visited.append(point)
		higher_points = get_high_points(data, point[0], point[1])
		for p in higher_points:
			if p not in already_visited and p not in not_visited and int(data[p[0]][p[1]]) != 9:
				not_visited.append(p)

	return already_visited



def part_two():
	data = open('day_9.txt', 'r').read().split('\n')[:-1]
	lows = []
	for y in range(len(data)):
		for x in range(len(data[y])):
			if low_point(data, y, x):
				lows.append([y, x])

	basins = []
	for low in lows:
		basins.append(explore_basin(data, low))

	basins = sorted(basins, key=len, reverse=True)
	res = 1
	for i in range(3):
		res *= len(basins[i])

	return res


if __name__ == '__main__':
	main()
