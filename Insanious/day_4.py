from copy import deepcopy

def main():
	print(part_one())
	print(part_two())

def part_one():
	boards, bool_boards, numbers = parse()
	return solve(boards, bool_boards, numbers, last=False)

def part_two():
	boards, bool_boards, numbers = parse()
	return solve(boards, bool_boards, numbers, last=True)

def parse():
	data = open('day_4.txt', 'r').read()
	numbers = data.split('\n')[0].split(',')
	numbers = [int(x) for x in numbers]

	data = data.split('\n')[2:-1]
	data = [x for x in data if x]
	rows, cols = 5, 5
	boards = []
	board_nr = -1
	for line, i in zip(data, range(len(data))):
		if i % rows == 0:
			boards.append([])
			board_nr += 1
		splitted = line.split()
		boards[board_nr].append([int(x) for x in splitted])

	bool_boards = deepcopy(boards)
	for i in range(len(bool_boards)):
		for j in range(len(bool_boards[i])):
			bool_boards[i][j] = [0] * rows

	return boards, bool_boards, numbers

def calculate_score(board, bool_board, number):
	sum_of_unmarked = 0
	for i in range(len(board)):
		for j in range(len(board[i])):
			if bool_board[i][j] == 0:
				sum_of_unmarked += board[i][j]
	return sum_of_unmarked * number

def solve(boards, bool_boards, numbers, last):
	last_winner, last_bool_winner, last_number = None, None, None
	winners = []
	last_number = -1
	cols, rows = 5, 5
	for number in numbers:
		for i in range(len(boards)):
			for j in range(cols):
				for k in range(rows):
					if boards[i][j][k] == number:
						if last == False or (last == True and i not in winners): # if part_two; only update boards that hasn't been bingo'ed yet
							bool_boards[i][j][k] = 1

						if is_bingo(bool_boards[i]):
							if last == True:
								if i not in winners: # append winners to list if it hasn't won yet
									winners.append(i)
									last_number = number
							else:
								return calculate_score(boards[i], bool_boards[i], number)

	i = winners[-1]
	return calculate_score(boards[i], bool_boards[i], last_number)

def is_bingo(board):
	for i in range(5):
		if (board[i][0] == 1 and board[i][1] == 1 and board[i][2] == 1 and board[i][3] == 1 and board[i][4] == 1):
			return True
		if (board[0][i] == 1 and board[1][i] == 1 and board[2][i] == 1 and board[3][i] == 1 and board[4][i] == 1):
			return True

	return False

if __name__ == '__main__':
	main()
