import sys

playerX = "X"
playerO = "O"
current_player = playerO

xScore = 0
oScore = 0

def switch_players():
	global current_player
	if (current_player == playerO):
		current_player = playerX
	else:
		current_player = playerO

def print_board():
	print(top_line)
	print(separator)
	print(mid_line)
	print(separator)
	print(bot_line)

def set_board():
	global topl
	global topm
	global topr
	global midl
	global midm
	global midr
	global botl
	global botm
	global botr
	global top_line
	global mid_line
	global bot_line
	global separator

	topl = " "
	topm = " "
	topr = " "
	midl = " "
	midm = " "
	midr = " "
	botl = " "
	botm = " "
	botr = " "

	top_line = f" {topl} |  {topm}  | {topr} "
	mid_line = f" {midl} |  {midm}  | {midr} "
	bot_line = f" {botl} |  {botm}  | {botr} "
	separator= "---|-----|---"

def set_options():

	global option1
	global option2
	global option3
	global option4
	global option5
	global option6
	global option7
	global option8
	global option9

	option1 = "1."
	option2 = "2."
	option3 = "3."
	option4 = "4."
	option5 = "5."
	option6 = "6."
	option7 = "7."
	option8 = "8."
	option9 = "9."

def request_input():

	global topl
	global topm
	global topr
	global midl
	global midm
	global midr
	global botl
	global botm
	global botr
	global top_line
	global mid_line
	global bot_line

	global option1
	global option2
	global option3
	global option4
	global option5
	global option6
	global option7
	global option8
	global option9

	print(f"Current player: {current_player}")
	print("Make selection:")
	print(f" {option1}   {option2}   {option3}")
	print(f" {option4}   {option5}   {option6}")
	print(f" {option7}   {option8}   {option9}")

	while True:
		selection = input("Enter a number 1-9: ")

		if selection == "1":
			if (topl == playerX) or (topl == playerO):
				print("Invalid selection. Space is already occupied.")
			else:
				topl = current_player
				option1 = "  "
				break
		elif selection == "2":
			if (topm == playerX) or (topm == playerO):
				print("Invalid selection. Space is already occupied.")
			else:
				topm = current_player
				option2 = "  "
				break
		elif selection == "3":
			if (topr == playerX) or (topr == playerO):
				print("Invalid selection. Space is already occupied.")
			else:
				topr = current_player
				option3 = "  "
				break
		elif selection == "4":
			if (midl == playerX) or (midl == playerO):
				print("Invalid selection. Space is already occupied.")
			else:
				midl = current_player
				option4 = "  "
				break
		elif selection == "5":
			if (midm == playerX) or (midm == playerO):
				print("Invalid selection. Space is already occupied.")
			else:
				midm = current_player
				option5 = "  "
				break
		elif selection == "6":
			if (midr == playerX) or (midr == playerO):
				print("Invalid selection. Space is already occupied.")
			else:
				midr = current_player
				option6 = "  "
				break
		elif selection == "7":
			if (botl == playerX) or (botl == playerO):
				print("Invalid selection. Space is already occupied.")
			else:
				botl = current_player
				option7 = "  "
				break
		elif selection == "8":
			if (botm == playerX) or (botm == playerO):
				print("Invalid selection. Space is already occupied.")
			else:
				botm = current_player
				option8 = "  "
				break
		elif selection == "9":
			if (botr == playerX) or (botr == playerO):
				print("Invalid selection. Space is already occupied.")
			else:
				botr = current_player
				option9 = "  "
				break
		else:
			print("Invalid number. Please enter a number 1-9.")

	top_line = f" {topl} |  {topm}  | {topr} "
	mid_line = f" {midl} |  {midm}  | {midr} "
	bot_line = f" {botl} |  {botm}  | {botr} "

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

def detect_result():
	if (
		# Horizontal checks
		(topl == playerX and topm == playerX and topr == playerX) or 
		(midl == playerX and midm == playerX and midr == playerX) or
		(botl == playerX and botm == playerX and botr == playerX) or
		# Vertical checks
		(topl == playerX and midl == playerX and botl == playerX) or
		(topm == playerX and midm == playerX and botm == playerX) or
		(topr == playerX and midr == playerX and botr == playerX) or
		# Diagonal checks
		(topl == playerX and midm == playerX and botr == playerX) or
		(topr == playerX and midm == playerX and botl == playerX) or
		# Horizontal checks
		(topl == playerO and topm == playerO and topr == playerO) or 
		(midl == playerO and midm == playerO and midr == playerO) or
		(botl == playerO and botm == playerO and botr == playerO) or
		# Vertical checks
		(topl == playerO and midl == playerO and botl == playerO) or
		(topm == playerO and midm == playerO and botm == playerO) or
		(topr == playerO and midr == playerO and botr == playerO) or
		# Diagonal checks
		(topl == playerO and midm == playerO and botr == playerO) or
		(topr == playerO and midm == playerO and botl == playerO)
	):
		print_board()
		print(f"{current_player} wins!")
		update_scoreboard(current_player)
		show_scoreboard()
		play_again()
	elif (
		topl != " " and topm != " " and topr != " " and
		midl != " " and midm != " " and midr != " " and
		botl != " " and botm != " " and botr != " "
	):
		print_board()
		print("Game drawn.")
		play_again()

def main():

	while True:
		set_board()
		set_options()

		while True:
			detect_result()
			switch_players()
			print_board()
			request_input()

main()