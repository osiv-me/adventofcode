illegals = {')' : 3, ']' : 57, '}' : 1197, '>' : 25137}
bracket_values = {')' : 1, ']' : 2, '}' : 3, '>' : 4}

def main():
	print(part_one())
	print(part_two())

def is_closing(bracket):
	if bracket in [')', ']', '}', '>']: return True
	return False

def inverse(bracket):
	if bracket == '(': return ')'
	elif bracket == '[': return ']'
	elif bracket == '<': return '>'
	elif bracket == '{': return '}'
	return None

def calculate_incomplete_line(stack):
	result = 0
	while len(stack):
		last = inverse(stack.pop())
		result = result*5 + bracket_values[last]
	return result

def part_one():
	result = 0
	data = open('day_10.txt', 'r').read().split('\n')[:-1]

	for line in data:
		stack = [line[0]]
		for bracket in line[1:]:
			if not is_closing(bracket):
				stack.append(bracket)
			else:
				if bracket == inverse(stack[-1]):
					stack.pop()
				else:
					result += illegals[bracket]
					break

	return result


def part_two():
	data = open('day_10.txt', 'r').read().split('\n')[:-1]
	results = []

	for line in data:
		stack = [line[0]]
		for bracket in line[1:]:
			if not is_closing(bracket):
				stack.append(bracket)
			else:
				if bracket == inverse(stack[-1]):
					stack.pop()
				else:
					stack = []
					break

		if not len(stack): # illegal line
			continue

		results.append(calculate_incomplete_line(stack))

	return sorted(results)[len(results) // 2]

if __name__ == '__main__':
	main()
