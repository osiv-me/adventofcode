
def main():
	print(part_one())
	print(part_two())

def part_one():
	data = open('day_1.txt', 'r').read().split('\n')[:-1]
	data = [int(x) for x in data]

	count = 0
	for i in range(0, len(data) - 1):
		if data[i] < data[i+1]:
			count += 1
	return count

def part_two():
	data = open('day_1.txt', 'r').read().split('\n')[:-1]
	data = [int(x) for x in data]

	count, next_sum, last_sum = 0, 0, sum(data[:3])
	for i in range(1, len(data) - 2):
		next_sum = sum(data[i:i+3])
		if last_sum < next_sum:
			count += 1

		last_sum = next_sum

	return count

if __name__ == '__main__':
	main()
