import math

def main():
	print(part_one())
	print(part_two())

def part_one():
	data = open('day_7.txt', 'r').read().split(',')
	data[-1] = data[-1][:-1]
	data = [int(x) for x in data]
	data.sort()

	median = data[len(data) // 2]
	return sum([abs(crab - median) for crab in data])

def part_two():
	data = open('day_7.txt', 'r').read().split(',')
	data[-1] = data[-1][:-1]
	data = [int(x) for x in data]
	data.sort()

	# brute-force is op
	lowest = math.inf
	for i in range(data[-1]):
		res = sum_fuel(data, i)
		if res < lowest:
			lowest = res

	return lowest

def sum_fuel(data, value):
	fuel = 0
	for i in range(len(data)):
		n = abs(data[i] - value)
		fuel += (n*n+n) // 2
	return fuel

if __name__ == '__main__':
	main()
