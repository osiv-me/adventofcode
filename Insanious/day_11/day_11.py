data = ''

def main():
	print(part_one())
	print(part_two())

def get_adjacent_hits(y, x):
	miny = 0 if y-1 < 0 else y-1
	minx = 0 if x-1 < 0 else x-1
	maxy = len(data) if y+2 > len(data) else y+2
	maxx = len(data) if x+2 > len(data) else x+2

	hits = [[i, j] for i in range(miny, maxy) for j in range(minx, maxx)]
	hits.remove([y, x])
	return hits

def part_one():
	global data
	data = open('day_11.txt', 'r').read().split('\n')[:-1]
	nr_of_flashes = 0
	for _ in range(100):
		already_flashed = []
		hits = []
		for y in range(len(data)):
			line = list(data[y])
			for x in range(len(line)):
				line[x] = str(int(line[x]) + 1)
				if int(line[x]) > 9: # octopus gonna flash
					nr_of_flashes += 1 # increment
					line[x] = '0' # reset octopus
					already_flashed.append([y, x])

					new_hits = get_adjacent_hits(y, x)
					for hit in new_hits:
						if hit not in already_flashed:
							hits.append(hit)
			data[y] = ''.join(line)

		while len(hits):
			adj = hits.pop(0)
			if adj in already_flashed:
				continue

			line = list(data[adj[0]])
			line[adj[1]] = str(int(line[adj[1]]) + 1) # increment

			if int(line[adj[1]]) > 9: # octopus gonna flash
				nr_of_flashes += 1
				line[adj[1]] = '0' # reset octopus
				already_flashed.append([adj[0], adj[1]])

				new_hits = get_adjacent_hits(adj[0], adj[1])
				for hit in new_hits:
					if hit not in already_flashed:
						hits.append(hit)

			data[adj[0]] = ''.join(line)
	return nr_of_flashes

def part_two():
	global data
	data = open('day_11.txt', 'r').read().split('\n')[:-1]
	nr_of_flashes = 0
	step = 0
	flashes_in_round = 0
	while flashes_in_round < len(data)*len(data):
		step += 1
		flashes_in_round = 0
		already_flashed = []
		hits = []
		for y in range(len(data)):
			line = list(data[y])
			for x in range(len(line)):
				line[x] = str(int(line[x]) + 1)
				if int(line[x]) > 9: # octopus gonna flash
					nr_of_flashes += 1 # increment
					flashes_in_round += 1
					line[x] = '0' # reset octopus
					already_flashed.append([y, x])

					new_hits = get_adjacent_hits(y, x)
					for hit in new_hits:
						if hit not in already_flashed:
							hits.append(hit)
			data[y] = ''.join(line)

		while len(hits):
			adj = hits.pop(0)
			if adj in already_flashed:
				continue

			line = list(data[adj[0]])
			line[adj[1]] = str(int(line[adj[1]]) + 1) # increment

			if int(line[adj[1]]) > 9: # octopus gonna flash
				nr_of_flashes += 1
				flashes_in_round += 1
				line[adj[1]] = '0' # reset octopus
				already_flashed.append([adj[0], adj[1]])

				new_hits = get_adjacent_hits(adj[0], adj[1])
				for hit in new_hits:
					if hit not in already_flashed:
						hits.append(hit)

			data[adj[0]] = ''.join(line)

	return step

if __name__ == '__main__':
	main()
