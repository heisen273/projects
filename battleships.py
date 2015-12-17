import sys
from random import randint
board = []
print(chr(27) + "[2J")
for x in range(0, 10):
    board.append((["O"]) * 10)

def print_board(board):
    for row in board:
        print " ".join(row)

print_board(board)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board) - 1)
    

ship_row = random_row(board)
ship_col = random_col(board)
n=[0,1,2,3,4,5,6,7,8,9]
for turn in range(10):
		print "GUESS MUST BE BETWEEN 0 AND 9"
		guess_row = int(raw_input("Guess Row:"))
		guess_col = int(raw_input("Guess Col:"))
		print "GUESS MUST BE BETWEEN 0 AND 9"
		sys.stderr.write("\x1b[2J\x1b[H")
		print ship_row
		print ship_col
# Write your code below!
		if guess_row == ship_row and guess_col == ship_col:
		  	print "Congratulations! You sank my battleship!"
			board[guess_row][guess_col]="\033[1;31mX\033[1;m"
			print_board(board)
			break
		elif (guess_row>10 or guess_row<0) or (guess_col>10 or guess_col<0):
			print "WRONG NUMBER, FELLA"
		elif board[guess_row][guess_col]=="X":
			print "You've guessed this one already!"
		else:
    			print "You missed my battleship!"
			board[guess_row][guess_col]="X"
   			print_board(board)
			if turn==9:
				print "GAME OVER, no more turns"
		print "Turn",turn+1
