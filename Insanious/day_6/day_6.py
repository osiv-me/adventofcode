from queue import PriorityQueue

def main():
	print(part_one())
	print(part_two())


def part_one():
	data = open('day_6.txt', 'r').read().split(',')
	data[-1] = data[-1][:-1]
	data = [int(x) for x in data]

	for _ in range(80):
		length = len(data)
		cnt = 0
		for i in range(length):
			if data[i] == 0:
				data[i] = 7 # since we are decreasing later anyways
				data.append(8)
			data[i] -= 1

	return len(data)

def part_two():
	data = open('day_6.txt', 'r').read().split(',')
	data[-1] = data[-1][:-1]
	data = [int(x) for x in data]

	fish_bucket = {}
	for i in range(0, 10):
		fish_bucket[i] = 0
	for fish in data:
		fish_bucket[fish] += 1

	counter = -1 # -1 since we're incrementing in the beginning to get the first run to be 0
	for _ in range(256):
		counter += 1
		nr_of_zero_fish = fish_bucket[(0 + counter) % 10]
		if fish_bucket[(0 + counter) % 10] > 0:
			fish_bucket[(7 + counter) % 10] += nr_of_zero_fish # add sevens to list
			fish_bucket[(0 + counter) % 10] = 0 # empty zero-list
			fish_bucket[(9 + counter) % 10] += nr_of_zero_fish # add nines to list

	return sum([ val for key, val in fish_bucket.items()])

def print_fishies(fish_bucket):
	li = []
	for key, val in fish_bucket.items():
		for i in range(0, val):
			li.append(key)
	li.sort()
	print(li)

if __name__ == '__main__':
	main()
