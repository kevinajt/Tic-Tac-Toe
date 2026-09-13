import sys

playerX = "X"
playerO = "O"
current_player = playerX
xScore = 0
oScore = 0

def switch_players():
	global current_player
	if (current_player == playerO):
		current_player = playerX
	else:
		current_player = playerO

def set_board():
	global board
	board = []

	i = 0
	while i < 9:
		board.append(" ")
		i += 1

def print_board():
	separator = "---|-----|---"

	i = 0
	while i < 7:
		print(f" {board[i]} |  {board[i+1]}  | {board[i+2]} ")
		if i < 4:
			print(separator)
		i += 3

def set_options():
	global option
	option = []
	i = 1
	while i < 10:
		option.append(f"{i}.")
		i += 1

def request_input():
	global board
	global option

	print(f"Current player: {current_player}")
	print("Make selection:")
	print(f" {option[0]}   {option[1]}   {option[2]}")
	print(f" {option[3]}   {option[4]}   {option[5]}")
	print(f" {option[6]}   {option[7]}   {option[8]}")

	while True:
		while True:
			selection = input("Enter a number 1-9: ")
			try:
				selection = int(selection) - 1
				break
			except ValueError:
				print("Invalid input. Please enter a number 1-9.")

		if 0 <= selection <= 8:
			if (board[selection] == playerX) or (board[selection] == playerO):
				print("Invalid selection. Space is already occupied.")
			else:
				board[selection] = current_player
				option[selection] = "  "
				break
		else:
			print("Invalid input. Please enter a number 1-9.")

def show_scoreboard():
	print("Current Score")
	print(f"X: {xScore}")
	print(f"O: {oScore}")

def update_scoreboard(current_player):
	global oScore
	global xScore

	if current_player == playerO:
		oScore += 1
	elif current_player == playerX:
		xScore += 1

def play_again():
	while True:
		choice = input("Play again? y/n: ")
		if choice == "y":
			set_board()
			set_options()
			break
		elif choice == "n":
			sys.exit()
		else:
			print("Invalid selection. Please enter y to play again or n to exit.")

def detect_win():
	win_condition = [
					# horizontal wins
					[0,1,2],[3,4,5],[6,7,8],
				  	# vertical wins
				  	[0,3,6],[1,4,7],[2,5,8],
					# diagonal wins
					[0,4,8],[2,4,6]
					]

	for i in win_condition:
		if (
			board[i[0]] == current_player and
			board[i[1]] == current_player and
			board[i[2]] == current_player
		):
			print_board()
			print(f"{current_player} wins!")
			update_scoreboard(current_player)
			show_scoreboard()
			play_again()

def detect_draw():
	for i in board:
			if i == " ":
				return

	print_board()
	print("Game drawn.")
	play_again()

def main():
	while True:
		set_board()
		set_options()

		while True:
			print_board()
			request_input()
			detect_win()
			detect_draw()
			switch_players()

main()