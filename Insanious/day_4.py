from copy import deepcopy

def main():
	print(part_one())
	print(part_two())

def part_one():
	boards, bool_boards, numbers = parse()
	winning_board, winning_bool_board, last_number = check_boards(boards, bool_boards, numbers, last=False)
	return calculate_score(winning_board, winning_bool_board, last_number)

def part_two():
	boards, bool_boards, numbers = parse()
	winning_board, winning_bool_board, last_number = check_boards(boards, bool_boards, numbers, last=True)
	return calculate_score(winning_board, winning_bool_board, last_number)

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

def check_boards(boards, bool_boards, numbers, last):
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
								return boards[i], bool_boards[i], number

	i = winners[-1]
	return boards[i], bool_boards[i], last_number # return last winner

def is_bingo(board):
	bingo = False
	for row in board:
		if sum(row) == 5:
			return True

	col_totals = [sum(x) for x in zip(*board)]
	for col in col_totals:
		if col == 5:
			return True

	return False

if __name__ == '__main__':
	main()
